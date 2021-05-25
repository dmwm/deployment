/*!
  \file SiPixelMapsRenderPlugin
  \brief RenderPlugin for Tracker Phase-2 Validation plots

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

class SiPhaseTrackerRenderPlugin : public DQMRenderPlugin
{

public:

  virtual void initialise (int, char **)
  {}

  virtual bool applies(const VisDQMObject &o, const VisDQMImgInfo &)
  {
    if(o.name.find( "TrackerPhase2ITCluster/" ) != std::string::npos)
      return true;

    if(o.name.find( "TrackerPhase2ITDigi/" ) != std::string::npos)
      return true;

    if(o.name.find( "TrackerPhase2ITRecHit/" ) != std::string::npos)
      return true;

    if(o.name.find( "TrackerPhase2OTCluster/" ) != std::string::npos)
      return true;

    if(o.name.find( "TrackerPhase2OTDigi/" ) != std::string::npos)
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

    if( o.name.find("Global_Position")!= std::string::npos){
      obj->SetStats( kFALSE );
      gStyle->SetPalette(1,0);
      obj->SetOption("colz");
      return;
    }

    if( o.name.find("Local_Position")!= std::string::npos){
      obj->SetStats( kFALSE );
      gStyle->SetPalette(1,0);
      obj->SetOption("colz");
      return;
    }

    if( o.name.find("LocalPosition")!= std::string::npos){
      obj->SetStats( kFALSE );
      gStyle->SetPalette(1,0);
      obj->SetOption("colz");
      return;
    }

    if( o.name.find("Global_ClusterPosition")!= std::string::npos){
      obj->SetStats( kFALSE );
      gStyle->SetPalette(1,0);
      obj->SetOption("colz");
      return;
    }

    if( o.name.find("Local_ClusterPosition")!= std::string::npos){
      obj->SetStats( kFALSE );
      gStyle->SetPalette(1,0);
      obj->SetOption("colz");
      return;
    }

    if( o.name.find("XPosVsYPos")!= std::string::npos){
      obj->SetStats( kFALSE );
      gStyle->SetPalette(1,0);
      obj->SetOption("colz");
      return;
    }

    if( o.name.find("RPosVsZPos")!= std::string::npos){
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

    if( o.name.find("OccupancyIn")!= std::string::npos){
      obj->SetStats( kFALSE );
      gStyle->SetPalette(1,0);
      obj->SetOption("colz");
      return;
    }
  }

  void postDrawTH1F(TCanvas *, const VisDQMObject &o)
  {
    TH1F* obj = dynamic_cast<TH1F*>( o.object );
    assert( obj );
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

static SiPhaseTrackerRenderPlugin instance;
