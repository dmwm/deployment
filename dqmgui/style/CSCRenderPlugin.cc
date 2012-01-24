/*
 * =====================================================================================
 *
 *       Filename:  CSCRenderPlugin.cc
 *
 *    Description:  CSC Render Plugin for DQM
 *
 *        Version:  1.0
 *        Created:  05/06/2008 03:53:34 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Valdas Rapsevicius (VR), Valdas.Rapsevicius@cern.ch
 *        Company:  CERN, CH
 *
 * =====================================================================================
 */

#include "DQM/DQMRenderPlugin.h"
#include "CSCRenderPlugin_ChamberMap.h"
#include "CSCRenderPlugin_SummaryMap.h"
#include "CSCRenderPlugin_EventDisplay.h"
#include "CSCRenderPlugin_EmuEventDisplay.h"
#include "CSC_TPE_hAll.h"

#include <math.h>
#include <string>
#include <iostream>
#include <bitset>
#include <TH1.h>
#include <TH2.h>
#include <TH3.h>
#include <TBox.h>
#include <TText.h>
#include <TPRegexp.h>
#include <TStyle.h>
#include <TCanvas.h>

#define REREPLACE(pat, str, rep) { TString s(str); TPRegexp(pat).Substitute(s, rep); str = s; }

typedef std::map<std::string, bool> MapOfPatternResults;

/**
 * @class CSCRenderPlugin
 * @brief Actual render plugin for CSCs
 */
class CSCRenderPlugin : public DQMRenderPlugin {

  private:

    ChamberMap chamberMap;
    SummaryMap summaryMap;
    EventDisplay eventDisplay;
    EmuEventDisplay emuEventDisplay;
    MapOfPatternResults mopr;
    CSC_TPE_hAll hAll;

  public:

    virtual bool applies( const VisDQMObject &o, const VisDQMImgInfo & ) {
      if ( o.name.find( "CSC/" ) != std::string::npos )
        return true;
      return false;
    }

    virtual void preDraw( TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &, VisDQMRenderInfo & ) {

      if(o.object == NULL)
        return;

      TH1* obj = dynamic_cast<TH1*>( o.object );
      if(obj == NULL) return;

      c->cd();

      gStyle->SetPalette(1,0);
      obj->SetFillColor(45);

  // ============== Start generated from emuDQMBooking.xml by emuBooking2RenderPlugin.xsl ==================

  if(reMatch(".*/FEDEntries$", o.name)) {
    /** Applying definition [FEDIntegrityMap] **/
    obj->SetStats(false);
    obj->SetOption("bar1text");
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/FEDFatal$", o.name)) {
    /** Applying definition [FEDIntegrityMap] **/
    obj->SetStats(false);
    obj->SetOption("bar1text");
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/FEDNonFatal$", o.name)) {
    /** Applying definition [FEDIntegrityMap] **/
    obj->SetStats(false);
    obj->SetOption("bar1text");
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/FEDFormatFatal$", o.name)) {
    /** Applying definition [FEDIntegrityMap] **/
    obj->SetStats(false);
    obj->SetOption("bar1text");
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_STATS_summary$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_STATS_occupancy$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_STATS_format_err$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_STATS_l1sync_err$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_STATS_fifofull_err$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_STATS_inputto_err$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_STATS_wo_alct$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_STATS_wo_clct$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_STATS_wo_cfeb$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_STATS_cfeb_bwords$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/Physics_EMU$", o.name)) {
    /** Applying histogram **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("col");
    return;
  }
  if(reMatch(".*/Physics_ME1$", o.name)) {
    /** Applying definition [physicsMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("col");
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/Physics_ME2$", o.name)) {
    /** Applying definition [physicsMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("col");
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/Physics_ME3$", o.name)) {
    /** Applying definition [physicsMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("col");
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/Physics_ME4$", o.name)) {
    /** Applying definition [physicsMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("col");
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/DMB_Unpacked$", o.name)) {
    /** Applying definition [DMBMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_L1A_out_of_sync$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_L1A_out_of_sync_Fract$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMaximum(1.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    if(obj->GetMinimum() == obj->GetMaximum()) {
      obj->SetMaximum(obj->GetMinimum() + 0.01);
    }
    gPad->SetLogz();
    return;
  }
  if(reMatch(".*/DMB_wo_ALCT$", o.name)) {
    /** Applying definition [DMBMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/DMB_wo_CLCT$", o.name)) {
    /** Applying definition [DMBMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/DMB_wo_CFEB$", o.name)) {
    /** Applying definition [DMBMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/DMB_Reporting$", o.name)) {
    /** Applying definition [DMBMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/DMB_input_fifo_full$", o.name)) {
    /** Applying definition [DMBMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/DMB_input_timeout$", o.name)) {
    /** Applying definition [DMBMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/DMB_Unpacked_with_errors$", o.name)) {
    /** Applying definition [DMBMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/DMB_Unpacked_Fract$", o.name)) {
    /** Applying definition [DMBMap] **/
    obj->SetStats(false);
    obj->SetMaximum(1.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/DMB_wo_ALCT_Fract$", o.name)) {
    /** Applying definition [DMBMap] **/
    obj->SetStats(false);
    obj->SetMaximum(1.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/DMB_wo_CLCT_Fract$", o.name)) {
    /** Applying definition [DMBMap] **/
    obj->SetStats(false);
    obj->SetMaximum(1.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/DMB_wo_CFEB_Fract$", o.name)) {
    /** Applying definition [DMBMap] **/
    obj->SetStats(false);
    obj->SetMaximum(1.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/DMB_Format_Errors$", o.name)) {
    /** Applying definition [DMBMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/DMB_Format_Errors_Fract$", o.name)) {
    /** Applying definition [DMBMap] **/
    obj->SetStats(false);
    obj->SetMaximum(1.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    if(obj->GetMinimum() == obj->GetMaximum()) {
      obj->SetMaximum(obj->GetMinimum() + 0.01);
    }
    gPad->SetLogz();
    return;
  }
  if(reMatch(".*/DMB_Format_Warnings$", o.name)) {
    /** Applying definition [DMBMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/DMB_Format_Warnings_Fract$", o.name)) {
    /** Applying definition [DMBMap] **/
    obj->SetStats(false);
    obj->SetMaximum(1.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    if(obj->GetMinimum() == obj->GetMaximum()) {
      obj->SetMaximum(obj->GetMinimum() + 0.01);
    }
    gPad->SetLogz();
    return;
  }
  if(reMatch(".*/DMB_input_fifo_full_Fract$", o.name)) {
    /** Applying definition [DMBMap] **/
    obj->SetStats(false);
    obj->SetMaximum(1.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/DMB_input_timeout_Fract$", o.name)) {
    /** Applying definition [DMBMap] **/
    obj->SetStats(false);
    obj->SetMaximum(1.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/DMB_L1A_out_of_sync$", o.name)) {
    /** Applying definition [DMBMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/DMB_L1A_out_of_sync_Fract$", o.name)) {
    /** Applying definition [DMBMap] **/
    obj->SetStats(false);
    obj->SetMaximum(1.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    if(obj->GetMinimum() == obj->GetMaximum()) {
      obj->SetMaximum(obj->GetMinimum() + 0.01);
    }
    gPad->SetLogz();
    return;
  }
  if(reMatch(".*/CSC_Unpacked$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_DMB_input_fifo_full$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_DMB_input_timeout$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_Reporting$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_wo_ALCT$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_wo_CLCT$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_wo_CFEB$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_Unpacked_with_errors$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_Unpacked_with_warnings$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_Format_Errors$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_Format_Errors_Fract$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMaximum(1.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    if(obj->GetMinimum() == obj->GetMaximum()) {
      obj->SetMaximum(obj->GetMinimum() + 0.01);
    }
    gPad->SetLogz();
    return;
  }
  if(reMatch(".*/CSC_DMB_input_fifo_full_Fract$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMaximum(1.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_DMB_input_timeout_Fract$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMaximum(1.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_wo_ALCT_Fract$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMaximum(1.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_wo_CLCT_Fract$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMaximum(1.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_wo_CFEB_Fract$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMaximum(1.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_Unpacked_Fract$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMaximum(1.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_Format_Warnings$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_Format_Warnings_Fract$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMaximum(1.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    if(obj->GetMinimum() == obj->GetMaximum()) {
      obj->SetMaximum(obj->GetMinimum() + 0.01);
    }
    gPad->SetLogz();
    return;
  }
  if(reMatch(".*/All_Readout_Errors$", o.name)) {
    /** Applying histogram **/
    gPad->SetLeftMargin(0.3);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    return;
  }
  if(reMatch(".*/All_DDUs_in_Readout$", o.name)) {
    /** Applying histogram **/
    obj->SetStats(false);
    gStyle->SetOptStat("em");
    obj->SetOption("bar1text");
    return;
  }
  if(reMatch(".*/All_DDUs_L1A_Increment$", o.name)) {
    /** Applying histogram **/
    obj->SetStats(false);
    obj->SetOption("textcolz");
    return;
  }
  if(reMatch(".*/All_DDUs_Trailer_Errors$", o.name)) {
    /** Applying histogram **/
    gPad->SetLeftMargin(0.3);
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    return;
  }
  if(reMatch(".*/All_DDUs_Format_Errors$", o.name)) {
    /** Applying histogram **/
    gPad->SetLeftMargin(0.3);
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    return;
  }
  if(reMatch(".*/All_DDUs_Event_Size$", o.name)) {
    /** Applying histogram **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    return;
  }
  if(reMatch(".*/All_DDUs_Average_Event_Size$", o.name)) {
    /** Applying histogram **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("E1");
    return;
  }
  if(reMatch(".*/All_DDUs_Live_Inputs$", o.name)) {
    /** Applying histogram **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("textcolz");
    gPad->SetGridx();
    gPad->SetGridy();
    return;
  }
  if(reMatch(".*/All_DDUs_Average_Live_Inputs$", o.name)) {
    /** Applying histogram **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("E1");
    return;
  }
  if(reMatch(".*/All_DDUs_Inputs_with_Data$", o.name)) {
    /** Applying histogram **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("textcolz");
    gPad->SetGridx();
    gPad->SetGridy();
    return;
  }
  if(reMatch(".*/All_DDUs_Average_Inputs_with_Data$", o.name)) {
    /** Applying histogram **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("E1");
    return;
  }
  if(reMatch(".*/All_DDUs_Inputs_Errors$", o.name)) {
    /** Applying histogram **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("textcolz");
    gPad->SetGridx();
    gPad->SetGridy();
    return;
  }
  if(reMatch(".*/All_DDUs_Inputs_Warnings$", o.name)) {
    /** Applying histogram **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("textcolz");
    gPad->SetGridx();
    gPad->SetGridy();
    return;
  }
  if(reMatch(".*/CSC_ALCT0_BXN_mean$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMinimum(0.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_ALCT0_BXN_rms$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMinimum(0.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/Plus_endcap_ALCT0_dTime$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emruo");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/Minus_endcap_ALCT0_dTime$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emruo");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/CSC_CLCT0_BXN_mean$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMinimum(-170.);
    obj->SetMaximum(-140.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_CLCT0_BXN_rms$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMinimum(0.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/Plus_endcap_CLCT0_dTime$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emruo");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/Minus_endcap_CLCT0_dTime$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emruo");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/CSC_AFEB_RawHits_Time_mean$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMinimum(0.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_AFEB_RawHits_Time_rms$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMinimum(0.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/Plus_endcap_AFEB_RawHits_Time$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emruo");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/Minus_endcap_AFEB_RawHits_Time$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emruo");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/CSC_CFEB_SCA_CellPeak_Time_mean$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMinimum(0.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_CFEB_SCA_CellPeak_Time_rms$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMinimum(0.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/Plus_endcap_CFEB_SCA_CellPeak_Time$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emruo");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/Minus_endcap_CFEB_SCA_CellPeak_Time$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emruo");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/CSC_CFEB_Comparators_Time_mean$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetMinimum(0.);
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_CFEB_Comparators_Time_rms$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetMinimum(0.);
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/Plus_endcap_CFEB_Comparators_Time$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emruo");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/Minus_endcap_CFEB_Comparators_Time$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emruo");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/CSC_ALCT_CLCT_Match_mean$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMinimum(0.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_ALCT_CLCT_Match_rms$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMinimum(0.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/Plus_endcap_ALCT_CLCT_Match_Time$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emruo");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/Minus_endcap_ALCT_CLCT_Match_Time$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emruo");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/CSC_ALCT_Planes_with_Hits$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMinimum(0.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_CLCT_Planes_with_Hits$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMinimum(0.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_ALCT0_Quality$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMinimum(0.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_CLCT0_Quality$", o.name)) {
    /** Applying definition [chamberMap] **/
    obj->SetStats(false);
    obj->SetMinimum(0.);
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    gPad->SetGridx();
    gPad->SetGridy();
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/All_DDUs_BXNs$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("bar1");
    if(obj->GetMinimum() == obj->GetMaximum()) {
      obj->SetMaximum(obj->GetMinimum() + 0.01);
    }
    gPad->SetLogy();
    return;
  }
  if(reMatch(".*/BXN$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("bar1");
    return;
  }
  if(reMatch(".*/Buffer_Size$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emro");
    obj->SetOption("bar1");
    return;
  }
  if(reMatch(".*/CSC_Errors$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emro");
    obj->SetOption("bar1");
    return;
  }
  if(reMatch(".*/CSC_Errors_Rate$", o.name)) {
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_Warnings$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emro");
    obj->SetOption("bar1");
    return;
  }
  if(reMatch(".*/CSC_Warnings_Rate$", o.name)) {
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/DMB_Active_Header_Count$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("em");
    obj->SetOption("bar1text");
    return;
  }
  if(reMatch(".*/DMB_Connected_Inputs$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("bar1text");
    return;
  }
  if(reMatch(".*/DMB_Connected_Inputs_Rate$", o.name)) {
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/DMB_DAV_Header_Count_vs_DMB_Active_Header_Count$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("textcolz");
    return;
  }
  if(reMatch(".*/DMB_DAV_Header_Occupancy$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("bar1text");
    return;
  }
  if(reMatch(".*/DMB_DAV_Header_Occupancy_Rate$", o.name)) {
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/DMB_unpacked_vs_DAV$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("textcolz");
    return;
  }
  if(reMatch(".*/L1A_Increment$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("em");
    obj->SetOption("bar1");
    return;
  }
  if(reMatch(".*/Readout_Errors$", o.name)) {
    /** Applying histogram **/
    gPad->SetLeftMargin(0.6);
    gStyle->SetOptStat("e");
    obj->SetOption("textcolz");
    return;
  }
  if(reMatch(".*/Trailer_ErrorStat_Frequency$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("texthbar1");
    return;
  }
  if(reMatch(".*/Trailer_ErrorStat_Rate$", o.name)) {
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/Trailer_ErrorStat_Table$", o.name)) {
    /** Applying histogram **/
    gPad->SetLeftMargin(0.6);
    gStyle->SetOptStat("e");
    obj->SetOption("textcolz");
    return;
  }
  if(reMatch(".*/Word_Count$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emuo");
    obj->SetOption("bar1");
    return;
  }
  if(reMatch(".*/BinCheck_ErrorStat_Frequency$", o.name)) {
    /** Applying histogram **/
    gPad->SetLeftMargin(0);
    gStyle->SetOptStat("e");
    obj->SetOption("texthbar1");
    return;
  }
  if(reMatch(".*/BinCheck_ErrorStat_Table$", o.name)) {
    /** Applying histogram **/
    gPad->SetLeftMargin(0.4);
    gStyle->SetOptStat("e");
    obj->SetOption("textcolz");
    return;
  }
  if(reMatch(".*/BinCheck_WarningStat_Frequency$", o.name)) {
    /** Applying histogram **/
    gPad->SetLeftMargin(0);
    gStyle->SetOptStat("e");
    obj->SetOption("texthbar1");
    return;
  }
  if(reMatch(".*/BinCheck_WarningStat_Table$", o.name)) {
    /** Applying histogram **/
    gPad->SetLeftMargin(0.4);
    gPad->SetRightMargin(0);
    gStyle->SetOptStat("e");
    obj->SetOption("coltext");
    return;
  }
  if(reMatch(".*/CLCT_Number_Rate$", o.name)) {
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/CSC_Efficiency$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("histtext");
    return;
  }
  if(reMatch(".*/LCT0_Match_BXN_Difference$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emr");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/LCT1_Match_BXN_Difference$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emr");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/LCT_Match_Status$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("coltext");
    return;
  }
  if(reMatch(".*/ALCT%d_BXN$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("eo");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/ALCT%d_KeyWG$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("em");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/ALCT%d_Pattern$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("col");
    return;
  }
  if(reMatch(".*/ALCT%d_Pattern_Distr$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("em");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/ALCT%d_Quality$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("col");
    return;
  }
  if(reMatch(".*/ALCT%d_Quality_Distr$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("em");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/ALCT%d_Quality_Profile$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("P");
    return;
  }
  if(reMatch(".*/ALCT%d_dTime$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emuo");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/ALCT%d_dTime_Profile$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("P");
    return;
  }
  if(reMatch(".*/ALCT%d_dTime_vs_KeyWG$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("em");
    obj->SetOption("col");
    return;
  }
  if(reMatch(".*/ALCT1_vs_ALCT0_KeyWG$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("col");
    return;
  }
  if(reMatch(".*/ALCTTime_Ly%d$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("em");
    obj->SetOption("col");
    return;
  }
  if(reMatch(".*/ALCTTime_Ly%d_Profile$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("P");
    return;
  }
  if(reMatch(".*/ALCT_BXN$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("eo");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/ALCT_BXN_vs_DMB_BXN$", o.name)) {
    /** Applying histogram **/
    obj->SetStats(false);
    obj->SetOption("box");
    return;
  }
  if(reMatch(".*/ALCT_DMB_BXN_diff$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emuo");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/ALCT_DMB_L1A_diff$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emuo");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/ALCT_L1A$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("eo");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/ALCT_Ly%d_Efficiency$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/ALCT_Ly%d_Rate$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/ALCT_Match_Time$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emr");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/ALCT_Number_Efficiency$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/ALCT_Number_Of_Layers_With_Hits$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emo");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/ALCT_Number_Of_WireGroups_With_Hits$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emo");
    obj->SetOption("hist");
    if(obj->GetMinimum() == obj->GetMaximum()) {
      obj->SetMaximum(obj->GetMinimum() + 0.01);
    }
    gPad->SetLogy();
    return;
  }
  if(reMatch(".*/ALCT_Number_Rate$", o.name)) {
    /** Applying histogram **/
    return;
  }
  if(reMatch(".*/ALCT_Word_Count$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emo");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/CLCT%d_dTime_Profile$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("em");
    obj->SetOption("P");
    return;
  }
  if(reMatch(".*/CFEB%d_DMB_L1A_diff$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emuo");
    obj->SetOption("hist");
    if(obj->GetMinimum() == obj->GetMaximum()) {
      obj->SetMaximum(obj->GetMinimum() + 0.01);
    }
    gPad->SetLogy();
    return;
  }
  if(reMatch(".*/CFEB%d_Free_SCA_Cells$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    return;
  }
  if(reMatch(".*/CFEB%d_L1A_Sync_Time$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("eo");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/CFEB%d_L1A_Sync_Time_DMB_diff$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emuo");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/CFEB%d_L1A_Sync_Time_vs_DMB$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("col");
    return;
  }
  if(reMatch(".*/CFEB%d_LCT_PHASE_vs_L1A_PHASE$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("textcol");
    return;
  }
  if(reMatch(".*/CFEB%d_SCA_Block_Occupancy$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("eo");
    return;
  }
  if(reMatch(".*/CFEB%d_SCA_Blocks_Locked_by_LCTs$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("em");
    return;
  }
  if(reMatch(".*/CFEB%d_SCA_Blocks_Locked_by_LCTxL1$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("em");
    return;
  }
  if(reMatch(".*/CFEB_ActiveStrips_Ly%d$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("em");
    return;
  }
  if(reMatch(".*/CFEB_Active_Samples_vs_Strip_Ly%d$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("em");
    obj->SetOption("col");
    return;
  }
  if(reMatch(".*/CFEB_Active_Samples_vs_Strip_Ly%d_Profile$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("P");
    return;
  }
  if(reMatch(".*/CFEB_Cluster_Duration_Ly_%d$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("em");
    return;
  }
  if(reMatch(".*/CFEB_Clusters_Charge_Ly_%d$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("eom");
    return;
  }
  if(reMatch(".*/CFEB_Number_of_Clusters_Ly_%d$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("em");
    return;
  }
  if(reMatch(".*/CFEB_Out_Off_Range_Strips_Ly%d$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("em");
    return;
  }
  if(reMatch(".*/CFEB_Pedestal_withEMV_Sample_01_Ly%d$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("P");
    return;
  }
  if(reMatch(".*/CFEB_Pedestal_withRMS_Sample_01_Ly%d$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    return;
  }
  if(reMatch(".*/CFEB_PedestalRMS_Sample_01_Ly%d$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    return;
  }
  if(reMatch(".*/CFEB_SCA_Cell_Peak_Ly_%d$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("col");
    return;
  }
  if(reMatch(".*/CFEB_Width_of_Clusters_Ly_%d$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("em");
    return;
  }
  if(reMatch(".*/AFEB_RawHits_TimeBins$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emr");
    return;
  }
  if(reMatch(".*/CFEB_SCA_CellPeak_Time$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emr");
    return;
  }
  if(reMatch(".*/CFEB_Comparators_TimeSamples$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emr");
    return;
  }
  if(reMatch(".*/CLCT%d_BXN$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("eo");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/CLCT0_CLCT1_Clssification$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/CLCT0_Clssification$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/CLCT%d_DiStrip_Pattern$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("col");
    return;
  }
  if(reMatch(".*/CLCT%d_DiStrip_Quality$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("col");
    return;
  }
  if(reMatch(".*/CLCT%d_DiStrip_Quality_Profile$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("P");
    return;
  }
  if(reMatch(".*/CLCT%d_Half_Strip_Pattern$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("col");
    return;
  }
  if(reMatch(".*/CLCT%d_Half_Strip_Quality$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("col");
    return;
  }
  if(reMatch(".*/CLCT%d_Half_Strip_Quality_Profile$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("P");
    return;
  }
  if(reMatch(".*/CLCT%d_KeyDiStrip$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("em");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/CLCT%d_KeyHalfStrip$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("em");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/CLCT%d_dTime$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emuo");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/CLCT%d_dTime_vs_DiStrip$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("col");
    return;
  }
  if(reMatch(".*/CLCT%d_dTime_vs_Half_Strip$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("col");
    return;
  }
  if(reMatch(".*/CLCT0_KeyDiStrip_vs_ALCT0_KeyWiregroup$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    if(obj->GetMinimum() == obj->GetMaximum()) {
      obj->SetMaximum(obj->GetMinimum() + 0.01);
    }
    gPad->SetLogx();
    return;
  }
  if(reMatch(".*/CLCT1_vs_CLCT0_Key_Strip$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("col");
    return;
  }
  if(reMatch(".*/CLCTTime_Ly%d$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    return;
  }
  if(reMatch(".*/CLCTTime_Ly%d_Profile$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("P");
    return;
  }
  if(reMatch(".*/CLCT_BXN$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("eo");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/CLCT_BXN_vs_DMB_BXN$", o.name)) {
    /** Applying histogram **/
    obj->SetStats(false);
    obj->SetOption("box");
    return;
  }
  if(reMatch(".*/CLCT_DMB_BXN_diff$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emuo");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/CLCT_DMB_L1A_diff$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emuo");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/CLCT_L1A$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("eo");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/CLCT_Ly%d_Efficiency$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("eou");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/CLCT_Ly%d_Rate$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/CLCT_Number$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/CLCT_Number_Of_HalfStrips_With_Hits$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emo");
    obj->SetOption("hist");
    if(obj->GetMinimum() == obj->GetMaximum()) {
      obj->SetMaximum(obj->GetMinimum() + 0.01);
    }
    gPad->SetLogy();
    return;
  }
  if(reMatch(".*/CLCT_Number_Of_Layers_With_Hits$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emo");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/CLCT%d_Half_Strip_Pattern_Distr$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("em");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/CLCT%d_Half_Strip_Quality_Distr$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("em");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/DMB_CFEB_DAV_Unpacking_Inefficiency$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("textcolz");
    if(obj->GetMinimum() == obj->GetMaximum()) {
      obj->SetMaximum(obj->GetMinimum() + 0.01);
    }
    gPad->SetLogz();
    return;
  }
  if(reMatch(".*/DMB_FEB_Unpacked_vs_DAV$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("textcolz");
    return;
  }
  if(reMatch(".*/Actual_DMB_CFEB_DAV_Frequency$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("histtext");
    return;
  }
  if(reMatch(".*/Actual_DMB_CFEB_DAV_Rate$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/DMB_CFEB_DAV_multiplicity_Unpacking_Inefficiency$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("textcolz");
    if(obj->GetMinimum() == obj->GetMaximum()) {
      obj->SetMaximum(obj->GetMinimum() + 0.01);
    }
    gPad->SetLogz();
    return;
  }
  if(reMatch(".*/DMB_FEB_Combinations_DAV_Unpacking_Inefficiency$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("textcolz");
    if(obj->GetMinimum() == obj->GetMaximum()) {
      obj->SetMaximum(obj->GetMinimum() + 0.01);
    }
    gPad->SetLogz();
    return;
  }
  if(reMatch(".*/Actual_DMB_CFEB_DAV_multiplicity_Frequency$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("histtext");
    return;
  }
  if(reMatch(".*/DMB_FEB_DAV_Unpacking_Inefficiency$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("textcolz");
    if(obj->GetMinimum() == obj->GetMaximum()) {
      obj->SetMaximum(obj->GetMinimum() + 0.01);
    }
    gPad->SetLogz();
    return;
  }
  if(reMatch(".*/Actual_DMB_FEB_Combinations_DAV_Frequency$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("histtext");
    return;
  }
  if(reMatch(".*/Actual_DMB_FEB_DAV_Frequency$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("histtext");
    return;
  }
  if(reMatch(".*/Actual_DMB_CFEB_DAV_multiplicity_Rate$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/Actual_DMB_FEB_DAV_Rate$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("histtext");
    return;
  }
  if(reMatch(".*/Actual_DMB_FEB_Combinations_DAV_Rate$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/CSC_Rate$", o.name)) {
    /** Applying histogram **/
    obj->SetOption("histtext");
    return;
  }
  if(reMatch(".*/DMB_BXN_Distrib$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("eo");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/DMB_BXN_vs_DDU_BXN$", o.name)) {
    /** Applying histogram **/
    obj->SetStats(false);
    obj->SetOption("box");
    return;
  }
  if(reMatch(".*/DMB_CFEB_Active$", o.name)) {
    /** Applying histogram **/
    obj->SetStats(false);
    gStyle->SetOptStat("e");
    obj->SetOption("hbar");
    return;
  }
  if(reMatch(".*/DMB_CFEB_Active_vs_DAV$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("colz");
    return;
  }
  if(reMatch(".*/DMB_CFEB_DAV$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/DMB_CFEB_DAV_multiplicity$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/DMB_CFEB_MOVLP$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("texthist");
    return;
  }
  if(reMatch(".*/DMB_CFEB_Sync$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("eo");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/DMB_DDU_BXN_diff$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emou");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/DMB_DDU_L1A_diff$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emou");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/DMB_FEB_DAV_Efficiency$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("histtext");
    return;
  }
  if(reMatch(".*/DMB_FEB_DAV_Rate$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("histtext");
    return;
  }
  if(reMatch(".*/DMB_FEB_Combinations_DAV_Efficiency$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/DMB_FEB_Combinations_DAV_Rate$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/DMB_FEB_Unpacked_vs_DAV$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("textcolz");
    return;
  }
  if(reMatch(".*/DMB_FEB_Combinations_Unpacked_vs_DAV$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("texthbar");
    return;
  }
  if(reMatch(".*/DMB_FEB_Timeouts$", o.name)) {
    /** Applying histogram **/
    gPad->SetLeftMargin(0.2);
    gStyle->SetOptStat("e");
    obj->SetOption("texthbar");
    return;
  }
  if(reMatch(".*/DMB_FIFO_stats$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("textcolz");
    return;
  }
  if(reMatch(".*/DMB_L1A_Distrib$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("eo");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/DMB_L1A_vs_ALCT_L1A$", o.name)) {
    /** Applying histogram **/
    obj->SetStats(false);
    obj->SetOption("box");
    return;
  }
  if(reMatch(".*/DMB_L1A_vs_CLCT_L1A$", o.name)) {
    /** Applying histogram **/
    obj->SetStats(false);
    obj->SetOption("box");
    return;
  }
  if(reMatch(".*/DMB_L1A_vs_DDU_L1A$", o.name)) {
    /** Applying histogram **/
    obj->SetStats(false);
    obj->SetOption("box");
    return;
  }
  if(reMatch(".*/DMB_L1_Pipe$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("e");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/TMB_ALCT_BXN_diff$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emuo");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/TMB_ALCT_L1A_diff$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emuo");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/TMB_BXN_vs_ALCT_BXN$", o.name)) {
    /** Applying histogram **/
    obj->SetStats(false);
    obj->SetOption("box");
    return;
  }
  if(reMatch(".*/TMB_L1A_vs_ALCT_L1A$", o.name)) {
    /** Applying histogram **/
    obj->SetStats(false);
    obj->SetOption("box");
    return;
  }
  if(reMatch(".*/TMB_Word_Count$", o.name)) {
    /** Applying histogram **/
    gStyle->SetOptStat("emo");
    obj->SetOption("hist");
    return;
  }
  if(reMatch(".*/BinCheck_DataFlow_Problems_Table$", o.name)) {
    /** Applying histogram **/
    gPad->SetLeftMargin(0.5);
    gPad->SetRightMargin(0.1);
    gStyle->SetOptStat("e");
    obj->SetOption("textcolz");
    return;
  }
  if(reMatch(".*/BinCheck_Errors_Frequency$", o.name)) {
    /** Applying histogram **/
    gPad->SetLeftMargin(0.5);
    gPad->SetRightMargin(0.1);
    gStyle->SetOptStat("e");
    obj->SetOption("textcolz");
    if(obj->GetMinimum() == obj->GetMaximum()) {
      obj->SetMaximum(obj->GetMinimum() + 0.01);
    }
    gPad->SetLogz();
    return;
  }
  if(reMatch(".*/BinCheck_DataFlow_Problems_Frequency$", o.name)) {
    /** Applying histogram **/
    gPad->SetLeftMargin(0.5);
    gPad->SetRightMargin(0.1);
    gStyle->SetOptStat("e");
    obj->SetOption("textcolz");
    if(obj->GetMinimum() == obj->GetMaximum()) {
      obj->SetMaximum(obj->GetMinimum() + 0.01);
    }
    gPad->SetLogz();
    return;
  }

  // ============== End generated from emuDQMBooking.xml by emuBooking2RenderPlugin.xsl ==================

      if(reMatch(".*FEDIntegrity/FEDEntries$", o.name) ||
         reMatch(".*FEDIntegrity/FEDFatal$", o.name) ||
         reMatch(".*FEDIntegrity/FEDFormatFatal$", o.name) ||
         reMatch(".*FEDIntegrity/FEDNonFatal$", o.name))
      {
        obj->SetStats(false);
        obj->SetFillColor(45);
        gStyle->SetOptStat("em");
        return;
      }

      if(reMatch(".*/CSC_L1A_out_of_sync$", o.name))
      {
        obj->SetStats(false);
        gStyle->SetOptStat("e");
        gPad->SetGridx();
        gPad->SetGridy();
        return;
      }
    }

  virtual void postDraw( TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo & ) {

      if(o.object == NULL)
        return;

      TH1* obj = dynamic_cast<TH1*>( o.object );
      if(obj == NULL)
        return;

      c->cd();

      if(reMatch(".*CSC_[0-9]+_[0-9]+/Chamber_Event_Display_No[0-9]$", o.name))
      {
        TH2* tmp = dynamic_cast<TH2*>(obj);
        eventDisplay.drawSingleChamber(tmp);
        return;
      }

      if(reMatch(".*Summary/Physics_EMU$", o.name))
      {
        TH2* tmp = dynamic_cast<TH2*>(obj);
        summaryMap.drawDetector(tmp);
        return;
      }

      if(reMatch(".*Summary/Physics_ME[1234]$", o.name))
      {
        std::string station_str = o.name;
        REREPLACE(".*Summary/Physics_ME([1234])$", station_str, "$1");
        TH2* obj2 = dynamic_cast<TH2*>(obj);
        summaryMap.drawStation(obj2, atoi(station_str.c_str()));
        return;
      }

      if(reMatch(".*Summary/CSC_STATS_[a-zA-Z0-9_-]+$", o.name) ||
         reMatch(".*EventInfo/reportSummaryMap$", o.name))
      {
        TH2* obj2 = dynamic_cast<TH2*>(obj);
        chamberMap.drawStats(obj2);
        return;
      }

      if(reMatch(".*Summary/CSC_[a-zA-Z0-9_-]+$", o.name) ||
         reMatch(".*FEDIntegrity/CSC_[a-zA-Z0-9_-]+$", o.name))
      {
        TH2* obj2 = dynamic_cast<TH2*>(obj);
        chamberMap.draw(obj2);
        return;
      }

      if(reMatch(".*Summary/Event_Display_Anode$", o.name))
      {
        TH2* tmp = dynamic_cast<TH2*>(obj);
        emuEventDisplay.drawEventDisplay_ZR(tmp);
        return;
      }

      if(reMatch(".*Summary/Event_Display_Cathode$", o.name))
      {
        TH2* tmp = dynamic_cast<TH2*>(obj);
        emuEventDisplay.drawEventDisplay_ZPhi(tmp);
        return;
      }

      if(reMatch(".*Summary/Event_Display_XY$", o.name))
      {
        TH2* tmp = dynamic_cast<TH2*>(obj);
        emuEventDisplay.drawEventDisplay_XY(tmp);
        return;
      }

      if(reMatch(".*TriggerPrimitivesEmulator/h_All$", o.name))
      {
        TH3* tmp = dynamic_cast<TH3*>(obj);
        hAll.draw(tmp);
        return;
      }

    }

private:

  bool reMatch(const std::string pat, const std::string str) {
      bool result = false;

      std::string key(pat);
      key.append(1, (char)9);
      key.append(str);

      MapOfPatternResults::iterator iter = mopr.find(key);

      if (iter == mopr.end())
      {
        result = TPRegexp(pat).MatchB(str);
        mopr[key] = result;
      }
      else
      {
        result = iter->second;
      }

      return result;
    }
};

static CSCRenderPlugin instance;
