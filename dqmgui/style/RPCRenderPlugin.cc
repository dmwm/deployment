#include "DQM/DQMRenderPlugin.h"
#include "utils.h"
#include "TProfile2D.h"
#include "TStyle.h"
#include "TCanvas.h"
#include "TColor.h"
#include <iostream>
#include <cassert>
#include <sstream>
#include <fstream>
#include "TLine.h"
#include "TText.h"
#include "TPaletteAxis.h"
#include "TH2F.h"
#include "TList.h"

class RPCRenderPlugin : public DQMRenderPlugin {

public:

  virtual bool applies(const VisDQMObject &o, const VisDQMImgInfo &) {

    if (o.name.find( "RPC/RecHits" ) != std::string::npos) return true;
    if (o.name.find( "RPC/Noise" ) != std::string::npos) return true;
    if (o.name.find( "RPC/Muon" ) != std::string::npos) return true;
    if (o.name.find( "RPC/DCSInfo" ) != std::string::npos) return true;
    if (o.name.find( "RPC/RPCEfficiency" ) != std::string::npos) return true;
    if (o.name.find( "RPC/FEDIntegrity" ) != std::string::npos) return true;
    if (o.name.find("RPC/EventInfo") != std::string::npos) return true;
    if (o.name.find("RPC/AllHits") != std::string::npos) return true;
    if (o.name.find( "RPC/Segment_TnP") != std::string::npos) return true;
    return false;
  }

  virtual void preDraw(TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &, VisDQMRenderInfo &) {
    c->cd();

    if (dynamic_cast<TH2*>( o.object )) {
      preDrawTH2(c, o);
    } else if (dynamic_cast<TH1*>( o.object )) {
      preDrawTH1(c, o);
    }
  }

  virtual void postDraw(TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &) {
    if (dynamic_cast<TH2*>( o.object )) postDrawTH2(c,o);
  }


private:

  void preDrawTH1(TCanvas *c __attribute__ ((unused)) , const VisDQMObject &o) {
    TH1* obj = dynamic_cast<TH1*>(o.object);
    assert(obj);

    obj->GetXaxis()->SetLabelSize(0.05);
    obj->GetYaxis()->SetLabelSize(0.045);
    if (o.name.find("BX") != std::string::npos) {
      obj->StatOverflows(false);
    }
    if (o.name.find("RPC_chamberEff_Barrel_1D") != std::string::npos ||
        o.name.find("RPC_chamberEff_Barrel_allCh_1D") != std::string::npos ||
        o.name.find("RPC_chamberEff_Endcap_1D") != std::string::npos ||
        o.name.find("RPC_chamberEff_Endcap_allCh_1D") != std::string::npos) {
      obj->SetMinimum(0.);
      c->SetGrid(1,1);
    }

  }

  void preDrawTH2(TCanvas *c, const VisDQMObject &o) {
    TH2F* obj = dynamic_cast<TH2F*>(o.object);
    assert(obj);

    // This applies to all
    gStyle->SetCanvasBorderMode(0);
    gStyle->SetCanvasColor(kWhite);
    gStyle->SetPadBorderMode(0);
    gStyle->SetPadBorderSize(0);
    gStyle->SetOptStat(10);
    gStyle->SetPalette(1);

    if (o.name.find("Occupancy_for_") != std::string::npos && o.name.find("SummaryHistograms") != std::string::npos) {
      obj->SetOption("colztext");
    } else {
      obj->SetOption("colz");
    }

    obj->SetStats(kFALSE);
    obj->GetXaxis()->SetNdivisions(-510);
    obj->GetYaxis()->SetNdivisions(-510);
    obj->GetXaxis()->SetLabelSize(0.05);
    obj->GetYaxis()->SetLabelSize(0.045);
    obj->GetXaxis()->CenterLabels();
    obj->GetYaxis()->CenterLabels();
    c->SetGridx();
    c->SetGridy();

    if (o.name.find("SummaryMap") != std::string::npos) {
      if (o.name.find("reportSummaryMap") != std::string::npos) {
        //Normalization of summary map
        double rpc_map[12][15] = {{ 1, 1, 1, 1,-1,0.705882353,0.470588235,0.882352941,          1,0.764705882,-1, 1, 1, 1, 1},
                                  { 1, 1, 1, 1,-1,          1,0.294117647,0.647058824,0.705882353,          1,-1, 1, 1, 1, 1},
                                  { 1, 1, 1, 1,-1,0.588235294,0.294117647,0.882352941,0.882352941,          1,-1, 1, 1, 1, 1},
                                  { 1, 1, 1, 1,-1,0.476190476,0.333333333,0.523809524,0.619047619,0.904761905,-1, 1, 1, 1, 1},
                                  { 1, 1, 1, 1,-1,0.529411765,0.411764706,0.529411765,0.764705882,0.647058824,-1, 1, 1, 1, 1},
                                  { 1, 1, 1, 1,-1,0.764705882,0.764705882,0.470588235,          1,          1,-1, 1, 1, 1, 1},
                                  {-1,-1,-1,-1,-1,0.764705882,0.647058824,0.588235294,0.764705882,0.764705882,-1,-1,-1,-1,-1},
                                  {-1,-1,-1,-1,-1,0.764705882,0.764705882,0.647058824,          1,0.764705882,-1,-1,-1,-1,-1},
                                  {-1,-1,-1,-1,-1,0.866666667,0.733333333,0.733333333,          1,0.866666667,-1,-1,-1,-1,-1},
                                  {-1,-1,-1,-1,-1,0.764705882,0.117647059,0.764705882,0.882352941,0.882352941,-1,-1,-1,-1,-1},
                                  {-1,-1,-1,-1,-1,0.533333333,        0.6,0.733333333,          1,0.866666667,-1,-1,-1,-1,-1},
                                  {-1,-1,-1,-1,-1,0.647058824,0.705882353,0.764705882,0.941176471,0.647058824,-1,-1,-1,-1,-1}};

        obj->SetMinimum(-1.e-15);
        obj->SetMaximum(1.0);

        int xbins = obj->GetNbinsX();
        int ybins = obj->GetNbinsY();
        for (int i = 0; i < xbins; i++) {
          for (int j = 0; j < ybins; j++) {
            double tem = obj->GetBinContent(i+1, j+1);

            if (rpc_map[j][i] > 0 and tem > 0) {
              double newTemp = tem / rpc_map[j][i];
              if (newTemp > 1.0) newTemp = 1.0;
              obj->SetBinContent(i+1, j+1, newTemp);
            }
          }
        }
        gStyle->SetPaintTextFormat(".3f");
        dqm::utils::reportSummaryMapPalette(obj);
        obj->SetOption("colz text");

      } else if (o.name.find("noisySummaryMap") != std::string::npos) {
        obj->SetMinimum(0.0);
        obj->SetMaximum(3.0);

        int colorPaletteEff[5];
        colorPaletteEff[0] = 400; // Y
        colorPaletteEff[1] = 807; // O
        colorPaletteEff[2] = 807; // R
        colorPaletteEff[3] = 632; // R
        colorPaletteEff[4] = 632; // R

        gStyle->SetPalette(5, colorPaletteEff);
        gStyle->SetPaintTextFormat(".3f");
        obj->SetOption( "colz text" );
      } else {
        dqm::utils::reportSummaryMapPalette(obj);
      }
      return;
    }

    if (o.name.find("Occupancy") != std::string::npos) {
      if ((o.name.find("_for_Barrel") != std::string::npos || o.name.find("_for_Endcap") != std::string::npos)
          && o.name.find("SummaryHistograms") != std::string::npos) {
        obj->SetStats(kFALSE);
      } else {
        obj->SetStats(kTRUE);
        gStyle->SetOptStat(10);
      }
      return;
    }
    if (o.name.find("RPC_chamberEff_Barrel_W") != std::string::npos) {
        dqm::utils::reportSummaryMapPalette(obj);
        obj->GetXaxis()->SetNdivisions(-21,true);
        obj->GetYaxis()->SetNdivisions(-12,true);
        obj->SetMinimum(0.);
        obj->GetXaxis()->CenterLabels();
        obj->GetYaxis()->CenterLabels();
        obj->SetOption("text,colz");
        obj->SetMarkerSize( 2 );
        gStyle->SetPaintTextFormat("1.2f");
        c->SetGrid(1,1);
      return;
    }

    if (o.name.find("RPC_chamberEff_Endcap_Sta") != std::string::npos) {
        dqm::utils::reportSummaryMapPalette(obj);
        obj->GetXaxis()->SetNdivisions(-6,true);
        obj->GetYaxis()->SetNdivisions(36,true);
        obj->SetMinimum(0.);
        obj->GetXaxis()->CenterLabels();
        obj->GetYaxis()->CenterLabels();
        obj->SetOption("text45,colz");
        obj->SetMarkerSize( 2 );
        gStyle->SetPaintTextFormat("1.2f");
        c->SetGrid(1,1);
      return;
    }

  }

  void postDrawTH2(TCanvas *c __attribute__ ((unused)), const VisDQMObject &o) {
    TH2* obj = dynamic_cast<TH2*>(o.object);
    assert(obj);

    if (o.name.find("Roll_vs_Sector_Wheel") != std::string::npos && o.name.find("Occupancy") == std::string::npos) {

      TLine line;
      line.SetLineWidth(2);
      line.DrawLine(0.5, 17.5, 3.5, 17.5);
      line.DrawLine(3.5, 17.5, 3.5, 21.5);
      line.DrawLine(4.5, 21.5, 4.5, 17.5);
      line.DrawLine(4.5, 17.5, 8.5, 17.5);
      line.DrawLine(8.5, 17.5, 8.5, 15.5);
      line.DrawLine(8.5, 15.5, 9.5, 15.5);
      line.DrawLine(9.5, 15.5, 9.5, 17.5);
      line.DrawLine(9.5, 17.5, 10.5, 17.5);
      line.DrawLine(10.5, 17.5, 10.5, 15.5);
      line.DrawLine(10.5, 15.5, 11.5, 15.5);
      line.DrawLine(11.5, 15.5, 11.5, 17.5);
      line.DrawLine(11.5, 17.5, 12.5, 17.5);

      for (int x = 1; x < 13; x++) {
        for (int y = 18; y < 22; y++) {
          if (x != 4) obj->SetBinContent(x,y,-1);
        }
      }

      obj->SetBinContent(9,16,-1);
      obj->SetBinContent(9,17,-1);
      obj->SetBinContent(11,16,-1);
      obj->SetBinContent(11,17,-1);
    }

    
    if (o.name.find("SummaryMap") != std::string::npos) {

      TLine line;// draw lines to delimitate Barrel and Endcaps
      line.SetLineWidth(1);
      line.DrawLine(-3.5, 0.5, -3.5, 6.5);
      line.DrawLine(-7.5, 6.5,-3.5, 6.5 );
      line.DrawLine(-2.5, 0.5, -2.5, 12.5);
      line.DrawLine(2.5, 0.5, 2.5, 12.5);
      line.DrawLine(-2.5, 12.5, 2.5, 12.5);

      line.DrawLine(3.5, 0.5, 3.5, 6.5);
      line.DrawLine(3.5, 6.5,7.5, 6.5 );
      line.DrawLine(7.5, 0.5,7.5, 6.5 );

      if (o.name.find("noisySummaryMap") != std::string::npos) {
        TText* t_text = new TText();
        t_text->SetTextSize(0.035);
        t_text->DrawText(3.0, 11, "Average number of");
        t_text->DrawText(3.0, 10.3, "possible noisy strips");
        t_text->DrawText(3.0, 9.6, "per roll");
      }
      return;
    }

    if (o.name.find("Occupancy") != std::string::npos && o.name.find("SummaryBySectors") != std::string::npos
        && o.name.find("Wheel") != std::string::npos) {
      //sector occupancy plots
      TLine line;
      line.SetLineWidth(2);// Draw lines to delimitate the end of the roll
      //rb1in
      line.DrawLine(91, 0.5, 91, 2.5);
      line.DrawLine(91, 2.5, 85, 2.5);
      //rb1out
      line.DrawLine(85, 2.5, 85, 4.5);
      line.DrawLine(85, 4.5, 91, 4.5);
      //rb2in and rb2out

      if (o.name.find("Wheel_-2") != std::string::npos || o.name.find("Wheel_2") != std::string::npos) {
        line.DrawLine(91, 4.5, 91, 6.5);
        line.DrawLine(91, 6.5, 85, 6.5);
        line.DrawLine(85, 6.5, 85, 9.5);
      } else {
        line.DrawLine(91, 4.5, 91, 7.5);
        line.DrawLine(91, 7.5, 85, 7.5);
        line.DrawLine(85, 7.5, 85, 9.5);
      }
      line.DrawLine(85, 9.5, 43, 9.5);
      //rb3
      line.DrawLine(43, 9.5, 43, 13.5);

      gStyle->SetOptStat( 10 );

      //gPad->Update();
      //TPaletteAxis *palette;
      //palette = (TPaletteAxis*)obj->GetListOfFunctions()->FindObject("palette");
      //palette->GetAxis()->SetLabelSize(0.024);
      //gPad->Update();
    }

    if (o.name.find("Occupancy") != std::string::npos && o.name.find("SummaryByRings") != std::string::npos
      && o.name.find("Disk") != std::string::npos) {
      gStyle->SetOptStat( 10 );
    }

    if (o.name.find("Occupancy") != std::string::npos && o.name.find("SummaryHistograms") != std::string::npos
      && o.name.find("_for_") == std::string::npos) {
      gStyle->SetOptStat( 10 );
    }

    if (o.name.find("OccupancyNormByGeoAndRPCEvents") != std::string::npos) {
      obj->SetMaximum(0.2);
      return;
    }

    if (o.name.find("ClusterSize_") != std::string::npos) {
      obj->SetStats(kTRUE);
      gStyle->SetOptStat(10);
      return;
    }

    if (o.name.find("ClusterSizeMean") != std::string::npos) {
      obj->SetMinimum(0.0);
      obj->SetMaximum(5.0);

      int colorPalette_m[5];
      colorPalette_m[0] = 400;
      colorPalette_m[1] = 416; // Yallow
      colorPalette_m[2] = 416; // Orange
      colorPalette_m[3] = 807; // Red
      colorPalette_m[4] = 632;

      gStyle->SetPalette(5, colorPalette_m);
      return;
    }

    if (o.name.find("AsymmetryLeftRight") != std::string::npos) {
      obj->SetMinimum(-1.e-15);
      obj->SetMaximum(1.0);

      int colorPalette1[10];
      colorPalette1[0] = 416;
      colorPalette1[1] = 416;
      colorPalette1[2] = 416;
      colorPalette1[3] = 400; // Yallow
      colorPalette1[4] = 400; // Yallow
      colorPalette1[5] = 807; // Orange
      colorPalette1[6] = 807; // Orange
      colorPalette1[7] = 632; // Red
      colorPalette1[8] = 632;
      colorPalette1[9] = 632;

      gStyle->SetPalette(10, colorPalette1);
      return;
    }

    if (o.name.find("DeadChannelFraction") != std::string::npos) {
      obj->SetMinimum(-1.e-15);
      obj->SetMaximum(1.0);

      int colorPalette2[10];
      colorPalette2[0] = 416;
      colorPalette2[1] = 416;
      colorPalette2[2] = 416;
      colorPalette2[3] = 400; // Yallow
      colorPalette2[4] = 400; // Yallow
      colorPalette2[5] = 400; // Yallow
      colorPalette2[6] = 807; // Orange
      colorPalette2[7] = 807; // Orange
      colorPalette2[8] = 632; // Red
      colorPalette2[9] = 632;

      gStyle->SetPalette(10, colorPalette2);
      return;
    }

    if (o.name.find("RPCNoisyStrips") != std::string::npos) {

      obj->SetMinimum(-0.5);
      obj->SetMaximum(5.5);

      int colorPalette5[6];
      colorPalette5[0] = 416; // G
      colorPalette5[1] = 400; // Y
      colorPalette5[2] = 400; // Y
      colorPalette5[3] = 807; // O
      colorPalette5[4] = 632; // R
      colorPalette5[5] = 632; // R

      gStyle->SetPalette(6, colorPalette5);

      return;
    }

    if (o.name.find("NumberOfDigi_Mean") != std::string::npos) {
      obj->SetMinimum(0.5);
      obj->SetMaximum(10.5);

      int colorPalette5[5];
      colorPalette5[0] = 416; // G
      colorPalette5[1] = 416; // G
      colorPalette5[2] = 400; // Y
      colorPalette5[3] = 807; // O
      colorPalette5[4] = 632; // R

      gStyle->SetPalette(5, colorPalette5);
      return;
    }

    if (o.name.find("rpcHVStatus") != std::string::npos) {
      //obj->Reset();
      obj->SetMinimum(-0.5);
      obj->SetMaximum(1.5);

      int colorPaletteDCS[2];
      colorPaletteDCS[0] = 632; // Red
      colorPaletteDCS[1] = 416; // Green

      gStyle->SetPalette(2, colorPaletteDCS);
      return;
    }

    if (o.name.find("RollPercentage") != std::string::npos) {
      obj->SetOption("text");
      return;
    }
  } // End of postDrawTH2
};

static RPCRenderPlugin instance;
