/*!
  \file SiPixelHeterogenousRenderPlugin
  \brief RenderPlugin for pixel heterogenous plots

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

class SiPixelHeterogenousRenderPlugin : public DQMRenderPlugin
{

public:

  virtual void initialise (int, char **)
  {}

  virtual bool applies(const VisDQMObject &o, const VisDQMImgInfo &)
  {
    if(o.name.find( "SiPixelHeterogeneous" ) != std::string::npos)
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
    else if( dynamic_cast<TH2S*>( o.object ) )
    {
      this->preDrawTH2I( c, o );
    }
    else if( dynamic_cast<TProfile*>( o.object ) )
    {
      this->preDrawTProfile( c, o );
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
    else if( dynamic_cast<TH2I*>( o.object ) )
    {
      this->postDrawTH2I( c, o );
    }
    else if( dynamic_cast<TProfile*>( o.object ) )
    {
      this->postDrawTProfile( c, o );
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
    obj->SetStats( kFALSE );
    obj->SetOption("colz");
    return;
  }

  void preDrawTH2I(TCanvas *, const VisDQMObject &o)
  {
    TH2I* obj = dynamic_cast<TH2I*>( o.object );
    assert( obj );
    obj->SetStats( kFALSE );
    obj->SetOption("colz");
    return;
  }

  void preDrawTProfile(TCanvas *, const VisDQMObject &o)
  {
    TProfile* obj = dynamic_cast<TProfile*>( o.object );
    assert( obj );
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

  void postDrawTH2I(TCanvas *, const VisDQMObject &o)
  {
    TH2I* obj = dynamic_cast<TH2I*>( o.object );
    assert( obj );
  }

  void postDrawTProfile(TCanvas *, const VisDQMObject &o)
  {
    TProfile* obj = dynamic_cast<TProfile*>( o.object );
    assert( obj );
  }

};

static SiPixelHeterogenousRenderPlugin instance;
