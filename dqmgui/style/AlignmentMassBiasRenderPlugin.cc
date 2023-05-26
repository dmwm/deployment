#include "DQM/DQMRenderPlugin.h"
#include "TCanvas.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TProfile.h"
#include "TProfile2D.h"
#include "TStyle.h"
#include "TGaxis.h"
#include "TPaveStats.h"
#include "TList.h"
#include <cassert>

class AlignmentMassBiasRenderPlugin : public DQMRenderPlugin
{
public:

  virtual bool applies(const VisDQMObject &o, const VisDQMImgInfo &)
  {
    if(o.name.find("AlCaReco/TkAlDiMuonAndVertex/DiMuonMassBiasMonitor") != std::string::npos ||
       o.name.find("AlCaReco/TkAlZMuMu/DiMuonMassBiasMonitor") != std::string::npos ||
       o.name.find("AlCaReco/TkAlJpsiMuMu/DiMuonMassBiasMonitor") != std::string::npos ||
       o.name.find("AlCaReco/TkAlUpsilonMuMu/DiMuonMassBiasMonitor") != std::string::npos){
      return true;
    }
    else {
      return false;
    }
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

    if((o.name.find( "MeanDiMuMass" ) != std::string::npos)){
      obj->SetMarkerSize(1.);
      obj->SetMarkerStyle(20);
      obj->GetXaxis()->SetTitleSize(0.035);
      obj->GetXaxis()->SetLabelSize(0.035);
      obj->GetYaxis()->SetTitleSize(0.035);
      obj->GetYaxis()->SetLabelSize(0.035);
      if( (o.name.find( "TkAlDiMuonAndVertex" ) != std::string::npos) ||   
	  (o.name.find( "TkAlZMuMu" ) != std::string::npos)){
	obj->GetYaxis()->SetRangeUser(90.,92.);
      } else if( (o.name.find( "TkAlJpsiMuMu" ) != std::string::npos)){
	obj->GetYaxis()->SetRangeUser(3.06,3.14);
      } else if( (o.name.find( "TkAlUpsilonMuMu" ) != std::string::npos)){  
	obj->GetYaxis()->SetRangeUser(9.25,9.65);
      } 
    } else if ((o.name.find( "SigmaDiMuMass" ) != std::string::npos)) {
      obj->SetMarkerSize(1.);
      obj->SetMarkerStyle(20);
      obj->GetXaxis()->SetTitleSize(0.035);
      obj->GetXaxis()->SetLabelSize(0.035);
      obj->GetYaxis()->SetTitleSize(0.035);
      obj->GetYaxis()->SetLabelSize(0.035);
      if( (o.name.find( "TkAlDiMuonAndVertex" ) != std::string::npos) ||   
	  (o.name.find( "TkAlZMuMu" ) != std::string::npos)){
	obj->GetYaxis()->SetRangeUser(0.,3.);
      } else if( (o.name.find( "TkAlJpsiMuMu" ) != std::string::npos)){
	obj->GetYaxis()->SetRangeUser(0.,0.1);
      } else if( (o.name.find( "TkAlUpsilonMuMu" ) != std::string::npos)){  
	obj->GetYaxis()->SetRangeUser(0.,0.4);
      }
    } else {
      return;
    }
  }

  void preDrawTH2F(TCanvas *, const VisDQMObject &o)
  {
    TH2F* obj = dynamic_cast<TH2F*>( o.object );
    obj->SetStats( kFALSE );
    obj->SetContour(256);
    gStyle->SetPalette(57,0);

    obj->GetXaxis()->SetTitleSize(0.035);
    obj->GetXaxis()->SetLabelSize(0.035);
    obj->GetYaxis()->SetTitleSize(0.035);
    obj->GetYaxis()->SetLabelSize(0.035);
    obj->SetOption("colz");
    assert( obj );
  }

  void preDrawTProfile(TCanvas *, const VisDQMObject &o)
  {
    TProfile* obj = dynamic_cast<TProfile*>( o.object );
    assert( obj );

    if((o.name.find( "MeanDiMuMass" ) != std::string::npos)){
      obj->SetMarkerSize(1.);
      obj->SetMarkerStyle(20);
      obj->GetXaxis()->SetTitleSize(0.035);
      obj->GetXaxis()->SetLabelSize(0.035);
      obj->GetYaxis()->SetTitleSize(0.035);
      obj->GetYaxis()->SetLabelSize(0.035);
      if( (o.name.find( "TkAlDiMuonAndVertex" ) != std::string::npos) ||   
	  (o.name.find( "TkAlZMuMu" ) != std::string::npos)){
	obj->GetYaxis()->SetRangeUser(90.,92.);
      } else if( (o.name.find( "TkAlJpsiMuMu" ) != std::string::npos)){
	obj->GetYaxis()->SetRangeUser(3.06,3.14);
      } else if( (o.name.find( "TkAlUpsilonMuMu" ) != std::string::npos)){  
	obj->GetYaxis()->SetRangeUser(9.25,9.65);
      } 
    } else if ((o.name.find( "SigmaDiMuMass" ) != std::string::npos)) {
      obj->SetMarkerSize(1.);
      obj->SetMarkerStyle(20);
      obj->GetXaxis()->SetTitleSize(0.035);
      obj->GetXaxis()->SetLabelSize(0.035);
      obj->GetYaxis()->SetTitleSize(0.035);
      obj->GetYaxis()->SetLabelSize(0.035);
      if( (o.name.find( "TkAlDiMuonAndVertex" ) != std::string::npos) ||   
	  (o.name.find( "TkAlZMuMu" ) != std::string::npos)){
	obj->GetYaxis()->SetRangeUser(0.,3.);
      } else if( (o.name.find( "TkAlJpsiMuMu" ) != std::string::npos)){
	obj->GetYaxis()->SetRangeUser(0.,0.1);
      } else if( (o.name.find( "TkAlUpsilonMuMu" ) != std::string::npos)){  
	obj->GetYaxis()->SetRangeUser(0.,0.4);
      }
    } else {
      return;
    }
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

static AlignmentMassBiasRenderPlugin instance;
