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

class SiPixelRenderPlugin : public DQMRenderPlugin
{
public:
  virtual bool applies( const VisDQMObject &o, const VisDQMImgInfo & )
    {
      if( o.name.find( "Pixel/" ) != std::string::npos )
        return true;
      if( o.name.find( "PixelPhase1/" ) != std::string::npos )
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

      TH1* th1 = dynamic_cast<TH1*>(obj);
      TAxis* xa = th1->GetXaxis();
      TAxis* ya = th1->GetYaxis();
      xa->SetTitleSize(0.04);
      xa->SetLabelSize(0.03);
      ya->SetTitleSize(0.04);
      ya->SetLabelSize(0.03);
      TGaxis::SetMaxDigits(3);


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
      // TODO: maybe fix these in CMSSW?
      if( o.name.find( "adcCOMB" ) != std::string::npos && obj->GetEntries() > 0. ){ gPad->SetLogy(1); gPad->SetTopMargin(0.15); }
      if( o.name.find( "chargeCOMB" ) != std::string::npos && obj->GetEntries() > 0. ){ obj->GetXaxis()->SetRange(1,51); gPad->SetLogy(1); gPad->SetTopMargin(0.15); }
      if( o.name.find( "OnTrack/charge_siPixelClusters" ) != std::string::npos ){ obj->GetXaxis()->SetRange(1,51); }
      if( o.name.find( "OffTrack/charge_siPixelClusters" ) != std::string::npos ){ obj->GetXaxis()->SetRange(1,51); }
      if( o.name.find( "OnTrack/size_siPixelClusters" ) != std::string::npos ){ obj->GetXaxis()->SetRange(1,41); }
      if( o.name.find( "OffTrack/size_siPixelClusters" ) != std::string::npos ){ obj->GetXaxis()->SetRange(1,41); }
      if( o.name.find( "barrelEventRate" ) != std::string::npos && obj->GetEntries() > 0. ) {gPad->SetLogx(1); gPad->SetLogy(1); gPad->SetTopMargin(0.15); gPad->SetRightMargin(0.15); }
      if( o.name.find( "endcapEventRate" ) != std::string::npos && obj->GetEntries() > 0. ) {gPad->SetLogx(1); gPad->SetLogy(1); gPad->SetTopMargin(0.15); gPad->SetRightMargin(0.15); }
      if( o.name.find( "ALLMODS_chargeCOMB" ) != std::string::npos ) obj->GetXaxis()->SetRange(1,51);
      if( o.name.find( "noOccROCsBarrel" ) != std::string::npos ){ float currentX = (float) obj->GetBinCenter(obj->FindLastBinAbove(1.0))+5.; obj->GetXaxis()->SetRangeUser(0.,currentX);
        obj->GetYaxis()->SetRangeUser(250,350);}
      if( o.name.find( "noOccROCsEndcap" ) != std::string::npos ){ float currentX = (float) obj->GetBinCenter(obj->FindLastBinAbove(1.0))+5.; obj->GetXaxis()->SetRangeUser(0.,currentX);
        obj->GetYaxis()->SetRangeUser(300,350);}
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
      if( o.name.find( "SUMOFF_ndigis_Endcap" ) != std::string::npos ){ obj->SetMinimum(-1.0); obj->SetMaximum(8.); }
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

      // TODO: add EXTEND_* decorations for Phase1 here. 
      // (maybe as a function, TH2 could use it as well)

      // Upper/Lower limit decoration for SUMOFFs.
      if( o.name.find( "SUMOFF_adc_Barrel" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,85.,193.,85.);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,115.,193.,115.);
      }
      else if( o.name.find( "SUMDIG_adc_Barrel" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,85.,769.,85.);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,120.,769.,120.);
      }
      else if( o.name.find( "SUMOFF_adc_Endcap" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,95.,97.,95.);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,115.,97.,115.);
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
        obj->SetMaximum(8.);
        TLine tl; tl.SetLineColor(4); tl.DrawLine(1.,3.5,97.,3.5);
        TLine t2; t2.SetLineColor(4); t2.DrawLine(1.,6.,97.,6.);
      }
      else if( o.name.find( "SUMDIG_ndigis_Endcap" ) != std::string::npos ){
        TLine tl; tl.SetLineColor(4); tl.DrawLine(1.,3.2,673.,3.2);
        TLine t2; t2.SetLineColor(4); t2.DrawLine(1.,7.0,673.,7.0);
      }
      else if( o.name.find( "SUMOFF_charge_OnTrack_Barrel" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,22.5,193.,22.5);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,35.0,193.,35.0);
      }
      else if( o.name.find( "SUMOFF_nclusters_OnTrack_Barrel" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,1.2,193.,1.2);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,5.0,193.,5.0);
      }
      else if( o.name.find( "SUMOFF_size_OnTrack_Barrel" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,2.9,193.,2.9);
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
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,19.,97.,19.);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,27.,97.,27.);
      }
      else if( o.name.find( "SUMOFF_nclusters_OnTrack_Endcap" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,1.15,97.,1.15);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(1.,1.65,97.,1.65);
      }
      else if( o.name.find( "SUMOFF_size_OnTrack_Endcap" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(1.,1.7,97.,1.7);
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
      else if( o.name.find( "OnTrack/charge_siPixelClusters" ) != std::string::npos ){
        Int_t ibin = obj->GetMaximumBin();
        Double_t val = obj->GetBinContent(ibin);
        TLine tl; tl.SetLineColor(4); tl.DrawLine(21.,0.,21.,val);
      }
      else if( o.name.find( "averageDigiOccupancy" ) != std::string::npos ){
        TLine tl; tl.SetLineColor(4); tl.DrawLine(-0.5,0.6,39.5,0.6);
        TLine t2; t2.SetLineColor(4); t2.DrawLine(-0.5,1.6,39.5,1.6);
      }
      else if( o.name.find( "noOccROCsBarrel" ) != std::string::npos ){
        float currentX = (float) obj->GetBinCenter(obj->FindLastBinAbove(1.0))+5.;
        TLine tl; tl.SetLineColor(4); tl.SetLineStyle(2); tl.DrawLine(0.0,267.0,currentX,267.0);
      }
      else if( o.name.find( "noOccROCsEndcap" ) != std::string::npos ){
        float currentX = (float) obj->GetBinCenter(obj->FindLastBinAbove(1.0))+5.;
        TLine tl; tl.SetLineColor(4); tl.SetLineStyle(2); tl.DrawLine(0.0,314.0,currentX,314.0);
      }
    }

  void postDrawTH2( TCanvas * /*c*/, const VisDQMObject &o )
    {
      TH2* obj = dynamic_cast<TH2*>( o.object );
      assert( obj );
      // Add Th2 post-draw code here.
    }

};

static SiPixelRenderPlugin instance;
