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
#include "TMath.h"
#include "TText.h"
#include "TPaletteAxis.h"
#include "TH2F.h"
#include "TLine.h"
#include "TList.h"
#include "TH2Poly.h"
#include "TString.h"
#include "HGCalAuxiliaryInfo.h"

#include <iostream>

class HGCalRenderPlugin : public DQMRenderPlugin {
public:
  virtual bool applies(const VisDQMObject &o, const VisDQMImgInfo &) {
    if (o.name.find("HGCAL/Modules") != std::string::npos)
      return true;
    else if (o.name.find("HGCAL/Layers") != std::string::npos)
      return true;
    else if (o.name.find("HGCAL/Digis") != std::string::npos)
      return true;
    else
      return false;
  }

  virtual void preDraw(TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &, VisDQMRenderInfo &) {
    c->cd();
    c->SetRightMargin(0.15);

    if (dynamic_cast<TH2Poly *>(o.object)) {
      preDrawHex(o);
    } else if (dynamic_cast<TH2F *>(o.object)) {
      preDrawTH2(c, o);
    } else if (dynamic_cast<TH1F *>(o.object)) {
      preDrawTH1(c, o);
    }
  }

  virtual void postDraw(TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &) {
    if (dynamic_cast<TH2 *>(o.object))
      postDrawTH2(c, o);
    if (dynamic_cast<TH2Poly *>(o.object))
      postDrawHex(c, o);
  }

private:
  void preDrawTH1(TCanvas *c __attribute__((unused)), const VisDQMObject &o) {
    TH1 *obj = dynamic_cast<TH1 *>(o.object);
    assert(obj);
  }

  void preDrawHex(const VisDQMObject &o) {
    TH2Poly *obj = dynamic_cast<TH2Poly *>(o.object);
    TString name(obj->GetName());
    assert(obj);

    gStyle->SetPalette(kBird);
    obj->SetOption("colz");

    //customize display of hex plots
    if (name.Contains("hex_channelId") || name.Contains("hex_hgcrocPin") || name.Contains("hex_sicellPadId")) {
      gStyle->SetPaintTextFormat(".0f");
      obj->SetMarkerSize(0.7);
      obj->SetOption("colztext");
    } else if (name.Contains("_layer_")) {
      gStyle->SetPaintTextFormat(".2e");
      obj->SetMarkerSize(2.0);
      obj->SetOption("colztext");
    } else {
      gStyle->SetPaintTextFormat(".2f");
      obj->SetMarkerSize(0.7);
      obj->SetOption("colz");
    }

    obj->SetStats(kFALSE);
    obj->GetXaxis()->CenterLabels();
    obj->GetYaxis()->CenterLabels();

  }  // end of preDrawHex

  void preDrawTH2(TCanvas *c, const VisDQMObject &o) {
    TH2F *obj = dynamic_cast<TH2F *>(o.object);
    assert(obj);

    // This applies to all
    gStyle->SetCanvasBorderMode(0);
    gStyle->SetCanvasColor(kWhite);
    gStyle->SetPadBorderMode(0);
    gStyle->SetPadBorderSize(0);
    gStyle->SetOptStat(10);

    if ( (o.name.find("econd") != std::string::npos) || (o.name.find("Quality") != std::string::npos) ) {
      gStyle->SetOptStat(10);
      gStyle->SetPalette(kCherry);
      TColor::InvertPalette();
      obj->SetStats(kTRUE);
    } else {
      gStyle->SetOptStat(1111);
      gStyle->SetPalette(1);
      obj->SetStats(kTRUE);
    }

    obj->SetOption("colz");
    obj->GetXaxis()->SetNdivisions(-510);
    obj->GetYaxis()->SetNdivisions(-510);
    obj->GetXaxis()->CenterLabels();
    obj->GetYaxis()->CenterLabels();
    c->SetGridx();
    c->SetGridy();

  }  // end of preDrawTH2

  void postDrawTH2(TCanvas *c __attribute__((unused)), const VisDQMObject &o) {
    TH2 *obj = dynamic_cast<TH2 *>(o.object);
    assert(obj);
  }  // End of postDrawTH2

  void postDrawHex(TCanvas *c __attribute__((unused)), const VisDQMObject &o) {
    TH2Poly *obj = dynamic_cast<TH2Poly *>(o.object);
    TString name(obj->GetName());
    assert(obj);

    // Get the palette axis
    TPaletteAxis *palette = (TPaletteAxis*)obj->GetListOfFunctions()->FindObject("palette");
    if (palette) {
        obj->GetZaxis()->SetTitleOffset(1.2);
        obj->GetZaxis()->SetTitleFont(42);
        obj->GetZaxis()->SetTitleSize(0.035);
        c->Update();
    }

    //--------------------------------------------------
    // Draw auxiliary lines
    //--------------------------------------------------
    std::vector<std::vector<double>> x_coords;
    std::vector<std::vector<double>> y_coords;

    if (name.Contains("_module_")) {
      x_coords = aux::x_coords_LD_full;
      y_coords = aux::y_coords_LD_full;
    } else if (name.Contains("LD_0")) {
      x_coords = aux::x_coords_LD_full;
      y_coords = aux::y_coords_LD_full;
    } else if (name.Contains("LD_3")) {
      x_coords = aux::x_coords_LD_3;
      y_coords = aux::y_coords_LD_3;
    } else if (name.Contains("LD_4")) {
      x_coords = aux::x_coords_LD_4;
      y_coords = aux::y_coords_LD_4;
    } else if (name.Contains("HD_0")) {
      x_coords = aux::x_coords_HD_full;
      y_coords = aux::y_coords_HD_full;
    }

    bool drawLine = true;
    if (drawLine) {
      TLine line;
      line.SetLineStyle(1);
      line.SetLineColor(kRed-7);
      line.SetLineWidth(2);

      for (unsigned iline = 0; iline < x_coords.size(); ++iline) {
        const auto &x = x_coords.at(iline);
        const auto &y = y_coords.at(iline);
        for (unsigned j = 0; j < x.size() - 1; ++j) {
          line.DrawLine(x[j], y[j], x[j + 1], y[j + 1]);
        }
      }
    }

    bool drawText = true;
    if (drawText) {
      TText text;
      text.SetTextAlign(22);
      text.SetTextFont(43);
      text.SetTextSize(12);

      if (name.Contains("HD") || name.Contains("MH")) {
        double theta1 = 0.;
        double theta2 = 4 * TMath::Pi() / 3.;
        double theta3 = 2 * TMath::Pi() / 3.;

        std::vector<double> theta_angle_text = {0, 0, 120, 120, -120, -120};
        std::vector<double> theta_coordinate_text = {theta1, theta1, theta2, theta2, theta3, theta3};
        std::vector<double> x_coordinate_text = {-6.25, 6.25, -6.25, 6.25, -6.25, 6.25};
        std::vector<double> y_coordinate_text = {26, 26, 26, 26, 26, 26};
        std::vector<TString> v_texts = {"chip-0", "chip-1", "chip-2", "chip-3", "chip-4", "chip-5"};

        double arbUnit_to_cm = 6.9767 / 20.;

        // evaluate (r, phi) and apply rotation
        for (int i = 0; i < 6; ++i) {
          text.SetTextAngle(theta_angle_text[i]);
          double theta = theta_coordinate_text[i];
          double cos_theta = TMath::Cos(theta);
          double sin_theta = TMath::Sin(theta);

          double x = x_coordinate_text[i];
          double y = y_coordinate_text[i];
          double r = sqrt(pow(x, 2) + pow(y, 2));
          double cos_phi = x / r;
          double sin_phi = y / r;
          x = r * (cos_phi * cos_theta + sin_phi * sin_theta) * arbUnit_to_cm;
          y = r * (sin_phi * cos_theta - cos_phi * sin_theta) * arbUnit_to_cm;

          text.DrawText(x, y, v_texts[i]);
        }

      } else if (name.Contains("LD") || name.Contains("ML") || name.Contains("_module")) {  // LD
        double theta1 = -TMath::Pi() / 3.;
        double theta2 = TMath::Pi() / 3.;
        double theta3 = TMath::Pi();
        std::vector<double> theta_angle_text = {60, 60, -60, -60, 0, 0};
        std::vector<double> theta_coordinate_text = {theta1, theta1, theta2, theta2, theta3, theta3};
        std::vector<double> x_coordinate_text = {-6.25, 6.25, -6.25, 6.25, -6.25, 6.25};
        std::vector<double> y_coordinate_text = {26, 26, 26, 26, 26, 26};
        std::vector<TString> v_texts = {"chip-0, half-1", "chip-0, half-0", "chip-1, half-1", "chip-1, half-0", "chip-2, half-1", "chip-2, half-0"};

        double arbUnit_to_cm = 6.9767 / 20.;

        // evaluate (r, phi) and apply rotation
        for (int i = 0; i < 6; ++i) {
          if (name.Contains("LD_3") && (i == 2 || i == 3 || i == 4))
            continue;
          if (name.Contains("LD_4") && (i == 0 || i == 1 || i == 5))
            continue;
          text.SetTextAngle(theta_angle_text[i]);
          double theta = theta_coordinate_text[i];
          double cos_theta = TMath::Cos(theta);
          double sin_theta = TMath::Sin(theta);

          double x = x_coordinate_text[i];
          double y = y_coordinate_text[i];
          double r = sqrt(pow(x, 2) + pow(y, 2));
          double cos_phi = x / r;
          double sin_phi = y / r;
          x = r * (cos_phi * cos_theta + sin_phi * sin_theta) * arbUnit_to_cm;
          y = r * (sin_phi * cos_theta - cos_phi * sin_theta) * arbUnit_to_cm;

          if (name.Contains("LD_3") && (i == 5))
            text.DrawText(x, y, "chip-1, half-0");
          else if (name.Contains("LD_4") && (i == 2))
            text.DrawText(x, y, "chip-1, half-0");
          else if (name.Contains("LD_4") && (i == 3))
            text.DrawText(x, y, "chip-0, half-1");
          else if (name.Contains("LD_4") && (i == 4))
            text.DrawText(x, y, "chip-0, half-0");
          else
            text.DrawText(x, y, v_texts[i]);
        }
      }
    }

  }  // End of postDrawHex
};

static HGCalRenderPlugin instance;
