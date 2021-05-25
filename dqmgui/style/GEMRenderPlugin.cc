#include "DQM/DQMRenderPlugin.h"
 
#include "GEMRenderPlugin_SummaryChamber.h"

#include "TH1F.h"
#include "TH2F.h"
#include "TProfile.h"
#include "TCanvas.h"
#include "TPaveStats.h"

#include <cassert>

//----------------------------------------------------------------------------------------------------

class GEMRenderPlugin : public DQMRenderPlugin
{

public:
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

    // NOTE
    if (TPRegexp("^GEM/GEMEfficiency/\\w+Muon/Efficiency/muon_\\w+_(?:matched_)?ge(\\+|\\-)\\d1_(odd|even)$").MatchB(o.name))
    {
      // e.g. GEM/GEMEfficiency/StandaloneMuon/Efficiency/muon_eta_ge-11_odd
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
    else if (TPRegexp("^GEM/GEMEfficiency/\\w+Muon/Resolution/(residual|pull)_\\w+_ge(\\+|\\-)\\d1_(odd|even)_ieta\\d$").MatchB(o.name))
    {
      // e.g. GEM/GEMEfficiency/StandaloneMuon/Resolution/pull_x_ge-11_even_ieta1
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
    else if (TPRegexp("^GEM/digi/total_strips_per_event_[\\w\\W]+$").Match(o.name))
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

    if (o.name.find("GEM/StatusDigi") != std::string::npos)
    {
      obj->SetStats(false);
    }

    if (o.name.find("GEM/StatusDigi/per_time_") != std::string::npos)
    {
      drawTimeHisto(dynamic_cast<TH2F*>(o.object));
    }

    if (TPRegexp("GEM/GEMEfficiency/\\w+Muon/Efficiency/detector_(?:matched_)?ge(\\+|\\-)\\d1$").MatchB(o.name))
    {
      // e.g. GEM/GEMEfficiency/StandaloneMuon/Efficiency/detector_matched_ge-11
      obj->SetOption("colz");
      gStyle->SetOptStat("e");
    }
    else if (TPRegexp("GEM/GEMEfficiency/\\w+Muon/Efficiency/eff_detector_ge(\\+|\\-)\\d1$").MatchB(o.name))
    {
      // e.g. GEM/GEMEfficiency/StandaloneMuon/Efficiency/eff_detector_ge-11
      obj->SetOption("colz");
      gStyle->SetOptStat(0);

      obj->SetMinimum(0.80);
      obj->SetMaximum(1.00);
    }
    else if (TPRegexp("GEM/GEMEfficiency/\\w+Muon/Resolution/residual_phi_ge(\\+|\\-)\\d1_(odd|even)$").MatchB(o.name))
    {
      // e.g. GEM/GEMEfficiency/StandaloneMuon/Resolution/residual_phi_ge-11_even
      obj->SetOption("colz text");
      obj->SetStats(false);
      gStyle->SetOptStat(0);

      obj->Scale(1000); // rad to mrad
      obj->GetYaxis()->SetBinLabel(1, "#splitline{Mean}{[mrad]}");
      obj->GetYaxis()->SetBinLabel(2, "#splitline{Std. Dev.}{[mrad]}");

      obj->SetNdivisions(-obj->GetNbinsX(), "Y"); // use a negative number to turn off ndivisios optimization.
      obj->SetNdivisions(-obj->GetNbinsY(), "X");

      gStyle->SetGridStyle(1);
      gStyle->SetGridWidth(3);
      gStyle->SetPaintTextFormat(".3f");
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

    c->SetGridx();
    c->SetGridy();
  }

  void postDrawTProfile(TCanvas *c, const VisDQMObject &o)
  {
    TProfile* obj = dynamic_cast<TProfile*>(o.object);
    assert(obj);

    if (TPRegexp("^GEM/GEMEfficiency/\\w+Muon/Efficiency/eff_muon_\\w+_ge(\\+|\\-)\\d1_(odd|even)").MatchB(o.name))
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
