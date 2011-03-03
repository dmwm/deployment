// $Id: EERenderPlugin.cc,v 1.165 2010/10/04 11:04:03 dellaric Exp $

/*!
  \file EERenderPlugin
  \brief Display Plugin for Quality Histograms
  \author G. Della Ricca
  \author B. Gobbo
  \version $Revision: 1.165 $
  \date $Date: 2010/10/04 11:04:03 $
*/

#include "DQM/DQMRenderPlugin.h"
#include "utils.h"

#include "TH1F.h"
#include "TH1D.h"
#include "TH2F.h"
#include "TH2D.h"
#include "TH3F.h"
#include "TProfile.h"
#include "TProfile2D.h"
#include "TStyle.h"
#include "TCanvas.h"
#include "TGaxis.h"
#include "TColor.h"
#include "TROOT.h"
#include "TGraph.h"
#include "TLine.h"
#include "TPaletteAxis.h"
#include <iostream>
#include <math.h>
#include <cassert>

class EERenderPlugin : public DQMRenderPlugin
{
  static const int ixSectorsEE[202];
  static const int iySectorsEE[202];
  static const int inTowersEE[400];
  static const int ixTTEEHorizontal1[1381];
  static const int ixTTEEHorizontal2[1386];
  static const int iyTTEEHorizontal1[1381];
  static const int iyTTEEHorizontal2[1386];
  static const int ixTTEEVertical1[1381];
  static const int ixTTEEVertical2[1385];
  static const int iyTTEEVertical1[1381];
  static const int iyTTEEVertical2[1385];
  static const int ixTCCEEHorizontal[699];
  static const int iyTCCEEHorizontal[699];
  static const int ixTCCEEVertical[729];
  static const int iyTCCEEVertical[729];

  static const int ixLabels[720];
  static const int iyLabels[720];
  static const int bincontentLabels[720];

  TH2S* text1;
  TH2C* text3;
  TH2C* text4;
  TH2C* text6;
  TH2C* text7;
  TH2C* text8;
  TH2C* text9;
  TH2C* text10;
  TH2C* text11;
  TH2C* text12;
  TH2C* text13;
  TH2C* text14;
  TH2C* text15;
  TH2C* text16;

  int pCol3[7];
  int pCol4[10];
  int pCol5[10];
  int pCol6[7];

  TGaxis* timingAxis;

public:
  virtual void initialise( int, char ** )
    {
      float rgb[7][3]   = {{ 1.00,   0.00,   0.00},   { 0.00,   1.00,   0.00},
                           { 1.00,   0.96,   0.00},   { 0.50,   0.00,   0.00},
                           { 0.00,   0.40,   0.00},   { 0.94,   0.78,   0.00},
                           { 1.00,   1.00,   1.00}};

      float rgb2[10][3] = {{ 0.0000, 0.6510, 1.0000}, { 0.0000, 0.6135, 0.9455},
                           { 0.0000, 0.5760, 0.8911}, { 0.0000, 0.5386, 0.8366},
                           { 0.0000, 0.5011, 0.7821}, { 0.0000, 0.4636, 0.7277},
                           { 0.0000, 0.4261, 0.6732}, { 0.0000, 0.3887, 0.6187},
                           { 0.0000, 0.3512, 0.5643}, { 0.0000, 0.3137, 0.5098}};


      for(int i=0; i<6; i++)
      {
        TColor* color = gROOT->GetColor( 301+i );
        if( ! color ) color = new TColor( 301+i, 0, 0, 0, "");
        color->SetRGB( rgb[i][0], rgb[i][1], rgb[i][2] );
      }

      for(int i=0; i<10; i++)
      {
        TColor* color = gROOT->GetColor( 401+i );
        if( ! color ) color = new TColor( 401+i, 0, 0, 0, "");
        color->SetRGB( rgb2[i][0], rgb2[i][1], rgb2[i][2] );
      }

      for(int i=0; i<10; i++)
      {
        TColor* color = gROOT->GetColor( 501+i );
        if( ! color ) color = new TColor( 501+i, 0, 0, 0, "");
        color->SetRGB( rgb2[i][1], 0, 0 );
      }

      for(int i=0; i<7; i++) pCol3[i]  = i+301;
      for(int i=0; i<10; i++) pCol4[i] = i+401;
      for(int i=0; i<10; i++) pCol5[i] = i+501;

      pCol6[0] = kGray+2;
      pCol6[1] = kWhite;
      pCol6[2] = kRed;
      pCol6[3] = kOrange;
      pCol6[4] = kGreen;
      pCol6[5] = kAzure;
      pCol6[6] = kViolet;

      timingAxis = 0;

      text1 = new TH2S( "ee_text1", "text1", 100, -2., 98., 100, -2., 98.);
      text3 = new TH2C( "ee_text3", "text3", 10, 0,  10,  5,   0,  5 );
      text4 = new TH2C( "ee_text4", "text4",  2, 0,   2,  1,   0,  1 );
      text6 = new TH2C( "ee_text6", "text6", 10, 0., 100., 10, 0., 100. );
      text7 = new TH2C( "ee_text7", "text7", 10, 0., 100., 10, 0., 100. );
      text8 = new TH2C( "ee_text8", "text8", 10, -150., 150., 10, -150., 150. );
      text9 = new TH2C( "ee_text9", "text9", 10, -150., 150., 10, -150., 150. );
      text10 = new TH2C( "ee_text10", "text10", 20, 0., 40., 10, 0., 20. );
      text11 = new TH2C( "ee_text11", "text11", 20, 0., 200., 10, 0., 100. );
      text12 = new TH2C( "ee_text12", "text12", 10, 0., 20., 10, 0., 20. );
      text13 = new TH2C( "ee_text13", "text13", 10, 0., 20., 10, 0., 20. );
      text14 = new TH2C( "ee_text14", "text14", 100, 0., 100., 100, 0., 100.);
      text15 = new TH2C( "ee_text15", "text15", 100, 0., 100., 100, 0., 100.);
      text16 = new TH2C( "eb_text16", "text16", 9, 0., 45., 2, -10., 10. );

      text1->SetMinimum(  0.01 );
      text3->SetMinimum(  0.01 );
      text4->SetMinimum(  0.01 );
      text6->SetMinimum( -9.01 );
      text7->SetMinimum( +0.01 );
      text8->SetMinimum( -9.01 );
      text9->SetMinimum( +0.01 );
      text10->SetMinimum( -9.01 );
      text11->SetMinimum( -9.01 );
      text12->SetMinimum( -9.01 );
      text13->SetMinimum( +0.01 );
      text16->SetMinimum( -9.01 );

      text6->SetMaximum( -0.01 );
      text7->SetMaximum( +9.01 );
      text8->SetMaximum( -0.01 );
      text9->SetMaximum( +9.01 );
      text10->SetMaximum( -0.01 );
      text11->SetMaximum( -0.01 );
      text12->SetMaximum( -0.01 );
      text13->SetMaximum( +9.01 );
      text16->SetMaximum( +9.01 );

      for(int j=0; j<400; j++)
      {
        int x = 5*(1 + j%20);
        int y = 5*(1 + j/20);
        text1->SetBinContent(x, y, inTowersEE[j]);
      }

      for(int i=1; i<=10; i++)
      {
        for(int j=1; j<=10; j++)
        {
          text6->SetBinContent(i, j, -10);
          text7->SetBinContent(i, j, -10);
          text8->SetBinContent(i, j, -10);
          text9->SetBinContent(i, j, -10);
          text12->SetBinContent(i, j, -10);
          text13->SetBinContent(i, j, -10);
        }
      }

      for(int i=0; i<2; i++)
      {
        text3->Fill( 2+i*5, 2, i+1+68 );
        text4->Fill( i, 0., i+1+68 );
      }

      text6->SetBinContent(2, 5, -3);
      text6->SetBinContent(2, 7, -2);
      text6->SetBinContent(4, 9, -1);
      text6->SetBinContent(7, 9, -9);
      text6->SetBinContent(9, 7, -8);
      text6->SetBinContent(9, 5, -7);
      text6->SetBinContent(8, 3, -6);
      text6->SetBinContent(6, 2, -5);
      text6->SetBinContent(3, 3, -4);

      text7->SetBinContent(2, 5, +3);
      text7->SetBinContent(2, 7, +2);
      text7->SetBinContent(4, 9, +1);
      text7->SetBinContent(7, 9, +9);
      text7->SetBinContent(9, 7, +8);
      text7->SetBinContent(9, 5, +7);
      text7->SetBinContent(8, 3, +6);
      text7->SetBinContent(5, 2, +5);
      text7->SetBinContent(3, 3, +4);

      text8->SetBinContent(2, 5, -3);
      text8->SetBinContent(2, 7, -2);
      text8->SetBinContent(4, 9, -1);
      text8->SetBinContent(7, 9, -9);
      text8->SetBinContent(9, 7, -8);
      text8->SetBinContent(9, 5, -7);
      text8->SetBinContent(8, 3, -6);
      text8->SetBinContent(6, 2, -5);
      text8->SetBinContent(3, 3, -4);

      text9->SetBinContent(2, 5, +3);
      text9->SetBinContent(2, 7, +2);
      text9->SetBinContent(4, 9, +1);
      text9->SetBinContent(7, 9, +9);
      text9->SetBinContent(9, 7, +8);
      text9->SetBinContent(9, 5, +7);
      text9->SetBinContent(8, 3, +6);
      text9->SetBinContent(5, 2, +5);
      text9->SetBinContent(3, 3, +4);

      text10->SetBinContent(2, 5, -3);
      text10->SetBinContent(2, 7, -2);
      text10->SetBinContent(4, 9, -1);
      text10->SetBinContent(7, 9, -9);
      text10->SetBinContent(9, 7, -8);
      text10->SetBinContent(9, 5, -7);
      text10->SetBinContent(8, 3, -6);
      text10->SetBinContent(6, 2, -5);
      text10->SetBinContent(3, 3, -4);

      text10->SetBinContent(10+2, 5, +3);
      text10->SetBinContent(10+2, 7, +2);
      text10->SetBinContent(10+4, 9, +1);
      text10->SetBinContent(10+7, 9, +9);
      text10->SetBinContent(10+9, 7, +8);
      text10->SetBinContent(10+9, 5, +7);
      text10->SetBinContent(10+8, 3, +6);
      text10->SetBinContent(10+5, 2, +5);
      text10->SetBinContent(10+3, 3, +4);

      text11->SetBinContent(2, 5, -3);
      text11->SetBinContent(2, 7, -2);
      text11->SetBinContent(4, 9, -1);
      text11->SetBinContent(7, 9, -9);
      text11->SetBinContent(9, 7, -8);
      text11->SetBinContent(9, 5, -7);
      text11->SetBinContent(8, 3, -6);
      text11->SetBinContent(6, 2, -5);
      text11->SetBinContent(3, 3, -4);

      text11->SetBinContent(10+2, 5, +3);
      text11->SetBinContent(10+2, 7, +2);
      text11->SetBinContent(10+4, 9, +1);
      text11->SetBinContent(10+7, 9, +9);
      text11->SetBinContent(10+9, 7, +8);
      text11->SetBinContent(10+9, 5, +7);
      text11->SetBinContent(10+8, 3, +6);
      text11->SetBinContent(10+5, 2, +5);
      text11->SetBinContent(10+3, 3, +4);

      text12->SetBinContent(2, 5, -3);
      text12->SetBinContent(2, 7, -2);
      text12->SetBinContent(4, 9, -1);
      text12->SetBinContent(7, 9, -9);
      text12->SetBinContent(9, 7, -8);
      text12->SetBinContent(9, 5, -7);
      text12->SetBinContent(8, 3, -6);
      text12->SetBinContent(6, 2, -5);
      text12->SetBinContent(3, 3, -4);

      text13->SetBinContent(2, 5, +3);
      text13->SetBinContent(2, 7, +2);
      text13->SetBinContent(4, 9, +1);
      text13->SetBinContent(7, 9, +9);
      text13->SetBinContent(9, 7, +8);
      text13->SetBinContent(9, 5, +7);
      text13->SetBinContent(8, 3, +6);
      text13->SetBinContent(5, 2, +5);
      text13->SetBinContent(3, 3, +4);

      for(int i=0; i < 720; i++) {
        text14->SetBinContent(ixLabels[i],iyLabels[i],bincontentLabels[i]);
        text15->SetBinContent(100-ixLabels[i]+1,iyLabels[i],bincontentLabels[i]);
      }

      for(int i=1; i<=9; i++) {
        text16->SetBinContent(i, 1, -1*i);
        text16->SetBinContent(i, 2, i);
      }

      text1->SetMarkerSize( 2 );
      text3->SetMarkerSize( 2 );
      text4->SetMarkerSize( 2 );
      text6->SetMarkerSize( 2 );
      text7->SetMarkerSize( 2 );
      text8->SetMarkerSize( 2 );
      text9->SetMarkerSize( 2 );
      text10->SetMarkerSize( 2 );
      text11->SetMarkerSize( 2 );
      text12->SetMarkerSize( 2 );
      text13->SetMarkerSize( 2 );
      text14->SetMarkerSize(0.9);
      text15->SetMarkerSize(0.9);
      text16->SetMarkerSize( 2 );

    }

  virtual bool applies( const VisDQMObject &o, const VisDQMImgInfo & )
    {
      if( o.name.find( "EcalEndcap/EE" ) != std::string::npos )
        return true;

      if( o.name.find( "EcalEndcap/EcalInfo" ) != std::string::npos )
        return true;

      if( o.name.find( "EcalEndcap/EventInfo" ) != std::string::npos )
        return true;

      if( o.name.find( "EcalEndcap/Run summary/EE" ) != std::string::npos )
        return true;

      if( o.name.find( "EcalEndcap/Run summary/EcalInfo" ) != std::string::npos )
        return true;

      if( o.name.find( "EcalEndcap/Run summary/EventInfo" ) != std::string::npos )
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

      TGaxis::SetMaxDigits(4);

      gStyle->SetOptTitle(kTRUE);
      gStyle->SetTitleBorderSize(0);

      gStyle->SetOptStat(kFALSE);
      gStyle->SetStatBorderSize(1);

      gStyle->SetOptFit(kFALSE);

      gROOT->ForceStyle();

      if( dynamic_cast<TProfile2D*>( o.object ) )
      {
        preDrawTProfile2D( c, o, r );
      }
      else if( dynamic_cast<TProfile*>( o.object ) )
      {
        preDrawTProfile( c, o, r );
      }
      else if( dynamic_cast<TH3F*>( o.object ) )
      {
        preDrawTH3F( c, o, r );
      }
      else if( dynamic_cast<TH2F*>( o.object ) || dynamic_cast<TH2D*>( o.object ) )
      {
        preDrawTH2( c, o, r );
      }
      else if( dynamic_cast<TH1F*>( o.object ) || dynamic_cast<TH1D*>( o.object ) )
      {
        preDrawTH1( c, o, r );
      }
    }

  virtual void postDraw( TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo & )
    {
      c->cd();

      if( dynamic_cast<TProfile2D*>( o.object ) )
      {
        postDrawTProfile2D( c, o );
      }
      else if( dynamic_cast<TH3F*>( o.object ) )
      {
        postDrawTH3F( c, o );
      }
      else if( dynamic_cast<TH2F*>( o.object ) || dynamic_cast<TH2D*>( o.object ) )
      {
        postDrawTH2( c, o );
      }
      else if( dynamic_cast<TH1F*>( o.object ) || dynamic_cast<TH1D*>( o.object ) )
      {
        postDrawTH1( c, o );
      }
    }

private:
  void preDrawTProfile2D( TCanvas *c, const VisDQMObject &o, VisDQMRenderInfo &r )
    {
      TProfile2D* obj = dynamic_cast<TProfile2D*>( o.object );
      assert( obj );

      std::string name = o.name.substr(o.name.rfind("/")+1);

      int nbx = obj->GetNbinsX();
      int nby = obj->GetNbinsY();

      gStyle->SetPaintTextFormat();

      gStyle->SetOptStat(kFALSE);
      obj->SetStats(kFALSE);
      gPad->SetLogy(kFALSE);

      if( name.find( "EELT shape" ) != std::string::npos )
      {
        c->SetTheta(+30.);
        c->SetPhi(-60.);
        obj->GetXaxis()->SetTitleOffset(2.5);
        obj->GetYaxis()->SetTitleOffset(3.0);
        obj->GetZaxis()->SetTitleOffset(1.3);
        if( r.drawOptions.size() == 0 ) r.drawOptions = "lego";
        return;
      }

      if( name.find( "EELDT shape" ) != std::string::npos )
      {
        c->SetTheta(+30.);
        c->SetPhi(-60.);
        obj->GetXaxis()->SetTitleOffset(2.5);
        obj->GetYaxis()->SetTitleOffset(3.0);
        obj->GetZaxis()->SetTitleOffset(1.3);
        if( r.drawOptions.size() == 0 ) r.drawOptions = "lego";
        return;
      }

      if( name.find( "EETPT shape" ) != std::string::npos )
      {
        c->SetTheta(+30.);
        c->SetPhi(-60.);
        obj->GetXaxis()->SetTitleOffset(2.5);
        obj->GetYaxis()->SetTitleOffset(3.0);
        obj->GetZaxis()->SetTitleOffset(1.3);
        if( r.drawOptions.size() == 0 ) r.drawOptions = "lego";
        return;
      }

      if( name.find( "EECLT" ) != std::string::npos )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(10, kFALSE);
        obj->GetYaxis()->SetNdivisions(10, kFALSE);
        obj->SetMinimum(0.0);
        gStyle->SetPalette(10, pCol4);
        gPad->SetRightMargin(0.15);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( name.find( "EETMT" ) != std::string::npos )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(10, kFALSE);
        obj->GetYaxis()->SetNdivisions(10, kFALSE);
        obj->SetMinimum(25.);
        obj->SetMaximum(75.);

        gStyle->SetPalette(1);
        obj->SetContour(255);

        gPad->SetRightMargin(0.15);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( nbx == 50 && nby == 50 )
      {
        obj->GetXaxis()->SetNdivisions(10);
        obj->GetYaxis()->SetNdivisions(10);
        if(name.find( "EETTT" ) == std::string::npos ) {
          gStyle->SetPalette(1);
          gPad->SetGridx();
          gPad->SetGridy();
        }
      }

      if( nbx == 100 && nby == 100 )
      {
        if(name.find( "EETTT" ) == std::string::npos )
        {
          gPad->SetGridx();
          gPad->SetGridy();
          gStyle->SetPalette(1);
        }
        obj->GetXaxis()->SetNdivisions(10);
        obj->GetYaxis()->SetNdivisions(10);
      }

      if( nbx == 20 && nby == 20 &&
          name.find( "EESRT" ) != std::string::npos )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(10);
        obj->GetYaxis()->SetNdivisions(10);
      }

      obj->SetMinimum(0.0);
      gStyle->SetPalette(1);
      gPad->SetRightMargin(0.15);
      if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
    }

  void preDrawTProfile( TCanvas *, const VisDQMObject &o, VisDQMRenderInfo & )
    {
      TProfile* obj = dynamic_cast<TProfile*>( o.object );
      assert( obj );

      std::string name = o.name.substr(o.name.rfind("/")+1);

      gStyle->SetPaintTextFormat();

      gStyle->SetOptStat("e");
      obj->SetStats(kTRUE);
      gPad->SetLogy(kFALSE);
      obj->SetMinimum(0.0);

      if( name.find( "EEMM digi number profile" ) != std::string::npos ||
          name.find( "EELT laser L1" ) != std::string::npos ||
          ( name.find( "EETPT test pulse amplitude" ) != std::string::npos && name.find( "summary" ) != std::string::npos ) ||
          name.find( "EEPOT pedestal G12 mean" ) != std::string::npos || name.find( "EEPOT pedestal G12 rms" ) != std::string::npos )
      {
        gPad->SetBottomMargin(0.2);
        obj->GetXaxis()->LabelsOption("v");
      }

      if( name.find( "EEMM hit number profile" ) != std::string::npos )
      {
        gPad->SetBottomMargin(0.2);
        obj->GetXaxis()->LabelsOption("v");
      }

      if( name.find( "EEMM TP digi number profile" ) != std::string::npos )
      {
        gPad->SetBottomMargin(0.2);
        obj->GetXaxis()->LabelsOption("v");
      }

      if( name.find( "EESRT DCC event size" ) != std::string::npos )
      {
        gPad->SetBottomMargin(0.2);
        obj->GetXaxis()->LabelsOption("v");
      }

      if( name.find( "EETMT timing" ) != std::string::npos )
      {
        gPad->SetBottomMargin(0.2);
        obj->GetXaxis()->LabelsOption("v");
        obj->SetMinimum(-25.);
        obj->SetMaximum(25.);
      }
    }

  void preDrawTH3F( TCanvas *, const VisDQMObject &o, VisDQMRenderInfo & )
    {
      TH3F* obj = dynamic_cast<TH3F*>( o.object );
      assert( obj );

      std::string name = o.name.substr(o.name.rfind("/")+1);

      gStyle->SetPaintTextFormat();

      gStyle->SetOptStat(kFALSE);
      obj->SetStats(kFALSE);
      gPad->SetLogy(kFALSE);
    }

  void preDrawTH2( TCanvas *, const VisDQMObject &o, VisDQMRenderInfo &r )
    {
      TH2* obj = dynamic_cast<TH2*>( o.object );
      assert( obj );

      std::string name = o.name.substr(o.name.rfind("/")+1);

      int nbx = obj->GetNbinsX();
      int nby = obj->GetNbinsY();

      gStyle->SetPaintTextFormat();

      gStyle->SetOptStat(kFALSE);
      obj->SetStats(kFALSE);
      gPad->SetLogy(kFALSE);

      if( name.find( "EESRT" ) != std::string::npos )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        if( name.find( "EESRT event size vs DCC" ) != std::string::npos )
        {
          gPad->SetLogy(kTRUE);
          gPad->SetBottomMargin(0.2);
          obj->GetXaxis()->SetNdivisions(18, kFALSE);
          obj->GetYaxis()->SetNdivisions(2, kFALSE);
          obj->GetXaxis()->LabelsOption("v");
          obj->GetYaxis()->SetRangeUser(0.1, 0.608*132);
        }

        std::string zAxisTitle(obj->GetZaxis()->GetTitle());
        if( zAxisTitle.find("rate") != std::string::npos )
        {
          double xmin = obj->GetMinimum(0);
          double xmax = obj->GetMaximum();
          double eps = 1.e-9;
          if( xmax-xmin > eps ) obj->GetZaxis()->SetRangeUser(xmin, xmax);
        }

        gStyle->SetPalette(1);
        gPad->SetRightMargin(0.15);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( name.find( "TCC timing" ) != std::string::npos )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        gPad->SetBottomMargin(0.2);
        obj->GetXaxis()->SetNdivisions(36, kFALSE);
        obj->GetYaxis()->SetNdivisions(7, kFALSE);
        obj->GetXaxis()->LabelsOption("v");
        gStyle->SetPalette(1);
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if(name.find( "EECLT SC energy vs seed crystal energy" ) != std::string::npos )
      {
        gStyle->SetPalette(1);
        gPad->SetRightMargin(0.15);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( name.find( "EECLT" ) != std::string::npos )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(10, kFALSE);
        obj->GetYaxis()->SetNdivisions(10, kFALSE);
        obj->SetMinimum(0.0);
        gStyle->SetPalette(10, pCol4);
        gPad->SetRightMargin(0.15);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( name.find( "EETMT timing vs amplitude" ) != std::string::npos ||
          name.find( "EETMT timing EE+ vs EE-" ) != std::string::npos )
      {
        if( obj->GetMaximum() > 0. ) gPad->SetLogz(kTRUE);
        obj->SetMinimum(0.0);
        gStyle->SetPalette(1);
        gPad->SetRightMargin(0.15);
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( nbx == 50 && nby == 50 )
      {
        obj->GetXaxis()->SetNdivisions(10);
        obj->GetYaxis()->SetNdivisions(10);
      }

      if( nbx == 50 && nby == 50 && name.find( "EETTT" ) == std::string::npos )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(10);
        obj->GetYaxis()->SetNdivisions(10);
      }

      if( nbx == 20 && nby == 20 )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(20);
        obj->GetYaxis()->SetNdivisions(20);
      }

      if( nbx == 20 && nby == 20 &&
          name.find( "EESRT" ) != std::string::npos )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(10);
        obj->GetYaxis()->SetNdivisions(10);
      }

      if( nbx == 10 && ( nby == 1 || nby == 5 ) )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(10);
        obj->GetYaxis()->SetNdivisions(1);
      }

      if( nbx == 2 && nby == 1 )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(2);
        obj->GetYaxis()->SetNdivisions(1);
      }

      if( nbx == 100 && nby == 100 )
      {
        if(name.find( "EETTT" ) == std::string::npos )
        {
          gPad->SetGridx();
          gPad->SetGridy();
          gStyle->SetPalette(1);
        }
        obj->GetXaxis()->SetNdivisions(10);
        obj->GetYaxis()->SetNdivisions(10);
      }

      if( nbx == 45 && nby == 20 )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(9);
        obj->GetYaxis()->SetNdivisions(2);
      }

      if( nbx == 40 && nby == 20 )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(20);
        obj->GetYaxis()->SetNdivisions(10);
      }

      if( nbx == 200 && nby == 100 )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(20);
        obj->GetYaxis()->SetNdivisions(10);
      }

      if( name.find( "reportSummaryMap" ) != std::string::npos )
      {
        dqm::utils::reportSummaryMapPalette(obj);
        obj->SetTitle("EcalEndcap Report Summary Map");
        gStyle->SetPaintTextFormat("+g");
        return;
      }

      if( name.find( "DAQSummaryMap" ) != std::string::npos )
      {
        dqm::utils::reportSummaryMapPalette(obj);
        obj->SetTitle("EcalEndcap DAQ Summary Map");
        gStyle->SetPaintTextFormat("+g");
        return;
      }

      if( name.find( "DCSSummaryMap" ) != std::string::npos )
      {
        dqm::utils::reportSummaryMapPalette(obj);
        obj->SetTitle("EcalEndcap DCS Summary Map");
        gStyle->SetPaintTextFormat("+g");
        return;
      }

      if( name.find( "CertificationSummaryMap" ) != std::string::npos )
      {
        dqm::utils::reportSummaryMapPalette(obj);
        obj->SetTitle("EcalEndcap Data Certification Summary Map");
        gStyle->SetPaintTextFormat("+g");
        return;
      }

      if( name.find( "EEIT" ) != std::string::npos &&
          name.find( "quality" ) == std::string::npos )
      {
        obj->SetMinimum(0.0);
        gStyle->SetPalette(10, pCol5);
        gPad->SetRightMargin(0.15);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( name.find( "EETTT" ) != std::string::npos &&
          name.find( "quality" ) == std::string::npos )
      {
        if( name.find( "Trigger Primitives Timing" ) != std::string::npos )
        {
          obj->SetMinimum(-1.0);
          obj->SetMaximum(6.0);
        }
        else
        {
          obj->SetMinimum(0.0);
          gStyle->SetPalette(1);
        }

        if( name.find( "Error" ) == std::string::npos )
        {
          if( name.find( "Trigger Primitives Timing" ) != std::string::npos )
          {
            gStyle->SetPalette(7, pCol6);
            obj->SetContour(7);
          }
          else if( name.find( "Trigger Primitives Non Single Timing" ) != std::string::npos )
          {
            gStyle->SetPalette(10, pCol5);
          }
          else
          {
            gStyle->SetPalette(1);
          }
        }
        else
        {
          gStyle->SetPalette(1);
        }

        gPad->SetRightMargin(0.15);
        if( nbx == 50 && nby == 50 ) gStyle->SetPaintTextFormat("g");
        else gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( name.find( "G12 RMS map" ) != std::string::npos )
      {
        obj->SetMinimum(1.0);
        obj->SetMaximum(4.0);
        gStyle->SetPalette(1);
        gPad->SetRightMargin(0.15);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( name.find( "EEOT" ) != std::string::npos )
      {
        obj->SetMinimum(0.0);
        gStyle->SetPalette(10, pCol4);
        gPad->SetRightMargin(0.15);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( name.find( "EESFT" ) != std::string::npos &&
          name.find( "summary" ) == std::string::npos )
      {
        obj->SetMinimum(0.0);
        gStyle->SetPalette(10, pCol5);
        gPad->SetRightMargin(0.15);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( name.find( "EESRT" ) != std::string::npos )
      {
        obj->SetMinimum(0.0);
        gStyle->SetPalette(10, pCol4);
        gPad->SetRightMargin(0.15);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( name.find( "EECT" ) != std::string::npos )
      {
        obj->SetMinimum(0.0);
        gStyle->SetPalette(10, pCol4);
        gPad->SetRightMargin(0.15);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( name.find( "summary" ) != std::string::npos &&
          name.find( "Trigger Primitives Timing" ) == std::string::npos )
      {
        obj->SetMinimum(-0.00000001);
        obj->SetMaximum(7.0);
        gStyle->SetPalette(7, pCol3);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "col";
        return;
      }

      if( name.find( "quality" ) != std::string::npos )
      {
        obj->SetMinimum(-0.00000001);
        obj->SetMaximum(7.0);
        gStyle->SetPalette(7, pCol3);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "col";
        return;
      }

      if( name.find( "EEMM event" ) != std::string::npos )
      {
        obj->SetMinimum(0.0);
        gStyle->SetPalette(10, pCol4);
        gPad->SetRightMargin(0.15);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }
    }

  void preDrawTH1( TCanvas *, const VisDQMObject &o, VisDQMRenderInfo & )
    {
      TH1* obj = dynamic_cast<TH1*>( o.object );
      assert( obj );

      std::string name = o.name.substr(o.name.rfind("/")+1);

      int nbx = obj->GetNbinsX();

      gStyle->SetPaintTextFormat();

      gStyle->SetOptStat("euomr");
      obj->SetStats(kTRUE);
      gPad->SetLogy(kFALSE);

      if( obj->GetMaximum() > 0. ) gPad->SetLogy(kTRUE);

      if( name.find( "timing" ) != std::string::npos ||
          name.find( "rec hit thr" ) != std::string::npos ||
          name.find( "invariant mass" ) != std::string::npos ) gPad->SetLogy(kFALSE);

      if( nbx == 10 || nbx == 850 )
      {
        gPad->SetLogy(kFALSE);
        gStyle->SetOptStat("e");
        return;
      }

      if( name.find( "EVTTYPE" ) != std::string::npos )
      {
        gPad->SetBottomMargin(0.4);
        obj->GetXaxis()->LabelsOption("v");
      }

      if( name.find( "EEMM DCC" ) != std::string::npos )
      {
        gPad->SetBottomMargin(0.2);
        obj->GetXaxis()->LabelsOption("v");
      }

      if( name.find( "EEIT DCC" ) != std::string::npos )
      {
        gPad->SetBottomMargin(0.2);
        obj->GetXaxis()->LabelsOption("v");
      }

      if( name.find( "EEOT rec hit flags" ) != std::string::npos )
      {
        gPad->SetBottomMargin(0.4);
        obj->GetXaxis()->LabelsOption("v");
      }

      if( name.find( "front-end status bits" ) != std::string::npos )
      {
        gPad->SetBottomMargin(0.25);
        obj->GetXaxis()->LabelsOption("v");
        obj->GetXaxis()->SetBinLabel(1+8, "FORCED FS");
        obj->GetXaxis()->SetBinLabel(1+12, "FIFO FULL+L1A");
      }

      if( name.find( "EERDT" ) != std::string::npos )
      {
        gPad->SetBottomMargin(0.2);
        obj->GetXaxis()->LabelsOption("v");
      }

      if( name.find( "EERDT event type" ) != std::string::npos )
      {
        gPad->SetBottomMargin(0.4);
        obj->GetXaxis()->LabelsOption("v");
      }

      if( name.find( "front-end status errors summary" ) != std::string::npos )
      {
        gPad->SetBottomMargin(0.2);
        obj->GetXaxis()->LabelsOption("v");
      }

      if( name.find( "quality errors summary" ) != std::string::npos )
      {
        gPad->SetBottomMargin(0.2);
        obj->GetXaxis()->LabelsOption("v");
      }

      if( name.find( "EEOT digi occupancy summary 1D" ) != std::string::npos )
      {
        gPad->SetBottomMargin(0.2);
        obj->GetXaxis()->LabelsOption("v");
      }
    }

  void postDrawTProfile2D( TCanvas *c, const VisDQMObject &o )
    {
      TProfile2D* obj = dynamic_cast<TProfile2D*>( o.object );
      assert( obj );

      std::string name = o.name.substr(o.name.rfind("/")+1);

      if( name.find( "EELT shape" ) != std::string::npos )
      {
        return;
      }

      if( name.find( "EELDT shape" ) != std::string::npos )
      {
        return;
      }

      if( name.find( "EETPT shape" ) != std::string::npos )
      {
        return;
      }

      int nbx = obj->GetNbinsX();
      int nby = obj->GetNbinsY();

      c->SetBit(TGraph::kClipFrame);
      TLine l;
      l.SetLineWidth(1);
      for(int i=0; i<201; i=i+1)
      {
        if( (ixSectorsEE[i]!=0 || iySectorsEE[i]!=0) && (ixSectorsEE[i+1]!=0 || iySectorsEE[i+1]!=0) )
        {
          if( name.find( "EESRT" ) != std::string::npos && nbx == 20 && nby == 20 )
          {
            l.DrawLine(0.2*ixSectorsEE[i], 0.2*iySectorsEE[i], 0.2*ixSectorsEE[i+1], 0.2*iySectorsEE[i+1]);
          }
          else if( name.find( "EECLT" ) != std::string::npos &&
                   name.find( "seed" ) == std::string::npos )
          {
            l.DrawLine(3.0*(ixSectorsEE[i]-50), 3.0*(iySectorsEE[i]-50), 3.0*(ixSectorsEE[i+1]-50), 3.0*(iySectorsEE[i+1]-50));
          }
          else if( name.find( "EECLT SC energy vs seed crystal energy" ) == std::string::npos )
          {
            l.DrawLine(ixSectorsEE[i], iySectorsEE[i], ixSectorsEE[i+1], iySectorsEE[i+1]);
          }
        }
      }

      if( name.find( "EETTT" ) != std::string::npos && nbx == 50 && nby == 50 )
      {

        l.SetLineWidth(1);
        l.SetLineStyle(3);

        // drawing horizontal TT boundaries
        for(int i=0; i!=1381; i=i+1)
          l.DrawLine(ixTTEEHorizontal1[i]-1, iyTTEEHorizontal1[i]-1, ixTTEEHorizontal1[i]+1-1, iyTTEEHorizontal1[i]-1);
        for(int i=0; i!=1386; i=i+1)
          l.DrawLine(ixTTEEHorizontal2[i]-1, iyTTEEHorizontal2[i]-1, ixTTEEHorizontal2[i], iyTTEEHorizontal2[i]-1);
        // drawing vertical TT boundaries
        for(int i=0; i!=1381; i=i+1)
          l.DrawLine(ixTTEEVertical1[i]-1, iyTTEEVertical1[i]-1, ixTTEEVertical1[i]-1, iyTTEEVertical1[i]);
        for(int i=0; i!=1385; i=i+1)
          l.DrawLine(ixTTEEVertical2[i]-1, iyTTEEVertical2[i]-1, ixTTEEVertical2[i]-1, iyTTEEVertical2[i]);
        l.SetLineWidth(1);
        l.SetLineStyle(2);

        // drawing horizontal TCC boundaries
        for(int i=0; i<699; i=i+1)
          l.DrawLine(ixTCCEEHorizontal[i]-1, iyTCCEEHorizontal[i]-1, ixTCCEEHorizontal[i], iyTCCEEHorizontal[i]-1);

        // drawing vertical TCC boundaries
        for(int i=0; i<729; i=i+1)
        {
          l.DrawLine(ixTCCEEVertical[i]-1, iyTCCEEVertical[i]-1, ixTCCEEVertical[i]-1, iyTCCEEVertical[i]);
        }

        // printing TT ID numbers
        if( name.find( "EE+" ) != std::string::npos ) {
          int x1 = text14->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text14->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text14->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text14->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text14->GetXaxis()->SetRange(x1+1, x2-1);
          text14->GetYaxis()->SetRange(y1+1, y2-1);
          text14->Draw("text,same");
        } else if( name.find( "EE-" ) != std::string::npos ) {
          int x1 = text15->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text15->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text15->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text15->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text15->GetXaxis()->SetRange(x1+1, x2-1);
          text15->GetYaxis()->SetRange(y1+1, y2-1);
          text15->Draw("text,same");
        }
      }

      if( name.find( "EETTT" ) != std::string::npos && nbx == 100 && nby == 100 )
      {

/*
        l.SetLineWidth(1);
        l.SetLineStyle(3);

        // drawing horizontal TT boundaries
        for(int i=0; i!=1381; i=i+1)
        {
          l.DrawLine(ixTTEEHorizontal1[i]-1, iyTTEEHorizontal1[i]-1, ixTTEEHorizontal1[i]+1-1, iyTTEEHorizontal1[i]-1);
        }
        for(int i=0; i!=1386; i=i+1)
        {
          l.DrawLine(ixTTEEHorizontal2[i]-1, iyTTEEHorizontal2[i]-1, ixTTEEHorizontal2[i], iyTTEEHorizontal2[i]-1);
        }
        // drawing vertical TT boundaries
        for(int i=0; i!=1381; i=i+1)
        {
          l.DrawLine(ixTTEEVertical1[i]-1, iyTTEEVertical1[i]-1, ixTTEEVertical1[i]-1, iyTTEEVertical1[i]);
        }
        for(int i=0; i!=1385; i=i+1)
        {
          l.DrawLine(ixTTEEVertical2[i]-1, iyTTEEVertical2[i]-1, ixTTEEVertical2[i]-1, iyTTEEVertical2[i]);
        }
*/

        l.SetLineWidth(1);
        l.SetLineStyle(2);

        // drawing horizontal TCC boundaries
        for(int i=0; i<699; i=i+1)
        {
          l.DrawLine(ixTCCEEHorizontal[i]-1, iyTCCEEHorizontal[i]-1, ixTCCEEHorizontal[i], iyTCCEEHorizontal[i]-1);
        }
        // drawing vertical TCC boundaries
        for(int i=0; i<729; i=i+1)
        {
          l.DrawLine(ixTCCEEVertical[i]-1, iyTCCEEVertical[i]-1, ixTCCEEVertical[i]-1, iyTCCEEVertical[i]);
        }

      }

      if( name.find( "EECLT" ) != std::string::npos &&
          name.find( "seed" ) == std::string::npos )
      {
        if( name.find( "EE -" ) != std::string::npos )
        {
          int x1 = text8->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text8->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text8->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text8->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text8->GetXaxis()->SetRange(x1, x2);
          text8->GetYaxis()->SetRange(y1, y2);
          text8->Draw("text,same");
        }

        if( name.find( "EE +" ) != std::string::npos )
        {
          int x1 = text9->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text9->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text9->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text9->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text9->GetXaxis()->SetRange(x1, x2);
          text9->GetYaxis()->SetRange(y1, y2);
          text9->Draw("text,same");
        }
        return;
      }

      if( name.find( "EECLT SC energy vs seed crystal energy" ) != std::string::npos )
        return;

      if( name.find( "seed" ) != std::string::npos )
      {
        if( name.find( "EE -" ) != std::string::npos )
        {
          int x1 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text6->GetXaxis()->SetRange(x1, x2);
          text6->GetYaxis()->SetRange(y1, y2);
          text6->Draw("text,same");
        }

        if( name.find( "EE +" ) != std::string::npos )
        {
          int x1 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text7->GetXaxis()->SetRange(x1, x2);
          text7->GetYaxis()->SetRange(y1, y2);
          text7->Draw("text,same");
        }
        return;
      }

      if( name.find( "EESRT") != std::string::npos )
      {
        if( nbx == 100 && nby == 100 )
        {
          if( name.find( "EE -" ) != std::string::npos )
          {
            int x1 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
            int x2 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
            int y1 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
            int y2 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
            text6->GetXaxis()->SetRange(x1, x2);
            text6->GetYaxis()->SetRange(y1, y2);
            text6->Draw("text,same");
          }

          if( name.find( "EE +" ) != std::string::npos )
          {
            int x1 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
            int x2 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
            int y1 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
            int y2 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
            text7->GetXaxis()->SetRange(x1, x2);
            text7->GetYaxis()->SetRange(y1, y2);
            text7->Draw("text,same");
          }
        }
        else if( nbx == 20 && nby == 20 )
        {
          if( name.find( "EE -" ) != std::string::npos )
          {
            int x1 = text12->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
            int x2 = text12->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
            int y1 = text12->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
            int y2 = text12->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
            text12->GetXaxis()->SetRange(x1, x2);
            text12->GetYaxis()->SetRange(y1, y2);
            text12->Draw("text,same");
          }

          if( name.find( "EE +" ) != std::string::npos )
          {
            int x1 = text13->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
            int x2 = text13->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
            int y1 = text13->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
            int y2 = text13->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
            text13->GetXaxis()->SetRange(x1, x2);
            text13->GetYaxis()->SetRange(y1, y2);
            text13->Draw("text,same");
          }
        }
        return;
      }

      if( nbx == 50 && nby == 50 && name.find( "EETTT" ) == std::string::npos )
      {
        int x1 = text1->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
        int x2 = text1->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
        int y1 = text1->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
        int y2 = text1->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
        text1->GetXaxis()->SetRange(x1, x2);
        text1->GetYaxis()->SetRange(y1, y2);
        text1->Draw("text,same");
      }

      if( name.find( "EETMT" ) != std::string::npos &&
          (( nbx == 20 && nby == 20 ) || ( nbx == 50 && nby == 50 )) )
      {
        c->Update();
        TPaletteAxis* palette =
          (TPaletteAxis*) obj->GetListOfFunctions()->FindObject("palette");
        if( palette )
        {
          palette->SetLabelColor(10);;
          if( timingAxis ) delete timingAxis;
          float xup  = c->GetUxmax();
          float x2   = c->PadtoX(c->GetX2());
          float xr   = 0.05*(c->GetX2() - c->GetX1());
          float xmax = c->PadtoX(xup + xr);
          if (xmax > x2) xmax = c->PadtoX(c->GetX2()-0.01*xr);
          float ymin = c->PadtoY(c->GetUymin());
          float ymax = c->PadtoY(c->GetUymax());
          timingAxis = new TGaxis(xmax, ymin, xmax, ymax,
                                  obj->GetMinimum()-50.,
                                  obj->GetMaximum()-50., 10, "+LB");
          timingAxis->Draw();
        }
      }

      if( nbx == 20 && nby == 20 && name.find( "EETMT" ) != std::string::npos )
      {
        if( name.find( "EE -" ) != std::string::npos )
        {
          int x1 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text6->GetXaxis()->SetRange(x1, x2);
          text6->GetYaxis()->SetRange(y1, y2);
          text6->Draw("text,same");
        }

        if( name.find( "EE +" ) != std::string::npos )
        {
          int x1 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text7->GetXaxis()->SetRange(x1, x2);
          text7->GetYaxis()->SetRange(y1, y2);
          text7->Draw("text,same");
        }
        return;
      }

    }

  void postDrawTH3F( TCanvas *, const VisDQMObject & )
    {
    }

  void postDrawTH2( TCanvas *c, const VisDQMObject &o )
    {
      TH2* obj = dynamic_cast<TH2*>( o.object );
      assert( obj );

      std::string name = o.name.substr(o.name.rfind("/")+1);

      if( name.find( "EETMT timing vs amplitude" ) != std::string::npos ||
          name.find( "EETMT timing EE+ vs EE-") != std::string::npos )
        return;

      int nbx = obj->GetNbinsX();
      int nby = obj->GetNbinsY();

      c->SetBit(TGraph::kClipFrame);
      TLine l;
      l.SetLineWidth(1);
      for(int i=0; i<201; i=i+1)
      {
        if( (ixSectorsEE[i]!=0 || iySectorsEE[i]!=0) && (ixSectorsEE[i+1]!=0 || iySectorsEE[i+1]!=0) )
        {
          if( name.find( "reportSummaryMap") != std::string::npos && nbx == 40 && nby == 20 )
          {
            l.DrawLine(0.2*ixSectorsEE[i], 0.2*iySectorsEE[i], 0.2*ixSectorsEE[i+1], 0.2*iySectorsEE[i+1]);
            l.DrawLine(20+0.2*ixSectorsEE[i], 0.2*iySectorsEE[i], 20+0.2*ixSectorsEE[i+1], 0.2*iySectorsEE[i+1]);
          }
          else if( (name.find( "reportSummaryMap") != std::string::npos && nbx == 200 && nby == 100) ||
                   name.find( "DAQSummaryMap") != std::string::npos ||
                   name.find( "DCSSummaryMap") != std::string::npos ||
                   name.find( "CertificationSummaryMap") != std::string::npos )
          {
            l.DrawLine(ixSectorsEE[i], iySectorsEE[i], ixSectorsEE[i+1], iySectorsEE[i+1]);
            l.DrawLine(100+ixSectorsEE[i], iySectorsEE[i], 100+ixSectorsEE[i+1], iySectorsEE[i+1]);
          }
          else if( name.find( "EECLT" ) != std::string::npos &&
                   name.find( "seed" ) == std::string::npos )
          {
            l.DrawLine(3.0*(ixSectorsEE[i]-50), 3.0*(iySectorsEE[i]-50), 3.0*(ixSectorsEE[i+1]-50), 3.0*(iySectorsEE[i+1]-50));
          }
          else if( name.find( "EESRT" ) != std::string::npos && nbx == 20 && nby == 20 )
          {
            l.DrawLine(0.2*ixSectorsEE[i], 0.2*iySectorsEE[i], 0.2*ixSectorsEE[i+1], 0.2*iySectorsEE[i+1]);
          }
          else if( name.find( " PN " ) == std::string::npos &&
                   name.find( "EESRT event size vs DCC" ) == std::string::npos &&
                   name.find( "TCC timing" ) == std::string::npos )
          {
            l.DrawLine(ixSectorsEE[i], iySectorsEE[i], ixSectorsEE[i+1], iySectorsEE[i+1]);
          }
        }
      }

      if( name.find( "EETTT" ) != std::string::npos && nbx == 50 && nby == 50 )
      {

        l.SetLineWidth(1);
        l.SetLineStyle(3);

        // drawing horizontal TT boundaries
        for(int i=0; i!=1381; i=i+1)
        {
          l.DrawLine(ixTTEEHorizontal1[i]-1, iyTTEEHorizontal1[i]-1, ixTTEEHorizontal1[i]+1-1, iyTTEEHorizontal1[i]-1);
        }
        for(int i=0; i!=1386; i=i+1)
        {
          l.DrawLine(ixTTEEHorizontal2[i]-1, iyTTEEHorizontal2[i]-1, ixTTEEHorizontal2[i], iyTTEEHorizontal2[i]-1);
        }
        // drawing vertical TT boundaries
        for(int i=0; i!=1381; i=i+1)
        {
          l.DrawLine(ixTTEEVertical1[i]-1, iyTTEEVertical1[i]-1, ixTTEEVertical1[i]-1, iyTTEEVertical1[i]);
        }
        for(int i=0; i!=1385; i=i+1)
        {
          l.DrawLine(ixTTEEVertical2[i]-1, iyTTEEVertical2[i]-1, ixTTEEVertical2[i]-1, iyTTEEVertical2[i]);
        }

        l.SetLineWidth(1);
        l.SetLineStyle(2);

        // drawing horizontal TCC boundaries
        for(int i=0; i<699; i=i+1)
        {
          l.DrawLine(ixTCCEEHorizontal[i]-1, iyTCCEEHorizontal[i]-1, ixTCCEEHorizontal[i], iyTCCEEHorizontal[i]-1);
        }
        // drawing vertical TCC boundaries
        for(int i=0; i<729; i=i+1)
        {
          l.DrawLine(ixTCCEEVertical[i]-1, iyTCCEEVertical[i]-1, ixTCCEEVertical[i]-1, iyTCCEEVertical[i]);
        }

        // printing TT ID numbers
        int x1 = text14->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
        int x2 = text14->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
        int y1 = text14->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
        int y2 = text14->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
        text14->GetXaxis()->SetRange(x1+1, x2-1);
        text14->GetYaxis()->SetRange(y1+1, y2-1);
        text14->Draw("text,same");

      }

      if( name.find( "EETTT" ) != std::string::npos && nbx == 100 && nby == 100 )
      {

/*
        l.SetLineWidth(1);
        l.SetLineStyle(3);

        // drawing horizontal TT boundaries
        for(int i=0; i!=1381; i=i+1)
        {
          l.DrawLine(ixTTEEHorizontal1[i]-1, iyTTEEHorizontal1[i]-1, ixTTEEHorizontal1[i]+1-1, iyTTEEHorizontal1[i]-1);
        }
        for(int i=0; i!=1386; i=i+1)
        {
          l.DrawLine(ixTTEEHorizontal2[i]-1, iyTTEEHorizontal2[i]-1, ixTTEEHorizontal2[i], iyTTEEHorizontal2[i]-1);
        }
        // drawing vertical TT boundaries
        for(int i=0; i!=1381; i=i+1)
        {
          l.DrawLine(ixTTEEVertical1[i]-1, iyTTEEVertical1[i]-1, ixTTEEVertical1[i]-1, iyTTEEVertical1[i]);
        }
        for(int i=0; i!=1385; i=i+1)
        {
          l.DrawLine(ixTTEEVertical2[i]-1, iyTTEEVertical2[i]-1, ixTTEEVertical2[i]-1, iyTTEEVertical2[i]);
        }
*/

        l.SetLineWidth(1);
        l.SetLineStyle(2);

        // drawing horizontal TCC boundaries
        for(int i=0; i<699; i=i+1)
        {
          l.DrawLine(ixTCCEEHorizontal[i]-1, iyTCCEEHorizontal[i]-1, ixTCCEEHorizontal[i], iyTCCEEHorizontal[i]-1);
        }
        // drawing vertical TCC boundaries
        for(int i=0; i<729; i=i+1)
        {
          l.DrawLine(ixTCCEEVertical[i]-1, iyTCCEEVertical[i]-1, ixTCCEEVertical[i]-1, iyTCCEEVertical[i]);
        }

      }

      if( name.find( "EECLT" ) != std::string::npos &&
          name.find( "seed" ) == std::string::npos )
      {
        if( name.find( "EE -" ) != std::string::npos )
        {
          int x1 = text8->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text8->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text8->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text8->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text8->GetXaxis()->SetRange(x1, x2);
          text8->GetYaxis()->SetRange(y1, y2);
          text8->Draw("text,same");
        }

        if( name.find( "EE +" ) != std::string::npos )
        {
          int x1 = text9->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text9->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text9->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text9->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text9->GetXaxis()->SetRange(x1, x2);
          text9->GetYaxis()->SetRange(y1, y2);
          text9->Draw("text,same");
        }
        return;
      }

      if( name.find( "seed" ) != std::string::npos )
      {
        if( name.find( "EE -" ) != std::string::npos )
        {
          int x1 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text6->GetXaxis()->SetRange(x1, x2);
          text6->GetYaxis()->SetRange(y1, y2);
          text6->Draw("text,same");
        }

        if( name.find( "EE +" ) != std::string::npos )
        {
          int x1 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text7->GetXaxis()->SetRange(x1, x2);
          text7->GetYaxis()->SetRange(y1, y2);
          text7->Draw("text,same");
        }
        return;
      }

      if( name.find( "EEOT MEM" ) != std::string::npos )
      {
        int x1 = text3->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
        int x2 = text3->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
        int y1 = text3->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
        int y2 = text3->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
        text3->GetXaxis()->SetRange(x1, x2);
        text3->GetYaxis()->SetRange(y1, y2);
        text3->Draw("text,same");
        return;
      }

      if( name.find( "EEOT digi" ) != std::string::npos )
      {
        if( nbx == 50 && nby == 50 )
        {
          int x1 = text1->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text1->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text1->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text1->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text1->GetXaxis()->SetRange(x1, x2);
          text1->GetYaxis()->SetRange(y1, y2);
          text1->Draw("text,same");
          return;
        }

        if( name.find( "EE -" ) != std::string::npos )
        {
          int x1 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text6->GetXaxis()->SetRange(x1, x2);
          text6->GetYaxis()->SetRange(y1, y2);
          text6->Draw("text,same");
        }

        if( name.find( "EE +" ) != std::string::npos )
        {
          int x1 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text7->GetXaxis()->SetRange(x1, x2);
          text7->GetYaxis()->SetRange(y1, y2);
          text7->Draw("text,same");
        }
        return;
      }

      if( name.find( "EEOT rec hit" ) != std::string::npos )
      {
        if( name.find( "EE -" ) != std::string::npos )
        {
          int x1 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text6->GetXaxis()->SetRange(x1, x2);
          text6->GetYaxis()->SetRange(y1, y2);
          text6->Draw("text,same");
        }

        if( name.find( "EE +" ) != std::string::npos )
        {
          int x1 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text7->GetXaxis()->SetRange(x1, x2);
          text7->GetYaxis()->SetRange(y1, y2);
          text7->Draw("text,same");
        }
        return;
      }

      if( name.find( "EEOT TP digi" ) != std::string::npos )
      {
        if( name.find( "EE -" ) != std::string::npos )
        {
          int x1 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text6->GetXaxis()->SetRange(x1, x2);
          text6->GetYaxis()->SetRange(y1, y2);
          text6->Draw("text,same");
        }

        if( name.find( "EE +" ) != std::string::npos )
        {
          int x1 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text7->GetXaxis()->SetRange(x1, x2);
          text7->GetYaxis()->SetRange(y1, y2);
          text7->Draw("text,same");
        }
        return;
      }

      if( name.find( "EEOT test pulse digi" ) != std::string::npos )
      {
        if( name.find( "EE -" ) != std::string::npos )
        {
          int x1 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text6->GetXaxis()->SetRange(x1, x2);
          text6->GetYaxis()->SetRange(y1, y2);
          text6->Draw("text,same");
        }

        if( name.find( "EE +" ) != std::string::npos )
        {
          int x1 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text7->GetXaxis()->SetRange(x1, x2);
          text7->GetYaxis()->SetRange(y1, y2);
          text7->Draw("text,same");
        }
        return;
      }

      if( name.find( "EEOT laser digi" ) != std::string::npos )
      {
        if( name.find( "EE -" ) != std::string::npos )
        {
          int x1 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text6->GetXaxis()->SetRange(x1, x2);
          text6->GetYaxis()->SetRange(y1, y2);
          text6->Draw("text,same");
        }

        if( name.find( "EE +" ) != std::string::npos )
        {
          int x1 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text7->GetXaxis()->SetRange(x1, x2);
          text7->GetYaxis()->SetRange(y1, y2);
          text7->Draw("text,same");
        }
        return;
      }

      if( name.find( "EEOT led digi" ) != std::string::npos )
      {
        if( name.find( "EE -" ) != std::string::npos )
        {
          int x1 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text6->GetXaxis()->SetRange(x1, x2);
          text6->GetYaxis()->SetRange(y1, y2);
          text6->Draw("text,same");
        }

        if( name.find( "EE +" ) != std::string::npos )
        {
          int x1 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text7->GetXaxis()->SetRange(x1, x2);
          text7->GetYaxis()->SetRange(y1, y2);
          text7->Draw("text,same");
        }
        return;
      }

      if( name.find( "EEOT pedestal digi" ) != std::string::npos ||
          name.find( "G12 RMS map" ) != std::string::npos )
      {
        if( name.find( "EE -" ) != std::string::npos )
        {
          int x1 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text6->GetXaxis()->SetRange(x1, x2);
          text6->GetYaxis()->SetRange(y1, y2);
          text6->Draw("text,same");
        }

        if( name.find( "EE +" ) != std::string::npos )
        {
          int x1 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text7->GetXaxis()->SetRange(x1, x2);
          text7->GetYaxis()->SetRange(y1, y2);
          text7->Draw("text,same");
        }
        return;
      }

      if( name.find( "EESRT") != std::string::npos )
      {
        if( nbx == 100 && nby == 100 )
        {
          if( name.find( "EE -" ) != std::string::npos )
          {
            int x1 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
            int x2 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
            int y1 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
            int y2 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
            text6->GetXaxis()->SetRange(x1, x2);
            text6->GetYaxis()->SetRange(y1, y2);
            text6->Draw("text,same");
          }

          if( name.find( "EE +" ) != std::string::npos )
          {
            int x1 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
            int x2 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
            int y1 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
            int y2 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
            text7->GetXaxis()->SetRange(x1, x2);
            text7->GetYaxis()->SetRange(y1, y2);
            text7->Draw("text,same");
          }
        }
        else if( nbx == 20 && nby == 20 )
        {
          if( name.find( "EE -" ) != std::string::npos )
          {
            int x1 = text12->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
            int x2 = text12->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
            int y1 = text12->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
            int y2 = text12->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
            text12->GetXaxis()->SetRange(x1, x2);
            text12->GetYaxis()->SetRange(y1, y2);
            text12->Draw("text,same");
          }

          if( name.find( "EE +" ) != std::string::npos )
          {
            int x1 = text13->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
            int x2 = text13->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
            int y1 = text13->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
            int y2 = text13->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
            text13->GetXaxis()->SetRange(x1, x2);
            text13->GetYaxis()->SetRange(y1, y2);
            text13->Draw("text,same");
          }
        }
        return;
      }

      if( name.find( "reportSummaryMap" ) != std::string::npos && nbx == 40 && nby == 20 )
      {
        int x1 = text10->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
        int x2 = text10->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
        int y1 = text10->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
        int y2 = text10->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
        text10->GetXaxis()->SetRange(x1, x2);
        text10->GetYaxis()->SetRange(y1, y2);
        text10->Draw("text,same");
        return;
      }

      if( (name.find( "reportSummaryMap" ) != std::string::npos && nbx == 200 && nby == 100) ||
          name.find( "DAQSummaryMap" ) != std::string::npos ||
          name.find( "DCSSummaryMap" ) != std::string::npos ||
          name.find( "CertificationSummaryMap" ) != std::string::npos )
      {
        int x1 = text11->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
        int x2 = text11->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
        int y1 = text11->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
        int y2 = text11->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
        text11->GetXaxis()->SetRange(x1, x2);
        text11->GetYaxis()->SetRange(y1, y2);
        text11->Draw("text,same");
        return;
      }

      if( nbx == 50 && nby == 50 && name.find( "EETTT" ) == std::string::npos )
      {
        int x1 = text1->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
        int x2 = text1->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
        int y1 = text1->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
        int y2 = text1->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
        text1->GetXaxis()->SetRange(x1, x2);
        text1->GetYaxis()->SetRange(y1, y2);
        text1->Draw("text,same");
        return;
      }

      if( nbx == 10 && ( nby == 1 || nby == 5 ) )
      {
        int x1 = text3->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
        int x2 = text3->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
        int y1 = text3->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
        int y2 = text3->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
        text3->GetXaxis()->SetRange(x1, x2);
        text3->GetYaxis()->SetRange(y1, y2);
        text3->Draw("text,same");
        return;
      }

      if( nbx == 2 && nby == 1 )
      {
        int x1 = text4->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
        int x2 = text4->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
        int y1 = text4->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
        int y2 = text4->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
        text4->GetXaxis()->SetRange(x1, x2);
        text4->GetYaxis()->SetRange(y1, y2);
        text4->Draw("text,same");
        return;
      }

      if( nbx == 45 && nby == 20 )
      {
        int x1 = text16->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
        int x2 = text16->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
        int y1 = text16->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
        int y2 = text16->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
        text16->GetXaxis()->SetRange(x1, x2);
        text16->GetYaxis()->SetRange(y1, y2);
        text16->Draw("text,same");
        return;
      }

      if( name.find( "summary" ) != std::string::npos )
      {
        if( name.find( "EE -" ) != std::string::npos )
        {
          int x1 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text6->GetXaxis()->SetRange(x1, x2);
          text6->GetYaxis()->SetRange(y1, y2);
          text6->Draw("text,same");
        }

        if( name.find( "EE +" ) != std::string::npos )
        {
          int x1 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text7->GetXaxis()->SetRange(x1, x2);
          text7->GetYaxis()->SetRange(y1, y2);
          text7->Draw("text,same");
        }
        return;
      }
    }

  void postDrawTH1( TCanvas *, const VisDQMObject & )
    {
    }

};

const int EERenderPlugin::ixSectorsEE[202] = {
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

const int EERenderPlugin::iySectorsEE[202] = {
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

const int EERenderPlugin::inTowersEE[400] = {
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

  //note: for TTs each list is split into two because as one giant list root complains that there are too many arguments

const int EERenderPlugin::ixTTEEHorizontal1[1381] = {1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50};

const int EERenderPlugin::ixTTEEHorizontal2[1386] = {51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 86, 86, 86, 86, 86, 86, 86, 86, 86, 86, 86, 86, 86, 86, 86, 86, 86, 86, 86, 86, 86, 86, 86, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 91, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 94, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 96, 96, 96, 96, 96, 96, 96, 96, 96, 96, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 98, 98, 98, 98, 98, 98, 99, 99, 99, 99, 99, 99, 100, 100, 100, 100, 100};

const int EERenderPlugin::iyTTEEHorizontal1[1381] = {42, 46, 51, 56, 60, 61, 42, 46, 51, 56, 60, 61, 42, 46, 51, 56, 60, 61, 39, 42, 44, 46, 51, 56, 58, 60, 63, 66, 38, 42, 43, 46, 51, 56, 59, 60, 64, 66, 31, 34, 39, 43, 48, 51, 54, 59, 63, 68, 71, 76, 31, 33, 35, 39, 43, 44, 48, 50, 51, 52, 54, 58, 59, 63, 67, 69, 71, 76, 29, 31, 35, 39, 40, 42, 43, 46, 47, 48, 51, 54, 55, 56, 59, 60, 62, 63, 67, 71, 73, 76, 23, 26, 27, 31, 35, 36, 37, 38, 39, 43, 48, 51, 54, 59, 63, 64, 65, 66, 67, 71, 75, 76, 79, 81, 24, 26, 27, 31, 36, 39, 43, 48, 51, 54, 59, 63, 66, 71, 75, 76, 78, 81, 24, 28, 31, 32, 36, 41, 43, 46, 51, 56, 59, 61, 66, 70, 71, 74, 78, 81, 22, 24, 29, 31, 33, 36, 41, 44, 46, 47, 51, 55, 56, 58, 61, 66, 69, 71, 73, 78, 80, 81, 22, 25, 29, 33, 36, 38, 41, 44, 47, 51, 55, 58, 61, 64, 66, 69, 73, 77, 80, 81, 19, 21, 26, 28, 29, 34, 37, 41, 44, 48, 50, 51, 52, 54, 58, 61, 65, 68, 73, 74, 76, 81, 83, 86, 18, 21, 26, 30, 33, 38, 41, 45, 47, 51, 55, 57, 61, 64, 69, 72, 76, 81, 84, 86, 16, 22, 25, 27, 31, 36, 39, 42, 44, 48, 51, 54, 58, 60, 63, 66, 71, 75, 77, 80, 85, 86, 88, 16, 17, 22, 24, 27, 31, 32, 36, 38, 42, 44, 48, 49, 51, 53, 54, 58, 60, 64, 66, 70, 71, 75, 78, 80, 84, 86, 88, 15, 19, 23, 24, 28, 30, 32, 36, 39, 42, 45, 47, 48, 51, 54, 55, 57, 60, 63, 66, 70, 72, 74, 78, 79, 84, 87, 88, 19, 22, 26, 27, 29, 33, 35, 36, 39, 42, 45, 46, 48, 51, 54, 56, 57, 60, 63, 66, 67, 69, 73, 75, 76, 80, 81, 88, 19, 21, 26, 29, 32, 36, 40, 42, 46, 48, 51, 54, 56, 60, 62, 66, 70, 73, 76, 81, 88, 14, 16, 20, 22, 25, 26, 30, 31, 33, 36, 37, 41, 43, 46, 48, 51, 54, 56, 59, 61, 65, 66, 69, 71, 72, 76, 77, 81, 82, 86, 88, 93, 12, 18, 19, 22, 24, 28, 29, 31, 34, 36, 38, 41, 44, 46, 49, 51, 53, 56, 58, 61, 64, 66, 68, 71, 73, 74, 78, 79, 83, 84, 90, 93, 10, 12, 18, 23, 24, 28, 31, 35, 36, 38, 41, 44, 46, 49, 51, 53, 56, 58, 61, 64, 66, 67, 71, 74, 79, 84, 90, 92, 93, 11, 13, 17, 19, 22, 26, 27, 28, 31, 33, 34, 36, 39, 41, 44, 46, 49, 51, 53, 56, 58, 61, 63, 66, 68, 69, 71, 74, 75, 78, 80, 83, 85, 89, 91, 93, 11, 14, 16, 19, 21, 26, 30, 31, 34, 36, 38, 41, 45, 46, 50, 51, 52, 56, 57, 61, 64, 66, 68, 71, 72, 76, 78, 81, 83, 86, 88, 91, 93, 11, 15, 16, 20, 22, 25, 27, 30, 31, 34, 37, 39, 41, 42, 45, 47, 49, 51, 53, 55, 57, 60, 61, 63, 65, 68, 71, 73, 76, 77, 80, 82, 86, 87, 91, 96, 9, 11, 15, 18, 19, 22, 24, 28, 30, 31, 33, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 69, 71, 73, 75, 78, 80, 83, 84, 87, 91, 93, 96, 9, 12, 14, 19, 23, 25, 28, 31, 32, 36, 38, 39, 40, 41, 43, 45, 48, 49, 50, 51, 52, 53, 54, 57, 59, 61, 62, 63, 64, 66, 70, 71, 73, 74, 77, 79, 83, 88, 90, 93, 96, 8, 13, 15, 19, 21, 22, 25, 26, 31, 33, 36, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 66, 69, 71, 73, 74, 77, 80, 81, 83, 87, 89, 94, 96, 8, 13, 16, 18, 21, 26, 31, 33, 36, 39, 41, 44, 45, 46, 49, 51, 53, 56, 57, 58, 61, 63, 66, 69, 71, 73, 76, 81, 84, 86, 89, 94, 96, 8, 11, 16, 17, 21, 24, 28, 32, 35, 36, 37, 40, 41, 42, 44, 46, 48, 49, 51, 53, 54, 56, 58, 60, 61, 62, 65, 66, 67, 71, 74, 78, 81, 85, 86, 91, 94, 96, 8, 11, 12, 16, 19, 20, 21, 24, 28, 29, 32, 34, 36, 38, 40, 41, 42, 44, 46, 48, 50, 51, 52, 54, 56, 58, 60, 61, 62, 64, 66, 68, 69, 73, 74, 78, 81, 82, 83, 86, 90, 91, 94, 96, 7, 11, 14, 15, 16, 20, 22, 25, 27, 28, 31, 33, 35, 36, 38, 39, 41, 43, 44, 45, 46, 47, 49, 51, 53, 55, 56, 57, 58, 59, 61, 63, 64, 66, 69, 71, 74, 75, 77, 80, 82, 86, 87, 88, 91, 95, 96, 7, 11, 14, 16, 20, 23, 24, 26, 28, 31, 32, 35, 36, 38, 40, 41, 42, 43, 46, 48, 51, 54, 56, 59, 60, 61, 62, 64, 66, 69, 70, 71, 74, 76, 78, 79, 82, 86, 88, 91, 95, 96, 10, 11, 14, 16, 19, 23, 26, 28, 31, 36, 39, 41, 46, 49, 51, 53, 56, 61, 63, 66, 67, 71, 74, 76, 79, 83, 86, 88, 91, 92, 96, 6, 9, 13, 18, 21, 26, 30, 31, 34, 36, 39, 43, 46, 48, 51, 54, 56, 59, 61, 62, 65, 68, 71, 72, 76, 81, 84, 89, 93, 96, 98, 6, 10, 13, 14, 15, 18, 21, 22, 26, 28, 29, 32, 34, 37, 39, 43, 45, 46, 48, 51, 54, 56, 57, 59, 61, 62, 64, 68, 70, 73, 74, 76, 80, 81, 84, 87, 88, 89, 92, 96, 98, 5, 6, 9, 13, 16, 17, 18, 21, 24, 25, 26, 29, 33, 35, 38, 40, 41, 42, 43, 45, 46, 49, 51, 53, 56, 57, 59, 60, 61, 64, 67, 69, 73, 76, 77, 78, 81, 84, 85, 86, 89, 93, 96, 97, 98, 6, 8, 11, 13, 16, 20, 21, 24, 28, 31, 33, 34, 36, 38, 41, 45, 46, 49, 51, 53, 56, 57, 61, 64, 66, 68, 69, 71, 74, 78, 81, 82, 86, 89, 91, 94, 96, 98, 6, 9, 11, 13, 16, 21, 24, 29, 31, 35, 36, 41, 44, 46, 58, 61, 63, 66, 67, 71, 73, 78, 81, 86, 89, 91, 93, 96, 98, 6, 9, 13, 16, 21, 23, 26, 31, 34, 36, 38, 41, 44, 59, 61, 64, 66, 68, 71, 76, 79, 81, 86, 89, 93, 96, 101, 6, 8, 13, 16, 20, 21, 23, 26, 27, 31, 33, 35, 36, 39, 41, 43, 61, 63, 66, 67, 69, 71, 75, 76, 79, 81, 82, 86, 89, 94, 96, 101, 5, 7, 12, 13, 16, 20, 22, 23, 26, 30, 31, 34, 38, 42, 61, 64, 68, 71, 72, 76, 79, 80, 82, 86, 89, 90, 95, 97, 101, 4, 8, 13, 15, 16, 18, 20, 23, 25, 26, 31, 33, 38, 40, 41, 62, 64, 69, 71, 76, 77, 79, 82, 84, 86, 87, 89, 94, 98, 101, 4, 8, 13, 16, 19, 23, 26, 31, 34, 37, 41, 65, 68, 71, 76, 79, 83, 86, 89, 94, 98, 101, 4, 6, 9, 11, 12, 16, 19, 23, 26, 30, 31, 34, 36, 40, 66, 68, 71, 72, 76, 79, 83, 86, 90, 91, 93, 96, 98, 101, 4, 6, 8, 11, 12, 14, 15, 16, 18, 23, 26, 28, 29, 31, 33, 34, 36, 40, 66, 68, 69, 71, 73, 74, 76, 79, 84, 86, 87, 88, 90, 91, 94, 96, 98, 101, 4, 8, 12, 15, 17, 22, 23, 26, 29, 34, 35, 36, 38, 40, 64, 66, 67, 68, 73, 76, 79, 80, 85, 87, 90, 94, 98, 101, 4, 8, 12, 15, 18, 23, 25, 26, 28, 32, 33, 34, 36, 40, 66, 68, 69, 70, 74, 76, 77, 79, 84, 87, 90, 94, 98, 101, 4, 7, 12, 14, 18, 23, 26, 29, 34, 36, 40, 66, 68, 73, 76, 79, 84, 88, 90, 95, 98, 101};

const int EERenderPlugin::iyTTEEHorizontal2[1386] = {4, 7, 12, 14, 18, 23, 26, 29, 34, 36, 40, 66, 68, 73, 76, 79, 84, 88, 90, 95, 98, 101, 4, 8, 12, 15, 18, 23, 25, 26, 28, 32, 33, 34, 36, 40, 66, 68, 69, 70, 74, 76, 77, 79, 84, 87, 90, 94, 98, 101, 4, 8, 12, 15, 17, 22, 23, 26, 29, 34, 35, 36, 38, 40, 64, 66, 67, 68, 73, 76, 79, 80, 85, 87, 90, 94, 98, 101, 4, 6, 8, 11, 12, 14, 15, 16, 18, 23, 26, 28, 29, 31, 33, 34, 36, 40, 66, 68, 69, 71, 73, 74, 76, 79, 84, 86, 87, 88, 90, 91, 94, 96, 98, 101, 4, 6, 9, 11, 12, 16, 19, 23, 26, 30, 31, 34, 36, 40, 66, 68, 71, 72, 76, 79, 83, 86, 90, 91, 93, 96, 98, 101, 4, 8, 13, 16, 19, 23, 26, 31, 34, 37, 41, 65, 68, 71, 76, 79, 83, 86, 89, 94, 98, 101, 4, 8, 13, 15, 16, 18, 20, 23, 25, 26, 31, 33, 38, 40, 41, 62, 64, 69, 71, 76, 77, 79, 82, 84, 86, 87, 89, 94, 98, 101, 5, 7, 12, 13, 16, 20, 22, 23, 26, 30, 31, 34, 38, 41, 42, 64, 68, 71, 72, 76, 79, 80, 82, 86, 89, 90, 95, 97, 101, 6, 8, 13, 16, 20, 21, 23, 26, 27, 31, 33, 35, 36, 39, 41, 43, 61, 63, 66, 67, 69, 71, 75, 76, 79, 81, 82, 86, 89, 94, 96, 101, 6, 9, 13, 16, 21, 23, 26, 31, 34, 36, 38, 41, 43, 44, 61, 64, 66, 68, 71, 76, 79, 81, 86, 89, 93, 96, 101, 6, 9, 11, 13, 16, 21, 24, 29, 31, 35, 36, 39, 41, 44, 46, 58, 61, 66, 67, 71, 73, 78, 81, 86, 89, 91, 93, 96, 98, 6, 8, 11, 13, 16, 20, 21, 24, 28, 31, 33, 34, 36, 38, 41, 45, 46, 49, 51, 53, 56, 57, 61, 64, 66, 68, 69, 71, 74, 78, 81, 82, 86, 89, 91, 94, 96, 98, 5, 6, 9, 13, 16, 17, 18, 21, 24, 25, 26, 29, 33, 35, 38, 41, 42, 43, 45, 46, 49, 51, 53, 56, 57, 59, 60, 61, 62, 64, 67, 69, 73, 76, 77, 78, 81, 84, 85, 86, 89, 93, 96, 97, 98, 6, 10, 13, 14, 15, 18, 21, 22, 26, 28, 29, 32, 34, 38, 40, 41, 43, 45, 46, 48, 51, 54, 56, 57, 59, 63, 65, 68, 70, 73, 74, 76, 80, 81, 84, 87, 88, 89, 92, 96, 98, 6, 9, 13, 18, 21, 26, 30, 31, 34, 37, 40, 41, 43, 46, 48, 51, 54, 56, 59, 63, 66, 68, 71, 72, 76, 81, 84, 89, 93, 96, 98, 10, 11, 14, 16, 19, 23, 26, 28, 31, 35, 36, 39, 41, 46, 49, 51, 53, 56, 61, 63, 66, 71, 74, 76, 79, 83, 86, 88, 91, 92, 96, 7, 11, 14, 16, 20, 23, 24, 26, 28, 31, 32, 33, 36, 38, 40, 41, 42, 43, 46, 48, 51, 54, 56, 59, 60, 61, 62, 64, 66, 67, 70, 71, 74, 76, 78, 79, 82, 86, 88, 91, 95, 96, 7, 11, 14, 15, 16, 20, 22, 25, 27, 28, 31, 33, 36, 38, 39, 41, 43, 44, 45, 46, 47, 49, 51, 53, 55, 56, 57, 58, 59, 61, 63, 64, 66, 67, 69, 71, 74, 75, 77, 80, 82, 86, 87, 88, 91, 95, 96, 8, 11, 12, 16, 19, 20, 21, 24, 28, 29, 33, 34, 36, 38, 40, 41, 42, 44, 46, 48, 50, 51, 52, 54, 56, 58, 60, 61, 62, 64, 66, 68, 70, 73, 74, 78, 81, 82, 83, 86, 90, 91, 94, 96, 8, 11, 16, 17, 21, 24, 28, 31, 35, 36, 37, 40, 41, 42, 44, 46, 48, 49, 51, 53, 54, 56, 58, 60, 61, 62, 65, 66, 67, 70, 74, 78, 81, 85, 86, 91, 94, 96, 8, 13, 16, 18, 21, 26, 29, 31, 33, 36, 39, 41, 44, 45, 46, 49, 51, 53, 56, 57, 58, 61, 63, 66, 69, 71, 76, 81, 84, 86, 89, 94, 96, 8, 13, 15, 19, 21, 22, 25, 28, 29, 31, 33, 36, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 66, 69, 71, 76, 77, 80, 81, 83, 87, 89, 94, 96, 9, 12, 14, 19, 23, 25, 28, 29, 31, 32, 36, 38, 39, 40, 41, 43, 45, 48, 49, 50, 51, 52, 53, 54, 57, 59, 61, 62, 63, 64, 66, 70, 71, 74, 77, 79, 83, 88, 90, 93, 96, 9, 11, 15, 18, 19, 22, 24, 27, 29, 31, 33, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 69, 71, 72, 74, 78, 80, 83, 84, 87, 91, 93, 96, 11, 15, 16, 20, 22, 25, 26, 29, 31, 34, 37, 39, 41, 42, 45, 47, 49, 51, 53, 55, 57, 60, 61, 63, 65, 68, 71, 72, 75, 77, 80, 82, 86, 87, 91, 96, 11, 14, 16, 19, 21, 24, 26, 30, 31, 34, 36, 38, 41, 45, 46, 50, 51, 52, 56, 57, 61, 64, 66, 68, 71, 72, 76, 81, 83, 86, 88, 91, 93, 11, 13, 17, 19, 22, 24, 27, 28, 31, 33, 34, 36, 39, 41, 44, 46, 49, 51, 53, 56, 58, 61, 63, 66, 68, 69, 71, 74, 75, 76, 80, 83, 85, 89, 91, 93, 10, 12, 18, 23, 28, 31, 35, 36, 38, 41, 44, 46, 49, 51, 53, 56, 58, 61, 64, 66, 67, 71, 74, 78, 79, 84, 90, 92, 93, 12, 18, 19, 23, 24, 28, 29, 31, 34, 36, 38, 41, 44, 46, 49, 51, 53, 56, 58, 61, 64, 66, 68, 71, 73, 74, 78, 80, 83, 84, 90, 93, 14, 16, 20, 21, 25, 26, 30, 31, 33, 36, 37, 41, 43, 46, 48, 51, 54, 56, 59, 61, 65, 66, 69, 71, 72, 76, 77, 80, 82, 86, 88, 93, 21, 26, 29, 32, 36, 40, 42, 46, 48, 51, 54, 56, 60, 62, 66, 70, 73, 76, 81, 83, 88, 21, 22, 26, 27, 29, 33, 35, 36, 39, 42, 45, 46, 48, 51, 54, 56, 57, 60, 63, 66, 67, 69, 73, 75, 76, 80, 83, 86, 87, 88, 15, 18, 23, 24, 28, 30, 32, 36, 39, 42, 45, 47, 48, 51, 54, 55, 57, 60, 63, 66, 70, 72, 74, 78, 79, 83, 87, 88, 16, 18, 22, 24, 27, 31, 32, 36, 38, 42, 44, 48, 49, 51, 53, 54, 58, 60, 64, 66, 70, 71, 75, 78, 80, 85, 86, 88, 16, 17, 22, 25, 27, 31, 36, 39, 42, 44, 48, 51, 54, 58, 60, 63, 66, 71, 75, 77, 80, 86, 87, 88, 18, 21, 26, 30, 33, 38, 41, 45, 47, 51, 55, 57, 61, 64, 69, 72, 76, 81, 82, 83, 84, 85, 86, 19, 21, 26, 28, 29, 34, 37, 41, 44, 48, 50, 51, 52, 54, 58, 61, 65, 68, 73, 74, 76, 81, 83, 86, 22, 25, 29, 33, 36, 38, 41, 44, 47, 51, 55, 58, 61, 64, 66, 69, 73, 77, 80, 81, 22, 24, 29, 31, 33, 36, 41, 44, 46, 47, 51, 55, 56, 58, 61, 66, 69, 71, 73, 78, 80, 81, 24, 28, 31, 32, 36, 41, 43, 46, 51, 56, 59, 61, 66, 70, 71, 74, 78, 81, 24, 26, 27, 31, 36, 39, 43, 48, 51, 54, 59, 63, 66, 71, 75, 76, 78, 81, 23, 26, 27, 31, 35, 36, 37, 38, 39, 43, 48, 51, 54, 59, 63, 64, 65, 66, 67, 71, 75, 76, 79, 81, 29, 31, 35, 39, 40, 42, 43, 46, 47, 48, 51, 54, 55, 56, 59, 60, 62, 63, 67, 71, 73, 76, 31, 33, 35, 39, 43, 44, 48, 50, 51, 52, 54, 58, 59, 63, 67, 69, 71, 76, 31, 34, 39, 43, 48, 51, 54, 59, 63, 68, 71, 76, 38, 42, 43, 46, 51, 56, 59, 60, 64, 66, 39, 42, 44, 46, 51, 56, 58, 60, 63, 66, 42, 46, 51, 56, 60, 61, 42, 46, 51, 56, 60, 61, 42, 46, 51, 56, 60};

const int EERenderPlugin::ixTTEEVertical1[1381] = {42, 46, 51, 42, 46, 51, 42, 46, 51, 39, 42, 44, 46, 51, 38, 42, 43, 46, 51, 31, 34, 39, 43, 48, 51, 31, 33, 35, 39, 43, 44, 48, 50, 51, 29, 31, 35, 39, 40, 42, 43, 46, 47, 48, 51, 23, 26, 27, 31, 35, 36, 37, 38, 39, 43, 48, 51, 24, 26, 27, 31, 36, 39, 43, 48, 51, 24, 28, 31, 32, 36, 41, 43, 46, 51, 22, 24, 29, 31, 33, 36, 41, 44, 46, 47, 51, 22, 25, 29, 33, 36, 38, 41, 44, 47, 51, 19, 21, 26, 28, 29, 34, 37, 41, 44, 48, 50, 51, 18, 21, 26, 30, 33, 38, 41, 45, 47, 51, 16, 17, 22, 25, 27, 31, 36, 39, 42, 44, 48, 51, 16, 18, 22, 24, 27, 31, 32, 36, 38, 42, 44, 48, 49, 51, 15, 18, 23, 24, 28, 30, 32, 36, 39, 42, 45, 47, 48, 51, 21, 22, 26, 27, 29, 33, 35, 36, 39, 42, 45, 46, 48, 51, 21, 26, 29, 32, 36, 40, 42, 46, 48, 51, 14, 16, 20, 21, 25, 26, 30, 31, 33, 36, 37, 41, 43, 46, 48, 51, 12, 18, 19, 23, 24, 28, 29, 31, 34, 36, 38, 41, 44, 46, 49, 51, 10, 12, 18, 23, 28, 31, 35, 36, 38, 41, 44, 46, 49, 51, 11, 13, 17, 19, 22, 24, 27, 28, 31, 33, 34, 36, 39, 41, 44, 46, 49, 51, 11, 14, 16, 19, 21, 24, 26, 30, 31, 34, 36, 38, 41, 45, 46, 50, 51, 11, 15, 16, 20, 22, 25, 26, 29, 31, 34, 37, 39, 41, 42, 45, 47, 49, 51, 9, 11, 15, 18, 19, 22, 24, 27, 29, 31, 33, 37, 39, 41, 43, 45, 47, 49, 51, 9, 12, 14, 19, 23, 25, 28, 29, 31, 32, 36, 38, 39, 40, 41, 43, 45, 48, 49, 50, 51, 8, 13, 15, 19, 21, 22, 25, 28, 29, 31, 33, 36, 37, 39, 41, 43, 45, 47, 49, 51, 8, 13, 16, 18, 21, 26, 29, 31, 33, 36, 39, 41, 44, 45, 46, 49, 51, 8, 11, 16, 17, 21, 24, 28, 31, 35, 36, 37, 40, 41, 42, 44, 46, 48, 49, 51, 8, 11, 12, 16, 19, 20, 21, 24, 28, 29, 33, 34, 36, 38, 40, 41, 42, 44, 46, 48, 50, 51, 7, 11, 14, 15, 16, 20, 22, 25, 27, 28, 31, 33, 36, 38, 39, 41, 43, 44, 45, 46, 47, 49, 51, 7, 11, 14, 16, 20, 23, 24, 26, 28, 31, 32, 33, 36, 38, 40, 41, 42, 43, 46, 48, 51, 10, 11, 14, 16, 19, 23, 26, 28, 31, 35, 36, 39, 41, 46, 49, 51, 6, 9, 13, 18, 21, 26, 30, 31, 34, 37, 40, 41, 43, 46, 48, 51, 6, 10, 13, 14, 15, 18, 21, 22, 26, 28, 29, 32, 34, 38, 40, 41, 43, 45, 46, 48, 51, 5, 6, 9, 13, 16, 17, 18, 21, 24, 25, 26, 29, 33, 35, 38, 41, 42, 43, 45, 46, 49, 51, 6, 8, 11, 13, 16, 20, 21, 24, 28, 31, 33, 34, 36, 38, 41, 45, 46, 49, 51, 6, 9, 11, 13, 16, 21, 24, 29, 31, 35, 36, 39, 41, 44, 46, 6, 9, 13, 16, 21, 23, 26, 31, 34, 36, 38, 41, 43, 44, 6, 8, 13, 16, 20, 21, 23, 26, 27, 31, 33, 35, 36, 39, 41, 43, 5, 7, 12, 13, 16, 20, 22, 23, 26, 30, 31, 34, 38, 41, 42, 4, 8, 13, 15, 16, 18, 20, 23, 25, 26, 31, 33, 38, 40, 41, 4, 8, 13, 16, 19, 23, 26, 31, 34, 37, 41, 4, 6, 9, 11, 12, 16, 19, 23, 26, 30, 31, 34, 36, 40, 4, 6, 8, 11, 12, 14, 15, 16, 18, 23, 26, 28, 29, 31, 33, 34, 36, 40, 4, 8, 12, 15, 17, 22, 23, 26, 29, 34, 35, 36, 38, 40, 4, 8, 12, 15, 18, 23, 25, 26, 28, 32, 33, 34, 36, 40, 4, 7, 12, 14, 18, 23, 26, 29, 34, 36, 40, 4, 7, 12, 14, 18, 23, 26, 29, 34, 36, 40, 4, 8, 12, 15, 18, 23, 25, 26, 28, 32, 33, 34, 36, 40, 4, 8, 12, 15, 17, 22, 23, 26, 29, 34, 35, 36, 38, 40, 4, 6, 8, 11, 12, 14, 15, 16, 18, 23, 26, 28, 29, 31, 33, 34, 36, 40, 4, 6, 9, 11, 12, 16, 19, 23, 26, 30, 31, 34, 36, 40, 4, 8, 13, 16, 19, 23, 26, 31, 34, 37, 41, 4, 8, 13, 15, 16, 18, 20, 23, 25, 26, 31, 33, 38, 40, 41, 5, 7, 12, 13, 16, 20, 22, 23, 26, 30, 31, 34, 38, 42, 6, 8, 13, 16, 20, 21, 23, 26, 27, 31, 33, 35, 36, 39, 41, 43, 6, 9, 13, 16, 21, 23, 26, 31, 34, 36, 38, 41, 44, 6, 9, 11, 13, 16, 21, 24, 29, 31, 35, 36, 41, 44, 46, 6, 8, 11, 13, 16, 20, 21, 24, 28, 31, 33, 34, 36, 38, 41, 45, 46, 49, 51, 5, 6, 9, 13, 16, 17, 18, 21, 24, 25, 26, 29, 33, 35, 38, 40, 41, 42, 43, 45, 46, 49, 51, 6, 10, 13, 14, 15, 18, 21, 22, 26, 28, 29, 32, 34, 37, 39, 43, 45, 46, 48, 51, 6, 9, 13, 18, 21, 26, 30, 31, 34, 36, 39, 43, 46, 48, 51, 10, 11, 14, 16, 19, 23, 26, 28, 31, 36, 39, 41, 46, 49, 51, 7, 11, 14, 16, 20, 23, 24, 26, 28, 31, 32, 35, 36, 38, 40, 41, 42, 43, 46, 48, 51, 7, 11, 14, 15, 16, 20, 22, 25, 27, 28, 31, 33, 35, 36, 38, 39, 41, 43, 44, 45, 46, 47, 49, 51, 8, 11, 12, 16, 19, 20, 21, 24, 28, 29, 32, 34, 36, 38, 40, 41, 42, 44, 46, 48, 50, 51, 8, 11, 16, 17, 21, 24, 28, 32, 35, 36, 37, 40, 41, 42, 44, 46, 48, 49, 51, 8, 13, 16, 18, 21, 26, 31, 33, 36, 39, 41, 44, 45, 46, 49, 51, 8, 13, 15, 19, 21, 22, 25, 26, 31, 33, 36, 37, 39, 41, 43, 45, 47, 49, 51, 9, 12, 14, 19, 23, 25, 28, 31, 32, 36, 38, 39, 40, 41, 43, 45, 48, 49, 50, 51, 9, 11, 15, 18, 19, 22, 24, 28, 30, 31, 33, 37, 39, 41, 43, 45, 47, 49, 51, 11, 15, 16, 20, 22, 25, 27, 30, 31, 34, 37, 39, 41, 42, 45, 47, 49, 51, 11, 14, 16, 19, 21, 26, 30, 31, 34, 36, 38, 41, 45, 46, 50, 51, 11, 13, 17, 19, 22, 26, 27, 28, 31, 33, 34, 36, 39, 41, 44, 46, 49, 51, 10, 12, 18, 23, 24, 28, 31, 35, 36, 38, 41, 44, 46, 49, 51, 12, 18, 19, 22, 24, 28, 29, 31, 34, 36, 38, 41, 44, 46, 49, 51, 14, 16, 20, 22, 25, 26, 30, 31, 33, 36, 37, 41, 43, 46, 48, 51, 19, 21, 26, 29, 32, 36, 40, 42, 46, 48, 51, 19, 22, 26, 27, 29, 33, 35, 36, 39, 42, 45, 46, 48, 51, 15, 19, 23, 24, 28, 30, 32, 36, 39, 42, 45, 47, 48, 51, 16, 17, 22, 24, 27, 31, 32, 36, 38, 42, 44, 48, 49, 51, 16, 22, 25, 27, 31, 36, 39, 42, 44, 48, 51, 18, 21, 26, 30, 33, 38, 41, 45, 47, 51, 19, 21, 26, 28, 29, 34, 37, 41, 44, 48, 50, 51, 22, 25, 29, 33, 36, 38, 41, 44, 47, 51, 22, 24, 29, 31, 33, 36, 41, 44, 46, 47, 51, 24, 28, 31, 32, 36, 41, 43, 46, 51, 24, 26, 27, 31, 36, 39, 43, 48, 51, 23, 26, 27, 31, 35, 36, 37, 38, 39, 43, 48, 51, 29, 31, 35, 39, 40, 42, 43, 46, 47, 48, 51, 31, 33, 35, 39, 43, 44, 48, 50, 51, 31, 34, 39, 43, 48, 51, 38, 42, 43, 46, 51, 39, 42, 44, 46, 51, 42, 46, 51, 42, 46, 51, 42, 46, 51};

const int EERenderPlugin::ixTTEEVertical2[1385] = {56, 60, 61, 56, 60, 61, 56, 60, 61, 56, 58, 60, 63, 66, 56, 59, 60, 64, 66, 54, 59, 63, 68, 71, 76, 52, 54, 58, 59, 63, 67, 69, 71, 76, 54, 55, 56, 59, 60, 62, 63, 67, 71, 73, 76, 54, 59, 63, 64, 65, 66, 67, 71, 75, 76, 79, 81, 54, 59, 63, 66, 71, 75, 76, 78, 81, 56, 59, 61, 66, 70, 71, 74, 78, 81, 55, 56, 58, 61, 66, 69, 71, 73, 78, 80, 81, 55, 58, 61, 64, 66, 69, 73, 77, 80, 81, 52, 54, 58, 61, 65, 68, 73, 74, 76, 81, 83, 86, 55, 57, 61, 64, 69, 72, 76, 81, 84, 86, 54, 58, 60, 63, 66, 71, 75, 77, 80, 86, 88, 53, 54, 58, 60, 64, 66, 70, 71, 75, 78, 80, 85, 86, 88, 54, 55, 57, 60, 63, 66, 70, 72, 74, 78, 79, 83, 87, 88, 54, 56, 57, 60, 63, 66, 67, 69, 73, 75, 76, 80, 83, 88, 54, 56, 60, 62, 66, 70, 73, 76, 81, 83, 88, 54, 56, 59, 61, 65, 66, 69, 71, 72, 76, 77, 80, 82, 86, 88, 93, 53, 56, 58, 61, 64, 66, 68, 71, 73, 74, 78, 80, 83, 84, 90, 93, 53, 56, 58, 61, 64, 66, 67, 71, 74, 78, 79, 84, 90, 92, 93, 53, 56, 58, 61, 63, 66, 68, 69, 71, 74, 75, 76, 80, 83, 85, 89, 91, 93, 52, 56, 57, 61, 64, 66, 68, 71, 72, 76, 81, 83, 86, 88, 91, 93, 53, 55, 57, 60, 61, 63, 65, 68, 71, 72, 75, 77, 80, 82, 86, 87, 91, 96, 53, 55, 57, 59, 61, 63, 65, 69, 71, 72, 74, 78, 80, 83, 84, 87, 91, 93, 96, 52, 53, 54, 57, 59, 61, 62, 63, 64, 66, 70, 71, 74, 77, 79, 83, 88, 90, 93, 96, 53, 55, 57, 59, 61, 63, 65, 66, 69, 71, 76, 77, 80, 81, 83, 87, 89, 94, 96, 53, 56, 57, 58, 61, 63, 66, 69, 71, 76, 81, 84, 86, 89, 94, 96, 53, 54, 56, 58, 60, 61, 62, 65, 66, 67, 70, 74, 78, 81, 85, 86, 91, 94, 96, 52, 54, 56, 58, 60, 61, 62, 64, 66, 68, 70, 73, 74, 78, 81, 82, 83, 86, 90, 91, 94, 96, 53, 55, 56, 57, 58, 59, 61, 63, 64, 66, 67, 69, 71, 74, 75, 77, 80, 82, 86, 87, 88, 91, 95, 96, 54, 56, 59, 60, 61, 62, 64, 66, 67, 70, 71, 74, 76, 78, 79, 82, 86, 88, 91, 95, 96, 53, 56, 61, 63, 66, 71, 74, 76, 79, 83, 86, 88, 91, 92, 96, 54, 56, 59, 63, 66, 68, 71, 72, 76, 81, 84, 89, 93, 96, 98, 54, 56, 57, 59, 63, 65, 68, 70, 73, 74, 76, 80, 81, 84, 87, 88, 89, 92, 96, 98, 53, 56, 57, 59, 60, 61, 62, 64, 67, 69, 73, 76, 77, 78, 81, 84, 85, 86, 89, 93, 96, 97, 98, 53, 56, 57, 61, 64, 66, 68, 69, 71, 74, 78, 81, 82, 86, 89, 91, 94, 96, 98, 58, 61, 66, 67, 71, 73, 78, 81, 86, 89, 91, 93, 96, 98, 61, 64, 66, 68, 71, 76, 79, 81, 86, 89, 93, 96, 101, 61, 63, 66, 67, 69, 71, 75, 76, 79, 81, 82, 86, 89, 94, 96, 101, 64, 68, 71, 72, 76, 79, 80, 82, 86, 89, 90, 95, 97, 101, 62, 64, 69, 71, 76, 77, 79, 82, 84, 86, 87, 89, 94, 98, 101, 65, 68, 71, 76, 79, 83, 86, 89, 94, 98, 101, 66, 68, 71, 72, 76, 79, 83, 86, 90, 91, 93, 96, 98, 101, 66, 68, 69, 71, 73, 74, 76, 79, 84, 86, 87, 88, 90, 91, 94, 96, 98, 101, 64, 66, 67, 68, 73, 76, 79, 80, 85, 87, 90, 94, 98, 101, 66, 68, 69, 70, 74, 76, 77, 79, 84, 87, 90, 94, 98, 101, 66, 68, 73, 76, 79, 84, 88, 90, 95, 98, 101, 66, 68, 73, 76, 79, 84, 88, 90, 95, 98, 101, 66, 68, 69, 70, 74, 76, 77, 79, 84, 87, 90, 94, 98, 101, 64, 66, 67, 68, 73, 76, 79, 80, 85, 87, 90, 94, 98, 101, 66, 68, 69, 71, 73, 74, 76, 79, 84, 86, 87, 88, 90, 91, 94, 96, 98, 101, 66, 68, 71, 72, 76, 79, 83, 86, 90, 91, 93, 96, 98, 101, 65, 68, 71, 76, 79, 83, 86, 89, 94, 98, 101, 62, 64, 69, 71, 76, 77, 79, 82, 84, 86, 87, 89, 94, 98, 101, 61, 64, 68, 71, 72, 76, 79, 80, 82, 86, 89, 90, 95, 97, 101, 61, 63, 66, 67, 69, 71, 75, 76, 79, 81, 82, 86, 89, 94, 96, 101, 59, 61, 64, 66, 68, 71, 76, 79, 81, 86, 89, 93, 96, 100, 58, 61, 63, 66, 67, 71, 73, 78, 81, 86, 89, 91, 93, 96, 98, 53, 56, 57, 61, 64, 66, 68, 69, 71, 74, 78, 81, 82, 86, 89, 91, 94, 96, 98, 53, 56, 57, 59, 60, 61, 64, 67, 69, 73, 76, 77, 78, 81, 84, 85, 86, 89, 93, 96, 97, 98, 54, 56, 57, 59, 61, 62, 64, 68, 70, 73, 74, 76, 80, 81, 84, 87, 88, 89, 92, 96, 98, 54, 56, 59, 61, 62, 65, 68, 71, 72, 76, 81, 84, 89, 93, 96, 98, 53, 56, 61, 63, 66, 67, 71, 74, 76, 79, 83, 86, 88, 91, 92, 96, 54, 56, 59, 60, 61, 62, 64, 66, 69, 70, 71, 74, 76, 78, 79, 82, 86, 88, 91, 95, 96, 53, 55, 56, 57, 58, 59, 61, 63, 64, 66, 69, 71, 74, 75, 77, 80, 82, 86, 87, 88, 91, 95, 96, 52, 54, 56, 58, 60, 61, 62, 64, 66, 68, 69, 73, 74, 78, 81, 82, 83, 86, 90, 91, 94, 96, 53, 54, 56, 58, 60, 61, 62, 65, 66, 67, 71, 74, 78, 81, 85, 86, 91, 94, 96, 53, 56, 57, 58, 61, 63, 66, 69, 71, 73, 76, 81, 84, 86, 89, 94, 96, 53, 55, 57, 59, 61, 63, 65, 66, 69, 71, 73, 74, 77, 80, 81, 83, 87, 89, 94, 96, 52, 53, 54, 57, 59, 61, 62, 63, 64, 66, 70, 71, 73, 74, 77, 79, 83, 88, 90, 93, 96, 53, 55, 57, 59, 61, 63, 65, 69, 71, 73, 75, 78, 80, 83, 84, 87, 91, 93, 96, 53, 55, 57, 60, 61, 63, 65, 68, 71, 73, 76, 77, 80, 82, 86, 87, 91, 96, 52, 56, 57, 61, 64, 66, 68, 71, 72, 76, 78, 81, 83, 86, 88, 91, 93, 53, 56, 58, 61, 63, 66, 68, 69, 71, 74, 75, 78, 80, 83, 85, 89, 91, 93, 53, 56, 58, 61, 64, 66, 67, 71, 74, 79, 84, 90, 92, 93, 53, 56, 58, 61, 64, 66, 68, 71, 73, 74, 78, 79, 83, 84, 90, 93, 54, 56, 59, 61, 65, 66, 69, 71, 72, 76, 77, 81, 82, 86, 88, 93, 54, 56, 60, 62, 66, 70, 73, 76, 81, 88, 54, 56, 57, 60, 63, 66, 67, 69, 73, 75, 76, 80, 81, 86, 87, 88, 54, 55, 57, 60, 63, 66, 70, 72, 74, 78, 79, 84, 87, 88, 53, 54, 58, 60, 64, 66, 70, 71, 75, 78, 80, 84, 86, 88, 54, 58, 60, 63, 66, 71, 75, 77, 80, 85, 87, 88, 55, 57, 61, 64, 69, 72, 76, 81, 82, 83, 84, 85, 86, 52, 54, 58, 61, 65, 68, 73, 74, 76, 81, 83, 86, 55, 58, 61, 64, 66, 69, 73, 77, 80, 81, 55, 56, 58, 61, 66, 69, 71, 73, 78, 80, 81, 56, 59, 61, 66, 70, 71, 74, 78, 81, 54, 59, 63, 66, 71, 75, 76, 78, 81, 54, 59, 63, 64, 65, 66, 67, 71, 75, 76, 79, 81, 54, 55, 56, 59, 60, 62, 63, 67, 71, 73, 76, 52, 54, 58, 59, 63, 67, 69, 71, 76, 54, 59, 63, 68, 71, 76, 56, 59, 60, 64, 66, 56, 58, 60, 63, 66, 56, 60, 61, 56, 60, 61, 56, 60};

const int EERenderPlugin::iyTTEEVertical1[1381] = {1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 86, 86, 86, 86, 86, 86, 86, 86, 86, 86, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 90, 90, 90, 90, 90, 90, 90, 90, 90, 91, 91, 91, 91, 91, 91, 91, 91, 91, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 94, 94, 94, 94, 94, 94, 94, 94, 94, 95, 95, 95, 95, 95, 95, 96, 96, 96, 96, 96, 97, 97, 97, 97, 97, 98, 98, 98, 99, 99, 99, 100, 100, 100};

const int EERenderPlugin::iyTTEEVertical2[1385] = {1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 58, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 76, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 79, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 82, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 84, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 86, 86, 86, 86, 86, 86, 86, 86, 86, 86, 86, 86, 86, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 87, 88, 88, 88, 88, 88, 88, 88, 88, 88, 88, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 89, 90, 90, 90, 90, 90, 90, 90, 90, 90, 91, 91, 91, 91, 91, 91, 91, 91, 91, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 93, 94, 94, 94, 94, 94, 94, 94, 94, 94, 95, 95, 95, 95, 95, 95, 96, 96, 96, 96, 96, 97, 97, 97, 97, 97, 98, 98, 98, 99, 99, 99, 100, 100};


const int EERenderPlugin::ixTCCEEHorizontal[699]={1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 26, 26, 26, 26, 26, 26, 26, 26, 26, 27, 27, 27, 27, 27, 27, 27, 27, 27, 28, 28, 28, 28, 28, 28, 28, 28, 28, 29, 29, 29, 29, 29, 29, 29, 29, 29, 30, 30, 30, 30, 30, 30, 30, 30, 30, 31, 31, 31, 31, 31, 31, 31, 31, 31, 32, 32, 32, 32, 32, 32, 32, 32, 32, 33, 33, 33, 33, 33, 33, 33, 33, 33, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 41, 41, 41, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 42, 42, 42, 43, 43, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 44, 45, 45, 45, 45, 45, 45, 46, 46, 46, 46, 47, 47, 47, 47, 48, 48, 48, 48, 49, 49, 49, 49, 50, 50, 50, 50, 51, 51, 51, 51, 52, 52, 52, 52, 53, 53, 53, 53, 54, 54, 54, 54, 55, 55, 55, 55, 56, 56, 56, 56, 56, 56, 57, 57, 57, 57, 57, 57, 58, 58, 58, 58, 58, 58, 58, 59, 59, 59, 59, 59, 59, 59, 59, 60, 60, 60, 60, 60, 60, 60, 60, 61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 68, 68, 68, 68, 68, 68, 68, 68, 68, 69, 69, 69, 69, 69, 69, 69, 69, 69, 70, 70, 70, 70, 70, 70, 70, 70, 70, 71, 71, 71, 71, 71, 71, 71, 71, 71, 72, 72, 72, 72, 72, 72, 72, 72, 72, 73, 73, 73, 73, 73, 73, 73, 73, 73, 74, 74, 74, 74, 74, 74, 74, 74, 74, 75, 75, 75, 75, 75, 75, 75, 75, 75, 76, 76, 76, 76, 76, 76, 76, 76, 76, 77, 77, 77, 77, 77, 77, 77, 77, 77, 78, 78, 78, 78, 78, 78, 78, 78, 78, 79, 79, 79, 79, 79, 79, 79, 79, 79, 80, 80, 80, 80, 80, 80, 80, 80, 80, 81, 81, 81, 81, 81, 82, 82, 82, 82, 82, 82, 82, 83, 83, 83, 83, 83, 83, 83, 84, 84, 84, 84, 84, 84, 84, 85, 85, 85, 85, 85, 85, 85, 86, 86, 86, 86, 86, 86, 86, 87, 87, 87, 87, 87, 87, 87, 88, 88, 88, 88, 88, 89, 89, 89, 89, 89, 90, 90, 90, 90, 90, 91, 91, 91, 91, 91, 92, 92, 92, 92, 92, 93, 93, 93, 94, 94, 94, 95, 95, 95, 96, 96, 96, 97, 97, 97, 98, 98, 98, 99, 99, 99, 100, 100};

const int EERenderPlugin::iyTCCEEHorizontal[699]={42, 60, 61, 42, 60, 61, 42, 60, 61, 42, 60, 66, 42, 60, 66, 43, 59, 76, 43, 59, 76, 43, 59, 76, 26, 43, 59, 76, 81, 26, 43, 59, 76, 81, 28, 43, 59, 74, 81, 29, 44, 58, 73, 81, 29, 44, 58, 73, 81, 29, 44, 50, 52, 58, 73, 86, 30, 45, 47, 55, 57, 72, 86, 31, 39, 44, 58, 63, 71, 88, 32, 38, 44, 58, 64, 70, 88, 32, 36, 45, 57, 66, 70, 88, 33, 35, 46, 56, 67, 69, 88, 32, 46, 56, 70, 88, 16, 30, 33, 46, 56, 69, 72, 86, 93, 18, 29, 34, 46, 56, 68, 73, 84, 93, 18, 28, 36, 46, 56, 66, 74, 84, 93, 19, 27, 36, 46, 56, 66, 75, 83, 93, 19, 26, 36, 46, 56, 66, 76, 83, 93, 22, 25, 37, 47, 55, 65, 77, 80, 96, 22, 24, 37, 47, 55, 65, 78, 80, 96, 23, 25, 38, 48, 54, 64, 77, 79, 96, 22, 25, 39, 47, 55, 63, 77, 80, 96, 21, 26, 39, 46, 56, 63, 76, 81, 96, 21, 28, 41, 48, 54, 61, 74, 81, 96, 20, 29, 41, 48, 54, 61, 73, 82, 96, 20, 31, 41, 47, 55, 61, 71, 82, 96, 7, 20, 31, 41, 48, 54, 61, 71, 82, 95, 96, 10, 19, 31, 41, 49, 53, 61, 71, 83, 92, 96, 13, 18, 34, 43, 48, 54, 59, 68, 84, 89, 98, 13, 14, 15, 18, 34, 43, 48, 54, 59, 68, 84, 87, 88, 89, 98, 16, 17, 18, 35, 45, 49, 53, 57, 67, 84, 85, 86, 98, 16, 20, 36, 45, 49, 53, 57, 64, 82, 86, 98, 16, 21, 36, 44, 46, 58, 63, 81, 86, 98, 16, 26, 41, 44, 61, 76, 86, 101, 16, 27, 41, 43, 61, 75, 86, 101, 16, 30, 42, 61, 72, 86, 101, 16, 33, 41, 69, 86, 101, 16, 34, 41, 68, 86, 101, 16, 40, 86, 101, 15, 40, 87, 101, 15, 40, 87, 101, 15, 40, 87, 101, 14, 40, 88, 101, 14, 40, 88, 101, 15, 40, 87, 101, 15, 40, 87, 101, 15, 40, 87, 101, 16, 40, 86, 101, 16, 34, 41, 68, 86, 101, 16, 33, 41, 69, 86, 101, 16, 30, 41, 42, 72, 86, 101, 16, 27, 41, 43, 61, 75, 86, 101, 16, 26, 41, 44, 61, 76, 86, 101, 16, 21, 39, 44, 46, 58, 66, 81, 86, 98, 16, 20, 38, 45, 49, 53, 57, 66, 82, 86, 98, 16, 17, 18, 35, 45, 49, 53, 57, 67, 84, 85, 86, 98, 13, 14, 15, 18, 34, 43, 48, 54, 59, 68, 84, 87, 88, 89, 98, 13, 18, 34, 43, 48, 54, 59, 68, 84, 89, 98, 10, 19, 31, 41, 49, 53, 61, 71, 83, 92, 96, 7, 20, 31, 41, 48, 54, 61, 71, 82, 95, 96, 20, 31, 41, 47, 55, 61, 71, 82, 96, 20, 29, 41, 48, 54, 61, 73, 82, 96, 21, 28, 41, 48, 54, 61, 74, 81, 96, 21, 26, 39, 46, 56, 63, 76, 81, 96, 22, 25, 39, 47, 55, 63, 77, 80, 96, 23, 25, 38, 48, 54, 64, 77, 79, 96, 22, 24, 37, 47, 55, 65, 78, 80, 96, 22, 25, 37, 47, 55, 65, 77, 80, 96, 19, 26, 36, 46, 56, 66, 76, 83, 93, 19, 27, 36, 46, 56, 66, 75, 83, 93, 18, 28, 36, 46, 56, 66, 74, 84, 93, 18, 29, 34, 46, 56, 68, 73, 84, 93, 16, 30, 33, 46, 56, 69, 72, 86, 93, 32, 46, 56, 70, 88, 33, 35, 46, 56, 67, 69, 88, 32, 36, 45, 57, 66, 70, 88, 32, 38, 44, 58, 64, 70, 88, 31, 39, 44, 58, 63, 71, 88, 30, 45, 47, 55, 57, 72, 86, 29, 44, 50, 52, 58, 73, 86, 29, 44, 58, 73, 81, 29, 44, 58, 73, 81, 28, 43, 59, 74, 81, 26, 43, 59, 76, 81, 26, 43, 59, 76, 81, 43, 59, 76, 43, 59, 76, 43, 59, 76, 42, 60, 66, 42, 60, 66, 42, 60, 61, 42, 60, 61, 42, 60};

const int EERenderPlugin::ixTCCEEVertical[729]={51, 61, 51, 61, 51, 61, 51, 66, 51, 66, 34, 51, 68, 76, 35, 51, 67, 76, 35, 51, 67, 76, 35, 51, 67, 81, 36, 51, 66, 81, 36, 51, 66, 81, 36, 51, 66, 81, 38, 51, 64, 81, 21, 37, 50, 51, 52, 65, 81, 86, 21, 38, 47, 51, 55, 64, 81, 86, 22, 39, 51, 63, 80, 88, 22, 38, 51, 64, 80, 88, 24, 36, 39, 51, 63, 66, 78, 88, 26, 35, 39, 51, 63, 67, 76, 88, 26, 32, 40, 51, 62, 70, 76, 88, 26, 30, 41, 51, 61, 72, 76, 93, 28, 29, 41, 51, 61, 73, 74, 93, 28, 41, 51, 61, 74, 93, 27, 28, 41, 51, 61, 74, 75, 93, 26, 30, 41, 51, 61, 72, 76, 93, 11, 25, 31, 42, 51, 60, 71, 77, 91, 96, 11, 24, 31, 43, 51, 59, 71, 78, 91, 96, 12, 23, 32, 43, 51, 59, 70, 79, 90, 96, 15, 22, 33, 43, 51, 59, 69, 80, 87, 96, 16, 21, 33, 44, 51, 58, 69, 81, 86, 96, 17, 21, 36, 44, 51, 58, 66, 81, 85, 96, 19, 20, 21, 36, 44, 51, 58, 66, 81, 82, 83, 96, 20, 22, 36, 45, 51, 57, 66, 80, 82, 96, 20, 23, 38, 46, 51, 56, 64, 79, 82, 96, 19, 23, 39, 46, 51, 56, 63, 79, 83, 96, 18, 26, 41, 46, 51, 56, 63, 76, 84, 98, 18, 28, 41, 46, 51, 56, 63, 74, 84, 98, 17, 29, 41, 46, 51, 56, 62, 73, 85, 98, 16, 31, 41, 46, 51, 56, 61, 71, 86, 98, 16, 31, 41, 46, 61, 71, 86, 98, 16, 36, 43, 44, 66, 86, 101, 6, 16, 36, 43, 66, 86, 96, 101, 12, 16, 38, 42, 64, 86, 90, 101, 15, 16, 18, 38, 40, 41, 62, 64, 84, 86, 87, 101, 16, 19, 41, 83, 86, 101, 16, 26, 30, 31, 40, 71, 72, 76, 86, 101, 15, 28, 29, 31, 33, 34, 40, 68, 69, 71, 73, 74, 87, 101, 15, 35, 36, 38, 40, 64, 66, 67, 87, 101, 15, 40, 87, 101, 14, 40, 88, 101, 14, 40, 88, 101, 15, 40, 87, 101, 15, 35, 36, 38, 40, 64, 66, 67, 87, 101, 15, 28, 29, 31, 33, 34, 40, 68, 69, 71, 73, 74, 87, 101, 16, 26, 30, 31, 40, 71, 72, 76, 86, 101, 16, 19, 41, 83, 86, 101, 15, 16, 18, 38, 40, 41, 62, 64, 84, 86, 87, 101, 12, 16, 38, 42, 64, 86, 90, 101, 6, 16, 36, 43, 66, 86, 96, 101, 16, 36, 44, 59, 66, 86, 100, 16, 31, 41, 46, 61, 71, 86, 98, 16, 31, 41, 46, 51, 56, 61, 71, 86, 98, 17, 29, 40, 46, 51, 56, 61, 73, 85, 98, 18, 28, 39, 46, 51, 56, 61, 74, 84, 98, 18, 26, 39, 46, 51, 56, 61, 76, 84, 98, 19, 23, 39, 46, 51, 56, 63, 79, 83, 96, 20, 23, 38, 46, 51, 56, 64, 79, 82, 96, 20, 22, 36, 45, 51, 57, 66, 80, 82, 96, 19, 20, 21, 36, 44, 51, 58, 66, 81, 82, 83, 96, 17, 21, 36, 44, 51, 58, 66, 81, 85, 96, 16, 21, 33, 44, 51, 58, 69, 81, 86, 96, 15, 22, 33, 43, 51, 59, 69, 80, 87, 96, 12, 23, 32, 43, 51, 59, 70, 79, 90, 96, 11, 24, 31, 43, 51, 59, 71, 78, 91, 96, 11, 25, 31, 42, 51, 60, 71, 77, 91, 96, 26, 30, 41, 51, 61, 72, 76, 93, 27, 28, 41, 51, 61, 74, 75, 93, 28, 41, 51, 61, 74, 93, 28, 29, 41, 51, 61, 73, 74, 93, 26, 30, 41, 51, 61, 72, 76, 93, 26, 32, 40, 51, 62, 70, 76, 88, 26, 35, 39, 51, 63, 67, 76, 88, 24, 36, 39, 51, 63, 66, 78, 88, 22, 38, 51, 64, 80, 88, 22, 39, 51, 63, 80, 88, 21, 38, 47, 51, 55, 64, 81, 86, 21, 37, 50, 51, 52, 65, 81, 86, 38, 51, 64, 81, 36, 51, 66, 81, 36, 51, 66, 81, 36, 51, 66, 81, 35, 51, 67, 81, 35, 51, 67, 76, 35, 51, 67, 76, 34, 51, 68, 76, 51, 66, 51, 66, 51, 61, 51, 61, 51};

const int EERenderPlugin::iyTCCEEVertical[729]={1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 40, 40, 40, 40, 40, 40, 40, 40, 41, 41, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 42, 42, 42, 43, 43, 43, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 45, 45, 45, 45, 45, 45, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 49, 49, 49, 49, 50, 50, 50, 50, 51, 51, 51, 51, 52, 52, 52, 52, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 56, 56, 56, 56, 56, 56, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 57, 58, 58, 58, 58, 58, 58, 58, 58, 59, 59, 59, 59, 59, 59, 59, 59, 60, 60, 60, 60, 60, 60, 60, 61, 61, 61, 61, 61, 61, 61, 61, 62, 62, 62, 62, 62, 62, 62, 62, 62, 62, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 68, 68, 68, 68, 68, 68, 68, 68, 68, 68, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 71, 71, 71, 71, 71, 71, 71, 71, 71, 71, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 73, 73, 73, 73, 73, 73, 73, 73, 73, 73, 74, 74, 74, 74, 74, 74, 74, 74, 74, 74, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 76, 76, 76, 76, 76, 76, 76, 76, 77, 77, 77, 77, 77, 77, 77, 77, 78, 78, 78, 78, 78, 78, 79, 79, 79, 79, 79, 79, 79, 79, 80, 80, 80, 80, 80, 80, 80, 80, 81, 81, 81, 81, 81, 81, 81, 81, 82, 82, 82, 82, 82, 82, 82, 82, 83, 83, 83, 83, 83, 83, 83, 83, 84, 84, 84, 84, 84, 84, 85, 85, 85, 85, 85, 85, 86, 86, 86, 86, 86, 86, 86, 86, 87, 87, 87, 87, 87, 87, 87, 87, 88, 88, 88, 88, 89, 89, 89, 89, 90, 90, 90, 90, 91, 91, 91, 91, 92, 92, 92, 92, 93, 93, 93, 93, 94, 94, 94, 94, 95, 95, 95, 95, 96, 96, 97, 97, 98, 98, 99, 99, 100};


const int EERenderPlugin::ixLabels[720]={99, 99, 97, 97, 95, 94, 92, 91, 87, 84, 79, 77, 74, 69, 64, 61, 58, 54, 47, 43, 40, 37, 32, 27, 24, 22, 17, 14, 10, 9, 7, 6, 4, 4, 2, 2, 2, 2, 4, 4, 6, 7, 9, 10, 14, 17, 22, 24, 27, 32, 37, 40, 43, 47, 54, 58, 61, 64, 69, 74, 77, 79, 84, 87, 91, 92, 94, 95, 97, 97, 99, 99, 96, 96, 94, 94, 92, 91, 89, 87, 84, 82, 78, 75, 72, 69, 65, 61, 57, 52, 49, 44, 40, 36, 32, 29, 26, 23, 19, 16, 14, 12, 10, 9, 7, 7, 5, 5, 5, 5, 7, 7, 9, 10, 12, 14, 16, 19, 23, 26, 29, 32, 36, 40, 44, 49, 52, 57, 61, 65, 69, 72, 75, 78, 82, 85, 87, 89, 91, 92, 94, 94, 96, 96, 92, 92, 91, 90, 89, 87, 85, 84, 81, 78, 76, 73, 70, 67, 64, 60, 57, 52, 49, 44, 41, 37, 34, 31, 28, 25, 23, 20, 17, 16, 14, 12, 11, 10, 9, 9, 9, 9, 10, 11, 12, 14, 16, 17, 20, 23, 25, 28, 31, 34, 37, 41, 44, 49, 52, 57, 60, 64, 67, 70, 73, 76, 78, 81, 84, 85, 87, 89, 90, 91, 92, 92, 88, 87, 87, 87, 87, 84, 82, 81, 79, 76, 74, 71, 68, 66, 62, 59, 56, 53, 48, 45, 42, 39, 35, 33, 30, 27, 25, 23, 20, 19, 17, 14, 14, 14, 14, 13, 13, 14, 14, 14, 14, 17, 19, 20, 22, 25, 27, 30, 33, 35, 39, 42, 45, 48, 53, 56, 59, 62, 66, 68, 71, 74, 76, 78, 81, 82, 84, 87, 87, 87, 87, 88, 85, 84, 83, 84, 82, 80, 79, 78, 75, 74, 72, 69, 67, 64, 61, 58, 56, 52, 49, 45, 43, 40, 37, 34, 32, 29, 28, 26, 23, 22, 21, 19, 17, 18, 17, 16, 16, 17, 18, 17, 19, 21, 22, 23, 26, 27, 29, 32, 34, 37, 40, 43, 45, 49, 52, 56, 58, 61, 64, 67, 69, 72, 73, 75, 78, 79, 80, 82, 84, 83, 84, 85, 82, 80, 80, 80, 79, 78, 77, 76, 74, 72, 69, 67, 64, 62, 59, 57, 54, 52, 49, 47, 44, 42, 39, 37, 34, 32, 29, 27, 25, 24, 23, 22, 21, 21, 21, 19, 19, 21, 21, 21, 22, 23, 24, 25, 27, 29, 32, 34, 37, 39, 42, 44, 47, 49, 52, 54, 57, 59, 62, 64, 67, 69, 72, 74, 76, 77, 78, 79, 80, 80, 80, 82, 77, 77, 77, 77, 76, 74, 74, 72, 71, 69, 67, 66, 64, 62, 59, 57, 54, 52, 49, 47, 44, 42, 39, 37, 35, 34, 32, 30, 29, 27, 27, 25, 24, 24, 24, 24, 24, 24, 24, 24, 25, 27, 27, 29, 30, 32, 34, 35, 37, 39, 42, 44, 47, 49, 52, 54, 57, 59, 62, 64, 66, 67, 69, 71, 72, 74, 74, 76, 77, 77, 77, 77, 74, 74, 74, 74, 72, 72, 71, 69, 69, 67, 65, 64, 62, 59, 58, 55, 54, 52, 49, 47, 46, 43, 42, 39, 37, 36, 34, 33, 32, 30, 29, 29, 27, 27, 27, 27, 27, 27, 27, 27, 29, 29, 30, 32, 32, 34, 36, 37, 39, 42, 43, 46, 47, 49, 52, 54, 55, 58, 59, 62, 64, 65, 67, 68, 69, 71, 72, 72, 74, 74, 74, 74, 71, 71, 69, 69, 69, 69, 69, 67, 66, 64, 62, 62, 60, 59, 57, 55, 54, 52, 49, 47, 46, 44, 42, 41, 39, 39, 37, 35, 34, 32, 32, 32, 32, 32, 30, 30, 30, 30, 32, 32, 32, 32, 32, 34, 35, 37, 39, 39, 41, 42, 44, 46, 47, 49, 52, 54, 55, 57, 59, 60, 62, 62, 64, 66, 67, 69, 69, 69, 69, 69, 71, 71, 67, 67, 66, 64, 62, 60, 57, 54, 52, 49, 47, 44, 41, 39, 37, 35, 34, 34, 34, 34, 35, 37, 39, 41, 44, 47, 49, 52, 54, 57, 60, 62, 64, 66, 67, 67, 64, 63, 62, 62, 60, 59, 56, 54, 52, 49, 47, 45, 42, 42, 39, 39, 38, 37, 37, 38, 39, 39, 41, 42, 45, 47, 49, 52, 54, 56, 59, 59, 62, 62, 63, 64};

const int EERenderPlugin::iyLabels[720]={54, 58, 61, 64, 69, 74, 77, 79, 84, 87, 91, 92, 94, 95, 97, 97, 99, 99, 99, 99, 97, 96, 94, 94, 91, 91, 86, 84, 79, 77, 74, 69, 64, 61, 57, 52, 47, 43, 40, 37, 32, 27, 24, 22, 17, 14, 10, 9, 7, 6, 4, 4, 2, 2, 2, 2, 4, 5, 7, 7, 10, 10, 15, 17, 22, 24, 27, 32, 37, 40, 44, 49, 52, 57, 61, 65, 69, 72, 75, 78, 81, 84, 87, 89, 91, 92, 94, 94, 96, 96, 96, 95, 94, 94, 92, 91, 89, 86, 85, 82, 78, 75, 72, 68, 64, 60, 57, 52, 49, 44, 40, 36, 32, 29, 26, 23, 19, 16, 14, 12, 10, 9, 7, 7, 5, 5, 5, 6, 7, 7, 9, 10, 12, 15, 16, 19, 23, 26, 29, 33, 37, 41, 44, 49, 52, 57, 60, 64, 67, 70, 73, 76, 78, 81, 84, 85, 87, 89, 90, 91, 92, 92, 91, 91, 91, 90, 89, 87, 85, 84, 81, 78, 76, 73, 70, 67, 64, 60, 57, 52, 49, 44, 41, 37, 34, 31, 28, 25, 23, 20, 17, 16, 14, 12, 11, 10, 9, 9, 10, 10, 10, 11, 12, 14, 16, 17, 20, 23, 25, 28, 31, 34, 37, 41, 44, 49, 53, 56, 59, 62, 66, 68, 71, 74, 76, 78, 81, 82, 84, 87, 87, 87, 87, 88, 88, 87, 87, 87, 86, 84, 82, 81, 78, 76, 74, 71, 67, 65, 62, 59, 56, 52, 48, 45, 42, 39, 35, 33, 30, 27, 25, 23, 20, 19, 17, 14, 14, 14, 14, 13, 13, 14, 14, 14, 15, 17, 19, 20, 23, 25, 27, 30, 34, 36, 39, 42, 45, 49, 52, 56, 58, 61, 64, 67, 69, 72, 73, 75, 78, 79, 80, 82, 84, 83, 84, 85, 85, 84, 83, 83, 82, 80, 79, 78, 75, 74, 72, 69, 67, 64, 61, 58, 55, 52, 49, 45, 43, 40, 37, 34, 32, 29, 28, 26, 23, 22, 21, 19, 17, 18, 17, 16, 16, 17, 18, 18, 19, 21, 22, 23, 26, 27, 29, 32, 34, 37, 40, 43, 46, 49, 52, 54, 57, 59, 62, 64, 67, 69, 71, 74, 76, 77, 78, 79, 80, 80, 80, 82, 81, 80, 80, 79, 79, 77, 77, 75, 73, 71, 69, 66, 64, 62, 59, 57, 54, 52, 49, 47, 44, 42, 39, 37, 34, 32, 30, 27, 25, 24, 23, 22, 21, 21, 21, 19, 20, 21, 21, 22, 22, 24, 24, 26, 28, 30, 32, 35, 37, 39, 42, 44, 47, 49, 52, 54, 57, 59, 62, 64, 66, 67, 69, 71, 72, 74, 74, 76, 77, 77, 77, 77, 77, 77, 77, 77, 75, 74, 74, 72, 70, 69, 67, 66, 63, 62, 59, 56, 54, 51, 49, 47, 44, 42, 39, 37, 35, 34, 32, 30, 29, 27, 27, 25, 24, 24, 24, 24, 24, 24, 24, 24, 26, 27, 27, 29, 31, 32, 34, 35, 38, 39, 42, 45, 47, 50, 52, 54, 55, 58, 59, 62, 64, 65, 67, 68, 69, 71, 72, 72, 74, 74, 74, 74, 74, 74, 73, 74, 72, 72, 71, 69, 69, 67, 64, 63, 61, 59, 58, 55, 53, 51, 49, 47, 46, 43, 42, 39, 37, 36, 34, 33, 32, 30, 29, 29, 27, 27, 27, 27, 27, 27, 28, 27, 29, 29, 30, 32, 32, 34, 37, 38, 40, 42, 43, 46, 48, 50, 52, 54, 55, 57, 59, 60, 61, 62, 64, 66, 67, 68, 69, 69, 69, 69, 71, 71, 71, 71, 69, 69, 69, 68, 68, 67, 65, 64, 62, 61, 60, 58, 56, 54, 54, 51, 49, 47, 46, 44, 42, 41, 40, 39, 37, 35, 34, 33, 32, 32, 32, 32, 30, 30, 30, 30, 32, 32, 32, 33, 33, 34, 36, 37, 39, 40, 41, 43, 45, 47, 47, 50, 52, 54, 57, 60, 62, 64, 66, 67, 67, 66, 66, 66, 64, 62, 59, 57, 54, 52, 49, 47, 44, 41, 39, 37, 35, 34, 34, 35, 35, 35, 37, 39, 42, 44, 47, 49, 52, 54, 56, 59, 59, 62, 62, 63, 64, 64, 63, 62, 62, 59, 59, 56, 54, 52, 49, 47, 45, 42, 42, 39, 39, 38, 37, 37, 38, 39, 39, 42, 42, 45, 47, 49};

const int EERenderPlugin::bincontentLabels[720]={3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 11, 12, 9, 10, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 15, 16, 13, 14, 19, 20, 17, 18, 19, 20, 17, 18, 19, 20, 17, 18, 19, 20, 17, 18, 19, 20, 17, 18, 19, 20, 17, 18, 19, 20, 17, 18, 19, 20, 17, 18, 19, 20, 17, 18, 19, 20, 17, 18, 19, 20, 17, 18, 19, 20, 17, 18, 19, 20, 17, 18, 19, 20, 17, 18, 19, 20, 17, 18, 19, 20, 17, 18, 19, 20, 17, 18, 19, 20, 17, 18, 23, 21, 23, 21, 23, 21, 23, 21, 23, 21, 23, 21, 23, 21, 23, 21, 23, 21, 23, 21, 23, 21, 23, 21, 23, 21, 23, 21, 23, 21, 23, 21, 23, 21, 23, 21, 27, 25, 27, 25, 27, 25, 27, 25, 27, 25, 27, 25, 27, 25, 27, 25, 27, 25, 27, 25, 27, 25, 27, 25, 27, 25, 27, 25, 27, 25, 27, 25, 27, 25, 27, 25};

static EERenderPlugin instance;
