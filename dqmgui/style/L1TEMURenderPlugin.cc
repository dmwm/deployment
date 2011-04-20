/*!
  \file L1TEMURenderPlugin.cc
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

class L1TEMURenderPlugin : public DQMRenderPlugin
{
public:
  virtual bool applies(const VisDQMObject &o, const VisDQMImgInfo &)
    {
      // determine whether core object is an L1TEMU object
      if (o.name.find( "L1TEMU/" ) != std::string::npos &&
          o.name.find( "L1TdeRCT/" ) == std::string::npos )
        return true;

      return false;
    }

  virtual void preDraw (TCanvas * c, const VisDQMObject &o, const VisDQMImgInfo &, VisDQMRenderInfo &)
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

  virtual void postDraw (TCanvas * c, const VisDQMObject & o, const VisDQMImgInfo &)
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

      // Code used in SiStripRenderPlugin -- do we want similar defaults?
      /*
        gStyle->SetOptStat(0111);
        if ( obj->GetMaximum(1.e5) > 0. )
          gPad->SetLogy(1);
        else
          gPad->SetLogy(0);
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
        dqm::utils::reportSummaryMapPalette(obj);

	obj->GetXaxis()->SetBinLabel(1,"Data");
	obj->GetXaxis()->SetBinLabel(2,"Emulator");
	obj->GetXaxis()->SetLabelSize(0.1);

        obj->SetOption("col");
        obj->SetTitle("L1TEMU Report Summary Map");

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
      // nothing to put here just yet
      // in the future, we can add text output based on error status,
      // or set bin range based on filled histograms, etc.
      // Maybe add a big "OK" sign to histograms with no entries (i.e., no errors)?


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


	TBox* b_box_w = new TBox();
	TBox* b_box_r = new TBox();
	TBox* b_box_y = new TBox();
	TBox* b_box_g = new TBox();

	b_box_g->SetFillColor(920);
	b_box_y->SetFillColor(919);
	b_box_r->SetFillColor(901);
	b_box_w->SetFillColor(0);


	TLegend* leg = new TLegend(0.16, 0.11, 0.44, 0.38);
	leg->AddEntry(b_box_g,"Good",   "f");
	leg->AddEntry(b_box_y,"Warning","f");
	leg->AddEntry(b_box_r,"Error",  "f");
	leg->AddEntry(b_box_w,"Masked", "f");
	leg->Draw();

	return;
      }


    }
};

static L1TEMURenderPlugin instance;
