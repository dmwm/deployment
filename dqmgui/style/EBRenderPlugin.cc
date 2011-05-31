// $Id: EBRenderPlugin.cc,v 1.142 2011/05/28 09:49:02 emanuele Exp $

/*!
  \file EBRenderPlugin
  \brief Display Plugin for Quality Histograms
  \author G. Della Ricca
  \author B. Gobbo
  \version $Revision: 1.142 $
  \date $Date: 2011/05/28 09:49:02 $
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
#include "TPaletteAxis.h"
#include "TROOT.h"

#include <iostream>
#include <sstream>
#include <iomanip>
#include <stdexcept>
#include <math.h>
#include <cassert>

class EBRenderPlugin : public DQMRenderPlugin
{
  TH2C* text1;
  TH2C* text2;
  TH2C* text3;
  TH2C* text4;
  TH2C* text6;
  TH2C* text7;
  TH2C* text8;
  TH2C* text9;
  TH2C* text10;

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

      text1 = new TH2C( "eb_text1", "text1", 85, 0,  85, 20,   0, 20 );
      text2 = new TH2C( "eb_text2", "text2", 17, 0,  17,  4,   0,  4 );
      text3 = new TH2C( "eb_text3", "text3", 10, 0,  10,  5,   0,  5 );
      text4 = new TH2C( "eb_text4", "text4",  2, 0,   2,  1,   0,  1 );
      text6 = new TH2C( "eb_text6", "text6", 18, 0, 360,  2, -85, 85 );
      text7 = new TH2C( "eb_text7", "text7", 18, -M_PI*(9+1.5)/9, M_PI*(9-1.5)/9, 2, -1.479, 1.479);
      text8 = new TH2C( "eb_text8", "text8", 18, 0., 72., 2, -17., 17. );
      text9 = new TH2C( "eb_text9", "text9", 18, 0., 72., 2, 0., 34. );
      text10 = new TH2C( "eb_text10", "text10", 18, 0., 90., 2, -10., 10. );

      text1->SetMinimum(   0.10 );
      text2->SetMinimum(   0.10 );
      text3->SetMinimum(   0.10 );
      text4->SetMinimum(   0.10 );
      text6->SetMinimum( -18.01 );
      text7->SetMinimum( -18.01 );
      text8->SetMinimum( -18.01 );
      text9->SetMinimum( -18.01 );
      text10->SetMinimum( -18.01 );

      for(int i=0; i<68; i++)
      {
        text1->Fill( 2+(i/4)*5, 2+(i%4)*5, i+1 );
        text2->Fill( i/4, i%4, i+1 );
      }

      for(int i=0; i<2; i++)
      {
        text3->Fill( 2+i*5, 2, i+1+68 );
        text4->Fill( i, 0., i+1+68 );
      }

      for(int i=0; i<36; i++)
      {
        int x = 1 + i%18;
        int y = 1 + i/18;
        text6->SetBinContent(x, y, iEB(i+1));
      }

      for(int i=0; i<36; i++)
      {
        int x = 1 + i%18;
        int y = 2 - i/18;
        int z = x + 8;
        if( z > 18 ) z = z - 18;
        if( y == 1 )
        {
          text7->SetBinContent(x, y, -z);
        }
        else
        {
          text7->SetBinContent(x, y, +z);
        }
      }

      for(int i=0; i<36; i++)
      {
        int x = 1 + i%18;
        int y = 1 + i/18;
        text8->SetBinContent(x, y, iEB(i+1));
        text9->SetBinContent(x, y, iEB(i+1));
        text10->SetBinContent(x, y, iEB(i+1));
      }

      text1->SetMarkerSize( 2 );
      text2->SetMarkerSize( 2 );
      text3->SetMarkerSize( 2 );
      text4->SetMarkerSize( 2 );
      text6->SetMarkerSize( 2 );
      text7->SetMarkerSize( 2 );
      text8->SetMarkerSize( 2 );
      text9->SetMarkerSize( 2 );
      text10->SetMarkerSize( 2 );
    }

  virtual bool applies( const VisDQMObject &o, const VisDQMImgInfo & )
    {
      if( o.name.find( "EcalBarrel/EB" ) != std::string::npos )
        return true;

      if( o.name.find( "EcalBarrel/EcalInfo" ) != std::string::npos )
        return true;

      if( o.name.find( "EcalBarrel/EventInfo" ) != std::string::npos )
        return true;

      if( o.name.find( "EcalBarrel/Run summary/EB" ) != std::string::npos )
        return true;

      if( o.name.find( "EcalBarrel/Run summary/EcalInfo" ) != std::string::npos )
        return true;

      if( o.name.find( "EcalBarrel/Run summary/EventInfo" ) != std::string::npos )
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

      if( name.find( "EBLT shape" ) != std::string::npos )
      {
        c->SetTheta(+30.);
        c->SetPhi(-60.);
        obj->GetXaxis()->SetTitleOffset(2.5);
        obj->GetYaxis()->SetTitleOffset(3.0);
        obj->GetZaxis()->SetTitleOffset(1.3);
        if( r.drawOptions.size() == 0 ) r.drawOptions = "lego";
        return;
      }

      if( name.find( "EBTPT shape" ) != std::string::npos )
      {
        c->SetTheta(+30.);
        c->SetPhi(-60.);
        obj->GetXaxis()->SetTitleOffset(2.5);
        obj->GetYaxis()->SetTitleOffset(3.0);
        obj->GetZaxis()->SetTitleOffset(1.3);
        if( r.drawOptions.size() == 0 ) r.drawOptions = "lego";
        return;
      }

      if( name.find( "EBCLT" ) != std::string::npos )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(40118, kFALSE);
        obj->GetYaxis()->SetNdivisions(170102, kFALSE);
        obj->SetMinimum(0.0);
        gStyle->SetPalette(10, pCol4);
        gPad->SetRightMargin(0.15);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( name.find( "EBSRT" ) != std::string::npos )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(18, kFALSE);
        obj->GetYaxis()->SetNdivisions(2, kFALSE);
        obj->SetMinimum(0.0);
        gStyle->SetPalette(1);
        gPad->SetRightMargin(0.15);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( name.find( "EBTMT" ) != std::string::npos )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        if( nbx == 72 && nby == 34 )
        {
          obj->GetXaxis()->SetNdivisions(18, kFALSE);
          obj->GetYaxis()->SetNdivisions(2, kFALSE);
        }
        else if( nbx == 85 && nby == 20 )
        {
          obj->GetXaxis()->SetNdivisions(17);
          obj->GetYaxis()->SetNdivisions(4);
        }
        obj->SetMinimum(45.);
        obj->SetMaximum(55.);

        gStyle->SetPalette(1);
        obj->SetContour(255);

        gPad->SetRightMargin(0.15);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( nbx == 72 && nby == 34 )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(18, kFALSE);
        obj->GetYaxis()->SetNdivisions(2, kFALSE);
      }

      if( nbx == 85 && nby == 20 )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(17);
        obj->GetYaxis()->SetNdivisions(4);
      }

      if( nbx == 17 && nby == 4 )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(17);
        obj->GetYaxis()->SetNdivisions(4);
      }

      obj->SetMinimum(0.0);
      gStyle->SetPalette(10, pCol4);
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

      if( name.find( "EBMM digi number profile" ) != std::string::npos ||
          name.find( "EBLT laser L1" ) != std::string::npos ||
          ( name.find( "EBTPT test pulse amplitude" ) != std::string::npos && name.find( "summary" ) != std::string::npos ) ||
          name.find( "EBPOT pedestal G12 mean" ) || name.find( "EBPOT pedestal G12 rms" ) )
      {
        gPad->SetBottomMargin(0.2);
        obj->GetXaxis()->LabelsOption("v");
      }

      if( name.find( "EBMM hit number profile" ) != std::string::npos )
      {
        gPad->SetBottomMargin(0.2);
        obj->GetXaxis()->LabelsOption("v");
      }

      if( name.find( "EBMM TP digi number profile" ) != std::string::npos )
      {
        gPad->SetBottomMargin(0.2);
        obj->GetXaxis()->LabelsOption("v");
      }

      if( name.find( "EBSRT DCC event size" ) != std::string::npos )
      {
        gPad->SetBottomMargin(0.2);
        obj->GetXaxis()->LabelsOption("v");
      }

      if( name.find( "EBTMT timing" ) != std::string::npos )
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

      if( name.find( "EBSRT" ) != std::string::npos )
      {
        gPad->SetGridx();
        gPad->SetGridy();

        if( name.find( "EBSRT DCC" ) != std::string::npos )
        {
          obj->GetXaxis()->SetNdivisions(16, kFALSE);
          obj->GetYaxis()->SetNdivisions(8, kFALSE);
        }
        else
        {
          obj->GetXaxis()->SetNdivisions(18, kFALSE);
          obj->GetYaxis()->SetNdivisions(2, kFALSE);
        }
        if( name.find( "EBSRT event size vs DCC" ) != std::string::npos )
        {
          gPad->SetLogy(kTRUE);
          gPad->SetBottomMargin(0.2);
          obj->GetXaxis()->LabelsOption("v");
          obj->GetYaxis()->SetRangeUser(0.1, 0.608*68);
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

      if( name.find( "EBCLT SC energy vs seed crystal energy" ) != std::string::npos )
      {
        gStyle->SetPalette(1);
        gPad->SetRightMargin(0.15);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( name.find( "EBCLT" ) != std::string::npos )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(40118, kFALSE);
        obj->GetYaxis()->SetNdivisions(170102, kFALSE);
        obj->SetMinimum(0.0);
        gStyle->SetPalette(10, pCol4);
        gPad->SetRightMargin(0.15);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( name.find( "EBTMT timing vs amplitude" ) != std::string::npos )
      {
        if( obj->GetMaximum() > 0. ) gPad->SetLogz(kTRUE);
        obj->SetMinimum(0.0);
        gStyle->SetPalette(1);
        gPad->SetRightMargin(0.15);
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( nbx == 85 && nby == 20 )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(17);
        obj->GetYaxis()->SetNdivisions(4);
      }

      if( nbx == 17 && nby == 4 )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(17);
        obj->GetYaxis()->SetNdivisions(4);
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

      if( nbx == 360 && nby == 170 )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(18, kFALSE);
        obj->GetYaxis()->SetNdivisions(2, kFALSE);
      }

      if( nbx == 90 && nby == 20 )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(18, kFALSE);
        obj->GetYaxis()->SetNdivisions(2, kFALSE);
      }

      if( nbx == 72 && nby == 34 )
      {
        gPad->SetGridx();
        gPad->SetGridy();
        obj->GetXaxis()->SetNdivisions(18, kFALSE);
        obj->GetYaxis()->SetNdivisions(2, kFALSE);
      }

      if( name.find( "reportSummaryMap" ) != std::string::npos )
      {
        dqm::utils::reportSummaryMapPalette(obj);
        obj->SetTitle("EcalBarrel Report Summary Map");
        gStyle->SetPaintTextFormat("+g");
        return;
      }

      if( name.find( "DAQSummaryMap" ) != std::string::npos )
      {
        dqm::utils::reportSummaryMapPalette(obj);
        obj->SetTitle("EcalBarrel DAQ Summary Map");
        gStyle->SetPaintTextFormat("+g");
        return;
      }

      if( name.find( "DCSSummaryMap" ) != std::string::npos )
      {
        dqm::utils::reportSummaryMapPalette(obj);
        obj->SetTitle("EcalBarrel DCS Summary Map");
        gStyle->SetPaintTextFormat("+g");
        return;
      }

      if( name.find( "CertificationSummaryMap" ) != std::string::npos )
      {
        dqm::utils::reportSummaryMapPalette(obj);
        obj->SetTitle("EcalBarrel Data Certification Summary Map");
        gStyle->SetPaintTextFormat("+g");
        return;
      }

      if( name.find( "EBIT" ) != std::string::npos &&
          name.find( "quality" ) == std::string::npos )
      {
        obj->SetMinimum(0.0);
        gStyle->SetPalette(10, pCol5);
        gPad->SetRightMargin(0.15);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( name.find( "EBTTT" ) != std::string::npos &&
          name.find( "quality" ) == std::string::npos )
      {
        if( name.find( "EBTTT Trigger Primitives Timing" ) != std::string::npos )
        {
          obj->SetMinimum(-1.0);
          obj->SetMaximum(6.0);
        }
        else
        {
          obj->SetMinimum(0.0);
        }

        if( name.find( "Error" ) == std::string::npos )
        {
          if( name.find( "EBTTT Trigger Primitives Timing" ) != std::string::npos )
          {
            gStyle->SetPalette(7, pCol6);
            obj->SetContour(7);
          }
          else if( name.find( "EBTTT Trigger Primitives Non Single Timing" ) != std::string::npos )
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
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( name.find( "EBSFT" ) != std::string::npos &&
          name.find( "summary" ) == std::string::npos )
      {
        obj->SetMinimum(0.0);
        gStyle->SetPalette(10, pCol5);
        gPad->SetRightMargin(0.15);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( name.find( "G12 RMS map" ) != std::string::npos )
      {
        obj->SetMinimum(0.5);
        obj->SetMaximum(3.0);
        gStyle->SetPalette(1);
        gPad->SetRightMargin(0.15);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( name.find( "EBOT" ) != std::string::npos )
      {
        obj->SetMinimum(0.0);
        gStyle->SetPalette(10, pCol4);
        gPad->SetRightMargin(0.15);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( name.find( "EBCT" ) != std::string::npos )
      {
        obj->SetMinimum(0.0);
        gStyle->SetPalette(10, pCol4);
        gPad->SetRightMargin(0.15);
        gStyle->SetPaintTextFormat("+g");
        if( r.drawOptions.size() == 0 ) r.drawOptions = "colz";
        return;
      }

      if( name.find( "summary" ) != std::string::npos &&
          name.find( "Trigger Primitives Timing") == std::string::npos )
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

      if( name.find( "EBMM event" ) != std::string::npos )
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

      if( nbx == 10 || nbx == 1700 )
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

      if( name.find( "EBMM DCC" ) != std::string::npos )
      {
        gPad->SetBottomMargin(0.2);
        obj->GetXaxis()->LabelsOption("v");
      }

      if( name.find( "EBIT DCC" ) != std::string::npos )
      {
        gPad->SetBottomMargin(0.2);
        obj->GetXaxis()->LabelsOption("v");
      }

      if( name.find( "EBOT rec hit flags" ) != std::string::npos )
      {
        gPad->SetBottomMargin(0.4);
        obj->GetXaxis()->LabelsOption("v");
      }

      if( name.find( "EBRDT" ) != std::string::npos )
      {
        gPad->SetBottomMargin(0.2);
        obj->GetXaxis()->LabelsOption("v");
      }

      if( name.find( "EBRDT event type" ) != std::string::npos )
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

      if( name.find( "EBOT digi occupancy summary 1D" ) != std::string::npos )
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

      int nbx = obj->GetNbinsX();
      int nby = obj->GetNbinsY();

      if( name.find( "EBLT shape" ) != std::string::npos )
      {
        return;
      }

      if( name.find( "EBTPT shape" ) != std::string::npos )
      {
        return;
      }

      if( name.find( "EBCLT" ) != std::string::npos )
      {
        int x1 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
        int x2 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
        int y1 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
        int y2 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
        text7->GetXaxis()->SetRange(x1, x2);
        text7->GetYaxis()->SetRange(y1, y2);
        text7->Draw("text,same");
        return;
      }

      if( nbx == 17 && nby == 4 )
      {
        int x1 = text2->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
        int x2 = text2->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
        int y1 = text2->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
        int y2 = text2->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
        text2->GetXaxis()->SetRange(x1, x2);
        text2->GetYaxis()->SetRange(y1, y2);
        text2->Draw("text,same");
        return;
      }

      if( name.find( "EBTMT" ) != std::string::npos &&
          (( nbx == 72 && nby == 34 ) || ( nbx == 85 && nby == 20 )) )
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

      if( nbx == 72 && nby == 34 )
      {
        if( name.find( "EBTMT" ) == std::string::npos )
        {
          int x1 = text8->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text8->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text8->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text8->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text8->GetXaxis()->SetRange(x1, x2);
          text8->GetYaxis()->SetRange(y1, y2);
          text8->Draw("text,same");
          return;
        }
        else
        {
          int x1 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
          int x2 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
          int y1 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
          int y2 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
          text6->GetXaxis()->SetRange(x1, x2);
          text6->GetYaxis()->SetRange(y1, y2);
          text6->Draw("text,same");

          return;
        }
      }

      int x1 = text1->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
      int x2 = text1->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
      int y1 = text1->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
      int y2 = text1->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
      text1->GetXaxis()->SetRange(x1, x2);
      text1->GetYaxis()->SetRange(y1, y2);
      text1->Draw("text,same");
    }

  void postDrawTH3F( TCanvas *, const VisDQMObject & )
    {
    }

  void postDrawTH2( TCanvas *, const VisDQMObject &o )
    {
      TH2* obj = dynamic_cast<TH2*>( o.object );
      assert( obj );

      std::string name = o.name.substr(o.name.rfind("/")+1);

      int nbx = obj->GetNbinsX();
      int nby = obj->GetNbinsY();

      if( name.find( "EBCLT" ) != std::string::npos &&
          name.find( "seed" ) == std::string::npos )
      {
        int x1 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
        int x2 = text7->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
        int y1 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
        int y2 = text7->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
        text7->GetXaxis()->SetRange(x1, x2);
        text7->GetYaxis()->SetRange(y1, y2);
        text7->Draw("text,same");
        return;
      }

      if( name.find( "EBOT MEM" ) != std::string::npos )
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

      if( name.find( "EBOT digi" ) != std::string::npos )
      {
        if( nbx == 85 && nby == 20 )
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

        int x1 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
        int x2 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
        int y1 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
        int y2 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
        text6->GetXaxis()->SetRange(x1, x2);
        text6->GetYaxis()->SetRange(y1, y2);
        text6->Draw("text,same");
        return;
      }

      if( name.find( "EBOT rec hit" ) != std::string::npos )
      {
        int x1 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
        int x2 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
        int y1 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
        int y2 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
        text6->GetXaxis()->SetRange(x1, x2);
        text6->GetYaxis()->SetRange(y1, y2);
        text6->Draw("text,same");
        return;
      }

      if( name.find( "EBOT TP digi" ) != std::string::npos )
      {
        int x1 = text8->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
        int x2 = text8->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
        int y1 = text8->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
        int y2 = text8->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
        text8->GetXaxis()->SetRange(x1, x2);
        text8->GetYaxis()->SetRange(y1, y2);
        text8->Draw("text,same");
        return;
      }

      if( name.find( "EBOT test pulse digi" ) != std::string::npos )
      {
        int x1 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
        int x2 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
        int y1 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
        int y2 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
        text6->GetXaxis()->SetRange(x1, x2);
        text6->GetYaxis()->SetRange(y1, y2);
        text6->Draw("text,same");
        return;
      }

      if( name.find( "EBOT laser digi" ) != std::string::npos )
      {
        int x1 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
        int x2 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
        int y1 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
        int y2 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
        text6->GetXaxis()->SetRange(x1, x2);
        text6->GetYaxis()->SetRange(y1, y2);
        text6->Draw("text,same");
        return;
      }

      if( name.find( "EBOT pedestal digi" ) != std::string::npos ||
          name.find( "G12 RMS map" ) != std::string::npos )
      {
        int x1 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
        int x2 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
        int y1 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
        int y2 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
        text6->GetXaxis()->SetRange(x1, x2);
        text6->GetYaxis()->SetRange(y1, y2);
        text6->Draw("text,same");
        return;
      }

      if( name.find( "SummaryMap" ) != std::string::npos )
      {
        int x1 = text9->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
        int x2 = text9->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
        int y1 = text9->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
        int y2 = text9->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
        text9->GetXaxis()->SetRange(x1, x2);
        text9->GetYaxis()->SetRange(y1, y2);
        text9->Draw("text,same");
        return;
      }

      if( nbx == 85 && nby == 20 )
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

      if( nbx == 17 && nby == 4 )
      {
        int x1 = text2->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
        int x2 = text2->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
        int y1 = text2->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
        int y2 = text2->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
        text2->GetXaxis()->SetRange(x1, x2);
        text2->GetYaxis()->SetRange(y1, y2);
        text2->Draw("text,same");
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

      if( nbx == 72 && nby == 34 )
        {
          if( name.find( "seed" ) != std::string::npos )
            {
              int x1 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
              int x2 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
              int y1 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
              int y2 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
              text6->GetXaxis()->SetRange(x1, x2);
              text6->GetYaxis()->SetRange(y1, y2);
              text6->Draw("text,same");
              return;
            } else {
              int x1 = text8->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
              int x2 = text8->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
              int y1 = text8->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
              int y2 = text8->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
              text8->GetXaxis()->SetRange(x1, x2);
              text8->GetYaxis()->SetRange(y1, y2);
              text8->Draw("text,same");
              return;
            }
        }

      if( nbx == 90 && nby == 20 )
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

      if( name.find( "summary" ) != std::string::npos )
      {
        int x1 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmin());
        int x2 = text6->GetXaxis()->FindFixBin(obj->GetXaxis()->GetXmax());
        int y1 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmin());
        int y2 = text6->GetYaxis()->FindFixBin(obj->GetYaxis()->GetXmax());
        text6->GetXaxis()->SetRange(x1, x2);
        text6->GetYaxis()->SetRange(y1, y2);
        text6->Draw("text,same");
        return;
      }
    }

  void postDrawTH1( TCanvas *, const VisDQMObject & )
    {
    }

  int iEB( const int ism ) throw( std::runtime_error )
    {
      // EB-
      if( ism >=  1 && ism <= 18 ) return( -ism );

      // EB+
      if( ism >= 19 && ism <= 36 ) return( +ism - 18 );

      std::ostringstream s;
      s << "Wrong SM id determination: iSM = " << ism;
      throw( std::runtime_error( s.str() ) );
    }

};

static EBRenderPlugin instance;
