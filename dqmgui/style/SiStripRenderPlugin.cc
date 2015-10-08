/*!
  \file SiStripRenderPlugin
  \brief Display Plugin for SiStrip DQM Histograms
  \author S. Dutta
  \version $Revision: 1.45 $
  \date $Date: 2011/11/16 17:35:55 $
*/

#include "DQM/DQMRenderPlugin.h"
#include "utils.h"

#include "TProfile2D.h"
#include "TProfile.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TStyle.h"
#include "TCanvas.h"
#include "TColor.h"
#include "TText.h"
#include "TLine.h"
#include "TMath.h"
#include <cassert>

class SiStripRenderPlugin : public DQMRenderPlugin
{
public:
  virtual bool applies( const VisDQMObject &o, const VisDQMImgInfo & )
    {
      if ((o.name.find( "SiStrip/" ) == std::string::npos) &&
	  (o.name.find( "Tracking/" ) == std::string::npos))
         return false;

      if( o.name.find( "/EventInfo/" ) != std::string::npos )
        return true;

      if( o.name.find( "/MechanicalView/" ) != std::string::npos )
        return true;

      if( o.name.find( "/ReadoutView/" ) != std::string::npos )
        return true;

      if( o.name.find( "/TrackParameters/" ) != std::string::npos )
        return true;

      if( o.name.find( "/MessageLog/" ) != std::string::npos )
        return true;

      if( o.name.find( "/BaselineValidator/" ) != std::string::npos )
        return true;

      return false;
    }

  virtual void preDraw( TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &, VisDQMRenderInfo & )
    {
      c->cd();

      if( dynamic_cast<TH2F*>( o.object ) )
      {
        preDrawTH2F( c, o );
      }
      else if( dynamic_cast<TH1F*>( o.object ) )
      {
        preDrawTH1F( c, o );
      }
      else if( dynamic_cast<TProfile2D*>( o.object ) )
      {
        preDrawTProfile2D( c, o );
      }
      else if( dynamic_cast<TProfile*>( o.object ) )
      {
        preDrawTProfile( c, o );
      }
    }

  virtual void postDraw( TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo & )
    {
      c->cd();

      if( dynamic_cast<TH1F*>( o.object ) )
      {
        postDrawTH1F( c, o );
      }
      if( dynamic_cast<TH2F*>( o.object ) )
      {
        postDrawTH2F( c, o );
      }
      if( dynamic_cast<TProfile*>( o.object ) )
      {
        postDrawTProfile( c, o );
      }
    }

private:
  void preDrawTH2F( TCanvas *c, const VisDQMObject &o )
    {
      TH2F* obj = dynamic_cast<TH2F*>( o.object );
      assert( obj );

      // This applies to all
      gStyle->SetCanvasBorderMode( 0 );
      gStyle->SetPadBorderMode( 0 );
      gStyle->SetPadBorderSize( 0 );
      //    (data->pad)->SetLogy( 0 );;
      //  gStyle->SetOptStat( 0 );

      TAxis* xa = obj->GetXaxis();
      TAxis* ya = obj->GetYaxis();

      xa->SetTitleOffset(0.7);
      xa->SetTitleSize(0.05);
      xa->SetLabelSize(0.04);

      ya->SetTitleOffset(0.7);
      ya->SetTitleSize(0.05);
      ya->SetLabelSize(0.04);

      if( o.name.find( "PedsEvolution" ) != std::string::npos)
      {
        gStyle->SetOptStat( 1111 );
        obj->SetStats( kTRUE );
        obj->SetOption( "lego2" );
        return;
      }
      if( o.name.find( "CMDistribution " )  != std::string::npos)
      {
        obj->GetXaxis()->LabelsOption("d");
        obj->SetOption( "lego2" );
        return;
      }
      if( o.name.find( "CMSlopeDistribution " )  != std::string::npos)
      {
        obj->GetXaxis()->LabelsOption("d");
        obj->SetOption( "lego2" );
        return;
      }
      if( o.name.find( "PedestalDistribution " )  != std::string::npos)
      {
        obj->GetXaxis()->LabelsOption("d");
        obj->SetOption( "lego" );
        return;
      }
      if( o.name.find( "reportSummaryMap" )  != std::string::npos)
      {
        obj->SetStats( kFALSE );
        dqm::utils::reportSummaryMapPalette(obj);
        obj->SetOption("colztext");
        return;
      }
      if( o.name.find( "detFractionReportMap" )  != std::string::npos)
      {
        obj->SetStats( kFALSE );
        dqm::utils::reportSummaryMapPalette(obj);
        obj->SetOption("colztext");
        return;
      }
      if( o.name.find( "sToNReportMap" )  != std::string::npos)
      {
        obj->SetStats( kFALSE );
        dqm::utils::reportSummaryMapPalette(obj);
        obj->SetOption("colztext");
        return;
      }
      if( o.name.find( "SummaryOfCabling" )  != std::string::npos)
      {
        obj->SetStats( kFALSE );
        obj->SetOption("text");
        return;
      }

      if( o.name.find( "DataPresentInLastLS" )  != std::string::npos)
      {
        obj->SetStats( kFALSE );
        dqm::utils::reportSummaryMapPalette(obj);
        obj->SetOption("colztext");
        return;
      }

	  if( o.name.find( "StripClusVsPixClus" )  != std::string::npos)
      {
        obj->SetStats( kFALSE );
        gStyle->SetPalette(1,0);
        obj->SetOption("colz");
	return;
      }

	  if( o.name.find( "ClusterWidths_vs_Amplitudes" )  != std::string::npos)
      {
        obj->SetStats( kFALSE );
        gStyle->SetPalette(1,0);
		c->SetLogz(1);
        obj->SetOption("colz");
	return;
      }

	  if( o.name.find( "SeedPhiVsEta" )  != std::string::npos)
      {
        obj->SetStats( kFALSE );
        gStyle->SetPalette(1,0);
        obj->SetOption("colz");
	return;
      }

	if( o.name.find( "TrackCandPhiVsEta" )  != std::string::npos)
      {
        obj->SetStats( kFALSE );
        gStyle->SetPalette(1,0);
        obj->SetOption("colz");
	return;
      }

      if( o.name.find( "SeedsVsClusters" )  != std::string::npos)
      {
        obj->SetStats( kFALSE );
        gStyle->SetPalette(1,0);
        obj->SetOption("colz");
	return;
      }

      if( o.name.find( "TracksVs" )  != std::string::npos)
      {
        obj->SetStats( kFALSE );
        gStyle->SetPalette(1,0);
        obj->SetOption("colz");
	return;
      }

      if( o.name.find( "DeltaBx_vs_ApvCycle" )  != std::string::npos)
      {
        obj->SetStats( kFALSE );
        gStyle->SetPalette(1,0);
        obj->SetOption("colz");
	return;
      }

      if( o.name.find( "ADCvsAPVs" )  != std::string::npos)
      {
        obj->SetStats( kFALSE );
        gStyle->SetPalette(1,0);
        obj->SetOption("colz");
	return;
      }
      if( o.name.find( "FedIdVsApvId" )  != std::string::npos)
	{
	  obj->SetStats( kFALSE );
	  gStyle->SetPalette(1,0);
	  obj->SetOption("colz");
	return;
	}
      if( o.name.find( "DataPresentInLS" )  != std::string::npos)
	{
	  obj->SetStats( kFALSE );
	  dqm::utils::reportSummaryMapPalette(obj);
	  obj->SetOption("colz");
	return;
	}
      if( o.name.find( "ErrorsVsModules" )  != std::string::npos)
	{
	  gStyle->SetPalette(1,0);
	  gStyle->SetOptStat(10);
	  obj->SetOption("colz");

	  xa->SetTitleOffset(1.5);
	  ya->SetTitleOffset(1.5);

	  gPad->SetLeftMargin(0.2);
	  gPad->SetBottomMargin( 0.2 );

	  return;
	}

      return;
    }

  void preDrawTH1F( TCanvas *, const VisDQMObject &o )
    {
      TH1F* obj = dynamic_cast<TH1F*>( o.object );
      assert( obj );

      // This applies to all
      gStyle->SetOptStat(1110);
      //  if ( obj->GetMaximum(1.e5) > 0. ) {
      //    gPad->SetLogy(1);
      //  } else {
      //   gPad->SetLogy(0);
      //  }
      TAxis* xa = obj->GetXaxis();
      TAxis* ya = obj->GetYaxis();

      xa->SetTitleOffset(0.7);
      xa->SetTitleSize(0.05);
      xa->SetLabelSize(0.04);

      ya->SetTitleOffset(0.7);
      ya->SetTitleSize(0.04);
      ya->SetLabelSize(0.04);

      if( o.name.find( "Summary_MeanNumberOfDigis" )  != std::string::npos)
      {
        obj->SetStats( kFALSE );
  //        obj->SetMaximum(5.0); // COSMICS
  obj->SetMaximum(20.0); // COLLISIONS run179828 (2011highPU)
  //obj->SetMaximum(120.0); // HEAVY IONS
        obj->SetMinimum(-0.1);
	//do not return, because Summary_MeanNumberOfDigis__TOB string (below) is found here as well
	//return;
      }
      if( o.name.find( "Summary_MeanNumberOfDigis__TOB" )  != std::string::npos)
      {
        obj->SetStats( kFALSE );
  obj->SetMaximum(10.0); // COLLISIONS run179828 (2011highPU)
  //obj->SetMaximum(5.0); // COSMICS
  //obj->SetMaximum(70.0); // HEAVY IONS
        obj->SetMinimum(-0.1);
        return;
      }
      if( o.name.find( "Summary_MeanNumberOfClusters" )  != std::string::npos)
      {
        obj->SetStats( kFALSE );
	//obj->SetMaximum(1.0);
	obj->SetMaximum(4.0);
        obj->SetMinimum(-0.001);
        //return;
      }
      if( o.name.find( "Summary_MeanNumberOfClusters__TOB" )  != std::string::npos)
      {
        obj->SetStats( kFALSE );
	//obj->SetMaximum(1.0);
	obj->SetMaximum(1.5);
        obj->SetMinimum(-0.001);
        return;
      }
      if( o.name.find( "Summary_MeanClusterWidth" )  != std::string::npos)
      {
        obj->SetStats( kFALSE );
        obj->SetMaximum(10.0);
        obj->SetMinimum(-1.0);
        return;
      }

      if ( o.name.find( "GoodTrackPhi_" ) != std::string::npos or
	   o.name.find( "GoodTrackEta_" ) != std::string::npos or
	   o.name.find( "SeedPhi_" )  != std::string::npos
	   ) {

	size_t nbins        = obj->GetNbinsX();
	double entries      = obj->GetEntries();
	double meanbinentry = entries/double(nbins);
	double ymax = obj->GetMaximum();
	obj->SetMinimum(ymax-meanbinentry);

      }

    }

  void preDrawTProfile2D( TCanvas *, const VisDQMObject &o )
    {
      TProfile2D* obj = dynamic_cast<TProfile2D*>( o.object );
      assert( obj );

      // This applies to all
      gStyle->SetCanvasBorderMode( 0 );
      gStyle->SetPadBorderMode( 0 );
      gStyle->SetPadBorderSize( 0 );
      //    (data->pad)->SetLogy( 0 );;
      //  gStyle->SetOptStat( 0 );

      TAxis* xa = obj->GetXaxis();
      TAxis* ya = obj->GetYaxis();

      xa->SetTitleOffset(0.7);
      xa->SetTitleSize(0.05);
      xa->SetLabelSize(0.04);

      ya->SetTitleOffset(0.7);
      ya->SetTitleSize(0.05);
      ya->SetLabelSize(0.04);

      if( o.name.find( "TkHMap" )  != std::string::npos)
      {
        obj->SetStats( kFALSE );
        gStyle->SetPalette(1,0);
        obj->SetOption("colz");
        if (o.name.find( "TkHMap_FractionOfBadChannels" )  != std::string::npos) {
          obj->SetMinimum(0.0001);
          obj->SetMaximum(1.0);
        }
        return;
      }

      if( o.name.find( "VsPhiVsEtaPerTrack" )  != std::string::npos)
      {
        obj->SetStats( kFALSE );
        gStyle->SetPalette(1,0);
        obj->SetOption("colz");
      return;
    }

	  if( o.name.find( "StripClusVsBXandOrbit" ) != std::string::npos)
      {
        obj->SetStats( kFALSE );
        gStyle->SetPalette(1,0);
        obj->SetOption("colz");
	return;
      }

      return;
    }
  void preDrawTProfile( TCanvas *, const VisDQMObject &o )
    {
      TProfile* obj = dynamic_cast<TProfile*>( o.object );
      assert( obj );

      // This applies to all
      gStyle->SetCanvasBorderMode( 0 );
      gStyle->SetPadBorderMode( 0 );
      gStyle->SetPadBorderSize( 0 );
      //    (data->pad)->SetLogy( 0 );;
      //  gStyle->SetOptStat( 0 );

      TAxis* xa = obj->GetXaxis();
      TAxis* ya = obj->GetYaxis();

      xa->SetTitleOffset(0.7);
      xa->SetTitleSize(0.05);
      xa->SetLabelSize(0.04);

      ya->SetTitleOffset(0.7);
      ya->SetTitleSize(0.05);
      ya->SetLabelSize(0.04);

      obj->SetStats( kFALSE );
      obj->SetOption("e");

      if( o.name.find( "TkHMap" )  != std::string::npos)
      {
        obj->SetStats( kFALSE );
        gStyle->SetPalette(1,0);
        obj->SetOption("colz");
        if (o.name.find( "TkHMap_FractionOfBadChannels" )  != std::string::npos) {
          obj->SetMinimum(0.0001);
          obj->SetMaximum(1.0);
        }
      return;
    }

      if ( o.name.find( "DistanceOfClosestApproachToBSVsPhi") != std::string::npos ) {
	obj->SetMinimum(-0.02);
	obj->SetMaximum( 0.02);
      }

      if ( o.name.find( "zPointOfClosestApproachVsPhi") != std::string::npos ) {
	obj->SetMinimum(-5.);
	obj->SetMaximum( 5.);
      }

      if ( o.name.find( "TECLayersPerTrackVs") != std::string::npos or
	   o.name.find( "TECRecHitsPerTrackVs") != std::string::npos
	   ) {
	obj->SetMinimum(-0.5);
	obj->SetMaximum(12.);
      }
      if ( o.name.find( "TIBLayersPerTrackVs") != std::string::npos or
	   o.name.find( "TIBRecHitsPerTrackVs") != std::string::npos
	   ) {
	obj->SetMinimum(-0.5);
	obj->SetMaximum(6.);
      }
      if ( o.name.find( "TIDLayersPerTrackVs") != std::string::npos or
	   o.name.find( "TIDRecHitsPerTrackVs") != std::string::npos
	   ) {
	obj->SetMinimum(-0.5);
	obj->SetMaximum(6.);
      }
      if ( o.name.find( "TOBLayersPerTrackVs") != std::string::npos or
	   o.name.find( "TOBRecHitsPerTrackVs") != std::string::npos
	   ) {
	obj->SetMinimum(-0.5);
	obj->SetMaximum(10.);
      }
      if ( o.name.find( "NumberOfLayersPerTrackVs") != std::string::npos or
	   o.name.find( "NumberOfRecHitsPerTrackVs") != std::string::npos or
	   o.name.find( "NumberOfFoundRecHitsPerTrackVs") != std::string::npos
	   ) {
	obj->SetMinimum(-0.5);
	obj->SetMaximum(20.);
      }

      if ( o.name.find( "PixEndcapLayersPerTrackVs" ) != std::string::npos or
	   o.name.find( "PixEndcapRecHitsPerTrackVs") != std::string::npos
	   ) {
	obj->SetMinimum(-0.5);
	obj->SetMaximum(3.);
      }

      if ( o.name.find( "PixBarrelLayersPerTrackVs"  ) != std::string::npos or
	   o.name.find( "PixBarrelRecHitsPerTrackVs" ) != std::string::npos
	   ) {
	obj->SetMinimum(-0.5);
	obj->SetMaximum(4.);
      }

      if ( o.name.find( "ProbVs" ) != std::string::npos or
	   o.name.find( "Chi2oNDFVs" )  != std::string::npos
	   ){
	obj->SetMinimum(0.);
	obj->SetMaximum(1.5);
      }

      if( o.name.find( "TotalNumberOfClusterProfile__" ) != std::string::npos )
	{
	  float TIBLimit2 = 4000.0;
	  float TOBLimit2 = 4000.0;
	  float TIDLimit2 = 1200.0;
	  float TECLimit2 = 4800.0;
	  obj->SetMinimum(1);
	  float ymax = obj->GetMaximum()*1.2;

	  if (o.name.find( "TotalNumberOfClusterProfile__TIB" ) != std::string::npos) {
	    obj->SetMaximum(TMath::Max(ymax, TIBLimit2*20 ));
	  } else if (o.name.find( "TotalNumberOfClusterProfile__TOB" ) != std::string::npos) {
	    obj->SetMaximum(TMath::Max(ymax, TOBLimit2*20 ));
	  } else if (o.name.find( "TotalNumberOfClusterProfile__TEC" ) != std::string::npos) {
	    obj->SetMaximum(TMath::Max(ymax, TECLimit2*20 ));
	  }  else if (o.name.find( "TotalNumberOfClusterProfile__TID" ) != std::string::npos) {
	    obj->SetMaximum(TMath::Max(ymax, TIDLimit2*20 ));
	  }
	}

      return;
    }

  void postDrawTH1F( TCanvas *c, const VisDQMObject &o )
  {

    TH1F* obj = dynamic_cast<TH1F*>( o.object );
    assert( obj );

    std::string name = o.name.substr(o.name.rfind("/")+1);

    if( name.find( "NumberOfTracks_" ) != std::string::npos or
	name.find( "Chi2oNDF_" ) != std::string::npos or
	name.find( "TrackPt_" ) != std::string::npos or
	name.find( "TrackP_" ) != std::string::npos or
	name.find( "NumberOfSeeds_") != std::string::npos or
	name.find( "SeedPt_") != std::string::npos
	) {
      if (obj->GetEntries() > 10.0) c->SetLogy(1);
      c->SetGridy();
    }

    if ( name.find( "Summary_ClusterCharge_OffTrack__" )!= std::string::npos or
	 (name.find( "Track" )!= std::string::npos and
	  name.find( "Err" )!= std::string::npos) or
	 name.find( "NumberOfRecHitsLostPerTrack_") != std::string::npos
	 ) {
      if (obj->GetEntries() > 10.0) c->SetLogy(1);
    }

    TText tt;
    tt.SetTextSize(0.12);
    if (o.flags == 0) return;
    else
      {
        if (o.flags & DQMNet::DQM_PROP_REPORT_ERROR)
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
      }

  }

  void postDrawTH2F( TCanvas *c, const VisDQMObject &o )
    {
      TH2F* obj = dynamic_cast<TH2F*>( o.object );
      assert( obj );

      std::string name = o.name.substr(o.name.rfind("/")+1);

      TText tt;
      tt.SetTextSize(0.12);
      if (o.flags != 0)
	{
	  if (o.flags & DQMNet::DQM_PROP_REPORT_ERROR)
	    {
	      tt.SetTextColor(2);
	      tt.DrawTextNDC(0.5, 0.5, "Error");
	    }
	  else
	    if (o.flags & DQMNet::DQM_PROP_REPORT_WARN)
	      {
		tt.SetTextColor(5);
		tt.DrawTextNDC(0.5, 0.5, "Warning");
	      }
	  else
	    if (o.flags & DQMNet::DQM_PROP_REPORT_OTHER)
	      {
		tt.SetTextColor(1);
		tt.DrawTextNDC(0.5, 0.5, "Other ");
	      }
	}

      if( name.find( "reportSummaryMap" ) != std::string::npos )
      {
        c->SetGridx();
        c->SetGridy();
        return;
      }
      if( name.find( "detFractionReportMap" ) != std::string::npos )
      {
        c->SetGridx();
        c->SetGridy();
        return;
      }
      if( name.find( "sToNReportMap" ) != std::string::npos )
      {
        c->SetGridx();
        c->SetGridy();
        return;
      }
      if( name.find( "SummaryOfCabling" ) != std::string::npos )
      {
        c->SetGridx();
        c->SetGridy();
        return;
      }
    }

  void postDrawTProfile( TCanvas *c, const VisDQMObject &o )
  {
    TProfile* obj = dynamic_cast<TProfile*>( o.object );
    assert( obj );

    std::string name = o.name.substr(o.name.rfind("/")+1);

    TLine tl1;
    tl1.SetLineColor(3);
    tl1.SetLineWidth(3);

    TLine tl2;
    tl2.SetLineColor(4);
    tl2.SetLineWidth(3);

    float xmin = 0.0;
    float xmax = obj->GetXaxis()->GetXmax();
    float ymax = obj->GetMaximum()*1.2;

    // FOR PP
    /*
    float TIBLimit1 = 10000.0;
    float TOBLimit1 = 11000.0;
    float TIDLimit1 = 2000.0;
    float TECLimit1 = 10000.0;

    float TIBLimit2 = 2000.0;
    float TOBLimit2 = 2000.0;
    float TIDLimit2 = 600.0;
    float TECLimit2 = 2400.0;
    */
    float TIBLimit1 = 20000.0;
    float TOBLimit1 = 20000.0;
    float TIDLimit1 = 4000.0;
    float TECLimit1 = 20000.0;

    float TIBLimit2 = 4000.0;
    float TOBLimit2 = 4000.0;
    float TIDLimit2 = 1200.0;
    float TECLimit2 = 4800.0;
    /*
    //FOR HI
    float TIBLimit1 = 70000.0;
    float TOBLimit1 = 70000.0;
    float TIDLimit1 = 15000.0;
    float TECLimit1 = 70000.0;

    float TIBLimit2 = 15000.0;
    float TOBLimit2 = 15000.0;
    float TIDLimit2 = 4000.0;
    float TECLimit2 = 20000.0;
    */

    if( name.find( "TotalNumberOfDigiProfile__" ) != std::string::npos )
      {
        if (obj->GetEntries() > 10.0) c->SetLogy(1);
        c->SetGridy();
        if (name.find( "TotalNumberOfDigiProfile__TIB" ) != std::string::npos) {
           tl1.DrawLine(xmin, TIBLimit1,     xmax, TIBLimit1);
           tl2.DrawLine(xmin, TIBLimit1*0.5, xmax, TIBLimit1*0.5);
           tl2.DrawLine(xmin, TIBLimit1*2.0, xmax, TIBLimit1*2.0);
//          obj->SetMinimum(TIBLimit1*0.1);
          obj->SetMinimum(1);
          obj->SetMaximum(TMath::Max(ymax, TIBLimit1*50));
        } else if (name.find( "TotalNumberOfDigiProfile__TOB" ) != std::string::npos) {
           tl1.DrawLine(xmin, TOBLimit1,     xmax, TOBLimit1);
           tl2.DrawLine(xmin, TOBLimit1*0.5, xmax, TOBLimit1*0.5);
           tl2.DrawLine(xmin, TOBLimit1*2.0, xmax, TOBLimit1*2.0);
//          obj->SetMinimum(TOBLimit1*0.1);
          obj->SetMinimum(1);
	  obj->SetMaximum(TMath::Max(ymax, TOBLimit1*50));
        } else if (name.find( "TotalNumberOfDigiProfile__TEC" ) != std::string::npos) {
          tl1.DrawLine(xmin, TECLimit1,     xmax, TECLimit1);
          tl2.DrawLine(xmin, TECLimit1*0.5, xmax, TECLimit1*0.5);
          tl2.DrawLine(xmin, TECLimit1*2.0, xmax, TECLimit1*2.0);
//          obj->SetMinimum(TECLimit1*0.1);
          obj->SetMinimum(1);
          obj->SetMaximum(TMath::Max(ymax, TECLimit1*50));
        } else if (name.find( "TotalNumberOfDigiProfile__TID" ) != std::string::npos) {
           tl1.DrawLine(xmin, TIDLimit1,     xmax, TIDLimit1);
           tl2.DrawLine(xmin, TIDLimit1*0.5, xmax, TIDLimit1*0.5);
           tl2.DrawLine(xmin, TIDLimit1*2.0, xmax, TIDLimit1*2.0);
//          obj->SetMinimum(TIDLimit1*0.1);
          obj->SetMinimum(1);
          obj->SetMaximum(TMath::Max(ymax, TIDLimit1*50));
	}
        return;
      }
    if( name.find( "TotalNumberOfClusterProfile__" ) != std::string::npos )
      {
        if (obj->GetEntries() > 10.0) c->SetLogy(1);
        c->SetGridy();
        if (name.find( "TotalNumberOfClusterProfile__TIB" ) != std::string::npos) {
          tl1.DrawLine(xmin, TIBLimit2,     xmax, TIBLimit2);
          tl2.DrawLine(xmin, TIBLimit2*0.5, xmax, TIBLimit2*0.5);
          tl2.DrawLine(xmin, TIBLimit2*2.0, xmax, TIBLimit2*2.0);
	  //axis range set in PreDraw function to enable zooming in GUI
          //obj->SetMinimum(1);
	  //obj->SetMaximum(TMath::Max(ymax, TIBLimit2*20));
        } else if (name.find( "TotalNumberOfClusterProfile__TOB" ) != std::string::npos) {
          tl1.DrawLine(xmin, TOBLimit2,     xmax, TOBLimit2);
          tl2.DrawLine(xmin, TOBLimit2*0.5, xmax, TOBLimit2*0.5);
          tl2.DrawLine(xmin, TOBLimit2*2.0, xmax, TOBLimit2*2.0);
          //obj->SetMinimum(1);
          //obj->SetMaximum(TMath::Max(ymax, TOBLimit2*20));
        } else if (name.find( "TotalNumberOfClusterProfile__TEC" ) != std::string::npos) {
          tl1.DrawLine(xmin, TECLimit2,     xmax, TECLimit2);
          tl2.DrawLine(xmin, TECLimit2*0.5, xmax, TECLimit2*0.5);
          tl2.DrawLine(xmin, TECLimit2*2.0, xmax, TECLimit2*2.0);
          //obj->SetMinimum(1);
          //obj->SetMaximum(TMath::Max(ymax, TECLimit2*20));
        }  else if (name.find( "TotalNumberOfClusterProfile__TID" ) != std::string::npos) {
          tl1.DrawLine(xmin, TIDLimit2,     xmax, TIDLimit2);
          tl2.DrawLine(xmin, TIDLimit2*0.5, xmax, TIDLimit2*0.5);
          tl2.DrawLine(xmin, TIDLimit2*2.0, xmax, TIDLimit2*2.0);
          //obj->SetMinimum(1);
          //obj->SetMaximum(TMath::Max(ymax, TIDLimit2*20));
        }
        return;
      }
  }

};

static SiStripRenderPlugin instance;
