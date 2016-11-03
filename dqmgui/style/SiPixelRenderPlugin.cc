/*!
  \file SiPixelRenderPlugin
  \brief Display Plugin for Pixel DQM Histograms
  \author P.Merkel
  \version $Revision: 1.49 $
  \date $Date: 2012/04/10 09:44:09 $
*/

#include "DQM/DQMRenderPlugin.h"
#include "utils.h"

#include "TProfile2D.h"
#include "TStyle.h"
#include "TCanvas.h"
#include "TGraphPolar.h"
#include "TColor.h"
#include "TText.h"
#include "TLine.h"
#include "TGaxis.h"
#include <cassert>
#include <cctype>
#include <map>
#include <vector>

class SiPixelRenderPlugin : public DQMRenderPlugin
{
public:
  virtual bool applies( const VisDQMObject &o, const VisDQMImgInfo & )
    {
      if( o.name.find( "Pixel/" ) == 0 )
        return true;
      if( o.name.find( "PixelPhase1/" ) == 0 )
        return true;

      return false;
    }

  virtual void preDraw( TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &, VisDQMRenderInfo & )
    {
      c->cd();
      if( dynamic_cast<TH2*>( o.object ) )
      {
        preDrawTH2( c, o );
      }
      else if( dynamic_cast<TH1*>( o.object ) )
      {
        preDrawTH1( c, o );
      }
    }

  virtual void postDraw( TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo & )
    {
      c->cd();
      putName(o);

      if( dynamic_cast<TH2*>( o.object ) )
      {
        postDrawTH2( c, o );
      }
      else if( dynamic_cast<TH1*>( o.object ) )
      {
        postDrawTH1( c, o );
      }
    }

private:
  TText *name_text = nullptr;

  void putName(VisDQMObject const& o) {
    // we cannot delete this immediately, so wait for the next call
    if (name_text) delete name_text;

    name_text = new TText(0.05,0.01, o.name.c_str());
    name_text->SetTextColor(kBlack);
    name_text->SetTextSize(0.02);
    name_text->SetNDC();
    name_text->Draw("same");
  }

  // simple recursive descent parser for the "Column(0,30,50,)/Other(0,3,5,)/Last"
  // format used to carry the positions where histograms where concatenated by
  // EXTEND to this plugin.
  template<typename Iterator>
  struct LabelMarkerParser {
    std::vector<std::vector<int>> markers; // output
    std::string text; // cleaned-up label

    static std::pair<bool, int> parse_int(Iterator& start, Iterator end) {
      int out = 0;
      if (start == end || !std::isdigit(*start)) return std::make_pair(false, out);
      while (start != end && std::isdigit(*start))
        out = out * 10 + (*start++ - '0');
      return std::make_pair(true, out);
    }

    static std::string parse_text(Iterator& start, Iterator end) {
      std::string out;
      while (start != end && *start != '(' && *start != '/') out.push_back(*start++);
      return out;
    }

    static std::pair<bool, std::vector<int>> parse_list(Iterator& start, Iterator end) {
      std::vector<int> out;
      if (start == end || *start != '(') return std::make_pair(false, out);
      ++start;
      for(;;) {
        auto num = parse_int(start, end);
        if (num.first) out.push_back(num.second);
        else break;
        if (start != end && *start == ',') ++start;
      }
      if (start == end || *start != ')') return std::make_pair(false, out);
      ++start;
      return std::make_pair(true, out);
    }

    static std::pair<bool, LabelMarkerParser> parse_label(Iterator start, Iterator end) {
      std::vector<std::vector<int>> out;
      std::string text;
      for(;;) {
        text += parse_text(start, end);
        auto list = parse_list(start, end);
        // we might fail parsing here but consume input, but this is acceptable.
        if (list.first) out.emplace_back(list.second);
        if (start == end)  return std::make_pair(true, LabelMarkerParser{out, text});
        if (*start != '/') return std::make_pair(false, LabelMarkerParser{out, text});
        ++start;
        text += "/";
        if (start == end)  return std::make_pair(true, LabelMarkerParser{out, text});
      }
    }
  };

  void putMarkers(TH1* obj)
    {
      // TODO: Y-Axis as well?
      TAxis* ax = obj->GetXaxis();
      auto label = std::string(ax->GetTitle());
      auto res = LabelMarkerParser<std::string::iterator>::parse_label(label.begin(), label.end());
      if (!res.first || res.second.markers.size() == 0)
        return; // parse failed, probably no markers

      std::string newlabel = res.second.text;
      std::vector<std::vector<int>>& markers = res.second.markers;

      auto ymax = obj->GetMaximum() * 0.5;
      auto ymin = 0; // TODO: we actually want the y axis range here.
      auto step = (ymax-ymin)*0.5 / markers.size();
      // we only get one set of values each, but have to draw a full hierarchy
      putMarkersRecursive(markers.begin(), markers.end(), 0, ymin, ymax, step);

      ax->SetTitle(newlabel.c_str());
    }

  template<typename Iterator> // Iterator into vector of vectors
  void putMarkersRecursive(Iterator begin, Iterator end, int offset, double ymin, double ymax, double step) {
    if (begin == end) return;
    for (auto mark : *begin) {
      auto pos = double(mark) + 0.5 + double(offset);
      TLine tl;
      tl.SetLineColor(4);
      tl.DrawLine(pos, ymin, pos, ymax);
      putMarkersRecursive(begin+1, end, offset + mark, ymin, ymax - step, step);
    }
  }

  void preDrawTH2( TCanvas *, const VisDQMObject &o )
    {
      TH2* obj = dynamic_cast<TH2*>( o.object );
      assert( obj );

      // This applies to all
      gStyle->SetCanvasBorderMode( 0 );
      gStyle->SetPadBorderMode( 0 );
      gStyle->SetPadBorderSize( 0 );

      gStyle->SetOptStat( 0 );
      obj->SetStats( kFALSE );

      gStyle->SetPalette(1);
      gPad->SetRightMargin(0.15);
      obj->SetOption("colz");

      // TODO: content-based zooming might be useful.
      // (maybe as a function, could be useful for TH1 as well)

      // case-insensitive find is not easy...
      if (o.name.find( "sizeYvsEta" ) != std::string::npos
       || o.name.find( "sizeyvseta" ) != std::string::npos) {
        obj->SetStats( kTRUE );
        gStyle->SetOptStat( 1111111 );
        if(obj->GetEntries() > 0.) gPad->SetLogz(1);
      }

      if (o.name.find( "reportSummaryMap" ) == std::string::npos) {
        TAxis* xa = obj->GetXaxis();
        TAxis* ya = obj->GetYaxis();
        xa->SetTitleOffset(0.7);
        xa->SetTitleSize(0.065);
        xa->SetLabelSize(0.065);
        ya->SetTitleOffset(0.75);
        ya->SetTitleSize(0.065);
        ya->SetLabelSize(0.065);
      }

      // TODO: fix this in the right place?
      if( o.name.find( "endcapOccupancyMap" ) != std::string::npos ) obj->SetTitle("Endcap Digi Occupancy Map");

      //Separated out HitEfficiency maps to set scale
      if( o.name.find( "fficiency" ) != std::string::npos)
        {
          obj->SetOption("colz");
          obj->SetMaximum(1.0);
          obj->SetMinimum(0.95);
          return;
        }

      // FED things
      if( o.name.find( "FedChLErr" ) != std::string::npos )
        {
          gPad->SetGrid();
          obj->SetOption("colztext");
        }

      if( o.name.find( "FedETypeNErr" ) != std::string::npos )
        {
          gPad->SetGrid();
          gPad->SetLeftMargin(0.3);
          obj->SetOption("colztext");
          if( obj->GetEntries() > 0. ) gPad->SetLogz(1);
          return;
        }

      if( o.name.find( "FedChNErr" ) != std::string::npos )
        {
          gPad->SetGrid();
          gPad->SetRightMargin(0.15);
          gStyle->SetPalette(1);
          obj->SetOption("colztext");
          if( obj->GetEntries() > 0. ) gPad->SetLogz(1);
        }
      
      if( o.name.find( "avgfedDigiOccvsLumi" ) != std::string::npos )
        {
          obj->SetOption("colz");
          obj->SetMinimum(0.00001);
          obj->SetMaximum(0.8);
          int currentX = (int) obj->FindLastBinAbove(0.001)+1;
          obj->GetXaxis()->SetRange(1,currentX);
          return;
        }

      TH2F* obj2 = dynamic_cast<TH2F*>( o.object );

      if( o.name.find( "reportSummaryMap" ) != std::string::npos )
        {
          gPad->SetGrid();
          if(obj->GetNbinsX()==7) gPad->SetLeftMargin(0.3);
          dqm::utils::reportSummaryMapPalette(obj2);
          if(obj->GetNbinsX()>10){
            //Look at last filled bin (above -0.99) and use to zoom in on plot
            int currentX = (int) obj->FindLastBinAbove(-0.99)+1;
            obj->GetXaxis()->SetRange(1,currentX);}
          return;
        }
    }

  void postDrawTH2( TCanvas * /*c*/, const VisDQMObject &o )
    {
      TH2* obj = dynamic_cast<TH2*>( o.object );
      assert( obj );
      // Add Th2 post-draw code here.

      // WTH in postdraw? works in pre for TH1.
      TAxis* xa = obj->GetXaxis();
      TAxis* ya = obj->GetYaxis();
      xa->SetTitleSize(0.04);
      xa->SetLabelSize(0.03);
      ya->SetTitleSize(0.04);
      ya->SetLabelSize(0.03);
      TGaxis::SetMaxDigits(3);

   }


  void preDrawTH1( TCanvas *, const VisDQMObject &o )
    {
      TH1* obj = dynamic_cast<TH1*>( o.object );
      assert( obj );

      // This applies to all
      gStyle->SetOptStat(111);
      TAxis* xa = obj->GetXaxis();
      TAxis* ya = obj->GetYaxis();
      xa->SetTitleOffset(0.7);
      xa->SetTitleSize(0.04);
      xa->SetLabelSize(0.03);
      ya->SetTitleOffset(0.75);
      ya->SetTitleSize(0.04);
      ya->SetLabelSize(0.03);
      TGaxis::SetMaxDigits(3);

      // Always include 0.
      if( obj->GetMinimum() > 0.) obj->SetMinimum(0.);

      // Ranges for specific histograms.
      if( o.name.find( "adcCOMB" ) != std::string::npos && obj->GetEntries() > 0. ){ obj->SetMinimum(1.0); gPad->SetLogy(1); }
      if( o.name.find( "chargeCOMB" ) != std::string::npos && obj->GetEntries() > 0. ){ obj->SetMinimum(1.0); obj->GetXaxis()->SetRange(1,51); gPad->SetLogy(1); }
      if( o.name.find( "OnTrack/charge_siPixelClusters" ) != std::string::npos ){ obj->GetXaxis()->SetRange(1,51); }
      if( o.name.find( "OffTrack/charge_siPixelClusters" ) != std::string::npos ){ obj->GetXaxis()->SetRange(1,51); }
      if( o.name.find( "OnTrack/size_siPixelClusters" ) != std::string::npos ){ obj->GetXaxis()->SetRange(1,41); }
      if( o.name.find( "OffTrack/size_siPixelClusters" ) != std::string::npos ){ obj->GetXaxis()->SetRange(1,41); }

      // TODO: With SetLogy the minimum should always be forced non-0. Probably broken here.
      if( o.name.find( "barrelEventRate" ) != std::string::npos && obj->GetEntries() > 0. ) {gPad->SetLogx(1); gPad->SetLogy(1); gPad->SetTopMargin(0.15); gPad->SetRightMargin(0.15); }
      if( o.name.find( "endcapEventRate" ) != std::string::npos && obj->GetEntries() > 0. ) {gPad->SetLogx(1); gPad->SetLogy(1); gPad->SetTopMargin(0.15); gPad->SetRightMargin(0.15); }

      if( o.name.find( "noOccROCsBarrel" ) != std::string::npos ){ float currentX = (float) obj->GetBinCenter(obj->FindLastBinAbove(1.0))+5.; obj->GetXaxis()->SetRangeUser(0.,currentX);obj->GetYaxis()->SetRangeUser(100.,300.);}
      if( o.name.find( "noOccROCsEndcap" ) != std::string::npos ){ float currentX = (float) obj->GetBinCenter(obj->FindLastBinAbove(1.0))+5.; obj->GetXaxis()->SetRangeUser(0.,currentX);obj->GetYaxis()->SetRangeUser(0.,50.);}
      if( o.name.find( "FEDEntries" ) != std::string::npos ) gStyle->SetOptStat(0);
//       if( o.name.find( "size_siPixelClusters" ) != std::string::npos && obj->GetEntries() > 0. ) gPad->SetLogx(1);
      if( o.name.find( "OnTrack" ) != std::string::npos && o.name.find( "charge" ) != std::string::npos ) obj->SetTitle("ClusterCharge_OnTrack");
      if( o.name.find( "OnTrack" ) != std::string::npos && o.name.find( "size" ) != std::string::npos ) obj->SetTitle("ClusterSize_OnTrack");
      if( o.name.find( "OffTrack" ) != std::string::npos && o.name.find( "charge" ) != std::string::npos ) obj->SetTitle("ClusterCharge_OffTrack");
      if( o.name.find( "OffTrack" ) != std::string::npos && o.name.find( "size" ) != std::string::npos ) obj->SetTitle("ClusterSize_OffTrack");
      if( o.name.find( "SUMDIG_adc_Barrel" ) != std::string::npos ){ obj->SetMinimum(40.); obj->SetMaximum(155.); }
      if( o.name.find( "SUMDIG_ndigis_Barrel" ) != std::string::npos ){ obj->SetMaximum(20.); }
      if( o.name.find( "SUMDIG_adc_Endcap" ) != std::string::npos ){ obj->SetMinimum(45.); obj->SetMaximum(180.); }
      if( o.name.find( "SUMDIG_ndigis_Endcap" ) != std::string::npos ){ obj->SetMaximum(8.); }
      if( o.name.find( "SUMCLU_charge_Barrel" ) != std::string::npos ){ obj->SetMaximum(140.); }
      if( o.name.find( "SUMCLU_nclusters_Barrel" ) != std::string::npos ){ obj->SetMaximum(7.); }
      if( o.name.find( "SUMCLU_size_Barrel" ) != std::string::npos ){obj->SetMaximum(11.); }
      if( o.name.find( "SUMCLU_charge_Endcap" ) != std::string::npos ){ obj->SetMaximum(65.); }
      if( o.name.find( "SUMCLU_nclusters_Endcap" ) != std::string::npos ){ obj->SetMaximum(4.); }
      if( o.name.find( "SUMCLU_size_Endcap" ) != std::string::npos ){ obj->SetMaximum(4.); }
      if( o.name.find( "SUMOFF_adc_Barrel" ) != std::string::npos ){ obj->SetMinimum(-5.0); obj->SetMaximum(150.); }
      if( o.name.find( "SUMOFF_ndigis_Barrel" ) != std::string::npos ){ obj->SetMinimum(-5.0); obj->SetMaximum(60.0); }
      if( o.name.find( "SUMOFF_adc_Endcap" ) != std::string::npos ){ obj->SetMinimum(-10.0); obj->SetMaximum(150.); }
      if( o.name.find( "SUMOFF_ndigis_Endcap" ) != std::string::npos ){ obj->SetMinimum(-1.0); obj->SetMaximum(12.); }
      if( o.name.find( "SUMOFF_charge_OnTrack_Barrel" ) != std::string::npos ){ obj->SetMinimum(-5.); obj->SetMaximum(40.); }
      if( o.name.find( "SUMOFF_nclusters_OnTrack_Barrel" ) != std::string::npos ){ obj->SetMinimum(-1.0); obj->SetMaximum(6.0); }
      if( o.name.find( "SUMOFF_size_OnTrack_Barrel" ) != std::string::npos ){ obj->SetMinimum(-1.); obj->SetMaximum(8.); }
      if( o.name.find( "SUMOFF_charge_OnTrack_Endcap" ) != std::string::npos ){ obj->SetMinimum(-5.); obj->SetMaximum(45.); }
      if( o.name.find( "SUMOFF_nclusters_OnTrack_Endcap" ) != std::string::npos ){ obj->SetMinimum(-0.1); obj->SetMaximum(2.5); }
      if( o.name.find( "SUMOFF_size_OnTrack_Endcap" ) != std::string::npos ){ obj->SetMinimum(-0.1); obj->SetMaximum(4.); }
    }

  void postDrawTH1( TCanvas *, const VisDQMObject &o )
    {
      if (o.flags == 0) return;

      TH1* obj = dynamic_cast<TH1*>( o.object );
      assert( obj );

      // put EXTEND marker for phase1
      putMarkers(obj);

      // Upper/Lower limit decoration for SUMOFFs.
      if( o.name.find( "SUMOFF_adc_Barrel" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,85.,193.,85.);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,115.,193.,115.);
      }
      else if( o.name.find( "SUMDIG_adc_Barrel" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,70.,769.,70.);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,120.,769.,120.);
      }
      else if( o.name.find( "SUMOFF_adc_Endcap" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,95.,97.,95.);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,130.,97.,130.);
      }
      else if( o.name.find( "SUMDIG_adc_Endcap" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,85.,673.,85.);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,120.,673.,120.);
      }
      else if( o.name.find( "SUMOFF_ndigis_Barrel" ) != std::string::npos ){
        TLine tl; tl.SetLineColor(4); tl.DrawLine(1.,5.0,193.,5.0);
        TLine t2; t2.SetLineColor(4); t2.DrawLine(1.,50.0,193.,50.0);
      }
      else if( o.name.find( "SUMDIG_ndigis_Barrel" ) != std::string::npos ){
        TLine tl; tl.SetLineColor(4); tl.DrawLine(1.,4.5,769.,4.5);
        TLine t2; t2.SetLineColor(4); t2.DrawLine(1.,16.5,769.,16.5);
      }
      else if( o.name.find( "SUMOFF_ndigis_Endcap" ) != std::string::npos ){
        TLine tl; tl.SetLineColor(4); tl.DrawLine(1.,3.5,97.,3.5);
        TLine t2; t2.SetLineColor(4); t2.DrawLine(1.,8.0,97.,8.0);
      }
      else if( o.name.find( "SUMDIG_ndigis_Endcap" ) != std::string::npos ){
        TLine tl; tl.SetLineColor(4); tl.DrawLine(1.,3.2,673.,3.2);
        TLine t2; t2.SetLineColor(4); t2.DrawLine(1.,7.0,673.,7.0);
      }
      else if( o.name.find( "SUMOFF_charge_OnTrack_Barrel" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,12.0,193.,12.0);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,35.0,193.,35.0);
      }
      else if( o.name.find( "SUMOFF_nclusters_OnTrack_Barrel" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,1.0,193.,1.0);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,5.0,193.,5.0);
      }
      else if( o.name.find( "SUMOFF_size_OnTrack_Barrel" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,2.5,193.,2.5);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,6.1,193.,6.1);
      }
      else if( o.name.find( "SUMCLU_charge_Barrel" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,35.,769.,35.);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,90.,769.,90.);
      }
      else if( o.name.find( "SUMCLU_nclusters_Barrel" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,1.5,769.,1.5);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,5.4,769.,5.4);
      }
      else if( o.name.find( "SUMCLU_size_Barrel" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,2.5,769.,2.5);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,8.5,769.,8.5);
      }
      else if( o.name.find( "SUMOFF_charge_OnTrack_Endcap" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,15.,97.,15.);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,27.,97.,27.);
      }
      else if( o.name.find( "SUMOFF_nclusters_OnTrack_Endcap" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,1.15,97.,1.15);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,1.8,97.,1.8);
      }
      else if( o.name.find( "SUMOFF_size_OnTrack_Endcap" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,1.3,97.,1.3);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,2.2,97.,2.2);
      }
      else if( o.name.find( "SUMCLU_charge_Endcap" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,23.,673.,23.);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,38.,673.,38.);
      }
      else if( o.name.find( "SUMCLU_nclusters_Endcap" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,1.2,673.,1.2);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,3.2,673.,3.2);
      }
      else if( o.name.find( "SUMCLU_size_Endcap" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,1.9,673.,1.9);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,3.0,673.,3.0);
      }
    }

};

static SiPixelRenderPlugin instance;
