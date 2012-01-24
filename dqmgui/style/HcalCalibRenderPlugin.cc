/*!
  \file HcalRenderPlugin.cc
  \brief Display Plugin for Hcal DQM Histograms
  \author J. Temple
  \version $Revision: 1.12 $
  \date $Date: 2011/09/09 11:53:42 $
  \\
  \\ Code shamelessly borrowed from S. Dutta's SiStripRenderPlugin.cc code,
  \\ G. Della Ricca and B. Gobbo's EBRenderPlugin.cc, and other existing
  \\ subdetector plugins
  \\ preDraw and postDraw methods now check whether histogram was a TH1
  \\ or TH2, and call a private method appropriate for the histogram type

  // DQMNet::CoreObject replaced by VisDQMObject in Lassi's Oct. 31 revision
  */

#include "DQM/DQMRenderPlugin.h"
#include "utils.h"

#include "TROOT.h"
#include "TH1.h"
#include "TH2.h"
#include "TProfile.h"
#include "TProfile2D.h"
#include "TStyle.h"
#include "TCanvas.h"
#include "TGaxis.h"
#include "TColor.h"
#include "TText.h"
#include "TLine.h"
#include "TPaletteAxis.h"
#include <cassert>
#include <fstream>
#include <iostream>
#include <string>
#include <math.h>

#define HCAL_ETAMIN -44.5
#define HCAL_ETAMAX 44.5
#define HCAL_PHIMIN -0.5
#define HCAL_PHIMAX 73.5

//---define parameters for HTR/Channel Plots
#define MARGIN  1
#define FEDS2_X0 3
#define FEDS3_X0 4
#define SPIG2_Y0 3
#define SPIG3_Y0 4
#define CHNS2_X0 3
#define XS 2
#define YS 4
////#define _XBINS (24*ERIC_HDP_XS+ERIC_HDP_X0)
////#define _YBINS (15*ERIC_HDP_YS+ERIC_HDP_Y0)

using std::cout;
using std::endl;

class HcalCalibRenderPlugin : public DQMRenderPlugin
{
  // Color Schemes
  // seach scheme needs an array of color indices,
  // the number of contours to be used, and the number of RGB stop points
  Int_t summaryColors[80];
  Int_t NRGBs_summary;
  Int_t NCont_summary;

  Int_t pedestalColors[40];
  Int_t NRGBs_pedestal;
  Int_t NCont_pedestal;

  // error colors:  green for <5% error, then yellow->red, then grey above 100% (previously-known problems)
  int hcalErrorColors[105];
  Int_t NRGBs_hcalError;
  Int_t NCont_hcalError;

public:
  virtual void initialise (int, char **)
  {

    Int_t nColorsGradient=0; // stores number of gradients in each 'step' between colors
    int highestIndex=0;

    //make summaryColors, with a value of -1 indicated in gray, values >-1 and <0 in white,
    // values 0-0.98 scaling from red to yellow, and values > 0.98 in green.
    NRGBs_summary=7;
    NCont_summary=80;
    Double_t stops_summary[] = {0.00,0.025,0.4999,0.50,0.99,0.991,1.00}; // set limits for color transitions
    Double_t red_summary[]   = {0.6,1.00,1.00,1.00,1.00,0.00,0.00};
    Double_t green_summary[] = {0.6,1.00,1.00,0.00,1.00,0.80,0.80};
    Double_t blue_summary[]  = {0.6,1.00,1.00,0.00,0.00,0.00,0.00};
    nColorsGradient=0;
    highestIndex=0; // set starting index for new color (to avoid existing root colors)
    for (int g=1;g<NRGBs_summary;++g)
      {
	nColorsGradient = (Int_t) (floor(NCont_summary*stops_summary[g]) - floor(NCont_summary*stops_summary[g-1])); // specify number of gradients between stops (g-1) and (g)
        for (int c = 0; c < nColorsGradient; c++)
	  {
	    summaryColors[highestIndex]=1001+highestIndex;
	    TColor* color = gROOT->GetColor(1001+highestIndex);
	    // Make new color only if old color does not exist
	    if (!color)
	      color = new TColor(1001+highestIndex,
				 red_summary[g-1] + c * (red_summary[g] - red_summary[g-1])/ nColorsGradient,
				 green_summary[g-1] + c * (green_summary[g] - green_summary[g-1])/ nColorsGradient,
				 blue_summary[g-1] + c * (blue_summary[g] - blue_summary[g-1])/ nColorsGradient,
				 "  ");

	    highestIndex++;
	  }
      }

    // Sample pedestal color scheme; need to set something better at some point
    //make pedestalColors, with a value of -1 indicated in gray, values >-1 and <0 in white,
    // values 0-0.98 scaling from red to yellow, and values > 0.98 in green.
    NRGBs_pedestal=11;
    NCont_pedestal=40;
    Double_t stops_pedestal[] = {0.00,0.10,0.20,0.30,0.35,0.50,0.65,0.70,0.80,0.90,1.00}; // set limits for color transitions
    Double_t red_pedestal[]   = {0.60,1.00,0.50,0.00,0.00,0.00,0.00,0.75,1.00,1.00,1.00};
    Double_t green_pedestal[] = {0.60,0.00,0.00,0.50,0.90,1.00,0.90,0.75,0.50,0.25,0.00};
    Double_t blue_pedestal[]  = {0.60,1.00,1.00,0.75,0.10,0.00,0.10,0.00,0.00,0.00,0.00};
    nColorsGradient=0;
    highestIndex=0; // set starting index for new color (to avoid existing root colors)
    for (int g=1;g<NRGBs_pedestal;++g)
      {
	nColorsGradient = (Int_t) (floor(NCont_pedestal*stops_pedestal[g]) - floor(NCont_pedestal*stops_pedestal[g-1])); // specify number of gradients between stops (g-1) and (g)
        for (int c = 0; c < nColorsGradient; c++)
	  {
	    pedestalColors[highestIndex]=1101+highestIndex;
	    TColor* color = gROOT->GetColor(1101+highestIndex);
	    // Make new color only if old color does not exist
	    if (!color)
	      color = new TColor(1101+highestIndex,
				 red_pedestal[g-1] + c * (red_pedestal[g] - red_pedestal[g-1])/ nColorsGradient,
				 green_pedestal[g-1] + c * (green_pedestal[g] - green_pedestal[g-1])/ nColorsGradient,
				 blue_pedestal[g-1] + c * (blue_pedestal[g] - blue_pedestal[g-1])/ nColorsGradient,
				 "  ");

	    highestIndex++;
	  }
      }

    // repeat for hcal error colors.  Assign color positions starting at 1501
    NRGBs_hcalError = 9; // specify number of RGB boundaries for hcalError
    NCont_hcalError = 105; // specify number of contours for hcalError
    // Update on 1 October 10:  Switch 'black' color to 'white' for known bad channels
    Double_t stops_hcalError[] = { 0.00, 0.05/1.05, 0.40/1.05, 0.75/1.05, 0.95/1.05, 1.00/1.05, 1.01/1.05,1.02/1.05, 1.05/1.05};
    Double_t red_hcalError[]   = { 0.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.0, 1.0};
    Double_t green_hcalError[] = { 0.80, 1.00, 0.67, 0.33, 0.00, 0.00, 0.00, 1.0, 1.0};
    Double_t blue_hcalError[]  = { 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.0, 1.0};
    nColorsGradient=0;
    highestIndex=0;
    for (int g=1;g<NRGBs_hcalError;++g)
      {
        nColorsGradient = (Int_t) (floor(NCont_hcalError*stops_hcalError[g]) - floor(NCont_hcalError*stops_hcalError[g-1])); // specify number of gradients between stops (g-1) and (g)
        for (int c = 0; c < nColorsGradient; c++)
	  {
	    hcalErrorColors[highestIndex]=1501+highestIndex;
	    TColor* color = gROOT->GetColor(1501+highestIndex);
	    // Make new color only if old color does not exist
	    if (!color)
	      color = new TColor(1501+highestIndex,
				 red_hcalError[g-1] + c * (red_hcalError[g] - red_hcalError[g-1])/ nColorsGradient,
				 green_hcalError[g-1] + c * (green_hcalError[g] - green_hcalError[g-1])/ nColorsGradient,
				 blue_hcalError[g-1] + c * (blue_hcalError[g] - blue_hcalError[g-1])/ nColorsGradient,
				 "  ");

	    highestIndex++;
	  }
      }
  }

  virtual bool applies(const VisDQMObject &o, const VisDQMImgInfo &)
  {
    // determine whether core object is an Hcal object
    if (o.name.find( "HcalCalib/" ) != std::string::npos || o.name.find( "HcalCalib/" ) != std::string::npos)
      return true;

    return false;
  }

  virtual void preDraw (TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &, VisDQMRenderInfo &)
  {
    c->cd();

    gStyle->Reset("Default");
    gStyle->SetCanvasColor(10);
    gStyle->SetPadColor(10);
    gStyle->SetFillColor(10);
    gStyle->SetStatColor(10);
    gStyle->SetTitleFillColor(10);

    TGaxis::SetMaxDigits(4);

    gStyle->SetOptTitle(kTRUE);
    gStyle->SetTitleBorderSize(0);

    gStyle->SetOptStat(kFALSE);
    gStyle->SetStatBorderSize(1);

    gROOT->ForceStyle();

    // Ay yi yi -- need to remember that other histogram types
    // inherit from TH1, so we can't do the TH1 check first.
    if( dynamic_cast<TProfile2D*>( o.object ) )
      {      }
    else if ( dynamic_cast<TProfile*>( o.object ) )
      preDrawTProfile( c, o );

    // object is TH2 histogram
    else if( dynamic_cast<TH2*>( o.object ) )
      preDrawTH2( c, o );
    // object is TH1 histogram
    else if( dynamic_cast<TH1*>( o.object ) )
      preDrawTH1( c, o );
  }

  virtual void postDraw (TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &)
  {
    if( dynamic_cast<TProfile2D*>( o.object ) )
      {      }
    else if( dynamic_cast<TProfile*>( o.object ) )
      {      }
    // object is TH2 histogram
    else if( dynamic_cast<TH2*>( o.object ) )
      {
        postDrawTH2( c, o );
      }
    // object is TH1 histogram
    else if( dynamic_cast<TH1*>( o.object ) )
      {
        postDrawTH1( c, o );
      }
  }

private:
  void preDrawTH1 ( TCanvas * c, const VisDQMObject &o )
  {
    c->cd();
    // Do we want to do anything special yet with TH1 histograms?
    TH1* obj = dynamic_cast<TH1*>( o.object );
    assert (obj); // checks that object indeed exists

    // For now, all 1D plots have stats on.  Disable in future?
    gStyle->SetOptStat("iourmen");
    obj->SetStats(kTRUE);

    // List of all histograms that should be in log scale

    if (o.name.find("DataFormatMonitor/") !=std::string::npos ||
	o.name.find("RawDataMonitor_Hcal/")!=std::string::npos
	)
      {
	if (  (o.name.find("Corruption/03 OrN Difference")               !=std::string::npos) ||
	      (o.name.find("Corruption/04 HTR BCN when")                 !=std::string::npos) ||
	      (o.name.find("Corruption/05 BCN Difference")               !=std::string::npos) ||
	      (o.name.find("Corruption/06 EvN Difference")               !=std::string::npos) ||
	      (o.name.find("Data Flow/BCN from")                         !=std::string::npos) ||
	      (o.name.find("Data Flow/DCC Data Block Size Distribution") !=std::string::npos) ||
	      (o.name.find("Data Flow/DCC Event Counts")                 !=std::string::npos) ||
	      (o.name.find("Diagnostics/HTR Fiber Orbit")                !=std::string::npos) ||
	      (o.name.find("Diagnostics/HTR Status Word H")              !=std::string::npos) ||
	      (o.name.find("Diagnostics/HTR UnSupp")                     !=std::string::npos)
	      )
	  {
	    if (obj->GetMaximum()>0) gPad->SetLogy(1);
	  }

	else if (  (o.name.find("Data Flow/DCC Data Block Size Distribution")!=std::string::npos) ||
		   (o.name.find("Diagnostics/HTR Fiber Orbit")!=std::string::npos)
		   )
	  {
	    if (obj->GetMaximum()>0)
	      gPad->SetLogx(1);
	  }
      } // Raw Data search

    else if (o.name.find("RecHitMonitor_Hcal/") !=std::string::npos)
      {
	if (o.name.find("rechit_1D_plots")   !=std::string::npos)
	  {
	    if (obj->GetMaximum()>0)
	      gPad->SetLogy(1);
	    gStyle->SetOptStat("iourmen");
	    obj->SetStats( kTRUE );
	  }
	else if (o.name.find("AnomalousCellFlags") !=std::string::npos)
	  {
	    c->SetBottomMargin(0.30);
	    if (obj->GetMaximum()>0)
	      gPad->SetLogy(1);
	  }
	else if (o.name.find("HcalRecHitIeta")!=std::string::npos ||
		 o.name.find("HcalRecHitIphi")!=std::string::npos)
	  obj->SetMinimum(0);
      } // RecHitMonitor

    else if ((o.name.find("DetDiagPedestalMonitor_Hcal")!=std::string::npos)&&
	     (o.name.find("Pedestal-Reference Distribution")!=std::string::npos))
      {
	if (obj->GetMaximum()>0)
	  gPad->SetLogy(1);
      }

  } // void preDrawTH1(...)

  void preDrawTH2 ( TCanvas *c, const VisDQMObject &o )
  {
    c->cd();
    TH2* obj = dynamic_cast<TH2*>( o.object );
    assert( obj );

    gStyle->SetCanvasBorderMode( 0 );
    gStyle->SetPadBorderMode( 0 );
    gStyle->SetPadBorderSize( 0 );

    // default coloring scheme
    gStyle->SetPalette(1);
    obj->SetContour(100);
    obj->SetOption("colz");
    //c->SetRightMargin(2*c->GetRightMargin()); // double right margin
    gPad->SetGridx();
    gPad->SetGridy();

    if ((o.name.find("DataFormatMonitor/Corruption/") !=std::string::npos) ||
	(o.name.find("RawDataMonitor_Hcal/Corruption") !=std::string::npos)  ){
      // Set error palette for normalized histograms.
      obj->SetOption("colz");
      gStyle->SetFrameFillColor(17);
    }
    // Set default color scheme

    if (o.name.find("HcalCalib/EventInfo/reportSummaryMap")!=std::string::npos)
      {
	obj->SetOption("colztext90"); // draw marker at 90 degrees
	setColorScheme(obj,NCont_summary,summaryColors);
      }

   // Normalized error rate histograms plotted with error Fraction colors (0 = green, 1 = red)
    if ( (o.name.find("RecHitMonitor_Hcal/ ProblemRecHits")!= std::string::npos ) ||
	 (o.name.find("RecHitMonitor_Hcal/problem_rechits/")!= std::string::npos ) ||
	 (o.name.find("DigiMonitor_Hcal/ ProblemDigis")!= std::string::npos ) ||
	 (o.name.find("DigiMonitor_Hcal/problem_digis/")!= std::string::npos ) ||
	 (o.name.find("DetDiagPedestalMonitor_Hcal/ ProblemDetDiagPedestal")!= std::string::npos ) ||
	 (o.name.find("DetDiagPedestalMonitor_Hcal/problem_DetDiagPedestal/")!= std::string::npos ) ||
	 (o.name.find("DetDiagLaserMonitor_Hcal/ ProblemDetDiagLaser")!= std::string::npos ) ||
	 (o.name.find("DetDiagLaserMonitor_Hcal/problem_DetDiagLaser/")!= std::string::npos )
	 )
      {
	gStyle->SetFrameFillColor(17);  // set background to grey so that yellow can stand out

	// rescaling -- can probably be removed
        double scale = obj->GetBinContent(0,0);
        if (scale>1) // problem histograms don't have underflow bins filled any more
	  obj->Scale(1./scale);

	// Set error palette for normalized histograms.
	// Setting error color forces min/max to be 0./1.05, since otherwise, colors aren't sensible
	obj->SetMinimum(0.);
	obj->SetMaximum(1.05);
	setColorScheme(obj,NCont_hcalError,hcalErrorColors);
	obj->SetOption("colz");

	// cells satisfying hot criterion in <1% of events not shown by default?  Disrupts overall color mapping?
	if (o.name.find("HotCellMonitor_Hcal/")!=std::string::npos)
	  obj->SetMinimum(0.01);
      }

    // Set Pedestal mean maximum to 2x nominal (3 ADC counts)
    if (o.name.find("DetDiagPedestalMonitor_Hcal/Summary Plots/")!=std::string::npos)
      {
	if (
	    (o.name.find("pedestal mean map") !=std::string::npos)
	    )
	  {
	    obj->SetStats(0);
	    obj->SetMaximum(5);
	    obj->SetNdivisions(36,"Y");
	    obj->SetOption("colz");
	  }

	else if (
		 (o.name.find("pedestal rms map") !=std::string::npos)
		 )
	  {
	    obj->SetStats(0);
	    obj->SetMaximum(2);
	    obj->SetNdivisions(36,"Y");
	    obj->SetOption("colz");
	  }
      } // DetDiagPedestalMonitor_Hcal/Summary Plots/
    else if (o.name.find("DetDiagLaserMonitor_Hcal/")!=std::string::npos)
      {
	if (
	    (o.name.find("HBHEHF Laser (Timing-Ref)+1")!=std::string::npos) ||
	    (o.name.find("HO Laser (Timing-Ref)+1") !=std::string::npos)
	    )
	  {
	    obj->SetMinimum(0);
	    obj->SetMaximum(2);
	    obj->SetNdivisions(36,"Y");
	  }

	else if (
		 (o.name.find("HBHEHF Laser Energy_div_Ref")!=std::string::npos) ||
		 (o.name.find("HO Laser Energy_div_Ref") !=std::string::npos)
		 )
	  {
	    obj->SetMinimum(0.5);
	    obj->SetMaximum(1.5);
	    obj->SetNdivisions(36,"Y");
	  }
	else if ((o.name.find("Laser Timing HBHEHF")!=std::string::npos) ||
		 (o.name.find("Laser Timing HO")!=std::string::npos) ||
		 (o.name.find("Laser Energy HBHEHF")!=std::string::npos) ||
		 (o.name.find("Laser Energy HO")!=std::string::npos) )
	  {
	    obj->SetNdivisions(36,"Y");
	  }
      } // DetDiagLaserMonitor_Hcal
  } // void preDrawTH2

  void preDrawTProfile ( TCanvas *, const VisDQMObject &o )
  {
    TProfile* obj = dynamic_cast<TProfile*>( o.object );
    assert( obj );
    // Set TProfile boundaries to first/last bins that have non-zero content
    bool foundfirst=false;
    int firstnonzerobin=1;
    int lastnonzerobin=1;
    for (int i=1;i<=obj->GetNbinsX();++i)
      {
	if (foundfirst==false && obj->GetBinContent(i)!=0)
	  {
	    foundfirst=true;
	    firstnonzerobin=i;
	  }
	if (obj->GetBinContent(i)!=0)
	  lastnonzerobin=i+1;
      }
    if (lastnonzerobin-firstnonzerobin>1)
      obj->GetXaxis()->SetRange(firstnonzerobin,lastnonzerobin-1);
    obj->SetMarkerStyle(20);  // always show average as closed circle
    return;
  }

  void postDrawTH1( TCanvas *c, const VisDQMObject &o )
  {
    TH1* obj = dynamic_cast<TH1*>( o.object );
    assert( obj );

    if (o.name.find("DetDiagLaserMonitor_Hcal")!=std::string::npos)
      {
	if ((o.name.find("RBX average Time-Ref")!=std::string::npos)||
	    (o.name.find("RoBox average Time-Ref")!=std::string::npos))
	  {
	    obj->SetMarkerStyle(22);
	    obj->SetMarkerColor(kRed);
	    obj->GetYaxis()->SetRangeUser(obj->GetMinimum()-1,obj->GetMaximum()+1);
	    obj->GetXaxis()->SetNdivisions(520);
	    obj->GetXaxis()->SetBit(TAxis::kLabelsVert);
	    obj->GetXaxis()->SetLabelSize(0.05);
	    c->SetBottomMargin(0.2);
	    (obj->GetEntries()>0) ? obj->Draw("P") : obj->Draw("");
	  }
      }  // DetDiagLaserMonitor_Hcal
  }

  void postDrawTH2( TCanvas *c, const VisDQMObject &o )
  {
    c->cd();
    TH2* obj = dynamic_cast<TH2*>( o.object );
    assert( obj );

    if (o.name.find("reportSummaryMap" ) != std::string::npos)
      {
	if (obj->GetBinContent(0,0)==-1) // insufficient events for certification
	  {
	    TText t;
	    t.SetTextSize(0.1);
	    t.DrawText(1,1, "Insufficient Events for Run Certification!");
	  }
      }

    // in the future, we can add text output based on error status,
    // or set bin range based on filled histograms, etc.
    else if ( (o.name.find("RawDataMonitor_Hcal/Corruption")      != std::string::npos)   ||
	 (o.name.find("RawDataMonitor_Hcal/Corruption/F")      != std::string::npos) ||
	 (o.name.find("DataFormatMonitor/Corruption")      != std::string::npos)   ||
	 (o.name.find("DataFormatMonitor/Corruption/F")      != std::string::npos) )
      {
        TText t;
        t.SetTextSize( 0.1);
        if (obj->GetEffectiveEntries() <= 0.0)
	  t.DrawText(1, 1, "Empty == OK");
      }

    // Move histogram to accomodate colz column
    TPaletteAxis *pal = (TPaletteAxis*)obj->GetListOfFunctions()->FindObject("palette");
    if (pal!=0)
      {
	c->SetRightMargin(0.15);
	pal->SetX1NDC(0.85);
	pal->SetX2NDC(0.90);
      }

    // Want to move colz palette, but this crashes code, and does not move the palette.  Hmm...
    obj->GetYaxis()->SetTickLength(0.0);
    obj->GetXaxis()->SetTickLength(0.0);

    if (o.name.find("Data Flow/DCC Data Block Size Each FED")!=std::string::npos)
      c->SetLogy();

    if ( (o.name.find("Corruption/Chan") != std::string::npos )         )
      {
        c->SetBottomMargin(0.200);
        TLine line;
        line.SetLineWidth(1);
        for (int i=0; i<24; i++)
	  {   // x-axis:24 channels
	    for (int j=0; j<15; j++)
	      { // y-axis:15 spigots
		line.DrawLine(MARGIN+(i*CHNS2_X0), MARGIN+(j*SPIG2_Y0),
			      ((i+1) *  CHNS2_X0), MARGIN+(j*SPIG2_Y0)    );
		line.DrawLine(MARGIN+(i*CHNS2_X0), MARGIN+(j*SPIG2_Y0)+2,
			      ((i+1) *  CHNS2_X0), MARGIN+(j*SPIG2_Y0)+2  );

		line.DrawLine(MARGIN+(i*CHNS2_X0)  , MARGIN+(j*SPIG2_Y0),
			      MARGIN+(i*CHNS2_X0)  , ((j+1) *  SPIG2_Y0)    );
		line.DrawLine(MARGIN+(i*CHNS2_X0)+2, MARGIN+(j*SPIG2_Y0),
			      MARGIN+(i*CHNS2_X0)+2, ((j+1) *  SPIG2_Y0)    );
	      }
	  }
        // Draw a legend above the plot
        line.DrawLine((CHNS2_X0*20)  , (SPIG2_Y0*16)  ,
                      (CHNS2_X0*21)-1, (SPIG2_Y0*16)  );
        line.DrawLine((CHNS2_X0*20)  , (SPIG2_Y0*17)-1,
                      (CHNS2_X0*21)-1, (SPIG2_Y0*17)-1);

        line.DrawLine((CHNS2_X0*20)  , (SPIG2_Y0*16)  ,
                      (CHNS2_X0*20)  , (SPIG2_Y0*17)-1);
        line.DrawLine((CHNS2_X0*21)-1, (SPIG2_Y0*16)  ,
                      (CHNS2_X0*21)-1, (SPIG2_Y0*17)-1);
        TText tx;
        tx.SetTextSize( 0.02);
        tx.DrawText((CHNS2_X0*20)-6, (SPIG2_Y0*16)     , "DigiSize");
        tx.DrawText((CHNS2_X0*20)-4, (SPIG2_Y0*17)-1.75, "!DV"     );

        tx.DrawText((CHNS2_X0*21)  , (SPIG2_Y0*16)    , "CapRotat" );
        tx.DrawText((CHNS2_X0*21)  , (SPIG2_Y0*17)-1.75,"Er"      );

	obj->SetMinimum(0.);
	//obj->SetMaximum(1.);
        return;
      }
    else if ( (o.name.find("Data Flow/01") != std::string::npos )         )
      {
	if (obj->GetBinContent(0)>0)
	  obj->SetMaximum(obj->GetBinContent(0));
        c->SetBottomMargin(0.200);
        TLine line;
        line.SetLineWidth(1);
        for (int i=0; i<32; i++)
	  {   // x-axis:32 DCCs
	    for (int j=0; j<15; j++)
	      { // y-axis:15 spigots
		line.DrawLine(MARGIN+(i*FEDS2_X0), MARGIN+(j*SPIG3_Y0),
			      ((i+1) *  FEDS2_X0), MARGIN+(j*SPIG3_Y0)    );
		line.DrawLine(MARGIN+(i*FEDS2_X0), MARGIN+(j*SPIG3_Y0)+3,
			      ((i+1) *  FEDS2_X0), MARGIN+(j*SPIG3_Y0)+3  );

		line.DrawLine(MARGIN+(i*FEDS2_X0)  , MARGIN+(j*SPIG3_Y0),
			      MARGIN+(i*FEDS2_X0)  , ((j+1) *  SPIG3_Y0)    );
		line.DrawLine(MARGIN+(i*FEDS2_X0)+2, MARGIN+(j*SPIG3_Y0),
			      MARGIN+(i*FEDS2_X0)+2, ((j+1) *  SPIG3_Y0)    );
	      }
	  }
        // Draw a legend above the plot
        line.DrawLine((FEDS2_X0*28)-2, (SPIG3_Y0*16)-1,
                      (FEDS2_X0*31)-1, (SPIG3_Y0*16)-1);
        line.DrawLine((FEDS2_X0*28)-2, (SPIG3_Y0*17)  ,
                      (FEDS2_X0*31)-1, (SPIG3_Y0*17)  );

        line.DrawLine((FEDS2_X0*28)-2, (SPIG3_Y0*16)-1,
                      (FEDS2_X0*28)-2, (SPIG3_Y0*17)  );
        line.DrawLine((FEDS2_X0*31)-1, (SPIG3_Y0*16)-1,
                      (FEDS2_X0*31)-1, (SPIG3_Y0*17)  );
        TText tx;
        tx.SetTextSize( 0.02);
        tx.DrawText((FEDS2_X0*29)-7, (SPIG3_Y0*16)-2.0, "CE");

        tx.DrawText((FEDS2_X0*29)-4, (SPIG3_Y0*16)+2.5, "OW");
	tx.DrawText((FEDS2_X0*29)-4, (SPIG3_Y0*16)+1  , "BZ");
        tx.DrawText((FEDS2_X0*29)-4, (SPIG3_Y0*16)-0.5, "EE");

        tx.DrawText((FEDS2_X0*29)+0, (SPIG3_Y0*16)+2.5, "OFW");
	tx.DrawText((FEDS2_X0*29)+0, (SPIG3_Y0*16)+1  , "BSY");
        tx.DrawText((FEDS2_X0*29)+0, (SPIG3_Y0*16)-0.5, "L1A");
        return;
      }
    else if ( (o.name.find("Corruption/09") != std::string::npos )         )
      {
	obj->SetOption("colz");
	gStyle->SetFrameFillColor(17);
	obj->SetMinimum(0.);
        c->SetBottomMargin(0.200);
        TLine line;
        line.SetLineWidth(1);
        for (int i=0; i<32; i++)
	  {   // x-axis:32 DCCs
	    for (int j=0; j<15; j++)
	      { // y-axis:15 spigots
		line.DrawLine(MARGIN+(i*FEDS2_X0), MARGIN+(j*SPIG2_Y0),
			      ((i+1) *  FEDS2_X0), MARGIN+(j*SPIG2_Y0)    );
		line.DrawLine(MARGIN+(i*FEDS2_X0), MARGIN+(j*SPIG2_Y0)+2,
			      ((i+1) *  FEDS2_X0), MARGIN+(j*SPIG2_Y0)+2  );

		line.DrawLine(MARGIN+(i*FEDS2_X0)  , MARGIN+(j*SPIG2_Y0),
			      MARGIN+(i*FEDS2_X0)  , ((j+1) *  SPIG2_Y0)    );
		line.DrawLine(MARGIN+(i*FEDS2_X0)+2, MARGIN+(j*SPIG2_Y0),
			      MARGIN+(i*FEDS2_X0)+2, ((j+1) *  SPIG2_Y0)    );
	      }
	  }
        // Draw a legend above the plot
        line.DrawLine((FEDS2_X0*30)  , (SPIG2_Y0*16)  ,
                      (FEDS2_X0*31)-1, (SPIG2_Y0*16)  );
        line.DrawLine((FEDS2_X0*30)  , (SPIG2_Y0*17)-1,
                      (FEDS2_X0*31)-1, (SPIG2_Y0*17)-1);

        line.DrawLine((FEDS2_X0*30)  , (SPIG2_Y0*16)  ,
                      (FEDS2_X0*30)  , (SPIG2_Y0*17)-1);
        line.DrawLine((FEDS2_X0*31)-1, (SPIG2_Y0*16)  ,
                      (FEDS2_X0*31)-1, (SPIG2_Y0*17)-1);
        TText tx;
        tx.SetTextSize( 0.02);
        tx.DrawText((FEDS2_X0*30)-6, (SPIG2_Y0*16)     , "DigiSize");
        tx.DrawText((FEDS2_X0*30)-4, (SPIG2_Y0*17)-1.75, "!DV"     );

        tx.DrawText((FEDS2_X0*31)  , (SPIG2_Y0*16)    , "CapRotat" );
        tx.DrawText((FEDS2_X0*31)  , (SPIG2_Y0*17)-1.75,"Er"      );
        return;
      }

    if ( (o.name.find("DataFormatMonitor/Corruption/01") != std::string::npos) ||
	 (o.name.find("DataFormatMonitor/Corruption/02") != std::string::npos) ||
	 (o.name.find("DataFormatMonitor/Diagnostics/DCC Stat") != std::string::npos)    )
      {
        obj->SetStats(0);
        c->SetLeftMargin( 0.350); // in fractions of a TCanvas... ?
      }
    else  if ( (o.name.find("DataFormatMonitor/Diagnostics/HTR Status Word") != std::string::npos)    )
      {
        obj->SetStats(0);
        c->SetLeftMargin( 0.250); // in fractions of a TCanvas... ?
      }
    else if ( (o.name.find("Corruption/07") != std::string::npos ) ||
	      (o.name.find("Corruption/08") != std::string::npos )   )
      {
	obj->SetMaximum(obj->GetBinContent(0,0));
        TLine line;
        line.SetLineWidth(1);
        for (int i=0; i<32; i++)
	  {    // x-axis:32 DCC's (FEDs 700:731)
	    for (int j=0; j<15; j++)
	      {  // y-axis:15 spigots
		line.DrawLine(MARGIN+(i*FEDS3_X0), MARGIN+(j*SPIG3_Y0),
			      ((i+1) *  FEDS3_X0), MARGIN+(j*SPIG3_Y0)    );
		line.DrawLine(MARGIN+(i*FEDS3_X0), MARGIN+(j*SPIG3_Y0)+3,
			      ((i+1) *  FEDS3_X0), MARGIN+(j*SPIG3_Y0)+3    );

		line.DrawLine(MARGIN+(i*FEDS3_X0)  , MARGIN+(j*SPIG3_Y0),
			      MARGIN+(i*FEDS3_X0)  , ((j+1) *  SPIG3_Y0)    );
		line.DrawLine(MARGIN+(i*FEDS3_X0)+3, MARGIN+(j*SPIG3_Y0),
			      MARGIN+(i*FEDS3_X0)+3, ((j+1) *  SPIG3_Y0)    );
	      }}
        // Draw a legend above the plot
        line.DrawLine(FEDS3_X0*28.5, (SPIG3_Y0*16)-1,
                      FEDS3_X0*32  , (SPIG3_Y0*16)-1);
        line.DrawLine(FEDS3_X0*28.5, (SPIG3_Y0*17)+0,
                      FEDS3_X0*32  , (SPIG3_Y0*17)+0);

        line.DrawLine(FEDS3_X0*28.5, (SPIG3_Y0*16)-1,
                      FEDS3_X0*28.5, (SPIG3_Y0*17)+0);
        line.DrawLine(FEDS3_X0*32  , (SPIG3_Y0*16)-1,
                      FEDS3_X0*32  , (SPIG3_Y0*17)+0);
        TText tx;
        tx.SetTextSize( 0.02);
        if (o.name.find("LRB") != std::string::npos )
	  {
	    tx.DrawText((FEDS3_X0*30)-8, (SPIG3_Y0*17)-6  , "T");

	    tx.DrawText((FEDS3_X0*30)-5, (SPIG3_Y0*17)-2  , "E!P");
	    tx.DrawText((FEDS3_X0*30)-5, (SPIG3_Y0*17)-3.5, "ND" );
	    tx.DrawText((FEDS3_X0*30)-5, (SPIG3_Y0*17)-5  , "CRC");

	    tx.DrawText((FEDS3_X0*30)+0, (SPIG3_Y0*17)-2  , "UE");
	    tx.DrawText((FEDS3_X0*30)+0, (SPIG3_Y0*17)-3.5, "OV");
	    tx.DrawText((FEDS3_X0*30)+0, (SPIG3_Y0*17)-5  , "ST");

	    tx.DrawText((FEDS3_X0*30)+4, (SPIG3_Y0*17)-2  , "TR");
	    tx.DrawText((FEDS3_X0*30)+4, (SPIG3_Y0*17)-3.5, "ID");
	    tx.DrawText((FEDS3_X0*30)+4, (SPIG3_Y0*17)-5  , "ODD");}
        if (o.name.find("Half-HTR") != std::string::npos )
	  {
	    tx.DrawText((FEDS3_X0*30)-5, (SPIG3_Y0*17)-2  , "CT");
	    tx.DrawText((FEDS3_X0*30)-5, (SPIG3_Y0*17)-3.5, "HM");
	    tx.DrawText((FEDS3_X0*30)-5, (SPIG3_Y0*17)-5  , "TM");

	    tx.DrawText((FEDS3_X0*30)+0, (SPIG3_Y0*17)-2  , "BE");
	    tx.DrawText((FEDS3_X0*30)+0, (SPIG3_Y0*17)-3.5, "15");
	    tx.DrawText((FEDS3_X0*30)+0, (SPIG3_Y0*17)-5  , "CK");

	    tx.DrawText((FEDS3_X0*30)+4 , (SPIG3_Y0*17)-3.5, "WW");
	    tx.DrawText((FEDS3_X0*30)+4 , (SPIG3_Y0*17)-5  , "IW");
	  }
      }
  } // void postDrawTH2(...)

  void setColorScheme(TH2* obj, Int_t cont, Int_t* Colors)
  {
    obj->SetContour(cont);
    gStyle->SetPalette(cont, Colors);
  }

}; // HcalCalibRenderPlugin class

static HcalCalibRenderPlugin instance;
