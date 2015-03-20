/*!
  \File BeamPixelRenderPlugin
  \Display Plugin for BeamSpot from Pixel-Vertices
  \author Mauro Dinardo
  \version $ Revision: 2.0 $
  \date $ Date: 2015/23/02 23:00:00 $
*/

#include "DQM/DQMRenderPlugin.h"
#include "utils.h"

#include "TROOT.h"
#include "TProfile.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TStyle.h"
#include "TCanvas.h"
#include "TColor.h"
#include "TText.h"
#include "TPaveStats.h"
#include <cassert>
#include <math.h>

class BeamPixelRenderPlugin : public DQMRenderPlugin {

  int hcalRainbowColors[100];
  int NCont_rainbow;

public:

 virtual void initialise (int, char **)
  {
   // Make rainbow colors. Assign colors positions 1101-1200
    NCont_rainbow = 100; // Specify number of contours for rainbow

    double stops_rainbow[] = { 0.00, 0.34, 0.61, 0.84, 1.00 };
    double red_rainbow[]   = { 0.00, 0.00, 0.87, 1.00, 0.91 };
    double green_rainbow[] = { 0.00, 0.81, 1.00, 0.20, 0.00 };
    double blue_rainbow[]  = { 0.51, 1.00, 0.12, 0.00, 0.00 };
    int NRGBs_rainbow      = 5; // Specify number of RGB boundaries for rainbow
    int nColorsGradient    = 0;
    int highestIndex       = 0;

    for (int g = 1; g < NRGBs_rainbow; g++)
      {
        nColorsGradient = (int) (floor(NCont_rainbow * stops_rainbow[g]) - floor(NCont_rainbow * stops_rainbow[g-1])); // Specify number of gradients between stops (g-1) and (g)
        for (int c = 0; c < nColorsGradient; c++)
	  {
	    hcalRainbowColors[highestIndex] = 1101 + highestIndex;
	    TColor* color = gROOT->GetColor(1101 + highestIndex);
	    // Make new color only if old color does not exist
	    if (!color)
	      color = new TColor(1101 + highestIndex,
				 red_rainbow[g-1]   + c * (red_rainbow[g]   - red_rainbow[g-1])   / nColorsGradient,
				 green_rainbow[g-1] + c * (green_rainbow[g] - green_rainbow[g-1]) / nColorsGradient,
				 blue_rainbow[g-1]  + c * (blue_rainbow[g]  - blue_rainbow[g-1])  / nColorsGradient,
				 "  ");
	    highestIndex++;
	  }
      }
  }

  virtual bool applies(const VisDQMObject& o, const VisDQMImgInfo& )
  {
    if (o.name.find("BeamPixel/") != std::string::npos) return true;

    return false;
  }

  virtual void preDraw(TCanvas* c, const VisDQMObject& o, const VisDQMImgInfo& , VisDQMRenderInfo& )
  {
    c->cd();

    if (dynamic_cast<TH2F*>(o.object)) preDrawTH2F(c, o);
    if (dynamic_cast<TH1F*>(o.object)) preDrawTH1F(c, o);
    if (dynamic_cast<TProfile*>(o.object)) preDrawTProfile(c, o);
  }

private:

  void preDrawTH2F(TCanvas* c, const VisDQMObject& o)
  {
    TH2F* obj = dynamic_cast<TH2F*>(o.object);
    assert(obj);

    // This applies to all
    gStyle->SetCanvasBorderMode(0);
    gStyle->SetPadBorderMode(0);
    gStyle->SetPadBorderSize(0);

    TAxis* xa = obj->GetXaxis();
    TAxis* ya = obj->GetYaxis();

    if ((o.name.find("vertex zx") != std::string::npos) || (o.name.find("vertex zy") != std::string::npos) || (o.name.find("vertex xy") != std::string::npos))
      {
	xa->SetTitleOffset(1.15);
	ya->SetTitleOffset(1.15);

	xa->SetTitleSize(0.04);
	ya->SetTitleSize(0.04);

	xa->SetLabelSize(0.03);
	ya->SetLabelSize(0.03);

	c->SetGrid();
	obj->SetContour(NCont_rainbow);
	gStyle->SetPalette(NCont_rainbow, hcalRainbowColors);
	gStyle->SetPadRightMargin(0.02);
	gStyle->SetOptStat(1110);
	obj->SetStats(kTRUE);
	obj->SetOption("colz");
	gStyle->SetStatX(0.9);
	gStyle->SetStatY(0.9);

	return;
      }

    if (o.name.find("fit results") != std::string::npos)
      {
	xa->SetTitleOffset(1.15);
	ya->SetTitleOffset(1.15);

	xa->SetTitleSize(0.04);
	ya->SetTitleSize(0.04);

	xa->SetLabelSize(0.045);
	ya->SetLabelSize(0.045);

	c->SetGrid();
	obj->SetStats(kFALSE);
	obj->SetMarkerSize(2.);

	return;
      }

    if (o.name.find("reportSummaryMap") != std::string::npos)
      {
	c->SetGrid(kFALSE, kFALSE);
	obj->SetStats(kFALSE);

	return;
      }
  }

  void preDrawTH1F(TCanvas* c, const VisDQMObject& o)
  {
    TH1F* obj = dynamic_cast<TH1F*>(o.object);
    assert(obj);

    // This applies to all
    c->SetGrid(kFALSE, kFALSE);

    gStyle->SetCanvasBorderMode(0);
    gStyle->SetPadBorderMode(0);
    gStyle->SetPadBorderSize(0);
    gStyle->SetOptStat(111110);

    TAxis* xa = obj->GetXaxis();
    TAxis* ya = obj->GetYaxis();

    xa->SetTitleOffset(1.15);
    ya->SetTitleOffset(1.15);

    xa->SetTitleSize(0.04);
    ya->SetTitleSize(0.04);

    xa->SetLabelSize(0.03);
    ya->SetLabelSize(0.03);

    if ((o.name.find("hist pixelHits vs lumi") != std::string::npos) || (o.name.find("hist good vx vs lumi") != std::string::npos))
      {
	gStyle->SetOptFit(1110);
	gStyle->SetOptStat(10);

	gStyle->SetErrorX(0.);
	gStyle->SetEndErrorSize(0.);

	obj->SetMarkerStyle(20);
	obj->SetMarkerSize(0.4);
	obj->SetMarkerColor(4);

	return;
      }

    if ((o.name.find("muX vs lumi") != std::string::npos) || (o.name.find("muY vs lumi") != std::string::npos) || (o.name.find("muZ vs lumi") != std::string::npos) ||
	(o.name.find("sigmaX vs lumi") != std::string::npos) || (o.name.find("sigmaY vs lumi") != std::string::npos) || (o.name.find("sigmaZ vs lumi") != std::string::npos) ||
	(o.name.find("dxdz vs lumi") != std::string::npos) || (o.name.find("dydz vs lumi") != std::string::npos) || (o.name.find("pixelHits vs lumi") != std::string::npos) ||
	(o.name.find("good vertices vs lumi") != std::string::npos))
      {
	gStyle->SetOptFit(1110);
	gStyle->SetOptStat(10);

	obj->SetMarkerStyle(20);
	obj->SetMarkerSize(0.5);
	obj->SetMarkerColor(4);

	return;
      }
  }

  void preDrawTProfile(TCanvas* c, const VisDQMObject& o)
  {
    TProfile* obj = dynamic_cast<TProfile*>(o.object);
    assert(obj);

    // This applies to all
    gStyle->SetCanvasBorderMode(0);
    gStyle->SetPadBorderMode(0);
    gStyle->SetPadBorderSize(0);
    gStyle->SetOptStat(1110);

    TAxis* xa = obj->GetXaxis();
    TAxis* ya = obj->GetYaxis();

    xa->SetTitleOffset(1.15);
    ya->SetTitleOffset(1.15);

    xa->SetTitleSize(0.04);
    ya->SetTitleSize(0.04);

    xa->SetLabelSize(0.03);
    ya->SetLabelSize(0.03);

    c->SetGrid();
  }

};

static BeamPixelRenderPlugin instance;
