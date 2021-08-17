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

    gPad->SetGridx();
    gPad->SetGridy();
  }

  void postDrawTH1F(TCanvas *c, const VisDQMObject &o)
  {
    TH1F* obj = dynamic_cast<TH1F*>(o.object);
    assert(obj);

    if (TPRegexp("^GEM/Efficiency/type\\d/Efficiency/muon_\\w+_GE(\\+|\\-)\\d1(?:_matched)?$").MatchB(o.name))
    {
      obj->SetOption("hist E");
      gStyle->SetOptStat("euo");

      obj->SetLineColor(602);
      obj->SetFillColorAlpha(602, 0.3);

      if (auto stats = dynamic_cast<TPaveStats*>(obj->GetListOfFunctions()->FindObject("stats")))
      {
        stats->SetY1NDC(0.905);
        stats->SetY2NDC(1.0);
      }

    }
    else if (TPRegexp("^GEM/Efficiency/type\\d/Resolution/(residual|pull)_\\w+_GE(\\+|\\-)\\d1_R\\d$").MatchB(o.name))
    {
      obj->SetOption("hist E");
      gStyle->SetOptStat("emruos");

      obj->SetLineColor(602);
      obj->SetFillColorAlpha(602, 0.3);

      if (auto stats = dynamic_cast<TPaveStats*>(obj->GetListOfFunctions()->FindObject("stats")))
      {
        stats->SetY1NDC(0.905);
        stats->SetY2NDC(1.0);
      }

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

    if (TPRegexp("^GEM/Efficiency/type\\d/Efficiency/detector_GE(\\+|\\-)\\d1(?:matched_)?$").MatchB(o.name))
    {
      obj->SetOption("colz");
      gStyle->SetOptStat("e");
    }
    else if (TPRegexp("^GEM/Efficiency/type\\d/Efficiency/eff_detector_GE(\\+|\\-)\\d1$").MatchB(o.name))
    {
      obj->SetOption("colz");
      gStyle->SetOptStat(0);

      obj->SetNdivisions(-obj->GetNbinsX(), "Y"); // use a negative number to turn off ndivisios optimization.
      obj->SetNdivisions(-obj->GetNbinsY(), "X");

      obj->SetMinimum(0.80);
      obj->SetMaximum(1.00);

      gStyle->SetGridWidth(3);
    }
    else if (TPRegexp("^GEM/Efficiency/type\\d/Resolution/residual_rphi_(mean|stddev|skewness)$").MatchB(o.name))
    {
      obj->SetOption("colz text");
      obj->SetStats(false);
      gStyle->SetOptStat(0);

      obj->SetNdivisions(-obj->GetNbinsX(), "Y"); // use a negative number to turn off ndivisios optimization.
      obj->SetNdivisions(-obj->GetNbinsY(), "X");

      gStyle->SetGridStyle(1);
      gStyle->SetGridWidth(3);
      gStyle->SetPaintTextFormat(".3f");
    }
    else if (TPRegexp("^GEM/RecHits/rphi_occ_[\\w\\W]+$").Match(o.name))
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
    else if (TPRegexp("^GEM/EventInfo/vfat_statusSummary_[\\w\\W]+$").Match(o.name))
    {
      Int_t arrCol[ 3 ] = { 3, 2, 5 };  // 1: Green(=3), 2: Red(=2), 3: Yellow(=5)
      gStyle->SetPalette(3, arrCol);
      obj->SetMinimum(1.0);
      obj->SetMaximum(3.0);
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
    
    if (TPRegexp("^GEM/DAQStatus/amc13_status$").Match(o.name)) {
      obj->GetXaxis()->SetBinLabel(1, "GE11-M");
    }
    if (TPRegexp("^GEM/DAQStatus/amc_status_GE11-N$").Match(o.name)) {
      obj->SetTitle("AMC Status GE11-M");
    }

    c->SetGridx();
    c->SetGridy();
  }

  void postDrawTProfile(TCanvas *c, const VisDQMObject &o)
  {
    TProfile* obj = dynamic_cast<TProfile*>(o.object);
    assert(obj);

    if (TPRegexp("^GEM/Efficiency/type\\d/Efficiency/eff_muon_\\w+_GE(\\+|\\-)\\d1").MatchB(o.name))
    {
      obj->SetOption("E");
      obj->SetStats(false);
      gStyle->SetOptStat(0);

      obj->SetMinimum(-0.05);
      obj->SetMaximum(1.05);
      obj->SetLineColor(kRed);
      obj->SetLineWidth(2);
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

  int drawTimeHisto(TH2F *h2Curr)
  {
    std::string strNewName = std::string(h2Curr->GetName()).substr(std::string("per_time_").size());
    std::string strTmpPrefix = "tmp_";

    Int_t nNbinsX = h2Curr->GetNbinsX();
    Int_t nNbinsY = h2Curr->GetNbinsY();
    Int_t nNbinsXActual = 0;

    for ( nNbinsXActual = 0 ; nNbinsXActual < nNbinsX ; nNbinsXActual++ )
    {
      if ( h2Curr->GetBinContent(nNbinsXActual + 1, 0) <= 0 ) break;
    }

    std::string strTitle = std::string(h2Curr->GetTitle());

    //std::string strAxisX = h2Curr->GetXaxis()->GetTitle();
    std::string strAxisX = "Bin per " + std::to_string((Int_t)h2Curr->GetBinContent(0, 0)) + " events";
    std::string strAxisY = h2Curr->GetYaxis()->GetTitle();
    //strTitle += ";" + strAxisX + ";" + strAxisY;

    strTitle = "";
    TH2F *h2New = new TH2F(( strTmpPrefix + strNewName ).c_str(), strTitle.c_str(),
        nNbinsXActual, 0.0, (Double_t)nNbinsXActual, nNbinsY, 0.0, (Double_t)nNbinsY);

    h2New->GetXaxis()->SetTitle(strAxisX.c_str());
    h2New->GetYaxis()->SetTitle(strAxisY.c_str());

    for ( Int_t i = 1 ; i <= nNbinsY ; i++ )
    {
      std::string strLabel = h2Curr->GetYaxis()->GetBinLabel(i);
      if ( !strLabel.empty() ) h2New->GetYaxis()->SetBinLabel(i, strLabel.c_str());
    }

    for ( Int_t j = 0 ; j <= nNbinsY ; j++ )
    {
      for ( Int_t i = 1 ; i <= nNbinsXActual ; i++ )
      {
        h2New->SetBinContent(i, j, h2Curr->GetBinContent(i, j));
      }
    }

    h2New->Draw("colz");

    return 0;
  };
};

//----------------------------------------------------------------------------------------------------
static GEMRenderPlugin instance;
