/*
  \file L1TRenderPlugin.cc
  \\
  \\ Code shamelessly borrowed from J. Temple's HcalRenderPlugin.cc code,
  \\ which was shamelessly borrowed from S. Dutta's SiStripRenderPlugin.cc
  \\ code, G. Della Ricca and B. Gobbo's EBRenderPlugin.cc, and other existing
  \\ subdetector plugins
  \\ preDraw and postDraw methods now check whether histogram was a TH1
  \\ or TH2, and call a private method appropriate for the histogram type
*/

#include "DQM/DQMRenderPlugin.h"
#include "utils.h"

#include "TProfile2D.h"
#include "TROOT.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TStyle.h"
#include "TCanvas.h"
#include "TColor.h"
#include "TText.h"
#include "TBox.h"
#include "TLine.h"
#include "TLegend.h"
#include "TPRegexp.h"
#include <cassert>

#define REMATCH(pat, str) (TPRegexp(pat).MatchB(str))

class L1TRenderPlugin : public DQMRenderPlugin
{
  TH2F* dummybox;
  TBox* b_box_w;
  TBox* b_box_r;
  TBox* b_box_y;
  TBox* b_box_g;
  TBox* b_box_b;
  int l1t_pcol[60];
  float l1t_rgb[60][3];

public:
  virtual void initialise (int, char **)
    {
      // same as RenderPlugin default for now (no special action taken)

      //summaryText = new TH2C( "summaryText", "summaryText", 5, 1, 6, 4, 1, 5);
      //  float l1t_rgb[6][3] = {{1.00, 0.00, 0.00}, {0.00, 1.00, 0.00},
      //                     {1.00, 0.96, 0.00}, {0.50, 0.00, 0.00},
      //                     {0.00, 0.40, 0.00}, {0.94, 0.78, 0.00}};
      //   for( int i=0; i<6; i++ ) {
      //     TColor* color = gROOT->GetColor( 301+i );
      //     if ( ! color ) color = new TColor( 301+i, 0, 0, 0, "");
      //     color->SetRGB( rgb[i][0], rgb[i][1], rgb[i][2] );
      //   }
      //   for(int i=0; i<6; i++) cpal[i] = i + 301;
      dummybox = new  TH2F("dummyL1T","",22,-0.5,21.5,18,-0.5,17.5);

      for(int i=0; i<22; i++)
      {
        for(int j=0; j<18; j++)
        {
          dummybox->Fill(i,j,0.1);
        }
      }

      for( int i=0; i<60; i++ ){

	if ( i < 15 ){
	  l1t_rgb[i][0] = 1.00;
	  l1t_rgb[i][1] = 1.00;
	  l1t_rgb[i][2] = 1.00;
	}
	else if ( i < 30 ){
	  l1t_rgb[i][0] = 0.50;
	  l1t_rgb[i][1] = 0.80;
	  l1t_rgb[i][2] = 1.00;
	}
	else if ( i < 40 ){
	  l1t_rgb[i][0] = 1.00;
	  l1t_rgb[i][1] = 1.00;
	  l1t_rgb[i][2] = 1.00;
	}
	else if ( i < 57 ){
	  l1t_rgb[i][0] = 0.80+0.01*(i-40);
	  l1t_rgb[i][1] = 0.00+0.03*(i-40);
	  l1t_rgb[i][2] = 0.00;
	}
	else if ( i < 59 ){
	  l1t_rgb[i][0] = 0.80+0.01*(i-40);
	  l1t_rgb[i][1] = 0.00+0.03*(i-40)+0.15+0.10*(i-17-40);
	  l1t_rgb[i][2] = 0.00;
	}
	else if ( i == 59 ){
	  l1t_rgb[i][0] = 0.00;
	  l1t_rgb[i][1] = 0.80;
	  l1t_rgb[i][2] = 0.00;
	}

	l1t_pcol[i] = 1901+i;

	TColor* color = gROOT->GetColor( 1901+i );
	if( ! color ) color = new TColor( 1901+i, 0, 0, 0, "" );
	color->SetRGB( l1t_rgb[i][0], l1t_rgb[i][1], l1t_rgb[i][2] );
      }

      b_box_w = new TBox();
      b_box_r = new TBox();
      b_box_y = new TBox();
      b_box_g = new TBox();
      b_box_b = new TBox();

      b_box_g->SetFillColor(1960);
      b_box_y->SetFillColor(1959);
      b_box_r->SetFillColor(1941);
      b_box_w->SetFillColor(0);
      b_box_b->SetFillColor(1923);

    }

  virtual bool applies(const VisDQMObject &o, const VisDQMImgInfo &)
    {
      // determine whether core object is an L1T object
      if (o.name.find( "L1T/" ) != std::string::npos )
        return true;

      return false;
    }

  virtual void preDraw (TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &, VisDQMRenderInfo &)
    {
      c->cd();

      // object is TH2 histogram
      if( dynamic_cast<TH2F*>( o.object ) )
      {
        preDrawTH2F( c, o );
      }
      // object is TH1 histogram
      else if( dynamic_cast<TH1F*>( o.object ) )
      {
        preDrawTH1F( c, o );
      }
    }

  virtual void postDraw (TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &)
    {
      // object is TH2 histogram
      if( dynamic_cast<TH2F*>( o.object ) )
      {
        postDrawTH2F( c, o );
      }
      // object is TH1 histogram
      else if( dynamic_cast<TH1F*>( o.object ) )
      {
        postDrawTH1F( c, o );
      }
    }

private:
  void preDrawTH1F ( TCanvas *, const VisDQMObject &o )
    {
      // Do we want to do anything special yet with TH1F histograms?

      TH1F* obj = dynamic_cast<TH1F*>( o.object );
      assert (obj); // checks that object indeed exists

      gStyle->SetOptStat(111111);

      // GCT section
      if (o.name.find("L1TGCT") != std::string::npos) {

        // General style and stats
        //gStyle->SetPalette(1);
        //obj->SetOption("colz");
        gPad->SetGrid(1,1);
        gStyle->SetOptStat(11);

        // Axis labels

        // HF Ring Counts
        if (o.name.find("TowerCountNegEta") != std::string::npos ||
            o.name.find("TowerCountPosEta") != std::string::npos) {
          obj->GetXaxis()->SetTitle("HF Ring Tower Count");
          return;
        }

        // HF Ring Sums
        if (o.name.find("ETSumNegEta") != std::string::npos ||
            o.name.find("ETSumPosEta") != std::string::npos) {
          obj->GetXaxis()->SetTitle("HF Ring E_{T}");
          return;
        }

        // HF Ring ratios
        if( (o.name.find("HFRingRatioPosEta")!= std::string::npos ) ){
          obj->GetXaxis()->SetTitle("HF #eta + RING1 E_{T}/RING2 E_{T}");
          return;
        }

        // HF Ring ratios
        if( (o.name.find("HFRingRatioNegEta")!= std::string::npos) ){
          obj->GetXaxis()->SetTitle("HF #eta - RING1 E_{T}/RING2 E_{T}");
          return;
        }

        // Eta 1D
        if (o.name.find("Eta") != std::string::npos) {
          obj->GetXaxis()->SetTitle("#eta");
          obj->SetMinimum(0);
          return;
        }

        // Phi 1D
        if (o.name.find("Phi") != std::string::npos) {
          obj->GetXaxis()->SetTitle("#phi");
          obj->SetMinimum(0);
          return;
        }

        // Jet and electron ET
        if (o.name.find("Rank") != std::string::npos) {
          obj->GetXaxis()->SetTitle("E_{T}");
	  gPad->SetLogy(1);
          return;
        }

        // Energy sums overflow
        if (o.name.find("Of") != std::string::npos) {
          obj->GetXaxis()->SetTitle("Overflow Bit");
	  int bincheck = obj->GetNbinsX();
	  if( bincheck==2 ){
	    obj->GetXaxis()->SetBinLabel(1,"Off");
	    obj->GetXaxis()->SetBinLabel(2,"On");
	  }
          obj->GetXaxis()->SetNdivisions(2);
          return;
        }

        // Energy sums
        if (o.name.find("EtMiss") != std::string::npos) {
          obj->GetXaxis()->SetTitle("MET");
	  gPad->SetLogy(1);
          return;
        }

        // Energy sums
        if (o.name.find("HtMiss") != std::string::npos) {
          obj->GetXaxis()->SetTitle("MHT");
	  gPad->SetLogy(1);
          return;
        }

        // Energy sums
        if (o.name.find("EtTotal") != std::string::npos) {
          obj->GetXaxis()->SetTitle("Sum E_{T}");
	  gPad->SetLogy(1);
          return;
        }

        // Energy sums
        if (o.name.find("EtHad") != std::string::npos) {
          obj->GetXaxis()->SetTitle("H_{T}");
	  gPad->SetLogy(1);
          return;
        }

        return;
      }

      // rate histograms
      if ( (o.name.find("rate_algobit") != std::string::npos ||
	    o.name.find("rate_ttbit") != std::string::npos ||
	    o.name.find("Rate_AlgoBit") != std::string::npos ||
	    o.name.find("Rate_TechBit") != std::string::npos ||
	    o.name.find("Rate_Ratio") != std::string::npos ||
	    o.name.find("Integral_TechBit") != std::string::npos ||
	    o.name.find("Integral_AlgoBit") != std::string::npos ||
	    o.name.find("Physics_Trigger_Rate") != std::string::npos ||
	    o.name.find("Random_Trigger_Rate") != std::string::npos ||
	    o.name.find("Lost_Physics_Trigger_Rate") != std::string::npos ||
	    o.name.find("Deadtime_Percent") != std::string::npos ||
	    o.name.find("instTrigRate") != std::string::npos ||
	    o.name.find("instEventRate") != std::string::npos ||
	    o.name.find("Rate_Ratio") != std::string::npos ||
	    o.name.find("Number_of_Triggers") != std::string::npos ||
	    o.name.find("Physics_Triggers") != std::string::npos ||
	    o.name.find("Random_Triggers") != std::string::npos ||
	    o.name.find("Lost_Final_Trigger") != std::string::npos ||
	    o.name.find("DeadTime") != std::string::npos ||
	    o.name.find("Number_Resets") != std::string::npos ||
	    o.name.find("Orbit_Number") != std::string::npos ||
	    o.name.find("Number_of_Events") != std::string::npos ||
	    o.name.find("totAlgoRate") != std::string::npos ||
	    o.name.find("totTtRate") != std::string::npos ||
	    o.name.find("Instant_Lumi") != std::string::npos ||
	    o.name.find("Instant_Lumi_Err") != std::string::npos ||
	    o.name.find("Instant_Lumi_Qlty") != std::string::npos ||
	    o.name.find("Instant_Et_Lumi") != std::string::npos ||
	    o.name.find("Instant_Et_Lumi_Err") != std::string::npos ||
	    o.name.find("Instant_Et_Lumi_Qlty") != std::string::npos ||
	    o.name.find("Num_Orbits") != std::string::npos ||
	    o.name.find("Start_Orbit") != std::string::npos
	    ) )
	{
	  gStyle->SetOptStat(11);
	  obj->GetXaxis()->SetTitle("Luminosity Segment Number");
	  obj->GetYaxis()->SetTitle("Rate (Hz)");
	  int nbins = obj->GetNbinsX();
	  int maxRange = nbins;
	  for ( int i = nbins; i > 0; --i )
	    {
	      if ( obj->GetBinContent(i) != 0 )
		{
		  maxRange = i;
		  break;
		}
	    }
	  int minRange = 0;
	  for ( int i = 0; i <= nbins; ++i )
	    {
	      if ( obj->GetBinContent(i) != 0 )
		{
		  minRange = i;
		  break;
		}
	    }
	  minRange = ( minRange>0 ) ? minRange-1 : 0;
	  maxRange = ( nbins>maxRange ) ? maxRange+1 : nbins;

	  obj->GetXaxis()->SetRange(minRange, maxRange);

	  if ( (o.name.find("Integral_TechBit") != std::string::npos ||
		o.name.find("Integral_AlgoBit") != std::string::npos ||
		o.name.find("Rate_Ratio") != std::string::npos ||
		o.name.find("Deadtime_Percent") != std::string::npos ||
		o.name.find("Physics_Triggers") != std::string::npos ||
		o.name.find("Random_Triggers") != std::string::npos ||
		o.name.find("Orbit_Number") != std::string::npos ||
		o.name.find("Number_of_Events") != std::string::npos ||
		o.name.find("Lost_Final_Trigger") != std::string::npos ||
		o.name.find("DeadTime") != std::string::npos ||
		o.name.find("Number_Resets") != std::string::npos ||
		o.name.find("Instant_Lumi") != std::string::npos ||
		o.name.find("Instant_Lumi_Err") != std::string::npos ||
		o.name.find("Instant_Lumi_Qlty") != std::string::npos ||
		o.name.find("Instant_Et_Lumi") != std::string::npos ||
		o.name.find("Instant_Et_Lumi_Err") != std::string::npos ||
		o.name.find("Instant_Et_Lumi_Qlty") != std::string::npos ||
		o.name.find("Num_Orbits") != std::string::npos ||
		o.name.find("Start_Orbit") != std::string::npos
		) )
	    {
	      obj->GetYaxis()->SetTitle("");
	    }

	  else if ( (o.name.find("instTrigRate") != std::string::npos ||
		     o.name.find("instEventRate") != std::string::npos ||
		     o.name.find("Number_of_Triggers") != std::string::npos
		     ) )
	    {
	      obj->GetXaxis()->SetTitle("Time (sec)");
	    }
	}

      /// DTTF section
      if ( o.name.find("dttf_") != std::string::npos ) {
	// dqm::utils::reportSummaryMapPalette(obj);
	// obj->SetOption("colz");
	obj->GetYaxis()->SetRangeUser(0,
				      obj->GetBinContent(obj->GetMaximumBin() ) * 1.1 );

	if ( o.name.find("bx") != std::string::npos ) {

	  obj->GetXaxis()->SetNdivisions(3);
	  return;

	} else if ( o.name.find("charge" ) != std::string::npos ) {

	  obj->GetXaxis()->SetNdivisions(2);
	  return;

	} else if ( o.name.find("se" ) != std::string::npos ) {

	  if ( ( o.name.find("etaFine" ) != std::string::npos ) ||
	       ( o.name.find("nTracks" ) != std::string::npos ) ) {
	    obj->GetXaxis()->SetNdivisions(2);
	  }
	  return;

	} else if ( ( o.name.find("etaFine_fraction_wh") != std::string::npos )
                    || ( o.name.find("nTracks_wh" ) != std::string::npos ) ) {

	  obj->GetXaxis()->CenterLabels();
	  obj->GetXaxis()->SetNdivisions(12);
	  return;

	}

	return;

      }

      // Code used in SiStripRenderPlugin -- do we want similar defaults?

      /*
        gStyle->SetOptStat(0111);
        if ( obj->GetMaximum(1.e5) > 0. ) {
          gPad->SetLogy(1);
        } else {
          gPad->SetLogy(0);
        }
      */
    }

  void preDrawTH2F ( TCanvas *, const VisDQMObject &o )
    {
      TH2F* obj = dynamic_cast<TH2F*>( o.object );
      assert( obj );

      //put in preDrawTH2F
      if( o.name.find( "reportSummaryMap" )  != std::string::npos)
      {
        obj->SetStats( kFALSE );
//         dqm::utils::reportSummaryMapPalette(obj);
	obj->SetMaximum(1.0+1e-15);
	obj->SetMinimum(-2-1e-15);
	gStyle->SetPalette(60, l1t_pcol);

	obj->GetXaxis()->SetBinLabel(1,"Data");
	obj->GetXaxis()->SetBinLabel(2,"Emulator");
	obj->GetXaxis()->SetLabelSize(0.1);

        obj->SetOption("col");
        obj->SetTitle("L1T Report Summary Map");

        obj->GetXaxis()->CenterLabels();
        obj->GetYaxis()->CenterLabels();

        return;
      }

      gStyle->SetCanvasBorderMode( 0 );
      gStyle->SetPadBorderMode( 0 );
      gStyle->SetPadBorderSize( 0 );

      // I don't think we want to set stats to 0 for Hcal
      //gStyle->SetOptStat( 0 );
      //obj->SetStats( kFALSE );

      // Use same labeling format as SiStripRenderPlugin.cc
      TAxis* xa = obj->GetXaxis();
      TAxis* ya = obj->GetYaxis();

      xa->SetTitleOffset(0.7);
      xa->SetTitleSize(0.05);
      xa->SetLabelSize(0.04);

      ya->SetTitleOffset(0.7);
      ya->SetTitleSize(0.05);
      ya->SetLabelSize(0.04);

      // Now the important stuff -- set 2D hist drawing option to "colz"
      gStyle->SetPalette(1);
      obj->SetOption("colz");

      //gStyle->SetOptStat(0);

/*      if(
        o.name.find( "RctEmIsoEmEtEtaPhi" ) != std::string::npos ||
        o.name.find( "RctEmIsoEmOccEtaPhi" ) != std::string::npos ||
        o.name.find( "RctEmNonIsoEmEtEtaPhi" ) != std::string::npos ||
        o.name.find( "RctEmNonIsoEmOccEtaPhi" ) != std::string::npos ||
        o.name.find( "RctRegionsEtEtaPhi" ) != std::string::npos ||
        o.name.find( "RctRegionsOccEtaPhi" ) != std::string::npos
         ) */
      if(
        ( o.name.find( "Rct" ) != std::string::npos &&
	  (o.name.find( "Jet" ) != std::string::npos ||
           o.name.find( "IsoEm" ) != std::string::npos )) &&
        o.name.find( "EtaPhi" ) != std::string::npos
        )
      {
        gPad->SetGrid(1,1);
        gStyle->SetOptStat(11);
        obj->GetXaxis()->SetTitle("GCT eta");
        obj->GetYaxis()->SetTitle("GCT phi");
        return;
      }

      // GCT section
      if (o.name.find("L1TGCT") != std::string::npos) {

        // General style and stats
        gStyle->SetPalette(1);
        obj->SetOption("colz");
        gPad->SetGrid(1,1);
        gStyle->SetOptStat(11);

        // Axis labels

        // Energy sums MET and MHT correlations
        if (o.name.find("EtMissHtMissPhiCorr") != std::string::npos) {
          obj->GetXaxis()->SetTitle("MET #phi");
          obj->GetYaxis()->SetTitle("MHT #phi");
          return;
        }

        // Eta phi 2D plots
        if (o.name.find("EtaPhi") != std::string::npos) {
          obj->GetXaxis()->SetTitle("#eta");
          obj->GetYaxis()->SetTitle("#phi");
          return;
        }

        // BX plots
        if (o.name.find("Bx") != std::string::npos) {
          obj->GetXaxis()->SetTitle("BX");
          obj->GetXaxis()->SetNdivisions(5);
          obj->GetYaxis()->SetTitle("E_{T}");
	  int bincheck = obj->GetNbinsX();
	  if( bincheck==5 ){
	    obj->GetXaxis()->SetBinLabel(1,"-2");
	    obj->GetXaxis()->SetBinLabel(2,"-1");
	    obj->GetXaxis()->SetBinLabel(3,"0");
	    obj->GetXaxis()->SetBinLabel(4,"+1");
	    obj->GetXaxis()->SetBinLabel(5,"+2");
	  }
          return;
        }

       // Energy sums MET and MHT correlations
        if (o.name.find("EtMissHtMissCorr") != std::string::npos) {
          obj->GetXaxis()->SetTitle("MET");
          obj->GetYaxis()->SetTitle("MHT");
          return;
        }

       // Energy sums Sum ET and HT correlations
        if (o.name.find("EtTotalEtHadCorr") != std::string::npos) {
          obj->GetXaxis()->SetTitle("Sum E_{T}");
          obj->GetYaxis()->SetTitle("H_{T}");
          return;
        }

        // HF Ring correlations
        if (o.name.find("TowerCountCorr") != std::string::npos ||
            o.name.find("HFRing1Corr") != std::string::npos ||
            o.name.find("HFRing2Corr") != std::string::npos) {
          obj->GetXaxis()->SetTitle("HF #eta +");
          obj->GetYaxis()->SetTitle("HF #eta -");
          return;
        }

        return;
      }

      /// DTTF section
      if ( o.name.find("dttf") != std::string::npos ) {

        gPad->SetGrid(1,1);
	gStyle->SetOptStat(0);

 	if ( o.name.find("bx" ) != std::string::npos ) {

 	  obj->GetYaxis()->CenterLabels();
	  obj->GetYaxis()->SetNdivisions(3, true);

	  if ( o.name.find("wh") != std::string::npos ) {
	    obj->GetXaxis()->SetNdivisions(12, true);
	    obj->GetXaxis()->CenterLabels();
	  }

	  return;

	} else if ( o.name.find("gmt") != std::string::npos ) {

	  // gStyle->SetOptStat(110010);
	  obj->GetYaxis()->SetNdivisions(12);
	  obj->GetYaxis()->CenterLabels();
	  return;

	} else if ( o.name.find("phi_vs_eta") != std::string::npos ) {

	  // if ( o.name.find("wh") != std::string::npos ) {
	  //   gStyle->SetOptStat(110010);
	  // }
	  obj->GetYaxis()->SetNdivisions(12, false);
	  return;

	  //obj->GetXaxis()->SetNdivisions(8, false);

	} else if ( o.name.find("highQual" ) != std::string::npos ) {

	  obj->GetYaxis()->SetNdivisions(12, true);
 	  obj->GetZaxis()->SetRangeUser(0, 1);
	  obj->GetYaxis()->CenterLabels();
	  return;

	} else if ( o.name.find("occupancy" ) != std::string::npos ) {

	  obj->GetYaxis()->SetNdivisions(12, true);
	  obj->GetYaxis()->CenterLabels();
	  if ( o.name.find("tracks_occupancy_summary" ) != std::string::npos )
	    obj->GetZaxis()->SetRangeUser(0, 0.03);
	  return;

	} else if  ( o.name.find("quality" ) != std::string::npos ) {

  	  obj->GetYaxis()->SetNdivisions(8, true);
 	  obj->GetXaxis()->SetNdivisions(12, false);
 	  obj->GetXaxis()->CenterLabels();
	  obj->GetYaxis()->CenterLabels();
	  return;

	}

	//  } else if  ( o.name.find("Summary" ) != std::string::npos ) {
        //  gPad->SetGrid(1,1);
        //       obj->GetXaxis()->SetLabelSize(0.07);
        //       obj->GetYaxis()->SetLabelSize(0.07);
        //  obj->GetXaxis()->LabelsOption("h");

        //  obj->SetMaximum(5.0);

        //  int colorError1[5];
        //  colorError1[0] = 416;// kGreen
        //  colorError1[1] = 400;// kYellow
        //  colorError1[2] = 800;// kOrange
        //  colorError1[3] = 625;
        //  colorError1[4] = 632;// kRed
        //  gStyle->SetPalette(5, colorError1);

        //  gStyle->SetPalette(6, cpal);
	//  }

	return;

      }

      else if(REMATCH("BX_Correlation_*", o.name)) {
        TAxis* yBX = obj->GetYaxis();
        yBX->SetTitleOffset(1.1);
        return;
      }

      if(o.name.find("CSCTF_Chamber_Occupancies") != std::string::npos)
      {
        gStyle->SetOptStat(11);
        return;
      }
      if(o.name.find("CSCTF_occupancies") != std::string::npos)
      {
        gStyle->SetOptStat(11);
        return;
      }
      if(o.name.find("GMT_etaphi") != std::string::npos)
      {
        gStyle->SetOptStat(11);
        return;
      }
      if(o.name.find("BX_diffvslumi") != std::string::npos)
	{
	  obj->GetXaxis()->SetTitle("Luminosity Segment Number");
	  obj->GetYaxis()->SetTitle("#Delta bx");
	  //obj->GetXaxis()->SetNdivisions(6,true);
	  obj->GetYaxis()->SetNdivisions(9,true);
	  obj->GetYaxis()->CenterLabels();
	  //gPad->SetGrid(1,1);

	  int nxbins = obj->GetNbinsX();
	  int nybins = obj->GetNbinsY();
	  int maxRange = nxbins;
	  bool ynonempty = false;
	  for ( int i = nxbins; i > 0; --i ){
	    for ( int j = nybins; j > 0; --j ){
	      if ( obj->GetBinContent(i,j) != 0 ){
		ynonempty = true;
		break;
	      }
	    }
	    if(ynonempty){
	      maxRange = i;
	      break;
	    }
	  }
	  int minRange = 0;
	  ynonempty = false;
	  for ( int i = 0; i <= nxbins; ++i ){
	    for ( int j = 0; j <= nybins; ++j ){
	      if ( obj->GetBinContent(i,j) != 0 ){
		ynonempty = true;
		break;
	      }
	    }
	    if(ynonempty){
	      minRange = i;
	      break;
	    }
	  }
	  minRange = ( minRange>0 ) ? minRange-1 : 0;
	  maxRange = ( nxbins>maxRange ) ? maxRange+1 : nxbins;

	  obj->GetXaxis()->SetRange(minRange, maxRange);

	  return;
	}

    }

  void postDrawTH1F( TCanvas *, const VisDQMObject & )
    {

      /*
        // Add error/warning text to 1-D histograms.  Do we want this at this time?
        TText tt;
        tt.SetTextSize(0.12);

        if (o.flags == 0)
          return;
        else
        {
          if (o.flags & DQMNet::DQM_PROP_REPORT_ERROR)
          {
            tt.SetTextColor(2); // error color = RED
            tt.DrawTextNDC(0.5, 0.5, "Error");
          } // DQM_PROP_REPORT_ERROR
          else if (o.flags & DQMNet::DQM_PROP_REPORT_WARN)
          {
            tt.SetTextColor(5);
            tt.DrawTextNDC(0.5, 0.5, "Warning"); // warning color = YELLOW
          } // DQM_PROP_REPORT_WARN
          else if (o.flags & DQMNet::DQM_PROP_REPORT_OTHER)
          {
            tt.SetTextColor(1); // other color = BLACK
            tt.DrawTextNDC(0.5, 0.5, "Other ");
          } // DQM_PROP_REPORT_OTHER
          else
          {
            tt.SetTextColor(3);
            tt.DrawTextNDC(0.5, 0.5, "Ok ");
          } //else
        } // else (  o.flags != 0  )
      */
    }

  void postDrawTH2F( TCanvas *, const VisDQMObject &o )
    {

      TH2F* obj = dynamic_cast<TH2F*>( o.object );
      assert( obj );

      TBox* b_box = new TBox();
      TLine* l_line = new TLine();
      TText* t_text = new TText();

      if( o.name.find( "reportSummaryMap" )  != std::string::npos)
      {
	t_text->DrawText(1.5,11.3,"GT");
	t_text->DrawText(1.5,10.3,"Muons");
	t_text->DrawText(1.5,9.3, "Jets");
	t_text->DrawText(1.5,8.3, "TauJets");
	t_text->DrawText(1.5,7.3, "IsoEM");
	t_text->DrawText(1.5,6.3, "NonIsoEM");
	t_text->DrawText(1.5,5.3, "MET");

	t_text->DrawText(2.5,11.3,"GLT");
	t_text->DrawText(2.5,10.3,"GMT");
	t_text->DrawText(2.5,9.3, "RPC");
	t_text->DrawText(2.5,8.3, "CSCTPG");
	t_text->DrawText(2.5,7.3, "CSCTF");
	t_text->DrawText(2.5,6.3, "DTTPG");
	t_text->DrawText(2.5,5.3, "DTTF");
	t_text->DrawText(2.5,4.3, "HCAL");
	t_text->DrawText(2.5,3.3, "ECAL");
	t_text->DrawText(2.5,2.3, "GCT");
	t_text->DrawText(2.5,1.3, "RCT");

	int NbinsX = obj->GetNbinsX();
	int NbinsY = obj->GetNbinsY();

	std::vector<std::vector<double> > TrigResult( NbinsY, std::vector<double>(NbinsX) );

	for( int i=0; i<NbinsX; i++ ){
	  for( int j=0; j<NbinsY; j++ ) TrigResult[j][i] = obj->GetBinContent(i+1,j+1);
	}

	char* trig_result = new char[20];

	for( int j=0; j<NbinsY; j++ ){
	  if( TrigResult[j][0]>-0.5 ){
	    sprintf(trig_result,"%4.2f",TrigResult[j][0]);
	    t_text->DrawText(1.2,j+1.3,trig_result);
	  }
	  if( TrigResult[j][1]>-0.5 ){
	    sprintf(trig_result,"%4.2f",TrigResult[j][1]);
	    t_text->DrawText(2.2,j+1.3,trig_result);
	  }
	}
	delete [] trig_result;

	b_box->SetFillColor(17);
	b_box->DrawBox(1,1,2,5);

	l_line->SetLineWidth(2);
	l_line->DrawLine(2,1,2,12);

	l_line->DrawLine(2,4,3,4);
	l_line->DrawLine(2,3,3,3);
	l_line->DrawLine(2,2,3,2);
	l_line->DrawLine(2,1,3,1);

	l_line->DrawLine(1,5,3,5);
	l_line->DrawLine(1,6,3,6);
	l_line->DrawLine(1,7,3,7);
	l_line->DrawLine(1,8,3,8);
	l_line->DrawLine(1,9,3,9);
	l_line->DrawLine(1,10,3,10);
	l_line->DrawLine(1,11,3,11);

	TLegend* leg = new TLegend(0.16, 0.11, 0.44, 0.38);
	leg->AddEntry(b_box_g,"Good",   "f");
// 	leg->AddEntry(b_box_y,"Warning","f");
	leg->AddEntry(b_box_r,"Error",  "f");
	leg->AddEntry(b_box_b,"Waiting","f");
	leg->AddEntry(b_box_w,"Masked", "f");
	leg->Draw();

	return;
      }

      if( o.name.find( "CSCTF_Chamber_Occupancies" )  != std::string::npos)
      {

	b_box->SetFillColor(1);
	b_box->SetFillStyle(3013);

	l_line->SetLineWidth(1);

	int Num=6;
	for( int i=0; i<Num; i++){
	  double x1s = double(0.25+i*0.1*9);
	  double x1e = double(0.85+i*0.1*9);

	  double y1s = 3.5;
	  double y1e = 4.5;
	  double y2s = -5.5;
	  double y2e = -4.5;

	  // Draw boxes
	  b_box->DrawBox(x1s,y1s,x1e,y1e);
	  b_box->DrawBox(x1s,y2s,x1e,y2e);

	  // Draw horizontal boundary lines
	  l_line->DrawLine(x1s, y1s, x1e, y1s);
	  l_line->DrawLine(x1s, y2e, x1e, y2e);

	  // Draw vertical boundary lines
	  l_line->DrawLine(x1s, y1s, x1s, y1e);
	  l_line->DrawLine(x1s, y2s, x1s, y2e);

	  l_line->DrawLine(x1e, y1s, x1e, y1e);
	  l_line->DrawLine(x1e, y2s, x1e, y2e);
	}

	return;
      }

      if(
        ( o.name.find( "Rct" ) != std::string::npos ||
	  o.name.find( "Jet" ) != std::string::npos ||
	  o.name.find( "IsoEm" ) != std::string::npos ) &&
        o.name.find( "EtaPhi" ) != std::string::npos
        )
      {

	dummybox->Draw("box,same");

	if(
	   o.name.find( "IsoEm" ) != std::string::npos ||
	   o.name.find( "CenJet" ) != std::string::npos ||
	   o.name.find( "TauJet" ) != std::string::npos
	   )
	{
	  l_line->SetLineWidth(1);
	  l_line->DrawLine(3.5,-0.5,3.5,17.5);
	  l_line->DrawLine(17.5,-0.5,17.5,17.5);

	  b_box->SetFillColor(1);
	  b_box->SetFillStyle(3013);

	  b_box->DrawBox(-0.5,-0.5,3.5,17.5);
	  b_box->DrawBox(17.5,-0.5,21.5,17.5);
	}

	if (o.name.find( "ForJet" ) != std::string::npos)
	{
	  l_line->SetLineWidth(1);
	  l_line->DrawLine(3.5,-0.5,3.5,17.5);
	  l_line->DrawLine(17.5,-0.5,17.5,17.5);

	  b_box->SetFillColor(1);
	  b_box->SetFillStyle(3013);
          b_box->DrawBox(3.5,-0.5,17.5,17.5);
	}

	return;
      }

      // nothing to put here just yet
      // in the future, we can add text output based on error status,
      // or set bin range based on filled histograms, etc.
      // Maybe add a big "OK" sign to histograms with no entries (i.e., no errors)?

      //int nSubsystems = 20;

      //TPaveText *pt[nSubsystems];

      //for(int i =0; i<nSubsystems; i++) {
      // relative to pad dimensions
      //TText *text = pt->AddText("ECAL");
      //     switch(i) {
      //     case 0 :
      //       pt[i]= new TPaveText(0.14, 0.20, 0.14, 0.20, "NDC");
      //       pt[i]->AddText("ECAL");
      //       break;
      //     case 1 :
      //       pt[i]= new TPaveText(0.30, 0.20, 0.30,0.20, "NDC");
      //       pt[i]->AddText("HCAL");
      //       break;
      //     case 2 :
      //       pt[i]= new TPaveText(0.47, 0.20, 0.47,0.20, "NDC");
      //       pt[i]->AddText("RCT");
      //       break;
      //     case 3 :
      //       pt[i]= new TPaveText(0.63, 0.20, 0.63,0.20, "NDC");
      //       pt[i]->AddText("GCT");
      //       break;
      //     case 4 :
      //       pt[i]= new TPaveText(0.77, 0.20, 0.77,0.20, "NDC");
      //       pt[i]->AddText("DTTPG");
      //       break;
      //     case 5 :
      //       pt[i]= new TPaveText(0.77, 0.20, 0.77,0.20, "NDC");
      //       pt[i]->AddText("DTTF");
      //       break;
      //     case 6 :
      //       pt[i]= new TPaveText(0.77, 0.20, 0.77,0.20, "NDC");
      //       pt[i]->AddText("CSCTPG");
      //       break;
      //     case 7 :
      //       pt[i]= new TPaveText(0.77, 0.20, 0.77,0.20, "NDC");
      //       pt[i]->AddText("CSCTF");
      //       break;
      //     case 8 :
      //       pt[i]= new TPaveText(0.77, 0.20, 0.77,0.20, "NDC");
      //       pt[i]->AddText("DTTPG");
      //       sprintf(histo,"L1T_RPC");     break;
      //     case 9 :
      //       pt[i]= new TPaveText(0.77, 0.20, 0.77,0.20, "NDC");
      //       pt[i]->AddText("DTTPG");
      //       sprintf(histo,"L1T_GMT");     break;
      //     case 10 :
      //       pt[i]= new TPaveText(0.77, 0.20, 0.77,0.20, "NDC");
      //       pt[i]->AddText("DTTPG");
      //       sprintf(histo,"L1T_GT");      break;
      //     case 11 :
      //       pt[i]= new TPaveText(0.77, 0.20, 0.77,0.20, "NDC");
      //       pt[i]->AddText("DTTPG");
      //       sprintf(histo,"L1T_RPCTG");   break;
      //     case 12 :
      //       pt[i]= new TPaveText(0.77, 0.20, 0.77,0.20, "NDC");
      //       pt[i]->AddText("DTTPG");
      //       sprintf(histo,"L1T_EMUL");    break;
      //     case 13 :
      //       pt[i]= new TPaveText(0.77, 0.20, 0.77,0.20, "NDC");
      //       pt[i]->AddText("DTTPG");
      //       sprintf(histo,"L1T_Timing");  break;
      //     case 14 :
      //       pt[i]= new TPaveText(0.77, 0.20, 0.77,0.20, "NDC");
      //       pt[i]->AddText("DTTPG");
      //       sprintf(histo,"L1T_Test1");   break;
      //     case 15 :
      //       pt[i]= new TPaveText(0.77, 0.20, 0.77,0.20, "NDC");
      //       pt[i]->AddText("DTTPG");
      //       sprintf(histo,"L1T_Test2");   break;
      //     case 16 :
      //       pt[i]= new TPaveText(0.77, 0.20, 0.77,0.20, "NDC");
      //       pt[i]->AddText("DTTPG");
      //       sprintf(histo,"L1T_Test3");   break;
      //     case 17 :
      //       pt[i]= new TPaveText(0.77, 0.20, 0.77,0.20, "NDC");
      //       pt[i]->AddText("DTTPG");
      //       sprintf(histo,"L1T_Test4");break;
      //     case 18 :
      //       pt[i]= new TPaveText(0.77, 0.20, 0.77,0.20, "NDC");
      //       pt[i]->AddText("DTTPG");
      //       sprintf(histo,"L1T_Test5");   break;
      //     case 19 :
      //       pt[i]= new TPaveText(0.77, 0.20, 0.77,0.20, "NDC");
      //       pt[i]->AddText("DTTPG");
      //       sprintf(histo,"L1T_Test6");   break;
      //     }
      //   TPaveText *pt[8];

      //   pt[i]->SetFillColor(0); // text is black on white
      //   pt[i]->SetTextSize(0.04);
      //   pt[i]->SetTextAlign(12);
      //   pt[i]->SetFillStyle(4000);

      //   pt[i]->Draw("same");
      //to draw your text object
      //  }

    }
};

static L1TRenderPlugin instance;
