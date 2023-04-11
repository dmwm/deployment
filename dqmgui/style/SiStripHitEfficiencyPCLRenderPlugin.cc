/*!
  \file SiStripHitEfficiencyPCLRenderPlugin
  \brief RenderPlugin for SiStripHitEfficiency PCL ALCAPROMPT inspection

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

class SiStripHitEfficiencyPCLRenderPlugin : public DQMRenderPlugin
{
  
public:

  virtual void initialise (int, char **)
  {
  }

  virtual bool applies(const VisDQMObject &o, const VisDQMImgInfo &)
  {
    if(o.name.find( "AlCaReco/SiStripHitEfficiency" ) != std::string::npos)
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

    if (o.name.find("EfficiencySummary/eff_") != std::string::npos) {
      c->SetBottomMargin(0.15);
      return;
    }

  }

  void preDrawTH2F(TCanvas *, const VisDQMObject &o)
  {
    TH2F* obj = dynamic_cast<TH2F*>( o.object );
    assert( obj );
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
    
    if( (o.name.find("EfficiencySummaryVs") != std::string::npos)){

      if(o.name.find("Bx") == std::string::npos){
	obj->SetLineWidth(2);
	obj->SetLineColor(kBlack);
      }

      obj->SetStats( kFALSE );
      gPad->SetGrid();

      TAxis* xa = obj->GetXaxis();
      TAxis* ya = obj->GetYaxis();

      xa->SetTitleOffset(0.9);
      xa->SetTitleSize(0.05);
      xa->SetLabelSize(0.04);
      xa->CenterTitle();

      ya->SetRangeUser(0.9,1.0);
      ya->SetTitleOffset(0.9);
      ya->SetTitleSize(0.05);
      ya->SetLabelSize(0.04);
      ya->CenterTitle();
    }

    if (o.name.find("EfficiencySummary/eff_") != std::string::npos) {

      obj->SetStats( kFALSE );

      if(o.name.find("all") != std::string::npos){
	obj->SetLineColor(kBlack);
	obj->SetMarkerColor(kBlack);           
	obj->SetMarkerStyle(21);
      }

      if(o.name.find("good") != std::string::npos){
	obj->SetLineColor(kRed);
	obj->SetMarkerColor(kRed);           
	obj->SetMarkerStyle(20);	
      }

      gPad->SetGrid();

      TAxis* xa = obj->GetXaxis();
      TAxis* ya = obj->GetYaxis();

      xa->LabelsOption("v");
      xa->SetTitleOffset(0.9);
      xa->SetTitleSize(0.05);
      xa->SetLabelSize(0.04);
      xa->CenterTitle();

      ya->SetRangeUser(0.9,1.0);
      ya->SetTitleOffset(0.9);
      ya->SetTitleSize(0.05);
      ya->SetLabelSize(0.04);
      ya->CenterTitle();
    }

    if( (o.name.find("Resolutions") != std::string::npos)){
      gPad->SetLogy();  	
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

    if( o.name.find("EfficiencySummaryVs") != std::string::npos){

      obj->SetStats( kFALSE );
      gPad->SetGrid();

      if(o.name.find("Bx") == std::string::npos){
	obj->SetLineWidth(2);
	obj->SetLineColor(kBlack);
      }

      TAxis* xa = obj->GetXaxis();
      TAxis* ya = obj->GetYaxis();

      xa->SetTitleOffset(0.9);
      xa->SetTitleSize(0.05);
      xa->SetLabelSize(0.04);
      xa->CenterTitle();

      ya->SetRangeUser(0.9,1.0);
      ya->SetTitleOffset(0.9);
      ya->SetTitleSize(0.05);
      ya->SetLabelSize(0.04);
      ya->CenterTitle();
    }
  }

void postDrawTProfile2D(TCanvas *, const VisDQMObject &o)
  {
    TProfile2D* obj = dynamic_cast<TProfile2D*>( o.object );
    assert( obj );
  }
};

static SiStripHitEfficiencyPCLRenderPlugin instance;
