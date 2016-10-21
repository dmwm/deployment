/*!
  \file SiPixelPhase1OnlineRenderPlugin
  \brief RenderPlugin for histograms showing some history in online
  \author Marcel Schneider
*/

#include "DQM/DQMRenderPlugin.h"
#include "utils.h"

#include "TProfile2D.h"
#include "TStyle.h"
#include "TCanvas.h"
#include "TColor.h"
#include <cassert>
#include <string>

using namespace std;

class SiPixelPhase1OnlineRenderPlugin : public DQMRenderPlugin
{
public:
  virtual bool applies( const VisDQMObject & o, const VisDQMImgInfo & )
    {
      if ((o.name.find( "PixelPhase1/" ) != std::string::npos )
        && (std::string(o.object->GetName()).find( "OnlineBlock" ) != std::string::npos )) {
        return true;
      } else {
        return false;
      }
    }

  virtual void preDraw( TCanvas * canvas, const VisDQMObject & o, const VisDQMImgInfo & , VisDQMRenderInfo & renderInfo)
    {
      canvas->cd();
      TH2* obj = dynamic_cast<TH2*>( o.object );
      if(!obj) return;

      obj->SetStats(1);
      gStyle->SetOptStat(111);
      renderInfo.drawOptions = "AXIS";
    }

  virtual void postDraw( TCanvas *canvas, const VisDQMObject &o, const VisDQMImgInfo & )
    {
      canvas->cd();
      TH2* obj = dynamic_cast<TH2*>( o.object );
      if(!obj) return;

      double ref = obj->GetEntries();
      double max = 0;

      for (int i = 1; i <= obj->GetNbinsY(); i++) {
        auto name = std::string(obj->GetName()) + "_" + std::to_string(i);
        TH1* h = new TH1F(name.c_str(), "", obj->GetNbinsX(),
                        obj->GetXaxis()->GetXmin(), obj->GetXaxis()->GetXmax());
        h->SetBit(kCanDelete);
        double entries = 1;
        for (int x = 1; x < obj->GetNbinsX(); x++) {
          entries += obj->GetBinContent(x, i);
          h->SetBinContent(x, obj->GetBinContent(x, i));
        }
        h->Scale(ref/entries);
        h->SetLineColor(i);
        h->Draw("SAME");
        max = std::max(max, h->GetMaximum());
      }

      obj->GetYaxis()->Set(1, 0, max*1.05);
      obj->GetYaxis()->SetTitle("");
    }

private:
};

static SiPixelPhase1OnlineRenderPlugin instance;
