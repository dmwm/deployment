#include <cassert>
#include <string>

#include "DQM/DQMRenderPlugin.h"

#include "TCanvas.h"
#include "TColor.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TStyle.h"

class L1TStage2BMTFRenderPlugin : public DQMRenderPlugin {

 public:

  virtual bool applies(const VisDQMObject& o, const VisDQMImgInfo&) {
    if (o.name.find("L1T2016/L1TStage2BMTF/") != std::string::npos)
      return true;

    return false;
  }

  virtual void preDraw(TCanvas* c, const VisDQMObject& o, const VisDQMImgInfo&, VisDQMRenderInfo&) {
    if (dynamic_cast<TH1F*>(o.object)) {
      preDrawTH1F(c, o);
    } else if (dynamic_cast<TH2F*>(o.object)) {
      preDrawTH2F(c, o);
    }
  }

  virtual void postDraw(TCanvas* c, const VisDQMObject& o, const VisDQMImgInfo&) {
    if (dynamic_cast<TH1F*>(o.object)) {
      postDrawTH1F(c, o);
    } else if (dynamic_cast<TH2F*>(o.object)) {
      postDrawTH2F(c, o);
    }
  }

 private:

  void preDrawTH1F(TCanvas*, const VisDQMObject&) {}

  void preDrawTH2F(TCanvas*, const VisDQMObject& o) {
    TH2F* obj = dynamic_cast<TH2F*>(o.object);
    assert(obj);

    obj->SetOption("colz");
  }

  void postDrawTH1F(TCanvas*, const VisDQMObject&) {}

  void postDrawTH2F(TCanvas*, const VisDQMObject& o) {
    TH2F* obj = dynamic_cast<TH2F*>(o.object);
    assert(obj);

    gStyle->SetOptStat(10);
  }
};

static L1TStage2BMTFRenderPlugin instance;
