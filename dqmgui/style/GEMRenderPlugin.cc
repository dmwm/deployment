#include "DQM/DQMRenderPlugin.h"
 
#include "GEMRenderPlugin_SummaryChamber.h"

#include "TH1F.h"
#include "TH2F.h"
#include "TProfile.h"
#include "TProfile2D.h"
#include "TCanvas.h"
#include "TPaveStats.h"

#include <cassert>

//----------------------------------------------------------------------------------------------------

class GEMRenderPlugin : public DQMRenderPlugin
{

public:
  int nInitColorStatus;
  
  GEMRenderPlugin() : DQMRenderPlugin() {
    nInitColorStatus = -1;
  };
  
  virtual bool applies(const VisDQMObject &o, const VisDQMImgInfo &) override
  {
    if ((o.name.find( "GEM/" ) != std::string::npos))
      return true;
    return false;
  }

  virtual void preDraw(TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &, VisDQMRenderInfo &) override
  {
    if (o.object == nullptr)
      return;

    c->cd();

    gStyle->SetOptStat(10);

    if (dynamic_cast<TH1F*>(o.object))
    {
      preDrawTH1F(c, o);
    }
    else if (dynamic_cast<TH2F*>(o.object))
    {
      preDrawTH2F(c, o);
    }
  }

  virtual void postDraw( TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &imgInfo ) override
  {
    if (o.object == nullptr)
      return;

    c->cd();

    gStyle->SetOptStat(10);

    if (o.name.rfind("summary_statusChamber") != std::string::npos ||
        o.name.rfind("reportSummaryMap")      != std::string::npos)
    {
      TH2* obj2 = dynamic_cast<TH2*>(o.object);
      if (obj2 == nullptr) return;
      
      summaryCh.drawStats(obj2);
      
      //obj2->SetStats(false);
      gStyle->SetOptStat("e");
      obj2->SetOption("");
      gPad->SetGridx();
      gPad->SetGridy();

      return;
    }
    else if (dynamic_cast<TH1F*>(o.object))
    {
      postDrawTH1F(c, o);
    }
    else if (dynamic_cast<TH2F*>(o.object))
    {
      postDrawTH2F(c, o, imgInfo);
    }
    else if (dynamic_cast<TProfile*>(o.object))
    {
      postDrawTProfile(c, o);
    }
    else if (dynamic_cast<TProfile2D*>(o.object))
    {
      postDrawTProfile2D(c, o);
    }
  }

private:
  SummaryChamber summaryCh;
  const int kEntriesColor_ = kAzure - 5;
  const int kEfficiencyColor_ = 46;

  void preDrawTH1F(TCanvas *, const VisDQMObject &o)
  {
    if (o.object == nullptr)
      return;

    bool setColor = true;
    if (o.name.rfind(" U") == o.name.size() - 2)
      setColor = false;
    if (o.name.rfind(" V") == o.name.size() - 2)
      setColor = false;
    if (o.name.find("events per BX") != std::string::npos)
      setColor = false;

    TH1F* obj = dynamic_cast<TH1F*>(o.object);
    assert(obj);

    if (setColor)
      obj->SetLineColor(2);

    obj->SetLineWidth(2);
  }

  void preDrawTH2F(TCanvas *, const VisDQMObject &o)
  {
    TH2F* obj = dynamic_cast<TH2F*>(o.object);
    assert(obj);

    obj->SetOption("colz");

    if (TPRegexp("^GEM/EventInfo/chamberStatus_inLumi_[\\w\\W]+$").MatchB(o.name))
    {
      drawLumiFunction(obj);
    }

    gPad->SetGridx();
    gPad->SetGridy();
  }

  void postDrawTH1F(TCanvas *c, const VisDQMObject &o)
  {
    TH1F* obj = dynamic_cast<TH1F*>(o.object);
    assert(obj);

    if (TPRegexp("^GEM/Efficiency/type\\d/Efficiency/muon_\\w+_GE\\d{1,2}-(P|M)(?:_matched)?$").MatchB(o.name))
    {
      // e.g. "GEM/Efficiency/type1/Efficiency/muon_eta_GE11-M"
      // offline
      obj->SetOption("hist E");
      gStyle->SetOptStat("euo");

      obj->SetLineColor(kEntriesColor_);
      obj->SetFillColorAlpha(kEntriesColor_, 0.3);

    }
    else if (TPRegexp("^GEM/Efficiency/type\\d/Efficiency/(chamber|ieta)_GE\\d{1,2}-(P|M)-L\\d(?:_matched)?$").MatchB(o.name))
    {
      // e.g. "GEM/Efficiency/type1/Efficiency/chamber_GE21-P-L2"
      // offline
      obj->SetOption("P");

      obj->SetMarkerStyle(4); //
      obj->SetMarkerSize(2);
      const int marker_color = TPRegexp("\\w_matched").MatchB(o.name) ? kEfficiencyColor_ : kEntriesColor_;
      obj->SetMarkerColor(marker_color);
      obj->SetLineColorAlpha(kEfficiencyColor_, 0.0);

      applyBinNumbering(obj, "x");
    }
    else if (TPRegexp("^GEM/Efficiency/type\\d/Resolution/(residual|pull)_\\w+_GE(\\+|\\-)\\d1_R\\d$").MatchB(o.name))
    {
      // Offline DQM

      obj->SetOption("hist E");
      gStyle->SetOptStat("emruos");

      obj->SetLineColor(kEntriesColor_);
      obj->SetFillColorAlpha(kEntriesColor_, 0.3);
    }
    else if (TPRegexp("^GEM/Digis/digis_per_[\\w\\W]+$").Match(o.name))
    {
      c->SetLogy(true);
    }
    else if (TPRegexp("^GEM/RecHits/rechits_per_[\\w\\W]+$").Match(o.name))
    {
      c->SetLogy(true);
    }
    else
    {
      gStyle->SetOptStat(10);
    }

    c->SetGridx();
    c->SetGridy();
  }

  void postDrawTH2F(TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &imgInfo)
  {
    TH2F* obj = dynamic_cast<TH2F*>(o.object);
    assert(obj);

    if (TPRegexp("^GEM/Efficiency/type\\d/Efficiency/detector_GE\\d{1,2}-(P|M)-L\\d(?:_matched)?$").MatchB(o.name))
    {
      // e.g. "GEM/Efficiency/type1/Efficiency/detector_GE11-P-L1"
      // Offline DQM
      obj->SetOption("colz");
      gStyle->SetOptStat("e");

      applyBinNumbering(obj, "x");
      applyBinNumbering(obj, "y");
    }
    else if (TPRegexp("^GEM/Efficiency/type\\d/Efficiency/eff_detector_GE\\d{1,2}-(P|M)-L\\d$").MatchB(o.name))
    {
      // e.g. "GEM/Efficiency/type1/Efficiency/eff_detector_GE11-P-L1"
      // Offline DQM
      obj->SetOption("colz");
      obj->SetMinimum(0.00);
      obj->SetMaximum(1.00);

      applyBinNumbering(obj, "x");
      applyBinNumbering(obj, "y");

      // turn off the stat box
      gStyle->SetOptStat(0);
      gStyle->SetGridWidth(3);
    }
    else if (TPRegexp("^GEM/Efficiency/type\\d/Resolution/residual_rphi_(mean|stddev|skewness)$").MatchB(o.name))
    {
      // Offline DQM
      obj->SetOption("colz text");

      const TString name{o.name};
      if (name.EndsWith("mean"))
      {
        obj->SetMaximum(0.2);
        obj->SetMinimum(-0.2);
      } else if (name.EndsWith("skewness"))
      {
        obj->SetMaximum(1);
        obj->SetMinimum(-1);
      }

      const int kNumColors = 255;
      obj->SetContour(kNumColors);

      const int kNumEndPointColors = 3;
      // blue-white-red palette for mean and skewness
      Double_t stops[kNumEndPointColors] = {0., .5, 1.};
      if (name.EndsWith("stddev")) {
        // white-red palette for stddev
        stops[1] = 0.0;
      }
      Double_t red[kNumEndPointColors]   = {0., 1., 1.};
      Double_t green[kNumEndPointColors] = {0., 1., 0.};
      Double_t blue[kNumEndPointColors]  = {1., 1., 0.};
      TColor::CreateGradientColorTable(kNumEndPointColors, stops, red, green, blue, kNumColors);

      gStyle->SetPaintTextFormat(".3f");

      // no stat box
      obj->SetStats(false);
      gStyle->SetOptStat(0);

      // grid
      obj->SetNdivisions(-obj->GetNbinsX(), "X");
      obj->SetNdivisions(-obj->GetNbinsY(), "Y");
      gStyle->SetGridStyle(1);
      gStyle->SetGridWidth(3);
    }
    else if (TPRegexp("^GEM/recHit/rechit_wheel_[\\w\\W]+$").Match(o.name))
    {
      float fR = obj->GetYaxis()->GetBinLowEdge(obj->GetNbinsY() + 1) * 1.1;
      float fRatioX = 1.0, fRatioY = 1.0, fRatio;
      if ( imgInfo.width > 0 && imgInfo.height > 0 ) {
        fRatio  = ( (float)imgInfo.width ) / ( (float)imgInfo.height );
        fRatioX = ( fRatio >= 1.0 ? fRatio : 1.0 );
        fRatioY = ( fRatio >= 1.0 ? 1.0    : 1.0 / fRatio );
      }
      auto hFrame = gPad->DrawFrame(-fR * fRatioX, -fR * fRatioY, fR * fRatioX, fR * fRatioY);
      hFrame->SetTitle(obj->GetTitle());
      hFrame->GetXaxis()->SetTitle(obj->GetXaxis()->GetTitle());
      hFrame->GetYaxis()->SetTitle(obj->GetYaxis()->GetTitle());
      obj->Draw("same colzpol");
    }
    else if (TPRegexp("^GEM/DAQStatus/vfat_statusSummary_[\\w\\W]+$").Match(o.name))
    {
      Int_t arrCol[ 2 ] = { 3, 2 };
      gStyle->SetPalette(2, arrCol);
      obj->SetMinimum(1.0);
      obj->SetMaximum(2.0);
      obj->SetOption("col");
    }
    else if (TPRegexp("^GEM/[\\w\\W]+/rphi_occ_[\\w\\W]+$").Match(o.name))
    {
      float fR = obj->GetYaxis()->GetBinLowEdge(obj->GetNbinsY() + 1) * 1.1;
      float fRatioX = 1.0, fRatioY = 1.0, fRatio;
      if ( imgInfo.width > 0 && imgInfo.height > 0 ) {
        fRatio  = ( (float)imgInfo.width ) / ( (float)imgInfo.height );
        fRatioX = ( fRatio >= 1.0 ? fRatio : 1.0 );
        fRatioY = ( fRatio >= 1.0 ? 1.0    : 1.0 / fRatio );
      }
      auto hFrame = gPad->DrawFrame(-fR * fRatioX, -fR * fRatioY, fR * fRatioX, fR * fRatioY);
      hFrame->SetTitle(obj->GetTitle());
      hFrame->GetXaxis()->SetTitle("X [cm]");
      hFrame->GetYaxis()->SetTitle("Y [cm]");
      obj->Draw("same colzpol");
    }
    else if (TPRegexp("^GEM/EventInfo/vfat_statusSummary_[\\w\\W]+$").Match(o.name))
    {
      Int_t arrCol[ 4 ] = { 3, 2, 5, 801 };  // 1: Green(=3), 2: Red(=2), 3: Yellow(=5), 4: Orange(=801)
      gStyle->SetPalette(4, arrCol);
      obj->SetMinimum(1.0);
      obj->SetMaximum(4.0);
      obj->SetOption("col");
    }
    else if (TPRegexp("^GEM/EventInfo/chamberStatus_inLumi_[\\w\\W]+$").Match(o.name))
    {
      Int_t arrCol[ 4 ] = { 3, 2, 5, 801 };  // 1: Green(=3), 2: Red(=2), 3: Yellow(=5), 4: Orange(=801)
      gStyle->SetPalette(4, arrCol);
      obj->SetMinimum(1.0);
      obj->SetMaximum(4.0);
      obj->SetOption("col");
    }
    
    if (TPRegexp("^GEM/DAQStatus/[\\w\\W]+_status$").Match(o.name) || 
        TPRegexp("^GEM/DAQStatus/[\\w\\W]+_status_[\\w\\W]+$").Match(o.name)) 
    {
      Int_t nNumGood = 20;
      
      if ( nInitColorStatus < 0 ) {
        Double_t arrdS[ 4 ] = { 0.0, ( 990.0 - nNumGood ) / 990, ( 990.0 - nNumGood + 1.0 ) / 990, 1.0 };
        Double_t arrdR[ 4 ] = { 1.0, 1.0, 1.0, 0.0 };
        Double_t arrdG[ 4 ] = { 1.0, 0.0, 1.0, 1.0 };
        Double_t arrdB[ 4 ] = { 0.0, 0.0, 0.0, 0.0 };
        nInitColorStatus = TColor::CreateGradientColorTable(5, arrdS, arrdR, arrdG, arrdB, 990);
      }
      
      auto nColorInit = nInitColorStatus;
      Int_t arrnPalette[ 990 ];
      for ( Int_t i = 0 ; i < 990 ; i++ ) arrnPalette[ i ] = nColorInit + i;
      gStyle->SetPalette(990, arrnPalette);
      
      Float_t fMax = obj->GetMaximum();
      obj->SetMaximum(fMax * 990.0 / ( 990.0 - nNumGood ));
      Float_t fL = fMax * ( 990.0 - nNumGood + 1 ) / ( 990.0 - nNumGood );
      for ( Int_t i = 0 ; i < obj->GetNbinsX() ; i++ ) {
        Float_t fVal = obj->GetBinContent(i + 1, 1);
        if ( fVal < 1.0 ) continue;
        obj->SetBinContent(i + 1, 1, fL + fVal * ( nNumGood - 1 ) / ( 990.0 - nNumGood ));
      }
      
      if ( TPRegexp("^GEM/DAQStatus/oh_status_[\\w\\W]+$").Match(o.name) ) {
        c->SetLeftMargin(0.200);
      } else {
        c->SetLeftMargin(0.135);
      }
    }

    c->SetGridx();
    c->SetGridy();
  }

  void postDrawTProfile(TCanvas *c, const VisDQMObject &o)
  {
    TProfile* obj = dynamic_cast<TProfile*>(o.object);
    assert(obj);

    // common cosmetics for the offlien DQM
    if (TPRegexp("^GEM/Efficiency/type\\d/Efficiency/eff_[\\S]+$").MatchB(o.name))
    {
      obj->SetOption("E");

      obj->SetMinimum(-0.02);
      obj->SetMaximum(1.02);

      obj->SetLineColor(kEfficiencyColor_);
      obj->SetLineWidth(2);

      // no stat box
      obj->SetStats(false);
      gStyle->SetOptStat(0);
    }

    if (TPRegexp("^GEM/Efficiency/type\\d/Efficiency/eff_(chamber|ieta)_GE\\d{1,2}-(P|M)-L\\d$").MatchB(o.name))
    {
      // e.g. "GEM/Efficiency/type1/Efficiency/eff_chamber_GE21-P-L2"
      applyBinNumbering(obj, "x");
    }
    else
    {
      obj->SetOption("E");
      gStyle->SetOptStat(10);
    }

    c->SetGridx();
    c->SetGridy();
  }

  void postDrawTProfile2D(TCanvas *c, const VisDQMObject &o)
  {
    TProfile2D* obj = dynamic_cast<TProfile2D*>(o.object);
    assert(obj);
    if (TPRegexp("^GEM/RecHits/rechit_average_[\\w\\W]+$").Match(o.name))
    {
      obj->SetOption("colz");
    }

    c->SetGridx();
    c->SetGridy();
  }

  void drawLumiFunction(TH2F *h2Curr)
  {
    Int_t nNbinsX = h2Curr->GetNbinsX();
    Int_t nNbinsXActual = 0;

    for ( ; nNbinsXActual < nNbinsX ; nNbinsXActual++ )
    {
      if ( h2Curr->GetBinContent(nNbinsXActual + 1, 0) <= 0 ) break;
    }
    h2Curr->GetXaxis()->SetRange(1, nNbinsXActual);
  };

  void applyBinNumbering(TH1* obj, const TString&& axis_name) {
    TAxis* axis = nullptr;
    if (axis_name.EqualTo("x"))
      axis = obj->GetXaxis();
    else if (axis_name.EqualTo("y"))
      axis = obj->GetYaxis();
    else
      return;

    if (axis == nullptr) {
      return;
    }

    const int nbins = axis->GetNbins();
    obj->SetNdivisions(-nbins, axis_name);
    for (int bin = 1; bin <= nbins; bin++) {
      const char* label = Form("%d", bin);
      axis->SetBinLabel(bin, label);
    }
  }
};

//----------------------------------------------------------------------------------------------------
static GEMRenderPlugin instance;
