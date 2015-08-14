/*!
  \file HcalRenderPlugin.cc
  \brief Display Plugin for Hcal DQM Histograms
  \author J. Temple
  \version $Revision: 1.51 $
  \date $Date: 2011/09/09 11:53:43 $
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
using std::string;

class HcalRenderPlugin : public DQMRenderPlugin
{
  // Color schemes

  // errorFracColors, standardColors aren't used
  int errorFracColors[20];
  int standardColors[20];

  Int_t defNCont_;  // default number of contours

  //reportSummary Color Scheme
  int summaryColors[100]; // grey for values of -1, then red at 0 and green above 0.98
  Int_t NRGBs_summary;
  Int_t NCont_summary;

  // error colors:  green for <5% error, then yellow->red, then grey above 100% (previously-known problems)
  int hcalErrorColors[105];
  Int_t NRGBs_hcalError;
  Int_t NCont_hcalError;

  // pretty rainbow scheme!
  int hcalRainbowColors[100];
  Int_t NRGBs_rainbow;
  Int_t NCont_rainbow;

  //timing plot -- rainbows, but plots values at midpoint as white
  // Doesn't yet work -- can't get a fine enough gradation to put white only at exactly 0
  /*
  int hcalTimingColors[100];
  Int_t NRGBs_timing;
  Int_t NCont_timing;
  */

public:
  virtual void initialise (int, char **)
  {
    // Error fraction colors, and standard colors
    // (error fractions colors are the reverse of standard colors)
    //  should probably make error colors run from yellow to red, don't include green?

    float rgb[20][3];

    for( int i=0; i<20; ++i )
      {
        if ( i < 17 )
	  {
	    rgb[i][0] = 0.80+0.01*i;
	    rgb[i][1] = 0.00+0.03*i;
	    rgb[i][2] = 0.00;
	  }
        else if ( i < 19 )
	  {
	    rgb[i][0] = 0.80+0.01*i;
	    rgb[i][1] = 0.00+0.03*i+0.15+0.10*(i-17);
	    rgb[i][2] = 0.00;
	  }
        else if ( i == 19 )
	  {
	    rgb[i][0] = 0.00;
	    rgb[i][1] = 0.80;
	    rgb[i][2] = 0.00;
	  }
        // flip colors from standard values (1=bad, 0=good)
        errorFracColors[19-i] = 901+i;
        standardColors[i]=901+i;
        TColor* color = gROOT->GetColor( 901+i );
        if( ! color ) color = new TColor( 901+i, 0, 0, 0, "" );
        color->SetRGB( rgb[i][0], rgb[i][1], rgb[i][2] );
      }

    // Make rainbow colors.  Assign colors positions 1101-1200;
    NRGBs_rainbow = 5; // specify number of RGB boundaries for rainbow
    NCont_rainbow = 100; // specify number of contours for rainbow
    Double_t stops_rainbow[] = { 0.00, 0.34, 0.61, 0.84, 1.00 };
    Double_t red_rainbow[]   = { 0.00, 0.00, 0.87, 1.00, 0.91 };
    Double_t green_rainbow[] = { 0.00, 0.81, 1.00, 0.20, 0.00 };
    Double_t blue_rainbow[]  = { 0.51, 1.00, 0.12, 0.00, 0.00 };
    Int_t nColorsGradient=0;

    int highestIndex=0;
    for (int g=1;g<NRGBs_rainbow;++g)
      {
        nColorsGradient = (Int_t) (floor(NCont_rainbow*stops_rainbow[g]) - floor(NCont_rainbow*stops_rainbow[g-1])); // specify number of gradients between stops (g-1) and (g)
        for (int c = 0; c < nColorsGradient; c++)
	  {
	    hcalRainbowColors[highestIndex]=1101+highestIndex;
	    TColor* color = gROOT->GetColor(1101+highestIndex);
	    // Make new color only if old color does not exist
	    if (!color)
	      color = new TColor(1101+highestIndex,
				 red_rainbow[g-1] + c * (red_rainbow[g] - red_rainbow[g-1])/ nColorsGradient,
				 green_rainbow[g-1] + c * (green_rainbow[g] - green_rainbow[g-1])/ nColorsGradient,
				 blue_rainbow[g-1] + c * (blue_rainbow[g] - blue_rainbow[g-1])/ nColorsGradient,
				 "  ");
	    highestIndex++;
	  }
      }

    //make summaryColors, with a value of -1 indicated in gray, values >-1 and <0 in white,
    // values 0-0.98 scaling from red to yellow, and values > 0.98 in green.
    // assign values 1201-1300
    NRGBs_summary=7;
    NCont_summary=100;
    Double_t stops_summary[] = {0.00, 0.025, 0.4999, 0.50, 0.99, 0.991, 1.00}; // set limits for color transitions
    Double_t red_summary[]   = {0.6,  1.0,   1.0,    1.0,  1.0,  0.0,   0.00};
    Double_t green_summary[] = {0.6,  1.0,   1.0,    0.0,  1.0,  0.8,   0.80};
    Double_t blue_summary[]  = {0.6,  1.0,   1.0,    0.0,  0.0,  0.0,   0.00};
    nColorsGradient=0;
    highestIndex=0;
    for (int g=1;g<NRGBs_summary;++g)
      {
	nColorsGradient = (Int_t) (floor(NCont_summary*stops_summary[g]) - floor(NCont_summary*stops_summary[g-1])); // specify number of gradients between stops (g-1) and (g)
        for (int c = 0; c < nColorsGradient; c++)
	  {
	    summaryColors[highestIndex]=1201+highestIndex;
	    TColor* color = gROOT->GetColor(1201+highestIndex);
	    // Make new color only if old color does not exist
	    if (!color)
	      color = new TColor(1201+highestIndex,
				 red_summary[g-1] + c * (red_summary[g] - red_summary[g-1])/ nColorsGradient,
				 green_summary[g-1] + c * (green_summary[g] - green_summary[g-1])/ nColorsGradient,
				 blue_summary[g-1] + c * (blue_summary[g] - blue_summary[g-1])/ nColorsGradient,
				 "  ");

	    highestIndex++;
	  }
      }

    /*
    NRGBs_timing = 8; // specify number of RGB boundaries for rainbow
    NCont_timing = 100; // specify number of contours for rainbow
    Double_t stops_timing[] = { 0.00, 0.34, 0.499, 0.500,  0.61, 0.84, 1.00 };
    Double_t red_timing[]   = { 0.00, 0.00, 0.0000, 1.0000, 0.0000, 0.87, 1.00, 0.91 };
    Double_t green_timing[] = { 0.00, 0.81, 1.0000, 1.0000, 1.0000, 1.00, 0.20, 0.00 };
    Double_t blue_timing[]  = { 0.51, 1.00, 1.0000, 1.0000, 0.0000, 0.12, 0.00, 0.00 };
    nColorsGradient=0;
    highestIndex=0;
    for (int g=1;g<NRGBs_timing;++g)
      {
        nColorsGradient = (Int_t) (floor(NCont_timing*stops_timing[g]) - floor(NCont_timing*stops_timing[g-1])); // specify number of gradients between stops (g-1) and (g)
	if (nColorsGradient<-1) continue;
        for (int c = 0; c < nColorsGradient; c++)
	  {
	    hcalTimingColors[highestIndex]=1401+highestIndex;
	    TColor* color = gROOT->GetColor(1401+highestIndex);
	    // Make new color only if old color does not exist
	    if (!color )
	      color = new TColor(1401+highestIndex,
				 red_timing[g-1] + c * (red_timing[g] - red_timing[g-1])/ nColorsGradient,
				 green_timing[g-1] + c * (green_timing[g] - green_timing[g-1])/ nColorsGradient,
				 blue_timing[g-1] + c * (blue_timing[g] - blue_timing[g-1])/ nColorsGradient,
				 "  ");
	    highestIndex++;
	  }
      }
    */

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
    if (o.name.find( "Hcal/" ) != std::string::npos)
      return true;

    return false;
  }

  virtual void preDraw (TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &, VisDQMRenderInfo &)
  {
    c->cd();

    gStyle->Reset("Default");
    defNCont_=gStyle->GetNumberContours(); // test this later
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
      {   postDrawTProfile( c, o );   }
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
    // Do we want to do anything special yet with TH1 histograms?
    TH1* obj = dynamic_cast<TH1*>( o.object );
    assert (obj); // checks that object indeed exists

    // For now, all 1D plots have stats on.  Disable in future?
    gStyle->SetOptStat("iourmen");
    obj->SetStats(kTRUE);

    // o.name is a std::string object
    // Add in list of names of histograms for which we want log plotting here.

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
      } // DataFormatMonitor/ search

    else if (o.name.find("DigiMonitor_Hcal/") !=std::string::npos)
      {

	// good_digis subdirectory
	if  (o.name.find("/good_digis/")!=std::string::npos)
	  {
	   if (o.name.find("Number of Good Digis") !=std::string::npos)
	     {
	       if (obj->GetMaximum()>0) gPad->SetLogy(1);
	     }
	   else if (o.name.find("digi_occupancy/") !=std::string::npos)
	     obj->SetMinimum(0);
	  } // good_digis subdirectory

	// digi_info subdirectory
	else if (o.name.find("/digi_info/")!=std::string::npos)
	  {
	    if ( (o.name.find(" CapID") != std::string::npos) ||
		 (o.name.find(" Digi Shape") != std::string::npos) ||
		 (o.name.find("Digi Shape - over thresh") !=std::string::npos)
		 )
	      {
		obj->SetMinimum(0.);
	      }
	    else if (o.name.find("Number of Digis") !=std::string::npos)
	      {
		if (obj->GetMaximum()>0) gPad->SetLogy(1);
		gStyle->SetOptStat("iourmen");
		obj->SetStats(kTRUE);
	      }
	    else if (o.name.find(" Capid 1st Time Slice") !=std::string::npos)
	      {
		if (obj->GetMaximum()>0) gPad->SetLogy(1);
	      }
	  } // digi_info subdirectory

	else if (o.name.find("/bad_digis/") !=std::string::npos)
	  {
	    gStyle->SetOptStat("iourmen");
	    obj->SetStats(kTRUE);
	    if ((o.name.find("# Bad Qual Digis")  != std::string::npos) ||
		(o.name.find("Bad Digi Fraction") != std::string::npos) ||
		(o.name.find("Unpacker Bad Digi Fraction") != std::string::npos) ||
		(o.name.find("Unpacker Error Count") != std::string::npos)
		)
	      gPad->SetLogx(1);
	  } // bad digi folder
      } // DigiMonitor_Hcal/ search

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

    else if (o.name.find("DeadCellMonitor_Hcal/") !=std::string::npos)
      {
	if (o.name.find("Problem_Total_DeadCells_") != std::string::npos )
	  {
	    gStyle->SetOptStat("iourmen");
	    obj->SetStats( kTRUE );
	  }
	else if (o.name.find("NumberOfDeadCellEvents")!=std::string::npos)
	  obj->SetMinimum(0);
      } // DeadCellMonitor

    else if (o.name.find("HcalInfo/") !=std::string::npos)
      {
	if (o.name.find("CalibrationType")!=std::string::npos && obj->GetMaximum()>0)
	  gPad->SetLogy();
      }
  } // void preDrawTH1(...)

  void preDrawTH2 ( TCanvas *c, const VisDQMObject &o )
  {
    TH2* obj = dynamic_cast<TH2*>( o.object );
    assert( obj );

    gStyle->SetCanvasBorderMode( 0 );
    gStyle->SetPadBorderMode( 0 );
    gStyle->SetPadBorderSize( 0 );

    // Do we want to set stats to 0 for Hcal?
    gStyle->SetOptStat( 0 );
    obj->SetStats( kFALSE );

    // Default coloring scheme
    setRainbowColor(obj); // sets to rainbow color with finer gradations than setPalette(1)
    obj->SetOption("colz");
    c->SetRightMargin(2*c->GetRightMargin()); // double right margin

    if ((o.name.find("DataFormatMonitor/Corruption/") !=std::string::npos) ||
	(o.name.find("RawDataMonitor_Hcal/Corruption") !=std::string::npos)  ){
      // Set error palette for normalized histograms.
      // Setting error color forces min/max to be 0./1.05, since otherwise, colors aren't sensible
      //setErrorColor(obj);
      obj->SetOption("colz");
      gStyle->SetFrameFillColor(17);
    }
    // Set default color scheme

    // For reportSummary plots, use the summaryColors defined within this code
    // green when =1, red when = 0, grey when = -1

    if (o.name.find("reportSummaryMap" ) != std::string::npos)
      {
	obj->SetContour(100);
        setSummaryColor(obj);
	gStyle->SetPaintTextFormat("5.4g"); // set to %5.4f  text format in cells
	obj->SetMarkerSize(3); // set font size to 3x normal
        obj->SetOption("text90colz"); // draw marker at 90 degrees
	// Set min, max values to -1, 1
	obj->SetMinimum(-1.);
	obj->SetMaximum(1.);
      }
    else if (o.name.find("ZDCMonitor_Hcal/ZDC_ReportSummary")!=std::string::npos)
      {
	obj->SetContour(100);
	setSummaryColor(obj);
	gStyle->SetPaintTextFormat("5.4g");
	obj->SetMarkerSize(3);
	obj->SetOption("text90colz");
	obj->SetMinimum(-1.);
	obj->SetMaximum(1.);
      }
    else if (o.name.find("ZDCMonitor_Hcal/ZDC_Channel_Summary")!=std::string::npos)
      {
	obj->SetContour(100);
	setSummaryColor(obj);
	gStyle->SetPaintTextFormat("5.4g");
	obj->SetMarkerSize(2);
	obj->SetOption("textcolz");
	obj->SetMinimum(-1.);
	obj->SetMaximum(1.);
      }
    else if (o.name.find("ZDCMonitor_Hcal/Errors/ZDC_TotalChannelErrors")!=std::string::npos)
      {
	obj->SetContour(100);
	setRainbowColor(obj);
	gStyle->SetPaintTextFormat("5.4g");
	obj->SetMarkerSize(2);
	obj->SetOption("textcolz");
      }
    else if (o.name.find("ZDCMonitor_Hcal/Errors/ColdChannel/ZDC_Cold_Channel_Fraction")!=std::string::npos)
      {
	obj->SetContour(100);
	setRainbowColor(obj);
	gStyle->SetPaintTextFormat("5.4g");
	obj->SetMarkerSize(2);
	obj->SetOption("textcolz");
	obj->SetMinimum(-1.);
	obj->SetMaximum(1.);
      }
    else if (o.name.find("ZDCMonitor_Hcal/Errors/ColdChannel/ZDC_Cold_Channel_Errors")!=std::string::npos)
      {
        obj->SetContour(100);
        setRainbowColor(obj);
        gStyle->SetPaintTextFormat("5.4g");
        obj->SetMarkerSize(2);
	obj->SetOption("textcolz");
      }
    else if (o.name.find("ZDCMonitor_Hcal/Errors/DeadChannel/ZDC_Dead_Channel_Fraction")!=std::string::npos)
      {
	obj->SetContour(100);
	setRainbowColor(obj);
	gStyle->SetPaintTextFormat("5.4g");
	obj->SetMarkerSize(2);
	obj->SetOption("textcolz");
	obj->SetMinimum(-1.);
	obj->SetMaximum(1.);
      }
    else if (o.name.find("ZDCMonitor_Hcal/Errors/DeadChannel/ZDC_Dead_Channel_Errors")!=std::string::npos)
      {
	obj->SetContour(100);
	setRainbowColor(obj);
	gStyle->SetPaintTextFormat("5.4g");
	obj->SetMarkerSize(2);
	obj->SetOption("textcolz");
      }
    else if (o.name.find("ZDCMonitor_Hcal/Errors/HotChannel/ZDC_Hot_Channel_Fraction")!=std::string::npos)
      {
	obj->SetContour(100);
	setRainbowColor(obj);
	gStyle->SetPaintTextFormat("5.4g");
	obj->SetMarkerSize(2);
	obj->SetOption("textcolz");
	obj->SetMinimum(-1.);
	obj->SetMaximum(1.);
      }
    else if (o.name.find("ZDCMonitor_Hcal/Errors/HotChannel/ZDC_Hot_Channel_Errors")!=std::string::npos)
      {
	obj->SetContour(100);
	setRainbowColor(obj);
	gStyle->SetPaintTextFormat("5.4g");
	obj->SetMarkerSize(2);
	obj->SetOption("textcolz");
      }
    else if (o.name.find("ZDCMonitor_Hcal/Errors/Digis/ZDC_Digi_Error_Fraction")!=std::string::npos)
      {
	obj->SetContour(100);
	setRainbowColor(obj);
	gStyle->SetPaintTextFormat("5.4g");
	obj->SetMarkerSize(2);
	obj->SetOption("textcolz");
	obj->SetMinimum(-1.);
	obj->SetMaximum(1.);
      }
    else if (o.name.find("ZDCMonitor_Hcal/Errors/Digis/ZDC_Digi_Errors")!=std::string::npos)
      {
	obj->SetContour(100);
	setRainbowColor(obj);
	gStyle->SetPaintTextFormat("5.4g");
	obj->SetMarkerSize(2);
	obj->SetOption("textcolz");
      }
    else if (o.name.find("ZDCMonitor_Hcal/Errors/Digis/DigiErrorCauses/ZDC_DigiErrors_CAPID")!=std::string::npos)
      {
	obj->SetContour(100);
	setRainbowColor(obj);
	gStyle->SetPaintTextFormat("5.4g");
	obj->SetMarkerSize(2);
	obj->SetOption("textcolz");
      }
    else if (o.name.find("ZDCMonitor_Hcal/Errors/Digis/DigiErrorCauses/ZDC_DigiErrors_DVER")!=std::string::npos)
      {
	obj->SetContour(100);
	setRainbowColor(obj);
	gStyle->SetPaintTextFormat("5.4g");
	obj->SetMarkerSize(2);
	obj->SetOption("textcolz");
      }
    else if (o.name.find("HcalInfo/CertificationMap")!=std::string::npos)
      {
	c->SetLeftMargin(0.20);
	obj->SetContour(100);
        setSummaryColor(obj);
	obj->SetOption("textcolz");
	obj->SetMinimum(-1.);
	obj->SetMaximum(1.);
      }
    else if (o.name.find("EventInfo/HB HE HF Depth 1 Summary Map") != std::string::npos ||
	     o.name.find("EventInfo/HB HE HF Depth 2 Summary Map") != std::string::npos ||
	     o.name.find("EventInfo/HE Depth 3 Summary Map") != std::string::npos ||
	     o.name.find("EventInfo/HO Depth 4 Summary Map") != std::string::npos ||
	     o.name.find("HcalInfo/SummaryClientPlots/StatusVsLS") !=std::string::npos
	     )
      {
	setSummaryColor(obj);
	obj->SetMinimum(-1.);
	obj->SetMaximum(1.);
      }

    else if (o.name.find("advancedReportSummaryMap" ) != std::string::npos)
      {
	obj->SetContour(40);
        setSummaryColor(obj);
        obj->SetOption("colz");
	obj->SetMinimum(-1.);
	obj->SetMaximum(1.);
      }

    // Pedestal mean plots -- center at 3, with range [1,5]
    else if ((o.name.find("CoarsePedestalMonitor_Hcal/HB HE HF Depth")!= std::string::npos) ||
	     (o.name.find("CoarsePedestalMonitor_Hcal/HE Depth")!= std::string::npos) ||
	     (o.name.find("CoarsePedestalMonitor_Hcal/HO Depth")!= std::string::npos))
      {
	obj->SetContour(100);
	setRainbowColor(obj);
	// same limits as for DetDiagPedestalMonitor
	obj->SetOption("colz");
	obj->SetMinimum(1.);
	obj->SetMaximum(5.);
      }

    // Normalized error rate histograms plotted with error Fraction colors (0 = green, 1 = red)
    else if ( (o.name.find("RecHitMonitor_Hcal/ ProblemRecHits")!= std::string::npos ) ||
	      (o.name.find("RecHitMonitor_Hcal/problem_rechits/")!= std::string::npos ) ||
	      (o.name.find("DigiMonitor_Hcal/ ProblemDigis")!= std::string::npos ) ||
	      (o.name.find("DigiMonitor_Hcal/problem_digis/")!= std::string::npos ) ||
	      (o.name.find("HotCellMonitor_Hcal/ ProblemHotCells")!= std::string::npos ) ||
	      (o.name.find("HotCellMonitor_Hcal/problem_hotcells/") != std::string::npos) ||
	      (o.name.find("DeadCellMonitor_Hcal/ ProblemDeadCells")!= std::string::npos ) ||
	      (o.name.find("DeadCellMonitor_Hcal/problem_deadcells/")!= std::string::npos ) ||
	      (o.name.find("BeamMonitor_Hcal/ ProblemBeamMonitor")!= std::string::npos ) ||
	      (o.name.find("BeamMonitor_Hcal/ Problem BeamMonitor")!= std::string::npos ) ||
	      (o.name.find("BeamMonitor_Hcal/problem_beammonitor/")!= std::string::npos )  ||
	      (o.name.find("TrigPrimMonitor_Hcal/ ProblemTriggerPrimitives")  != std::string::npos) ||
	      (o.name.find("TrigPrimMonitor_Hcal/problem_triggerprimitives")  != std::string::npos) ||
	      (o.name.find("NZSMonitor_Hcal/ ProblemNZS")  != std::string::npos) ||
	      (o.name.find("NZSMonitor_Hcal/problem_NZS/") != std::string::npos) ||
	      (o.name.find("RawDataMonitor_Hcal/ ProblemRawData")   != std::string::npos) ||
	      (o.name.find("RawDataMonitor_Hcal/problem_rawdata/") != std::string::npos) ||
	      (o.name.find("DataFormatMonitor/ HardwareWatchCells")!= std::string::npos) ||
	      (o.name.find("DataFormatMonitor/H")!= std::string::npos)  ||
	      (o.name.find("CoarsePedestalMonitor_Hcal/ ProblemCoarsePedestals")!= std::string::npos) ||
	      (o.name.find("CoarsePedestalMonitor_Hcal/problem_coarsepedestals")!= std::string::npos) ||
	      //(o.name.find("CoarsePedestalMonitor_Hcal/HB HE HF Depth")!= std::string::npos) ||
	      //(o.name.find("CoarsePedestalMonitor_Hcal/HE Depth")!= std::string::npos) ||
	      //(o.name.find("CoarsePedestalMonitor_Hcal/HO Depth")!= std::string::npos) ||
	      (o.name.find("HcalInfo/SummaryClientPlots") !=std::string::npos)
	      )
      {
	gStyle->SetFrameFillColor(17);  // set background to grey so that yellow can stand out

	// rescaling -- can probably be removed
        double scale = obj->GetBinContent(0,0);
        if (scale>1) // problem histograms don't have underflow bins filled any more
	  obj->Scale(1./scale);

	// Set error palette for normalized histograms.
	// Setting error color forces min/max to be 0./1.05, since otherwise, colors aren't sensible
	setErrorColor(obj);
	obj->SetOption("colz");

	// cells satisfying hot criterion in <1% of events not shown by default?  Disrupts overall color mapping?
	if (o.name.find("HotCellMonitor_Hcal/")!=std::string::npos)
	  obj->SetMinimum(0.01);
      }

    // Do we want these plots to show error fractions (0-1) as well?
    // I think it's useful to have raw number of events plotted here; don't renormalize yet

    else if (// Hot Cell subdirectories
	     (o.name.find("HotCellMonitor_Hcal/hot_pedestaltest/") != std::string::npos) ||
	     (o.name.find("HotCellMonitor_Hcal/hot_rechit_above_threshold/") != std::string::npos) ||
	     (o.name.find("HotCellMonitor_Hcal/hot_rechit_always_above_threshold/") != std::string::npos) ||
	     (o.name.find("HotCellMonitor_Hcal/hot_neighbortest/") != std::string::npos)  ||
	     // Dead Cell subdirectories
	     (o.name.find("DeadCellMonitor_Hcal/dead_digi_often_missing/")!= std::string::npos ) ||
	     (o.name.find("DeadCellMonitor_Hcal/dead_energytest/")!= std::string::npos ) ||
	     // Digi Subdirectories
	     (o.name.find("DigiMonitor_Hcal/bad_digis/bad_digi_occupancy/")!=std::string::npos) ||
	     (o.name.find("DigiMonitor_Hcal/bad_digis/bad_reportUnpackerErrors/")!=std::string::npos) ||
	     (o.name.find("DigiMonitor_Hcal/bad_digis/baddigisize/")!=std::string::npos) ||
	     (o.name.find("DigiMonitor_Hcal/bad_digis/badfibBCNoff/")!=std::string::npos) ||
	     //(o.name.find("DigiMonitor_Hcal/good_digis/digi_occupancy/")!=std::string::npos) // don't want to apply error color here
	     (o.name.find("BeamMonitor_Hcal/Lumi/HFlumi_total_")!=std::string::npos) ||
	     (o.name.find("DataFormatMonitor/ HardwareWatchCells")!= std::string::npos ) ||
	     (o.name.find("DataFormatMonitor/H")!= std::string::npos)
	     //(o.name.find("BeamMonitor_Hcal/Lumi/Abnormal PMT events")!=std::string::npos) // not sure we want to normalize this one yet -- raw # of errors may still be useful
	     )
      {
	gPad->SetGridx();
	gPad->SetGridy();
        double scale = obj->GetBinContent(0,0);
        if (scale>0)
	  {
	    obj->SetMaximum(obj->GetBinContent(0,0));
	    obj->SetMinimum(0.);
	    obj->SetStats(0);
	  }
        setOldErrorColor(obj);
        obj->SetOption("colz");
      }

    else if (o.name.find("DeadCellMonitor_Hcal/dead_digi_never_present")!=std::string::npos)
      obj->SetMaximum(2); // useful for offline running, where multiple entries fill the occupancy hist more than once.  Good occupancy will have value=1 (appears green in rainbow)

    else if (
	     (o.name.find("ADC Pedestals From Conditions DB")!=std::string::npos)
	     )
      {
        // ADC pedestals should be centered at 3; set maximum to 2*3=6
        obj->SetMinimum(0.);
	obj->SetMaximum(6.);
        setRainbowColor(obj); // sets to rainbow color with finer gradations than setPalette(1)
        obj->SetOption("colz");
      }
    else if (o.name.find("TrigPrimMonitor_Hcal/")!=std::string::npos)
      {
	if ((o.name.find("Error Flag_")!=std::string::npos) ||
	    (o.name.find("FG Correlation_")!=std::string::npos))
	  {
	    obj->SetOption("textcolz");
	    gPad->SetLogz();
	  }
      }
    else if (o.name.find("RecHitMonitor_Hcal/")!=std::string::npos)
      {
	if (o.name.find("RecHit Average Time")!=std::string::npos)
	  {
	    obj->SetMinimum(-150);
	    obj->SetMaximum(150);
	    //setTimingColor(obj);
	    // add color scheme later that plots t=0.0000 as white (indicating empty channels)
	  }
	else if ((o.name.find("RecHit Occupancy")!=std::string::npos)||
		 (o.name.find("RecHit Average Energy")!=std::string::npos)
		 )
	  {
	    if (obj->GetMaximum()>0 )// is this what we want?  Suppose average energy is <0?
	      gPad->SetLogz();
	  }
      } // RecHitMonitor_Hcal

  } // void preDrawTH2

  void preDrawTProfile ( TCanvas *, const VisDQMObject &o )
  {
    TProfile* obj = dynamic_cast<TProfile*>( o.object );
    assert( obj );
    // Set TProfile boundaries to first/last bins that have non-zero content
    bool foundfirst=false;
    int firstnonzerobin=1;
    int lastnonzerobin=1;
    double minvalue=9999999;
    for (int i=1;i<=obj->GetNbinsX();++i)
      {
	if (foundfirst==false && obj->GetBinContent(i)!=0)
	  {
	    foundfirst=true;
	    firstnonzerobin=i;
	  }
	if (obj->GetBinContent(i)!=0)
	  lastnonzerobin=i+1;
	if (obj->GetBinContent(i)-obj->GetBinError(i)<minvalue)
	  minvalue = obj->GetBinContent(i)-obj->GetBinError(i);
      }
    if (minvalue>0)
      obj->SetMinimum(0); // do this for all TProfiles?
    if (lastnonzerobin-firstnonzerobin>1)
      obj->GetXaxis()->SetRange(firstnonzerobin,lastnonzerobin-1);
    obj->SetMarkerStyle(20); // always show average as a closed circle
    return;
  }

  void postDrawTH1( TCanvas *, const VisDQMObject &o )
  {
    TH1* obj = dynamic_cast<TH1*>( o.object );
    assert( obj );

    if ( ((o.name.find("DataFormatMonitor/Corruption")      != std::string::npos) ||
	  (o.name.find("RawDataMonitor_Hcal/Corruption")      != std::string::npos)   )&&
	 (obj->GetMaximum() == 0.0) )
      {
        TText t;
        t.SetTextSize( 0.1);
	if (o.name.find("BCN when OrN") !=std::string::npos)
	  t.DrawText(0, 0, "Empty == OK");
	else
	  t.DrawText(-1*(obj->GetNbinsX() * 0.5), 0, "Empty == OK");

      }
    else if (o.name.find("BeamMonitor_Hcal") !=std::string::npos)
      {
	if (o.name.find("/Lumi") !=std::string::npos && obj->GetMinimum()>0)
	  obj->SetMinimum(0);
      } // BeamMonitor_Hcal
  }

  void postDrawTH2( TCanvas *c, const VisDQMObject &o )
  {
    TH2* obj = dynamic_cast<TH2*>( o.object );
    assert( obj );

    if (o.name.find("reportSummaryMap" ) != std::string::npos)
      {
	if (obj->GetBinContent(0,0)==-1) // insufficient events for certification
	  {
	    TText t;
	    t.SetTextSize(0.05);
	    t.DrawText(0,0.9, "Insufficient Events for");
	    t.DrawText(0,0.8, "Run Certification!");
	  }
      }

    // in the future, we can add text output based on error status,
    // or set bin range based on filled histograms, etc.
    if ( (o.name.find("RawDataMonitor_Hcal/Corruption")      != std::string::npos)   ||
	 (o.name.find("RawDataMonitor_Hcal/Corruption/F")      != std::string::npos) ||
	 (o.name.find("DataFormatMonitor/Corruption")      != std::string::npos)   ||
	 (o.name.find("DataFormatMonitor/Corruption/F")      != std::string::npos) )
      {
        TText t;
	//setErrorColor(obj); // not sure we want to do this, unless we are sure plots are normalized

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
	//setErrorColor(obj);
	obj->SetOption("colz");
	gStyle->SetFrameFillColor(17);
	//obj->SetMaximum(1.05);
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
	setOldErrorColor(obj);
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
	setOldErrorColor(obj);
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
	    tx.DrawText((FEDS3_X0*30)+4 , (SPIG3_Y0*17)-5  , "IW");}
      }  // o.name.find("Corruption/08")

    else if ( (o.name.find("DigiMonitor_Hcal/ ProblemDigis")!= std::string::npos ) ||
	      (o.name.find("DigiMonitor_Hcal/problem_digis")!= std::string::npos ) ||
	      (o.name.find("BaselineMonitor_Hcal/ ProblemPedestals")!=std::string::npos) ||
	      (o.name.find("BaselineMonitor_Hcal/problem_pedestals")!=std::string::npos) ||
	      (o.name.find("HotCellMonitor_Hcal/ ProblemHotCells")!= std::string::npos ) ||
	      (o.name.find("HotCellMonitor_Hcal/problem_hotcells/") != std::string::npos) ||
	      (o.name.find("DeadCellMonitor_Hcal/ ProblemDeadCells")!= std::string::npos ) ||
	      (o.name.find("DeadCellMonitor_Hcal/problem_deadcells")!= std::string::npos ) ||
	      (o.name.find("RecHitMonitor_Hcal/ ProblemRecHits")!= std::string::npos ) ||
	      (o.name.find("RecHitMonitor_Hcal/problem_rechits")!= std::string::npos ) ||
	      (o.name.find("BeamMonitor_Hcal/ ProblemBeamMonitor")!= std::string::npos ) ||
	      (o.name.find("BeamMonitor_Hcal/problem_beammonitor")!= std::string::npos ) ||
	      //(o.name.find("DataFormatMonitor/ HardwareWatchCells") != std::string::npos) ||
	      (o.name.find("BeamMonitor_Hcal/ Problem BeamMonitor")!= std::string::npos ) ||
	      (o.name.find("BeamMonitor_Hcal/problem_beammonitor/")!= std::string::npos )  ||
	      (o.name.find("TrigPrimMonitor_Hcal/ ProblemTriggerPrimitives")  != std::string::npos) ||
	      (o.name.find("TrigPrimMonitor_Hcal/problem_triggerprimitives")  != std::string::npos) ||
	      (o.name.find("NZSMonitor_Hcal/ ProblemNZS")  != std::string::npos) ||
	      (o.name.find("NZSMonitor_Hcal/problem_NZS/") != std::string::npos) ||
	      (o.name.find("RawDataMonitor_Hcal/ ProblemRawData")   != std::string::npos) ||
	      (o.name.find("RawDataMonitor_Hcal/problem_rawdata/") != std::string::npos) ||
	      (o.name.find("CoarsePedestalMonitor_Hcal/ ProblemCoarsePedestals")   != std::string::npos) ||
	      (o.name.find("CoarsePedestalMonitor_Hcal/problem_coarsepedestals")!= std::string::npos) ||
	      (o.name.find("CoarsePedestalMonitor_Hcal/HB HE HF Depth")!= std::string::npos) ||
	      (o.name.find("CoarsePedestalMonitor_Hcal/HE Depth")!= std::string::npos) ||
	      (o.name.find("CoarsePedestalMonitor_Hcal/HO Depth")!= std::string::npos) ||
	      (o.name.find("DataFormatMonitor/ HardwareWatchCells")!= std::string::npos)

	      )
      {
        if ((obj->GetEntries()==0) ||
            ((obj->GetEntries()-obj->GetBinContent(0,0)) == 0) //underflow bin (0,0) stores ievt_; ignore this when checking for empty histograms?  nope, still doesn't work.  Dang!
	    )
	  {
	    gStyle->SetOptStat(1111);
	    obj->SetStats(1111);
	    TText t;
	    t.DrawText(1,1,"No entries found");
	  }
        else
	  {
	    gStyle->SetOptStat(0);
	    obj->SetStats(0);
	    gPad->SetGridx();
	    gPad->SetGridy();
	  }
      }

    if ((o.name.find("RecHitMonitor_Hcal")!=std::string::npos) &&
	(o.name.find("FlagCorrelation")!=std::string::npos))
      {
	gPad->SetLogz();
	obj->SetDrawOption("textcolz");
      }

    // Dead Cell check -- warn that plots need many events before they update
    if (o.name.find("DeadCellMonitor_Hcal/" )!=std::string::npos)
      {
	if ( (o.name.find("DeadCellMonitor_Hcal/dead_digi_often_missing")!=std::string::npos) ||
	     (o.name.find("DeadCellMonitor_Hcal/dead_digi_never_present")!=std::string::npos) ||
	     (o.name.find("DeadCellMonitor_Hcal/problem_deadcells")      !=std::string::npos) ||
	     (o.name.find("DeadCellMonitor_Hcal/ ProblemDeadCells")      !=std::string::npos) //||
	     // (o.name.find("DeadCellMonitor_Hcal/TotalDeadCells_HCAL_vs_LS") !=std::string::npos)
	     )
	  {
	    TText t;
	    t.DrawTextNDC(0.05,0.01,"Histogram updates every N lumi sections");
	  }
      } // if (o.name.find("DeadCellMonitor_Hcal/"...)

    //drawEtaPhiLines(obj);

  }

  ////////////
  void postDrawTProfile( TCanvas *c, const VisDQMObject &o )
  {
    TProfile* obj = dynamic_cast<TProfile*>( o.object );
    assert( obj );

    std::string name = o.name.substr(o.name.rfind("/")+1);

    int lastnonzerobin=1;

    if( (o.name.find("DeadCellMonitor_Hcal/TotalDeadCells_HCAL_vs_LS") !=std::string::npos) ||
	(o.name.find("DeadCellMonitor_Hcal/TotalDeadCells_HO_vs_LS") !=std::string::npos) ||
	(o.name.find("DeadCellMonitor_Hcal/TotalDeadCells_HBHEHF_vs_LS") !=std::string::npos)
	)
      {
	//Search for the last deadcell count
	for (int i=1;i<=obj->GetNbinsX();++i)
	  {
	    if (obj->GetBinContent(i)!=0)
	      lastnonzerobin=i+1;
	  }

        if (obj->GetBinContent(lastnonzerobin-1) > 50.0)
	  {
            if(obj->GetBinContent(0) > 0 )
              {
                TText t;
                t.SetTextSize(0.07);
                t.SetTextColor(1);
                t.DrawTextNDC(0.1,0.5,"Known problem, no need to call HCAL experts!");
              }
            else
              {
	    c->SetFillColor(2);
	    TText t;
	    t.SetTextSize(0.07);
	    t.SetTextColor(2);
	    t.DrawTextNDC(0.2,0.5,"WARNING: # of dead channels is above 50");
	  }
          }
        return;
      }
  }

  /////////////

void setRainbowColor(TH2* obj)
  {
    obj->SetContour(NCont_rainbow);
    gStyle->SetPalette(NCont_rainbow,hcalRainbowColors);
  }

  /*
void setTimingColor(TH2* obj)
  {
    obj->SetContour(NCont_timing);
    gStyle->SetPalette(NCont_timing,hcalTimingColors);
  }
  */

void setSummaryColor(TH2* obj)
{
  obj->SetContour(NCont_summary);
  gStyle->SetPalette(NCont_summary,summaryColors);
}

void setErrorColor(TH2* obj)
{
  obj->SetMinimum(0.00);
  obj->SetMaximum(1.05);
  obj->SetContour(NCont_hcalError);
  gStyle->SetPalette(NCont_hcalError,hcalErrorColors);
}

void setOldErrorColor(TH2* obj)
{
  obj->SetContour(100);
}

  void drawEtaPhiLines(TH2* obj)
  {
    // I don't think we want these any more; it's easier just to zoom in from onlineDQM
    TAxis *xaxis =obj->GetXaxis();
    TAxis *yaxis=obj->GetYaxis();
    if (xaxis->GetXmax()!=HCAL_ETAMAX) return;
    if (xaxis->GetXmin()!=HCAL_ETAMIN) return;
    if (yaxis->GetXmax()!=HCAL_PHIMAX) return;
    if (yaxis->GetXmin()!=HCAL_PHIMIN) return;

    TLine* vert=0;
    TLine* horiz=0;
    // Draw vertical lines

    for (int xx=int(xaxis->GetXmin());
	 xx<=int(xaxis->GetXmax()); ++xx)
      {
        if (xx<-42 || xx >= 42) continue;
        vert = new TLine(xx+0.5,0.5,xx+0.5,72.5);
        vert->SetLineStyle(3);
        vert->Draw("same");
      }

    // Draw horizontal lines
    for (int yy=int(yaxis->GetXmin()); yy<int(yaxis->GetXmax());++yy)
      {
        if (yy%4==0)
          horiz = new TLine(-41.5,yy+0.5,41.5,yy+0.5);
        else if (yy%2==0)
          horiz = new TLine(-39.5,yy+0.5,39.5,yy+0.5);
        else
          horiz = new TLine(-20.5,yy+0.5,20.5,yy+0.5);
        horiz->SetLineStyle(3);
        horiz->Draw("same");
      }
  }
}; // HcalRenderPlugin class

static HcalRenderPlugin instance;
