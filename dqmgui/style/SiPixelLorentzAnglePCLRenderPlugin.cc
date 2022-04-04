/*!
  \file SiPixelLorentzAnglePCLRenderPlugin
  \brief RenderPlugin for SiPixelLorentzAngle PCL ALCAPROMPT inspection

  \author Marco Musich
*/

#include "DQM/DQMRenderPlugin.h"
#include "utils.h"
#include "TCanvas.h"
#include "TF1.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TProfile.h"
#include "TObjString.h"
#include "TProfile2D.h"
#include "TStyle.h"
#include "TGaxis.h"
#include "TPaveStats.h"
#include "TList.h"
#include "TLine.h"
#include "TLatex.h"
#include <cassert>

class SiPixelLorentzAnglePCLRenderPlugin : public DQMRenderPlugin
{
  
  int palette_kry[256];
  int palette_yrk[256];

public:

  virtual void initialise (int, char **)
  {
  }

  virtual bool applies(const VisDQMObject &o, const VisDQMImgInfo &)
  {
    if(o.name.find( "AlCaReco/SiPixelLorentzAngle" ) != std::string::npos)
      return true;

    else return false;
  }

  virtual void preDraw(TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &, VisDQMRenderInfo &)
  {
    c->cd();

    if( dynamic_cast<TH1F*>( o.object ) )
    {
      this->preDrawTH1F( c, o );
    }
    else if( dynamic_cast<TH2F*>( o.object ) )
    {
      this->preDrawTH2F( c, o );
    }
    else if( dynamic_cast<TProfile*>( o.object ) )
    {
      this->preDrawTProfile( c, o );
    }
    else if( dynamic_cast<TProfile2D*>( o.object ) )
    {
      this->preDrawTProfile2D( c, o );
    }
  }

  virtual void postDraw(TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &)
  {
    c->cd();

    if( dynamic_cast<TH1F*>( o.object ) )
    {
      this->postDrawTH1F( c, o );
    }
    else if( dynamic_cast<TH2F*>( o.object ) )
    {
      this->postDrawTH2F( c, o );
    }
    else if( dynamic_cast<TProfile*>( o.object ) )
    {
      this->postDrawTProfile( c, o );
    }
    else if( dynamic_cast<TProfile2D*>( o.object ) )
    {
      this->postDrawTProfile2D( c, o );
    }
  }

private:

  void preDrawTH1F(TCanvas *c, const VisDQMObject &o)
  {
    TH1F* obj = dynamic_cast<TH1F*>( o.object );
    assert( obj );  

    if( o.name.find("h_LAbySector")!= std::string::npos ||
	o.name.find("h_bySector")!= std::string::npos ||
	o.name.find("h_deltaLAbySector")!= std::string::npos){
      c->SetBottomMargin(0.25);
      return;
    }
  }

  void preDrawTH2F(TCanvas *c, const VisDQMObject &o)
  {
    TH2F* obj = dynamic_cast<TH2F*>( o.object );
    assert( obj );

    if( o.name.find("h_drift_depth")!= std::string::npos){
      obj->SetStats( kFALSE );
      gStyle->SetPalette(1,0);
      obj->SetOption("colz");
      return;
    }

    if( o.name.find("h_BPixnew_drift")!= std::string::npos){
      obj->SetStats( kFALSE );
      gStyle->SetPalette(1,0);
      obj->SetOption("colz");
      return;
    }

    if( o.name.find("h2_byLayer")!= std::string::npos){
      c->SetRightMargin(0.20);
      obj->SetStats( kFALSE );
      obj->SetContour(256);
      gStyle->SetPalette(57,0);
      obj->SetOption("colz");
   
      TAxis* xa = obj->GetXaxis();
      TAxis* ya = obj->GetYaxis();
      TAxis* za = obj->GetZaxis();

      xa->SetTitleOffset(0.9);
      xa->SetTitleSize(0.05);
      xa->SetLabelSize(0.04);
      xa->CenterTitle();
      
      ya->SetTitleOffset(0.9);
      ya->SetTitleSize(0.05);
      ya->SetLabelSize(0.04);
      ya->CenterTitle();
      
      za->SetTitleOffset(1.2);
      za->SetTitleSize(0.05);
      za->SetLabelSize(0.04);
      za->CenterTitle();

      gPad->Update();

      return;
    }

  }

  void preDrawTProfile(TCanvas *, const VisDQMObject &o)
  {
    TProfile* obj = dynamic_cast<TProfile*>( o.object );
    assert( obj );
  }

  void preDrawTProfile2D(TCanvas *, const VisDQMObject &o)
  {
    TProfile2D* obj = dynamic_cast<TProfile2D*>( o.object );
    assert( obj );
  }

  void postDrawTH1F(TCanvas *, const VisDQMObject &o)
  {
    TH1F* obj = dynamic_cast<TH1F*>( o.object );
    assert( obj );
    
    TAxis* xa = obj->GetXaxis();
    TAxis* ya = obj->GetYaxis();

    xa->SetTitleOffset(0.9);
    xa->SetTitleSize(0.05);
    xa->SetLabelSize(0.04);
    xa->CenterTitle();

    ya->SetTitleOffset(0.9);
    ya->SetTitleSize(0.05);
    ya->SetLabelSize(0.04);
    ya->CenterTitle();

    double p0 = 0.;
    double e0 = 0.;
    double p1 = 0.;
    double e1 = 0.;
    double p2 = 0.;
    double e2 = 0.;
    double p3 = 0.;
    double e3 = 0.;
    double p4 = 0.;
    double e4 = 0.;
    double p5 = 0.;
    double e5 = 0.;
    double chi2 = 0.;
    int ndf = 0;
    //double prob = 0.;

    TF1* fit = (TF1*)obj->GetListOfFunctions()->FindObject("f1");
    if(fit!=nullptr){
      TF1* f1 = new TF1("f1", "[0] + [1]*x + [2]*x*x + [3]*x*x*x + [4]*x*x*x*x + [5]*x*x*x*x*x", 5., 280.);
      f1->SetParName(0, "offset");
      f1->SetParName(1, "tan#theta_{LA}");
      f1->SetParName(2, "quad term");
      f1->SetParName(3, "cubic term");
      f1->SetParName(4, "quartic term");
      f1->SetParName(5, "quintic term");
     
      p0 = fit->GetParameter(0);
      e0 = fit->GetParError(0);
      p1 = fit->GetParameter(1);
      e1 = fit->GetParError(1);
      p2 = fit->GetParameter(2);
      e2 = fit->GetParError(2);
      p3 = fit->GetParameter(3);
      e3 = fit->GetParError(3);
      p4 = fit->GetParameter(4);
      e4 = fit->GetParError(4);
      p5 = fit->GetParameter(5);
      e5 = fit->GetParError(5);
      chi2 = fit->GetChisquare();
      ndf  = fit->GetNDF();
      //prob = fit->GetProb();

      f1->SetParameter(0,p0);
      f1->SetParError(0, e0);
      f1->SetParameter(1,p1);
      f1->SetParError(1, e1);
      f1->SetParameter(2,p2);
      f1->SetParError(2, e2);
      f1->SetParameter(3,p3);
      f1->SetParError(3, e3);
      f1->SetParameter(4,p4);
      f1->SetParError(4, e4);
      f1->SetParameter(5,p5);
      f1->SetParError(5, e5);
      
      obj->GetListOfFunctions()->Remove(fit);
      f1->SetLineColor(kBlue);
      f1->SetLineWidth(4);
      f1->SetLineStyle(9);
      f1->SetRange(5.,280.);
      f1->Update();
      f1->Draw("same");
    }

    gPad->Update();
    if( o.name.find("h_mean")!= std::string::npos ||
	o.name.find("h_BPixnew_mean")!= std::string::npos ){
      obj->SetMarkerStyle(20);
      obj->SetMarkerSize(1);
      TPaveStats* st = (TPaveStats*)obj->GetListOfFunctions()->FindObject("stats");
      if(st!=nullptr)  {
	gStyle->SetOptStat(0);
	TPaveText* pt = new TPaveText();
	pt->SetBorderSize(0);

	// FIXME: THIS DOES WORK ONLY FOR PHASE-1
	double half_width = 0.0285 / 2 * 10000.;  // pixel width in units of micro meter 
	double f1_halfwidth = p0 + p1 * half_width + p2 * pow(half_width, 2) + p3 * pow(half_width, 3) +
	  p4 * pow(half_width, 4) + p5 * pow(half_width, 5);
	double f1_zerowidth = p0;
	// tan_LA = (f1(x = half_width) - f1(x = 0)) / (half_width - 0)
	double tan_LA = (f1_halfwidth - f1_zerowidth) / half_width; 

	pt->AddText(Form("tan#theta_{L}: %.3f",tan_LA));
	pt->AddText(Form("#chi^{2}/ndf: %.2f/%i",chi2,ndf));
	//pt->AddText(Form("Fit Prob: %.2f",prob));  generally 0
	pt->SetTextColor( obj->GetLineColor() );
	pt->SetX1NDC( .12 );
	pt->SetX2NDC( .35 );
	pt->SetY1NDC( .73 );
	pt->SetY2NDC( .87 );
	pt->Draw("same");
      }
    }

    if( o.name.find("h_LAbySector")!= std::string::npos ||
	o.name.find("h_bySector")!= std::string::npos ||
	o.name.find("h_deltaLAbySector")!= std::string::npos){
      gPad->Update();

      TAxis* xa = obj->GetXaxis();
      xa->LabelsOption("v");
      xa->SetLabelSize(0.03);
      xa->SetTitleOffset(2.5);

      float bounds[4]={7.5,15.5,23.5,31.5};
    
      TLatex Tl;
      Tl.SetTextAlign(11);
      Tl.SetTextColor(kRed);
      Tl.SetTextSize(0.04);

      TLine tl[4];
      for(unsigned int i=0;i<4;i++){
	tl[i].SetLineColor(kRed);
	tl[i].SetLineWidth(3);
	tl[i].SetLineStyle(7);
	tl[i].DrawLine(bounds[i],gPad->GetUymin(),bounds[i],gPad->GetUymax());

	Tl.DrawLatexNDC(0.01+gPad->GetLeftMargin()+0.167*i,0.86,Form("Layer %i",i+1));

      }
    }
  }

  void postDrawTH2F(TCanvas *, const VisDQMObject &o)
  {
    TH2F* obj = dynamic_cast<TH2F*>( o.object );
    assert( obj );
  }

  void postDrawTProfile(TCanvas *, const VisDQMObject &o)
  {
    TProfile* obj = dynamic_cast<TProfile*>( o.object );
    assert( obj );
  }

void postDrawTProfile2D(TCanvas *, const VisDQMObject &o)
  {
    TProfile2D* obj = dynamic_cast<TProfile2D*>( o.object );
    assert( obj );
  }
};

static SiPixelLorentzAnglePCLRenderPlugin instance;
