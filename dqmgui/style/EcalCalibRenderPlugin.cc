// $Id: EcalCalibRenderPlugin.cc,v 1.4 2011/09/02 20:27:19 yiiyama Exp $

/*!
  \file EcalCalibRenderPlugin
  \brief Display Plugin for Quality Histograms
  \author Y. Iiyama
  \version $Revision: 1.4 $
  \date $Date: 2011/09/02 20:27:19 $
*/

#include "DQM/DQMRenderPlugin.h"
#include "utils.h"

#include "TH1F.h"
#include "TH1D.h"
#include "TH2C.h"
#include "TH2S.h"
#include "TH2F.h"
#include "TH2D.h"
#include "TH3F.h"
#include "TProfile.h"
#include "TProfile2D.h"

#include "TStyle.h"
#include "TCanvas.h"
#include "TGaxis.h"
#include "TF1.h"
#include "TColor.h"
#include "TGraph.h"
#include "TROOT.h"
#include "TLine.h"
#include "TClass.h"

#include <iostream>
#include <sstream>
#include <iomanip>
#include <stdexcept>
#include <math.h>
#include <cassert>

class EcalCalibRenderPlugin : public DQMRenderPlugin
{
  static const int ixSectorsEE[202];
  static const int iySectorsEE[202];
  static const int inTowersEE[400];

  TH2C *ebLabelsSMCrystal;
  TH2S *eeLabelsSMCrystal;
  int pStatus[3]; // green, yellow, red

  TF1 *logFunc;
  TGaxis *logAxis;

public:
  ~EcalCalibRenderPlugin()
  {
    if(logAxis) delete logAxis;
    if(logFunc) delete logFunc;
  }

  virtual void initialise( int, char ** )
  {

    pStatus[0] = kRed;
    pStatus[1] = kYellow;
    pStatus[2] = kGreen;

    ebLabelsSMCrystal = new TH2C( "ebLabelsSMCrystal", "ebLabelsSMCrystal", 85, 0, 85, 20, 0, 20);
    eeLabelsSMCrystal = new TH2S( "eeLabelsSMCrystal", "eeLabelsSMCrystal", 100, -2., 98., 100, -2., 98.); // to be used for all SMs; range must be 100

    ebLabelsSMCrystal->SetMinimum( 0.1 );
    eeLabelsSMCrystal->SetMinimum( 0.1 );

    for(int i=0; i<68; i++){
      ebLabelsSMCrystal->SetBinContent( 2+(i/4)*5, 2+(i%4)*5, i+1 );
    }

    for(int i=0; i<400; i++){
      int x = 5*(1 + i%20);
      int y = 5*(1 + i/20);
      eeLabelsSMCrystal->SetBinContent( x, y, inTowersEE[i]);
    }

    ebLabelsSMCrystal->SetMarkerSize( 2 );
    eeLabelsSMCrystal->SetMarkerSize( 2 );

    logFunc = new TF1("logVernier", "log10(x)");
    logAxis = new TGaxis(0,0,1,1,"logVernier",510);
  }

  virtual bool applies( const VisDQMObject &o, const VisDQMImgInfo & )
  {
    if( o.name.find( "EcalCalibration/" ) != std::string::npos )
      return true;

    return false;
  }

  virtual void preDraw( TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &, VisDQMRenderInfo &r )
  {
    c->cd();

    gStyle->Reset("Default");

    gStyle->SetCanvasColor(10);
    gStyle->SetPadColor(10);
    gStyle->SetFillColor(10);
    gStyle->SetFrameFillColor(10);
    gStyle->SetStatColor(10);
    gStyle->SetTitleFillColor(10);

    gStyle->SetOptTitle(kTRUE);
    gStyle->SetTitleBorderSize(0);

    gStyle->SetOptStat(kFALSE);
    gStyle->SetStatBorderSize(1);

    gStyle->SetOptFit(kFALSE);

    gStyle->SetPalette( 1 );

    gStyle->SetPaintTextFormat("+g");

    gROOT->ForceStyle();

    TObject *obj = o.object;

    if( !obj ) return;

    if( obj->InheritsFrom("TH2") ){
      preDrawTH2( c, o, r );
    }

    if( obj->IsA() == TClass::GetClass("TProfile2D") )
      {
        preDrawTProfile2D( c, o, r );
      }
    else if( obj->IsA() == TClass::GetClass("TProfile") )
      {
        preDrawTProfile( c, o, r );
      }
    else if( obj->IsA() == TClass::GetClass("TH3F") )
      {
        preDrawTH3F( c, o, r );
      }
    else if( obj->IsA() == TClass::GetClass("TH2F") || obj->IsA() == TClass::GetClass("TH2D") )
      {
        preDrawTH2FD( c, o, r );
      }
    else if( obj->IsA() == TClass::GetClass("TH1F") || obj->IsA() == TClass::GetClass("TH1D") )
      {
        preDrawTH1( c, o, r );
      }
  }

  virtual void postDraw( TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo & )
  {
    c->cd();

    TObject *obj = o.object;

    if( !obj ) return;

    if( obj->InheritsFrom("TH2") ){
      postDrawTH2( c, o );
    }

    if( obj->IsA() == TClass::GetClass("TProfile2D") )
      {
        postDrawTProfile2D( c, o );
      }
    else if( obj->IsA() == TClass::GetClass("TProfile") )
      {
        postDrawTProfile( c, o );
      }
    else if( obj->IsA() == TClass::GetClass("TH3F") )
      {
        postDrawTH3F( c, o );
      }
    else if( obj->IsA() == TClass::GetClass("TH2F") || obj->IsA() == TClass::GetClass("TH2D") )
      {
        postDrawTH2FD( c, o );
      }
    else if( obj->IsA() == TClass::GetClass("TH1F") || obj->IsA() == TClass::GetClass("TH1D") )
      {
        postDrawTH1( c, o );
      }
  }

private:

  void preDrawTH2( TCanvas *, const VisDQMObject &o, VisDQMRenderInfo & ){
    TH2 *obj = dynamic_cast<TH2 *>( o.object );
    assert( obj );

    std::string name = o.name.substr(o.name.rfind("/")+1);

    int nbx = obj->GetNbinsX();
    int nby = obj->GetNbinsY();

    if( ( nbx == 85 && nby == 20 ) && name.find( "EB" ) != std::string::npos ){
      gPad->SetGridx();
      gPad->SetGridy();
      obj->GetXaxis()->SetNdivisions(17);
      obj->GetYaxis()->SetNdivisions(4);
    }

    if( ( nbx == 50 && nby == 50 ) && name.find( "EE" ) != std::string::npos ){
      gPad->SetGridx();
      gPad->SetGridy();
      obj->GetXaxis()->SetNdivisions(10);
      obj->GetYaxis()->SetNdivisions(10);
    }
  }

  void preDrawTProfile2D( TCanvas *, const VisDQMObject &o, VisDQMRenderInfo &r )
  {
    TProfile2D *obj = dynamic_cast<TProfile2D *>( o.object );
    assert( obj );

    std::string name = o.name.substr(o.name.rfind("/")+1);

    if( name.find("EcalLaser") != std::string::npos ){
      if( name.find("transparency") != std::string::npos ){
	obj->GetZaxis()->SetTickLength(0);
	obj->GetZaxis()->SetLabelSize(0);

	gPad->SetLogz(kTRUE);

	obj->SetMinimum(1./1.5);
	obj->SetMaximum(1.5);

	if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
      }
    }
  }

  void preDrawTProfile( TCanvas *, const VisDQMObject &o, VisDQMRenderInfo & )
  {
    TProfile *obj = dynamic_cast<TProfile *>( o.object );
    assert( obj );

    std::string name = o.name.substr(o.name.rfind("/")+1);

    if( name.find("EcalLaser") != std::string::npos ){

      if( name.find("L1 (blue) amplitude trend") != std::string::npos ){
	obj->SetMinimum(0.);
	obj->SetMaximum(1000.);
      }else if( name.find("L4 (red) amplitude trend") != std::string::npos ){
	obj->SetMinimum(0.);
	obj->SetMaximum(2000.);
      }else if( name.find("amplitude RMS trend") != std::string::npos ){
	obj->SetMinimum(0.);
	obj->SetMaximum(20.);
      }else if( name.find("jitter trend") != std::string::npos ){
	obj->SetMinimum(0.);
	obj->SetMaximum(20.);
      }else if( name.find("FWHM trend") != std::string::npos ){
	obj->SetMinimum(20.);
	obj->SetMaximum(100.);
      }else if( name.find("timing trend") != std::string::npos ){
	obj->SetMinimum(1370.);
	obj->SetMaximum(1560.);
      }else if( name.find("prepulse amplitude trend") != std::string::npos ){
	obj->SetMinimum(-0.5);
	obj->SetMaximum(2.);
      }else if( name.find("prepulse width trend") != std::string::npos ){
	obj->SetMinimum(0.);
	obj->SetMaximum(200.);
      }else if( name.find("error on") != std::string::npos ){
	gPad->SetLogy(kTRUE);
      }else if( name.find("approximate trigger rate") != std::string::npos ){
	gPad->SetLogy(kTRUE);
      }else if( name.find("number of") != std::string::npos ){
	obj->SetMinimum(0.);
	obj->SetMaximum(2500.);
      }else if( name.find("duration") != std::string::npos ){
	obj->SetMinimum(0.);
	obj->SetMaximum(16.);
      }else if( name.find("transparency") != std::string::npos ){
	obj->GetXaxis()->SetTimeDisplay(1);
	obj->GetXaxis()->SetTimeFormat("%d/%m");
	obj->GetXaxis()->SetNdivisions(2405, kTRUE);

	obj->GetXaxis()->SetRange(2, obj->GetNbinsX());

	if( name.find("max-min") == std::string::npos ){
	  double mean = obj->GetMean(2);
	  obj->SetMinimum( mean / 1.05 );
	  obj->SetMaximum( mean * 1.05 );

	  obj->GetYaxis()->SetTickLength(0);
	  obj->GetYaxis()->SetLabelSize(0);

	  gPad->SetLogy(kTRUE);
	}
      }

      return;
    }
  }

  void preDrawTH3F( TCanvas *, const VisDQMObject &, VisDQMRenderInfo & )
  {
  }

  void preDrawTH2FD( TCanvas *, const VisDQMObject &o, VisDQMRenderInfo &r )
  {
    TH2 *obj = dynamic_cast<TH2 *>( o.object );
    assert( obj );

    std::string name = o.name.substr(o.name.rfind("/")+1);

    gStyle->SetPaintTextFormat();

    gStyle->SetOptStat(kFALSE);
    obj->SetStats(kFALSE);
    gPad->SetLogy(kFALSE);

    if( name.find( "EcalLaser" ) != std::string::npos ){

      if( name.find("sequence validation") != std::string::npos ){
	obj->SetMinimum(0.);
	obj->SetMaximum(3.);

	gStyle->SetPalette(3,pStatus);

	if( r.drawOptions.size() == 0 ) r.drawOptions = "col";
      }

      return;
    }
  }

  void preDrawTH1( TCanvas *, const VisDQMObject &o, VisDQMRenderInfo &r )
  {
    TH1* obj = dynamic_cast<TH1*>( o.object );
    assert( obj );

    std::string name = o.name.substr(o.name.rfind("/")+1);

    if( name.find( "EcalLaser" ) != std::string::npos ){

      if( name.find( "duration max" ) != std::string::npos || name.find( "duration min" ) != std::string::npos ){
	obj->SetMarkerStyle(20);
	obj->SetMarkerSize(1);

	if( r.drawOptions.size() == 0 ) r.drawOptions = "P";
      }
    }
  }

  void postDrawTH2( TCanvas *c, const VisDQMObject &o )
  {
    TH2 *obj = dynamic_cast<TH2 *>( o.object );
    assert( obj );

    std::string name = o.name.substr(o.name.rfind("/")+1);

    int nbx = obj->GetNbinsX();
    int nby = obj->GetNbinsY();

    c->SetBit(TGraph::kClipFrame);
    TLine l;
    l.SetLineWidth(1);

    if( ( nbx == 85 && nby == 20 ) && name.find( "EB" ) != std::string::npos ){

      int x1 = ebLabelsSMCrystal->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
      int x2 = ebLabelsSMCrystal->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
      int y1 = ebLabelsSMCrystal->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
      int y2 = ebLabelsSMCrystal->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
      ebLabelsSMCrystal->GetXaxis()->SetRange(x1, x2);
      ebLabelsSMCrystal->GetYaxis()->SetRange(y1, y2);
      ebLabelsSMCrystal->Draw("text,same");

    }else if( ( nbx == 50 && nby == 50 ) && name.find( "EE" ) != std::string::npos ){

      for(int i=0; i<201; i=i+1){
	if( (ixSectorsEE[i]!=0 || iySectorsEE[i]!=0) && (ixSectorsEE[i+1]!=0 || iySectorsEE[i+1]!=0) )
	  l.DrawLine(ixSectorsEE[i], iySectorsEE[i], ixSectorsEE[i+1], iySectorsEE[i+1]);
      }

      int x1 = eeLabelsSMCrystal->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
      int x2 = eeLabelsSMCrystal->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
      int y1 = eeLabelsSMCrystal->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
      int y2 = eeLabelsSMCrystal->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
      eeLabelsSMCrystal->GetXaxis()->SetRange(x1, x2);
      eeLabelsSMCrystal->GetYaxis()->SetRange(y1, y2);
      eeLabelsSMCrystal->Draw("text,same");

    }

  }

  void postDrawTProfile2D( TCanvas *, const VisDQMObject &o )
  {
    TProfile2D *obj = dynamic_cast<TProfile2D *>( o.object );
    assert( obj );

    std::string name = o.name.substr(o.name.rfind("/")+1);

    if( name.find("EcalLaser") != std::string::npos ){

      if( name.find("transparency") != std::string::npos ){
	logFunc->SetRange( obj->GetMinimum(), obj->GetMaximum() );

	// FIXME cleverer way than just hardcoding? TPaletteAxis is somehow unreachable..
	float xmin = obj->GetXaxis()->GetXmin();
	float xmax = obj->GetXaxis()->GetXmax();
	float x = xmin + (xmax - xmin) * 1.0625;
	logAxis->SetFunction("logVernier");
	logAxis->SetOption("+L");
	logAxis->SetLabelOffset(0.01);
	logAxis->SetX1( x );
	logAxis->SetX2( x );
	logAxis->SetY1( obj->GetYaxis()->GetXmin() );
	logAxis->SetY2( obj->GetYaxis()->GetXmax() );
	logAxis->Draw();
      }
    }
  }

  void postDrawTH3F( TCanvas *, const VisDQMObject & )
  {
  }

  void postDrawTProfile( TCanvas *, const VisDQMObject &o )
  {
    TProfile *obj = dynamic_cast<TProfile *>( o.object );
    assert( obj );

    std::string name = o.name.substr(o.name.rfind("/")+1);

    TLine l1, l2, l3;
    l1.SetLineWidth(2), l2.SetLineWidth(2), l3.SetLineWidth(2);

    if( name.find("EcalLaser") != std::string::npos ){

      float xmin = obj->GetXaxis()->GetXmin();
      float xmax = obj->GetXaxis()->GetXmax();

      l1.SetLineStyle(1), l2.SetLineStyle(1), l3.SetLineStyle(1);
      l1.SetLineColor(kRed), l2.SetLineColor(kOrange), l3.SetLineColor(kGreen);

      if( name.find("L1 (blue) amplitude trend") != std::string::npos ){
	l1.DrawLine(xmin,100,xmax,100);
	l2.DrawLine(xmin,200,xmax,200);
      }else if( name.find("L4 (red) amplitude trend") != std::string::npos ){
	l1.DrawLine(xmin,200,xmax,200);
	l2.DrawLine(xmin,400,xmax,400);
      }else if( name.find("amplitude RMS trend") != std::string::npos ){
	l1.DrawLine(xmin,15,xmax,15);
	l2.DrawLine(xmin,5,xmax,5);
      }else if( name.find("jitter trend") != std::string::npos ){
	l1.DrawLine(xmin,15,xmax,15);
	l2.DrawLine(xmin,10,xmax,10);
      }else if( name.find("FWHM trend") != std::string::npos ){
	l1.DrawLine(xmin,75,xmax,75);
	l2.DrawLine(xmin,50,xmax,50);
      }else if( name.find("timing trend") != std::string::npos ){
	l1.DrawLine(xmin,1515,xmax,1515);
	l1.DrawLine(xmin,1415,xmax,1415);
	l2.DrawLine(xmin,1490,xmax,1490);
	l2.DrawLine(xmin,1440,xmax,1440);
	l3.DrawLine(xmin,1465,xmax,1465);
      }else if( name.find("transparency history") != std::string::npos ){
	logFunc->SetRange( obj->GetMinimum(), obj->GetMaximum() );

	logAxis->SetFunction("logVernier");
	logAxis->SetOption("-");
	logAxis->SetLabelOffset(0.01);
	logAxis->SetX1( obj->GetBinLowEdge(2) );
	logAxis->SetX2( obj->GetBinLowEdge(2) );
	logAxis->SetY1( obj->GetMinimum() );
	logAxis->SetY2( obj->GetMaximum() );
	logAxis->Draw();
      }

      return;
    }
  }

  void postDrawTH2FD( TCanvas *, const VisDQMObject & )
  {
  }

  void postDrawTH1( TCanvas *, const VisDQMObject & )
  {
  }

};

const int EcalCalibRenderPlugin::ixSectorsEE[202] = {
  61, 61, 60, 60, 59, 59, 58, 58, 57, 57, 55, 55, 45, 45, 43, 43, 42, 42,
  41, 41, 40, 40, 39, 39, 40, 40, 41, 41, 42, 42, 43, 43, 45, 45, 55, 55,
  57, 57, 58, 58, 59, 59, 60, 60, 61, 61, 0, 100,100, 97, 97, 95, 95, 92,
  92, 87, 87, 85, 85, 80, 80, 75, 75, 65, 65, 60, 60, 40, 40, 35, 35, 25,
  25, 20, 20, 15, 15, 13, 13,  8,  8,  5,  5,  3,  3,  0,  0,  3,  3,  5,
  5,  8,  8, 13, 13, 15, 15, 20, 20, 25, 25, 35, 35, 40, 40, 60, 60, 65,
  65, 75, 75, 80, 80, 85, 85, 87, 87, 92, 92, 95, 95, 97, 97,100,100,  0,
  61, 65, 65, 70, 70, 80, 80, 90, 90, 92,  0, 61, 65, 65, 90, 90, 97,  0,
  57, 60, 60, 65, 65, 70, 70, 75, 75, 80, 80,  0, 50, 50,  0, 43, 40, 40,
  35, 35, 30, 30, 25, 25, 20, 20,  0, 39, 35, 35, 10, 10,  3,  0, 39, 35,
  35, 30, 30, 20, 20, 10, 10,  8,  0, 45, 45, 40, 40, 35, 35,  0, 55, 55,
  60, 60, 65, 65
};

const int EcalCalibRenderPlugin::iySectorsEE[202] = {
  50, 55, 55, 57, 57, 58, 58, 59, 59, 60, 60, 61, 61, 60, 60, 59, 59, 58,
  58, 57, 57, 55, 55, 45, 45, 43, 43, 42, 42, 41, 41, 40, 40, 39, 39, 40,
  40, 41, 41, 42, 42, 43, 43, 45, 45, 50,  0, 50, 60, 60, 65, 65, 75, 75,
  80, 80, 85, 85, 87, 87, 92, 92, 95, 95, 97, 97,100,100, 97, 97, 95, 95,
  92, 92, 87, 87, 85, 85, 80, 80, 75, 75, 65, 65, 60, 60, 40, 40, 35, 35,
  25, 25, 20, 20, 15, 15, 13, 13,  8,  8,  5,  5,  3,  3,  0,  0,  3,  3,
  5,  5,  8,  8, 13, 13, 15, 15, 20, 20, 25, 25, 35, 35, 40, 40, 50,  0,
  45, 45, 40, 40, 35, 35, 30, 30, 25, 25,  0, 50, 50, 55, 55, 60, 60,  0,
  60, 60, 65, 65, 70, 70, 75, 75, 85, 85, 87,  0, 61,100,  0, 60, 60, 65,
  65, 70, 70, 75, 75, 85, 85, 87,  0, 50, 50, 55, 55, 60, 60,  0, 45, 45,
  40, 40, 35, 35, 30, 30, 25, 25,  0, 39, 30, 30, 15, 15,  5,  0, 39, 30,
  30, 15, 15,  5
};

const int EcalCalibRenderPlugin::inTowersEE[400] = {
  0,  0,  0,  0,  0,  0,  0, 27, 37, 41, 17, 13,  3,  0,  0,  0,  0,  0,
  0,  0,  0,  0,  0,  0, 21, 31, 29, 26, 36, 40, 16, 12,  2, 29, 31, 21,
  0,  0,  0,  0,  0,  0,  0, 21, 27, 30, 28, 25, 35, 39, 15, 11,  1, 28,
  30, 27, 21,  0,  0,  0,  0,  0, 14, 26, 25, 24, 23, 22, 34, 38, 14, 10,
  22, 23, 24, 25, 26, 14,  0,  0,  0, 14, 20, 19, 18, 17, 16, 15, 29, 33,
  9,  5, 15, 16, 17, 18, 19, 20, 14,  0,  0, 33, 13, 12, 11, 10,  9,  8,
  28, 32,  8,  4,  8,  9, 10, 11, 12, 13, 33,  0,  0, 30, 32, 31,  7,  6,
  5,  4, 33, 31,  7, 33,  4,  5,  6,  7, 31, 32, 30,  0, 34, 29, 28, 27,
  26, 25,  3,  2, 32, 30,  6, 32,  2,  3, 25, 26, 27, 28, 29, 34, 24, 23,
  22, 21, 20, 19, 18,  1, 21, 14, 21, 14,  1, 18, 19, 20, 21, 22, 23, 24,
  17, 16, 15, 14, 13, 12, 11, 10,  0,  0,  0,  0, 10, 11, 12, 13, 14, 15,
  16, 17,  9,  8,  7,  6,  5,  4,  3, 32,  0,  0,  0,  0, 32,  3,  4,  5,
  6,  7,  8,  9,  2,  1, 31, 30, 29, 28, 27, 26, 25,  3, 25,  3, 26, 27,
  28, 29, 30, 31,  1,  2, 25, 24, 23, 22, 21, 20, 19, 18, 16, 12, 12, 16,
  18, 19, 20, 21, 22, 23, 24, 25,  0, 17, 16, 15, 14, 13, 12, 33, 15, 11,
  11, 15, 33, 12, 13, 14, 15, 16, 17,  0,  0, 11, 10,  9,  8,  7, 32, 31,
  14, 10, 10, 14, 31, 32,  7,  8,  9, 10, 11,  0,  0, 25,  6,  5,  4, 29,
  28, 27, 13,  9,  9, 13, 27, 28, 29,  4,  5,  6, 25,  0,  0,  0,  3,  2,
  1, 26, 25, 24,  8,  4,  4,  8, 24, 25, 26,  1,  2,  3,  0,  0,  0,  0,
  0,  3, 23, 22, 21, 20,  7,  3,  3,  7, 20, 21, 22, 23,  3,  0,  0,  0,
  0,  0,  0,  0, 30, 19, 18, 17,  6,  2,  2,  6, 17, 18, 19, 30,  0,  0,
  0,  0,  0,  0,  0,  0,  0,  0,  0, 30,  5,  1,  1,  5, 30,  0,  0,  0,
  0,  0,  0,  0 };

static EcalCalibRenderPlugin instance;
