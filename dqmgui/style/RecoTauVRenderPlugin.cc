/*!
  \file RecoTauVRenderPlugin
  \author J.Lim
  \date $Date: 2021/09/12 $
*/

#include "DQM/DQMRenderPlugin.h"
#include "utils.h"

#include "TProfile2D.h"
#include "TStyle.h"
#include "TCanvas.h"
#include "TGraphPolar.h"
#include "TColor.h"
#include "TText.h"
#include "TLine.h"
#include <cassert>
#include <string>

using namespace std;

class RecoTauVRenderPlugin : public DQMRenderPlugin {

    public:
        virtual bool applies( const VisDQMObject & o, const VisDQMImgInfo & )
        {
            return ((o.name.find("RecoTauV/") != std::string::npos ));
        }

        // pre-draw, separated per histogram type
        virtual void preDraw(TCanvas* canvas, const VisDQMObject& o,
                const VisDQMImgInfo&, VisDQMRenderInfo&)
        {
            canvas->cd();
            if (dynamic_cast<TH2F*> (o.object)){
                // object is TH2 histogram
                preDrawTH2F(canvas, o);
            } else if (dynamic_cast<TH1F*> (o.object)){
                // object is TH1 histogram
                preDrawTH1F(canvas, o);
            }
        }

        // post-draw, separated per histogram type
        virtual void postDraw(TCanvas* canvas, const VisDQMObject& o,
                const VisDQMImgInfo&)
        {
            if (dynamic_cast<TH2F*> (o.object)){
                // object is TH2 histogram
                postDrawTH2F(canvas, o);
            } else if (dynamic_cast<TH1F*> (o.object)){
                // object is TH1 histogram
                postDrawTH1F(canvas, o);
            }
        }

    private:
        void preDrawTH1F(TCanvas*, const VisDQMObject& o){
            TH1F* obj = dynamic_cast<TH1F*> (o.object);
            // checks that object indeed exists
            assert(obj);
        }

        void preDrawTH2F(TCanvas*, const VisDQMObject& o) {
            TH2F* obj = dynamic_cast<TH2F*> (o.object);
            // checks that object indeed exists
            assert(obj);
        }
        void postDrawTH1F(TCanvas* c, const VisDQMObject& o) {
            gStyle->SetOptStat(0);
            c->cd();
            TH1F* obj = dynamic_cast<TH1F*> (o.object);
            // checks that object indeed exists
            if(o.name.find("_pt") != std::string::npos){
                obj->GetXaxis()->SetTitle("pt (GeV)");
                //Double_t bins[12] = {-20,0,20,40,60,80,100,120,140,160,180,200};
                //TH1F* newobj = (TH1F*) obj->Rebin(11,"rebinned",bins);
		TH1F* newobj = (TH1F*) obj->Rebin(2);
                newobj->SetMaximum(newobj->GetMaximum()*1.2);
                newobj->Draw();
                c->Modified();
                return;
            }else if(o.name.find("_eta") != std::string::npos){
                obj->GetXaxis()->SetTitle("eta");
                Double_t bins[9] = {-4,-3,-2,-1,0,1,2,3,4};
                TH1F* newobj = (TH1F*) obj->Rebin(8,"rebinned",bins);
                newobj->SetMaximum(newobj->GetMaximum()*1.2);
                newobj->Draw();
                c->Modified();
                return;
            }else if(o.name.find("_phi") != std::string::npos){
                obj->GetXaxis()->SetTitle("phi");
                Double_t bins[9] = {-4,-3,-2,-1,0,1,2,3,4};
                TH1F* newobj = (TH1F*) obj->Rebin(8,"rebinned",bins);
                newobj->SetMaximum(newobj->GetMaximum()*1.2);
                newobj->Draw();
                c->Modified();
                return;
            }else if(o.name.find("_mass") != std::string::npos){
                obj->GetXaxis()->SetTitle("mass (GeV)");
                Double_t bins[12] = {-0.2,0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0};
                TH1F* newobj = (TH1F*) obj->Rebin(11,"rebinned",bins);
                newobj->SetMaximum(newobj->GetMaximum()*1.2);
                newobj->Draw();
                c->Modified();
                return;
            }else if(o.name.find("_pu") != std::string::npos){
                obj->GetXaxis()->SetTitle("pile up");
                Double_t bins[12] = {-10,0,10,20,30,40,50,60,70,80,90,100};
                TH1F* newobj = (TH1F*) obj->Rebin(11,"rebinned",bins);
                newobj->SetMaximum(newobj->GetMaximum()*1.2);
                newobj->Draw();
                c->Modified();
                return;
            }else if(o.name.find("decayMode") != std::string::npos){
                if(o.name.find("Finding") == std::string::npos){
                    obj->GetXaxis()->SetTitle("Decay Mode");
                }
            }
            if(o.name.find("DeepTau2018v2p5VS") != std::string::npos){
                if(o.name.find("VSeraw") != std::string::npos){
                    obj->GetXaxis()->SetTitle("raw DeepTauvsElectron");
                }else if(o.name.find("VSjetraw") != std::string::npos){
                    obj->GetXaxis()->SetTitle("raw DeepTauvsJet");
                }else if(o.name.find("VSmuraw") != std::string::npos){
                    obj->GetXaxis()->SetTitle("raw DeepTauvsMuon");
                }
                TH1F* newobj = (TH1F*) obj->Rebin(2);
                newobj->Draw();
                c->Modified();
                return;
            }
            obj->SetMaximum(obj->GetMaximum()*1.2);
            c->Modified();
            return;
        }

        void postDrawTH2F(TCanvas*, const VisDQMObject &o) {
            gStyle->SetOptStat(0);
            TH2F* obj = dynamic_cast<TH2F*> (o.object);
            if(o.name.find("ntau_vs_dm") != std::string::npos){
                obj->GetXaxis()->SetTitle("nTau");
                obj->GetYaxis()->SetTitle("Decay Mode");
            }else if(o.name.find("pT") != std::string::npos){
                obj->GetXaxis()->SetTitle("pt (GeV)");
            }
        }
};

static RecoTauVRenderPlugin instance;
