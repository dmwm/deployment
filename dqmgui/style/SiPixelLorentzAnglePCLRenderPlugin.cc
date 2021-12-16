/*!
  \file SiPixelLorentzAnglePCLRenderPlugin
  \brief RenderPlugin for SiPixelLorentzAngle PCL ALCAPROMPT inspection

  \author Marco Musich
*/

#include "DQM/DQMRenderPlugin.h"
#include "utils.h"
#include "TCanvas.h"
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
#include <cassert>

class SiPixelLorentzAnglePCLRenderPlugin : public DQMRenderPlugin
{

public:

  virtual void initialise (int, char **)
  {}

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

  void preDrawTH1F(TCanvas *, const VisDQMObject &o)
  {
    TH1F* obj = dynamic_cast<TH1F*>( o.object );
    assert( obj );  
  }

  void preDrawTH2F(TCanvas *, const VisDQMObject &o)
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

    gPad->Update();
    TPaveStats* st = (TPaveStats*)obj->GetListOfFunctions()->FindObject("stats");
    if(st!=0)  {
      st->SetBorderSize(0);
      st->SetOptStat( 1110 );
      st->SetOptFit( 11 );
      st->SetTextColor( obj->GetLineColor() );
      st->SetX1NDC( .12 );
      st->SetX2NDC( .35 );
      st->SetY1NDC( .73 );
      st->SetY2NDC( .89 );
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
