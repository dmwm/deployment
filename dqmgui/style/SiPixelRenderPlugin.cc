/*!
  \file SiPixelRenderPlugin
  \brief Display Plugin for Pixel DQM Histograms
  \author P.Merkel
  \version $Revision: 1.44 $
  \date $Date: 2011/01/12 13:07:55 $
*/

#include "DQM/DQMRenderPlugin.h"
#include "utils.h"

#include "TProfile2D.h"
#include "TStyle.h"
#include "TCanvas.h"
#include "TGraphPolar.h"
#include "TColor.h"
#include "TText.h"
#include "TLine.h"
#include <cassert>

#define PI_12 0.261799
#define PI    3.141592
#define PI_2  1.570796

class SiPixelRenderPlugin : public DQMRenderPlugin
{
public:
  virtual bool applies( const VisDQMObject &o, const VisDQMImgInfo & )
    {
      if( o.name.find( "Pixel/" ) != std::string::npos )
        return true;

      return false;
    }

  virtual void preDraw( TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &, VisDQMRenderInfo & )
    {
      c->cd();
      if( dynamic_cast<TH2*>( o.object ) )
      {
        preDrawTH2( c, o );
      }
      else if( dynamic_cast<TH1*>( o.object ) )
      {
        preDrawTH1( c, o );
      }
    }

  virtual void postDraw( TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo & )
    {
      c->cd();

      if( dynamic_cast<TH2*>( o.object ) )
      {
        postDrawTH2( c, o );
      }
      else if( dynamic_cast<TH1*>( o.object ) )
      {
        postDrawTH1( c, o );
      }
    }

private:
/*
void paletteGraph(Double_t min, Double_t max){
	gStyle->SetPalette(1);
	gStyle->SetOptStat(0);
	gStyle->SetNumberContours(255);
	TCanvas* pal = new TCanvas("Palette", "Palette", 150, 600);
	TH2F* palet = new TH2F("Palette", "Palette", 1, 0, 1, 255, min, max);
	Double_t dc = (max - min) / 255;
	for(Int_t i = 0; i < 255; i++)
		palet->SetBinContent(1, i + 1, min + i * dc);
	palet->Draw("COL");
	gPad->SetLeftMargin(0.5);
	palet->SetLabelSize(0.2,"Y");
	palet->SetLabelOffset(0.05, "Y");
	palet->SetLabelOffset(99, "X");
	palet->SetTitle("");
	palet->SetTickLength(0,"X");
	palet->SetLabelSize(0,"X");
	gPad->SetGrid(false,false);
}
*/
Int_t getColor(TH2F* fH, Int_t i, Int_t j, Double_t zmin, Double_t zmax){
	Int_t ncolors  = gStyle->GetNumberOfColors();

	Double_t zc;
    	Double_t dz = zmax - zmin;
	if(dz <= 0)
		return -1;

	Int_t ndiv = fH->GetContour();
	if (ndiv == 0 ) {
		ndiv = gStyle->GetNumberContours();
		fH->SetContour(ndiv);
	}

	Int_t ndivz  = TMath::Abs(ndiv);

	if (fH->TestBit(TH1::kUserContour) == 0)
		fH->SetContour(ndiv);

	Double_t scale = ndivz/dz;
	Int_t color;
	const Double_t z = fH->GetBinContent(i,j);

	if (z < zmin || z==0.)
		return -1;
	if (fH->TestBit(TH1::kUserContour)) {
		zc = fH->GetContourLevelPad(0);
		if (z < zc)
			return -1;
		color = -1;
		for (Int_t k=0; k<ndiv; k++) {
			zc = fH->GetContourLevelPad(k);
			if (z < zc)
				continue;
			else
				color++;
		}
	} else
		color = Int_t(0.01+(z-zmin)*scale);

	Int_t theColor = Int_t((color+0.99)*Double_t(ncolors)/Double_t(ndivz));
	if (z >= zmax)
		theColor = ncolors-1;
	return theColor;
}

void polarGraph(TCanvas *c, TH2F* map){
	TGraphPolar *graphs[24][7];
	TColor *colors = new TColor();

	colors->SetPalette(1, 0);
	gStyle->SetPalette(1);
	gStyle->SetNumberContours(255);

		for(Int_t i = 0 ; i < 24; i++)
			for(Int_t j = 0 ; j < 7; j++)
			{
				graphs[i][j] = makeSlice(j + 1., j + 1.9999, PI_2-(i+1)*PI_12, PI_2-(i)*PI_12,
						colors->GetColorPalette(getColor(map,
i + 1, j + 1, map->GetMinimum(), map->GetMaximum())), 5,
						map->GetName());
				graphs[i][j]->Draw("F same");
			}
		c->Update();
		graphs[0][0]->GetPolargram()->SetToRadian();
		graphs[0][0]->SetMaximum(8);
		graphs[0][0]->GetPolargram()->SetNdivPolar(24);
		graphs[0][0]->GetPolargram()->SetNdivRadial(8);

		Int_t cnt(7);

		for(Int_t i = 0 ; i < 6 ; i++)
			graphs[0][0]->GetPolargram()->SetPolarLabel(i,Form("%d", cnt--));
		for(Int_t i = 6 ; i < 18 ; i++)
			graphs[0][0]->GetPolargram()->SetPolarLabel(i,Form("%d", i-5));
		cnt = 12;
		for(Int_t i = 19 ; i < 24 ; i++)
			graphs[0][0]->GetPolargram()->SetPolarLabel(i,Form("%d", cnt--));

}


TGraphPolar* makeSlice(Double_t rA, Double_t rB, Double_t phiA, Double_t phiB, Int_t
color, Int_t npts, std::string title){
	Double_t *r = new Double_t[2*npts+3];
	Double_t *th = new Double_t[2*npts+3];

	r[0] = rA;
	th[0] = phiA;
	for(Int_t i = 0 ; i <= npts ; i++){
		r[i + 1] = rB;
		th[i + 1] = i * (phiB - phiA) / npts + phiA;
		r[npts+2+i] = rA;
		th[npts+2+i] = phiB - i * (phiB - phiA) / npts;
	}


	TGraphPolar *grP = new TGraphPolar(2*npts+3,th,r);

	grP->SetTitle(title.c_str());
	grP->SetFillColor(color);
	grP->SetLineColor(color);
	grP->SetLineWidth(2);
	return grP;
}

void preDrawTH2( TCanvas *, const VisDQMObject &o )
    {
      TH2* obj = dynamic_cast<TH2*>( o.object );
      assert( obj );

      // This applies to all
      gStyle->SetCanvasBorderMode( 0 );
      gStyle->SetPadBorderMode( 0 );
      gStyle->SetPadBorderSize( 0 );
      //    (data->pad)->SetLogy( 0 );;
      gStyle->SetOptStat( 0 );
      obj->SetStats( kFALSE );
      if(o.name.find( "sizeYvsEta" ) != std::string::npos){
        obj->SetStats( kTRUE );
	gStyle->SetOptStat( 1111111 );
	if(obj->GetEntries() > 0.) gPad->SetLogz(1);
      }

      if( o.name.find( "reportSummaryMap" ) == std::string::npos){
        TAxis* xa = obj->GetXaxis();
        TAxis* ya = obj->GetYaxis();
        xa->SetTitleOffset(0.7);
        xa->SetTitleSize(0.065);
        xa->SetLabelSize(0.065);
        ya->SetTitleOffset(0.75);
        ya->SetTitleSize(0.065);
        ya->SetLabelSize(0.065);
      }

      if( o.name.find( "endcapOccupancyMap" ) != std::string::npos ) obj->SetTitle("Endcap Digi Occupancy Map");
      if( o.name.find( "hitmap" ) != std::string::npos  ||
          o.name.find( "Occupancy" ) != std::string::npos ||
	  o.name.find( "position_siPixelClusters" ) != std::string::npos ||
	  (o.name.find( "TRKMAP" ) != std::string::npos && o.name.find( "Layer" ) != std::string::npos) ||
	  o.name.find( "sizeYvsEta" ) != std::string::npos)
      {
        gStyle->SetPalette(1);
	gPad->SetRightMargin(0.15);
        obj->SetOption("colz");
        return;
      }
      //Separated out HitEfficiency maps to set scale
      if( o.name.find( "HitEfficiency_L" ) != std::string::npos)
        {
          gStyle->SetPalette(1);
          gPad->SetRightMargin(0.15);
          obj->SetOption("colz");
          obj->SetMaximum(1.0);
          obj->SetMinimum(0.90);
          return;
        }
      if( o.name.find( "HitEfficiency_D" ) != std::string::npos)
        {
          gStyle->SetPalette(1);
          gPad->SetRightMargin(0.15);
          obj->SetOption("colz");
          obj->SetMaximum(1.0);
          obj->SetMinimum(0.75);
          return;
        }
      if( o.name.find( "FedChLErrArray" ) != std::string::npos )
      {
        gPad->SetGrid();
	gPad->SetRightMargin(0.15);
        gStyle->SetPalette(1);
	obj->SetOption("colztext");
      }

      if( o.name.find( "FedETypeNErrArray" ) != std::string::npos )
      {
        gPad->SetGrid();
	gPad->SetLeftMargin(0.3);
	gPad->SetRightMargin(0.15);
        gStyle->SetPalette(1);
        obj->SetOption("colztext");
	if( obj->GetEntries() > 0. ) gPad->SetLogz(1);
	return;
      }

      if( o.name.find( "FedChNErrArray" ) != std::string::npos )
      {
        gPad->SetGrid();
	gPad->SetRightMargin(0.15);
        gStyle->SetPalette(1);
        obj->SetOption("colztext");
	if( obj->GetEntries() > 0. ) gPad->SetLogz(1);
      }
      if( o.name.find( "avgfedDigiOccvsLumi" ) != std::string::npos )
        {
          gPad->SetRightMargin(0.15);
          gStyle->SetPalette(1);
          obj->SetOption("colz");
          obj->SetMinimum(0.00001);
          obj->SetMaximum(0.8);
          return;
        }


      TH2F* obj2 = dynamic_cast<TH2F*>( o.object );

      if( o.name.find( "reportSummaryMap" ) != std::string::npos )
      {
        gPad->SetGrid();
        if(obj->GetNbinsX()==7) gPad->SetLeftMargin(0.3);
        dqm::utils::reportSummaryMapPalette(obj2);
        return;
      }
    }

  void preDrawTH1( TCanvas *, const VisDQMObject &o )
    {
      TH1* obj = dynamic_cast<TH1*>( o.object );
      assert( obj );

      // This applies to all
      gStyle->SetOptStat(111);
//       if ( obj->GetMaximum(1.e5) > 0. )
//       {
//         gPad->SetLogy(1);
//       }
//       else
//       {
//         gPad->SetLogy(0);
//       }

      TAxis* xa = obj->GetXaxis();
      TAxis* ya = obj->GetYaxis();
      xa->SetTitleOffset(0.7);
      xa->SetTitleSize(0.065);
      xa->SetLabelSize(0.065);
      ya->SetTitleOffset(0.75);
      ya->SetTitleSize(0.065);
      ya->SetLabelSize(0.065);

      if( o.name.find( "adcCOMB" ) != std::string::npos && obj->GetEntries() > 0. ){ gPad->SetLogy(1); gPad->SetTopMargin(0.15); }
      if( o.name.find( "chargeCOMB" ) != std::string::npos && obj->GetEntries() > 0. ){ obj->GetXaxis()->SetRange(1,51); gPad->SetLogy(1); gPad->SetTopMargin(0.15); }
      if( o.name.find( "OnTrack/charge_siPixelClusters" ) != std::string::npos ){ obj->GetXaxis()->SetRange(1,51); }
      if( o.name.find( "OffTrack/charge_siPixelClusters" ) != std::string::npos ){ obj->GetXaxis()->SetRange(1,51); }
      if( o.name.find( "OnTrack/size_siPixelClusters" ) != std::string::npos ){ obj->GetXaxis()->SetRange(1,41); }
      if( o.name.find( "OffTrack/size_siPixelClusters" ) != std::string::npos ){ obj->GetXaxis()->SetRange(1,41); }
      if( o.name.find( "barrelEventRate" ) != std::string::npos && obj->GetEntries() > 0. ) {gPad->SetLogx(1); gPad->SetLogy(1); gPad->SetTopMargin(0.15); gPad->SetRightMargin(0.15); }
      if( o.name.find( "endcapEventRate" ) != std::string::npos && obj->GetEntries() > 0. ) {gPad->SetLogx(1); gPad->SetLogy(1); gPad->SetTopMargin(0.15); gPad->SetRightMargin(0.15); }
      if( o.name.find( "ALLMODS_chargeCOMB" ) != std::string::npos ) obj->GetXaxis()->SetRange(1,51);
      if( o.name.find( "FEDEntries" ) != std::string::npos ) gStyle->SetOptStat(0);
//       if( o.name.find( "size_siPixelClusters" ) != std::string::npos && obj->GetEntries() > 0. ) gPad->SetLogx(1);
      if( o.name.find( "OnTrack" ) != std::string::npos && o.name.find( "charge" ) != std::string::npos ) obj->SetTitle("ClusterCharge_OnTrack");
      if( o.name.find( "OnTrack" ) != std::string::npos && o.name.find( "size" ) != std::string::npos ) obj->SetTitle("ClusterSize_OnTrack");
      if( o.name.find( "OffTrack" ) != std::string::npos && o.name.find( "charge" ) != std::string::npos ) obj->SetTitle("ClusterCharge_OffTrack");
      if( o.name.find( "OffTrack" ) != std::string::npos && o.name.find( "size" ) != std::string::npos ) obj->SetTitle("ClusterSize_OffTrack");
      if( o.name.find( "SUMDIG_adc_Barrel" ) != std::string::npos ){ obj->SetMaximum(130.); }
      if( o.name.find( "SUMDIG_ndigis_Barrel" ) != std::string::npos ){ obj->SetMaximum(14.); }
      if( o.name.find( "SUMDIG_adc_Endcap" ) != std::string::npos ){obj->SetMaximum(160.); }
      if( o.name.find( "SUMDIG_ndigis_Endcap" ) != std::string::npos ){obj->SetMaximum(5.); }
      if( o.name.find( "SUMCLU_charge_Barrel" ) != std::string::npos ){obj->SetMaximum(120.); }
      if( o.name.find( "SUMCLU_nclusters_Barrel" ) != std::string::npos ){obj->SetMaximum(3.); }
      if( o.name.find( "SUMCLU_size_Barrel" ) != std::string::npos ){obj->SetMaximum(11.); }
      if( o.name.find( "SUMCLU_charge_Endcap" ) != std::string::npos ){obj->SetMaximum(50.); }
      if( o.name.find( "SUMCLU_nclusters_Endcap" ) != std::string::npos ){obj->SetMaximum(1.6); }
      if( o.name.find( "SUMCLU_size_Endcap" ) != std::string::npos ){obj->SetMaximum(3.5); }
      if( o.name.find( "SUMOFF_adc_Barrel" ) != std::string::npos ){ obj->SetMinimum(70.); obj->SetMaximum(110.); }
      if( o.name.find( "SUMOFF_ndigis_Barrel" ) != std::string::npos ){ obj->SetMinimum(2.); obj->SetMaximum(14.); }
      if( o.name.find( "SUMOFF_adc_Endcap" ) != std::string::npos ){ obj->SetMinimum(90.); obj->SetMaximum(140.); }
      if( o.name.find( "SUMOFF_ndigis_Endcap" ) != std::string::npos ){ obj->SetMinimum(1.); obj->SetMaximum(6.); }


     // prettify for shifters:
//       if( o.name.find( "SUMDIG_ndigis_" ) != std::string::npos ||
//           o.name.find( "SUMCLU_nclusters_" ) != std::string::npos ||
// 	  o.name.find( "SUMCLU_size_" ) != std::string::npos ) gPad->SetLogy(0);
//       if( o.name.find( "SUMOFF_ndigis_" ) != std::string::npos ||
//           o.name.find( "SUMOFF_nclusters_" ) != std::string::npos ||
// 	  o.name.find( "SUMOFF_size_" ) != std::string::npos ) gPad->SetLogy(0);
    }

  void postDrawTH1( TCanvas *, const VisDQMObject &o )
    {
      TText tt;
      tt.SetTextSize(0.12);
      if (o.flags == 0) return;
      else
      {
        /*    if (o.flags & DQMNet::DQM_PROP_REPORT_ERROR)
              {
              tt.SetTextColor(2);
              tt.DrawTextNDC(0.5, 0.5, "Error");
              }
              else if (o.flags & DQMNet::DQM_PROP_REPORT_WARN)
              {
              tt.SetTextColor(5);
              tt.DrawTextNDC(0.5, 0.5, "Warning");
              }
              else if (o.flags & DQMNet::DQM_PROP_REPORT_OTHER)
              {
              tt.SetTextColor(1);
              tt.DrawTextNDC(0.5, 0.5, "Other ");
              }
              else
              {
              tt.SetTextColor(3);
              tt.DrawTextNDC(0.5, 0.5, "Ok ");
              }
        */
      }

      TH1* obj = dynamic_cast<TH1*>( o.object );
      assert( obj );

      if( o.name.find( "SUMOFF_adc_Barrel" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(0.,82.,192.,82.);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(0.,98.,192.,98.);
      }
      else if( o.name.find( "SUMDIG_adc_Barrel" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(0.,75.,768.,75.);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(0.,105.,768.,105.);
      }
      else if( o.name.find( "SUMOFF_adc_Endcap" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(0.,100.,96.,100.);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(0.,125.,96.,125.);
      }
      else if( o.name.find( "SUMDIG_adc_Endcap" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(0.,95.,672.,95.);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(0.,130.,672.,130.);
      }
      else if( o.name.find( "SUMOFF_ndigis_Barrel" ) != std::string::npos ){
        TLine tl; tl.SetLineColor(4); tl.DrawLine(0.,4.,192.,4.);
        TLine t2; t2.SetLineColor(4); t2.DrawLine(0.,13.5,192.,13.5);
      }
      else if( o.name.find( "SUMDIG_ndigis_Barrel" ) != std::string::npos ){
        TLine tl; tl.SetLineColor(4); tl.DrawLine(0.,3.,768.,3.);
        TLine t2; t2.SetLineColor(4); t2.DrawLine(0.,12.,768.,12.);
      }
      else if( o.name.find( "SUMOFF_ndigis_Endcap" ) != std::string::npos ){
        obj->SetMaximum(8.);
        TLine tl; tl.SetLineColor(4); tl.DrawLine(0.,2.5,96.,2.5);
        TLine t2; t2.SetLineColor(4); t2.DrawLine(0.,3.8,96.,3.8);
      }
      else if( o.name.find( "SUMDIG_ndigis_Endcap" ) != std::string::npos ){
        TLine tl; tl.SetLineColor(4); tl.DrawLine(0.,2.,672.,2.);
        TLine t2; t2.SetLineColor(4); t2.DrawLine(0.,3.6,672.,3.6);
      }
      else if( o.name.find( "SUMOFF_charge_OnTrack_Barrel" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(0.,4.,192.,4.);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(0.,40.,192.,40.);
      }
      else if( o.name.find( "SUMOFF_nclusters_OnTrack_Barrel" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(0.,0.9,192.,0.9);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(0.,2.,192.,2.);
      }
      else if( o.name.find( "SUMOFF_size_OnTrack_Barrel" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(0.,0.9,192.,0.9);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(0.,6.,192.,6.);
      }
      else if( o.name.find( "SUMCLU_charge_Barrel" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(0., 35.,768., 35.);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(0.,95.,768.,95.);
      }
      else if( o.name.find( "SUMCLU_nclusters_Barrel" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(0., 1.,768., 1.);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(0.,2.3,768.,2.3);
      }
      else if( o.name.find( "SUMCLU_size_Barrel" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(0.,2.5,768.,2.5);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(0.,9.,768.,9.);
      }
      else if( o.name.find( "SUMOFF_charge_OnTrack_Endcap" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(0., 7.,96., 7.);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(0.,50.,96.,50.);
      }
      else if( o.name.find( "SUMOFF_nclusters_OnTrack_Endcap" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(0.,0.9,96.,0.9);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(0.,2.,96.,2.);
      }
      else if( o.name.find( "SUMOFF_size_OnTrack_Endcap" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(0.,1.2,96.,1.2);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(0.,10.,96.,10.);
      }
      else if( o.name.find( "SUMCLU_charge_Endcap" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(0., 25.,672., 25.);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(0.,42.,672.,42.);
      }
      else if( o.name.find( "SUMCLU_nclusters_Endcap" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(0., 1.,672., 1.);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(0.,1.4,672.,1.4);
      }
      else if( o.name.find( "SUMCLU_size_Endcap" ) != std::string::npos ){
        TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(0., 1.8,672., 1.8);
        TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(0.,3.2,672.,3.2);
      }
      else if( o.name.find( "OnTrack/charge_siPixelClusters" ) != std::string::npos ){
        Int_t ibin = obj->GetMaximumBin();
        Double_t val = obj->GetBinContent(ibin);
        TLine tl; tl.SetLineColor(4); tl.DrawLine(21.,0.,21.,val);
      }
      else if( o.name.find( "averageDigiOccupancy" ) != std::string::npos ){
        TLine tl; tl.SetLineColor(4); tl.DrawLine(-0.5,0.6,39.5,0.6);
        TLine t2; t2.SetLineColor(4); t2.DrawLine(-0.5,1.6,39.5,1.6);
      }
//       else if( o.name.find( "OnTrack/size_siPixelClusters" ) != std::string::npos ||
//                o.name.find( "OffTrack/size_siPixelClusters" ) != std::string::npos ){
//         Int_t ibin = obj->GetMaximumBin();
//         Double_t val = obj->GetBinContent(ibin);
//         TLine tl; tl.SetLineColor(4); tl.DrawLine(10.,0.,10.,val);
//       }

    }

  void postDrawTH2( TCanvas *c, const VisDQMObject &o )
{

      TH2* obj = dynamic_cast<TH2*>( o.object );
      assert( obj );
      if( o.name.find( "TRKMAP" ) != std::string::npos && o.name.find( "Disc" ) != std::string::npos ){
        c->Clear();
	polarGraph(c, dynamic_cast<TH2F*>(obj));
      }

      if( o.name.find( "reportSummaryMap" ) != std::string::npos )
      {
	if(obj->GetNbinsX()==40){
	  TLine tl1; tl1.SetLineColor(4); tl1.DrawLine(32.,25.,32.,37.); //top right corner
	  TLine tl2; tl2.SetLineColor(4); tl2.DrawLine(32.,25.,40.,25.); //top right corner
	  //
	  TLine tl3; tl3.SetLineColor(4); tl3.DrawLine(3.,29.,3.,31.); //little boxes
	  TLine tl4; tl4.SetLineColor(4); tl4.DrawLine(5.,29.,5.,31.); //little boxes
	  TLine tl5; tl5.SetLineColor(4); tl5.DrawLine(3.,29.,5.,29.); //little boxes
	  TLine tl6; tl6.SetLineColor(4); tl6.DrawLine(3.,31.,5.,31.); //little boxes
	  //
	  TLine tl7; tl7.SetLineColor(4); tl7.DrawLine(11.,29.,11.,31.); //little boxes
	  TLine tl8; tl8.SetLineColor(4); tl8.DrawLine(13.,29.,13.,31.); //little boxes
	  TLine tl9; tl9.SetLineColor(4); tl9.DrawLine(11.,29.,13.,29.); //little boxes
	  TLine tl10; tl10.SetLineColor(4); tl10.DrawLine(11.,31.,13.,31.); //little boxes
	  //
	  TLine tl11; tl11.SetLineColor(4); tl11.DrawLine(19.,29.,19.,31.); //little boxes
	  TLine tl12; tl12.SetLineColor(4); tl12.DrawLine(21.,29.,21.,31.); //little boxes
	  TLine tl13; tl13.SetLineColor(4); tl13.DrawLine(19.,29.,21.,29.); //little boxes
	  TLine tl14; tl14.SetLineColor(4); tl14.DrawLine(19.,31.,21.,31.); //little boxes
	  //
	  TLine tl15; tl15.SetLineColor(4); tl15.DrawLine(27.,29.,27.,31.); //little boxes
	  TLine tl16; tl16.SetLineColor(4); tl16.DrawLine(29.,29.,29.,31.); //little boxes
	  TLine tl17; tl17.SetLineColor(4); tl17.DrawLine(27.,29.,29.,29.); //little boxes
	  TLine tl18; tl18.SetLineColor(4); tl18.DrawLine(27.,31.,29.,31.); //little boxes
	  //
	  TLine tl19; tl19.SetLineColor(4); tl19.DrawLine(3.,25.,3.,27.); //little boxes
	  TLine tl20; tl20.SetLineColor(4); tl20.DrawLine(5.,25.,5.,27.); //little boxes
	  TLine tl21; tl21.SetLineColor(4); tl21.DrawLine(3.,25.,5.,25.); //little boxes
	  TLine tl22; tl22.SetLineColor(4); tl22.DrawLine(3.,27.,5.,27.); //little boxes
	  //
	  TLine tl23; tl23.SetLineColor(4); tl23.DrawLine(11.,25.,11.,27.); //little boxes
	  TLine tl24; tl24.SetLineColor(4); tl24.DrawLine(13.,25.,13.,27.); //little boxes
	  TLine tl25; tl25.SetLineColor(4); tl25.DrawLine(11.,25.,13.,25.); //little boxes
	  TLine tl26; tl26.SetLineColor(4); tl26.DrawLine(11.,27.,13.,27.); //little boxes
	  //
	  TLine tl27; tl27.SetLineColor(4); tl27.DrawLine(19.,25.,19.,27.); //little boxes
	  TLine tl28; tl28.SetLineColor(4); tl28.DrawLine(21.,25.,21.,27.); //little boxes
	  TLine tl29; tl29.SetLineColor(4); tl29.DrawLine(19.,25.,21.,25.); //little boxes
	  TLine tl30; tl30.SetLineColor(4); tl30.DrawLine(19.,27.,21.,27.); //little boxes
	  //
	  TLine tl31; tl31.SetLineColor(4); tl31.DrawLine(27.,25.,27.,27.); //little boxes
	  TLine tl32; tl32.SetLineColor(4); tl32.DrawLine(29.,25.,29.,27.); //little boxes
	  TLine tl33; tl33.SetLineColor(4); tl33.DrawLine(27.,25.,29.,25.); //little boxes
	  TLine tl34; tl34.SetLineColor(4); tl34.DrawLine(27.,27.,29.,27.); //little boxes
	}
      }

}

};

static SiPixelRenderPlugin instance;
