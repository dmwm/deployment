/*!
  \file SiStripRenderPlugin
  \brief Display Plugin for SiStrip DQM Histograms
  \author S. Dutta
  \version $Revision: 1.45 $
  \date $Date: 2011/11/16 17:35:55 $
*/

#include "DQM/DQMRenderPlugin.h"
#include "utils.h"
#include "TPaveStats.h"
#include "TLegend.h"
#include "TProfile2D.h"
#include "TProfile.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TStyle.h"
#include "TCanvas.h"
#include "TColor.h"
#include "TText.h"
#include "TLine.h"
#include "TMath.h"
#include <cassert>

class BtagPlugin : public DQMRenderPlugin
{
public:
  virtual bool applies( const VisDQMObject &o, const VisDQMImgInfo & )
    {
      if ((o.name.find( "Btag/deepCSV_BvsAll_GLOBAL/FlavEffVsBEff_DUSG_discr_deepCSV_BvsAll_GLOBAL" ) == std::string::npos)) return false;
      //if ((o.name.find( "") == std::string::npos)) return false;

      return true;
    }

  virtual void preDraw( TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &, VisDQMRenderInfo & )
    {
      c->cd();

      if( dynamic_cast<TH1F*>( o.object ) )
      {
        preDrawTH1F( c, o );
        c->cd();
      }
    }

  virtual void postDraw( TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo & )
    {
      c->cd();
      if( dynamic_cast<TH1F*>( o.object ) )
      {
        postDrawTH1F(c);//,o);
        c->cd();
      }
 
    }

private:
    void preDrawTH1F( TCanvas *c, const VisDQMObject &o )
    {
      c->cd();
      TH1F* obj = dynamic_cast<TH1F*>( o.object );
      assert( obj );

      // This applies to all
      gStyle->SetOptStat(1000000001);
      //obj->SetStats( kFALSE );
     }

  void postDrawTH1F( TCanvas *c)//, const VisDQMObject &o )
    {
      
        c->cd();
       	TIter next(gPad->GetListOfPrimitives());
        TObject * cobj;
        int k = 0;

        //Count number of histograms
        while((cobj=next()))
        {
          if( dynamic_cast<TH1F*>(cobj) )
          {
           k=k+1;
          }
	}

        if(k<2){
		return;
	}
	
	k=0;
	next.Reset();
        TLegend* legend = new TLegend(0.1,0.7,0.48,0.9);
        legend->SetHeader("ROC Curves","C");

        gStyle->SetOptStat(1000000001);

        while((cobj=next()))
        {
          if( dynamic_cast<TH1F*>(cobj) )
          {
           TH1F* obj = dynamic_cast<TH1F*>( cobj ); 
           obj->SetStats( kFALSE );
           if(k==0) legend->AddEntry(obj,"DUSG","l");
           if(k==1) legend->AddEntry(obj,"C","l");
           k=k+1;
          }

	 else if( dynamic_cast<TPaveStats*>(cobj))
         {
           TPaveStats* ps = dynamic_cast<TPaveStats*>(cobj);
           gPad->GetListOfPrimitives()->Remove(ps);
         }
          
        }
        legend->Draw();
   }

  };


static BtagPlugin instance;
