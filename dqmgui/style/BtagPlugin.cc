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
            if ((o.name.find( "Btag/" ) == std::string::npos)) return false;

            return true;
        }


        virtual void preDraw( TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &, VisDQMRenderInfo & )
        {
            c->cd();
            if( dynamic_cast<TH1*>( o.object ) )
            {
                preDrawTH1( c, o );
            }

            if( dynamic_cast<TH2*>( o.object ) )
            {
                preDrawTH2( c, o );
            }
        }


        virtual void postDraw( TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo & )
        {
            c->cd();
            if( dynamic_cast<TH1*>( o.object ) )
            {
                postDrawTH1(c);//,o);
            }
        }


    private:
        void preDrawTH1( TCanvas *c, const VisDQMObject &o )
        {
            c->cd();
            TH1* obj = dynamic_cast<TH1*>( o.object );
            assert( obj );
        }


        void preDrawTH2( TCanvas *c, const VisDQMObject &o )
        {
            c->cd();
            TH1* obj = dynamic_cast<TH2*>( o.object );
            assert( obj );

            obj->SetStats( kFALSE );
        }



        void postDrawTH1( TCanvas *c)//, const VisDQMObject &o )
        {
            c->cd();
            TIter next(gPad->GetListOfPrimitives());
            TObject * cobj;

            // add legend for multiple entries
            if(next.GetCollection()->GetEntries() > 1)
            {
                TLegend* legend = new TLegend(0.12,0.7,0.48,0.88);

                while((cobj=next()))
                {
                    if( dynamic_cast<TH1*>(cobj) )
                    {
                        TH1* obj = dynamic_cast<TH1*>( cobj );
                        std::string hname = static_cast<std::string>(obj->GetName());
                        obj->SetStats( kFALSE );

                        if ((hname.find("_DUSG_discr_") != std::string::npos)) legend->AddEntry(obj,"DUSG","l");
                        else if ((hname.find("_C_discr_") != std::string::npos)) legend->AddEntry(obj, "C","l");
//                         else legend->AddEntry(obj, "???","l"); // enable for unkown labels
                    }
                    // remove stats from plot
                    else if( dynamic_cast<TPaveStats*>(cobj))
                    {
                        TPaveStats* ps = dynamic_cast<TPaveStats*>(cobj);
                        gPad->GetListOfPrimitives()->Remove(ps);
                    }
                }
                legend->Draw("NB");
            }
        }
};


static BtagPlugin instance;
