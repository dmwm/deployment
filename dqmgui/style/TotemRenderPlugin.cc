#include "DQM/DQMRenderPlugin.h"

#include "TH1F.h"
#include "TH2F.h"
#include "TCanvas.h"

#include <cassert>

//----------------------------------------------------------------------------------------------------

class TotemRenderPlugin : public DQMRenderPlugin
{
	public:
		virtual bool applies(const VisDQMObject &o, const VisDQMImgInfo &)
		{
    		if ((o.name.find( "Totem/" ) != std::string::npos))
      			return true;
			return false;
		}

		virtual void preDraw(TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &, VisDQMRenderInfo & )
		{
    		c->cd();

    		if (dynamic_cast<TH1F*>(o.object))
      			preDrawTH1F(c, o);

    		if (dynamic_cast<TH2F*>(o.object))
      			preDrawTH2F(c, o);
    	}

  		virtual void postDraw( TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo & )
		{
    		c->cd();
    		
			if (dynamic_cast<TH1F*>(o.object))
      			postDrawTH1F(c, o);

    		if (dynamic_cast<TH2F*>(o.object))
      			postDrawTH2F(c, o);
    	}

	private:
  		void preDrawTH1F(TCanvas *, const VisDQMObject &o)
  		{
    		TH1F* obj = dynamic_cast<TH1F*>(o.object);
    		assert(obj);

			obj->SetLineColor(2);
			obj->SetLineWidth(2);
    	}

  		void preDrawTH2F(TCanvas *, const VisDQMObject &o)
		{
    		TH2F* obj = dynamic_cast<TH2F*>(o.object);
    		assert(obj);
      
			obj->SetOption("colz");
		}

  		void postDrawTH1F(TCanvas *c, const VisDQMObject &)
		{
      		c->SetGridx();
      		c->SetGridy();
  		}

  		void postDrawTH2F(TCanvas *c, const VisDQMObject &)
		{
      		c->SetGridx();
      		c->SetGridy();
  		}
};

//----------------------------------------------------------------------------------------------------

static TotemRenderPlugin instance;
