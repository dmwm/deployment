/*
 * =====================================================================================
 *
 *       Filename:  SummaryChamber.cc
 *       (the original: CSCRenderPlugin_ChamberMap.cc)
 *
 *    Description:  Makes a real GEM map out of the dummy histogram.
 *                  For more description, see CSCRenderPlugin_ChamberMap.cc
 *
 *        Version:  0.1
 *        Created:  22/06/2019
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Yuriy Pakhotin (YP), pakhotin@ufl.edu; Valdas Rapsevicius (VR), Valdas.Rapsevicius@cern.ch
 *         (the original)
 *        Company:  CERN, CH
 *         Copier:  Byeonghak Ko, bko@cern.ch, University of Seoul
 *
 * =====================================================================================
 */


#include "GEMRenderPlugin_SummaryChamber.h"
#include <unordered_map>


uint32_t ChIdToInt(ChamberID &id) {
  return ( ( id.nRegion + 1 ) << 11 ) | ( id.nStation << 9 ) | ( id.nLayer << 6 ) | ( id.nChamber << 0 );
}


SummaryChamber::SummaryChamber() {
  m_fPosZeroX = 0.5;
  m_fPosZeroY = 0.5;
  
  AddMoreGEMBox(800);
  
  m_bBlank = new TBox(m_fPosZeroX, m_fPosZeroY, m_fPosZeroX, m_fPosZeroY);
  m_bBlank->SetFillColor(0);
  m_bBlank->SetLineColor(1);
  m_bBlank->SetLineStyle(1);
  
  for (int i = 0; i < 10; i++) {
    m_bLegend[ i ] = new TBox(0.0, 0.0, 1.0, 1.0);
    m_tLegend[ i ] = new TText(0.0, 0.0, "");
    
    m_bLegend[ i ]->SetLineColor(1);
    m_bLegend[ i ]->SetLineStyle(2);
    
    m_tLegend[ i ]->SetTextAlign(22);
    m_tLegend[ i ]->SetTextFont(42);
    m_tLegend[ i ]->SetTextSize(0.015);
  }
}


SummaryChamber::~SummaryChamber() {
  for ( int i = 0 ; i < (int)m_listGEMBox.size() ; i++ ) {
    delete m_listGEMBox[ i ];
    delete m_listGEMText[ i ];
  }
  
  for ( int i = 0 ; i < 10 ; i++ ) {
    delete m_bLegend[ i ];
    delete m_bLegend[ i ];
  }
  
  delete m_bBlank;
}


void SummaryChamber::AddMoreGEMBox(int nNumBox) {
  for ( int i = (int)m_listGEMBox.size() ; i < nNumBox ; i++ ) {
    m_listGEMBox.push_back(nullptr);
    m_listGEMText.push_back(nullptr);
    m_listGEMBox[ i ]   = new TBox(0.0, 0.0, 1.0, 1.0);
    m_listGEMText[ i ] = new TText(0.0, 0.0, "");
    
    m_listGEMBox[ i ]->SetLineColor(1);
    m_listGEMBox[ i ]->SetLineStyle(2);
    
    m_listGEMText[ i ]->SetTextAlign(22);
    m_listGEMText[ i ]->SetTextFont(42);
    m_listGEMText[ i ]->SetTextSize(0.015);
  }
}


void SummaryChamber::SetColor(float fVal, TBox *box, unsigned int &unStatusAll, unsigned int &unStatusBad) {
  switch ((int)( fVal + 0.5 )) {
    // No data, no error
    case 0:
      box->SetFillColor(COLOR_WHITE);
      unStatusAll += 1;
      break;
    // Data, no error
    case 1:
      box->SetFillColor(COLOR_GREEN);
      unStatusAll += 1;
      break;
    // Error, hot
    case 2:
      box->SetFillColor(COLOR_RED);
      unStatusAll += 1;
      unStatusBad += 1;
      break;
    // Standby
    case 3:
      box->SetFillColor(COLOR_YELLOW);
      unStatusAll += 1;
      unStatusBad += 1;
      break;
    //// Masked
    //case 4:
    //  box->SetFillColor(COLOR_GREY);
    //  break;
    //// Cold
    //case 5:
    //  box->SetFillColor(COLOR_BLUE);
    //  unStatusAll += 1;
    //  unStatusBad += 1;
    //  break;
  }
}


void SummaryChamber::drawStats(TH2*& me) {
  gStyle->SetPalette(1, 0);
  
  int nNbinsX = me->GetNbinsX();
  int nNbinsY = me->GetNbinsY();
  
  // IMPORTANT NOTE: The position of the left-bottom corner of the histogram is (0.5, 0.5) 
  //                 and that of the right-top corner is (nNbinsX + 0.5, nNbinsY + 0.5).
  m_fWHist = nNbinsX;
  m_fHHist = nNbinsY;
  
  /** Cosmetics... :P */
  me->GetXaxis()->SetTitle("Chamber");
  me->GetXaxis()->CenterTitle(true);
  me->GetXaxis()->SetLabelSize(0.0);
  me->GetXaxis()->SetTicks("0");
  me->GetXaxis()->SetNdivisions(0);
  me->GetXaxis()->SetTickLength(0.0);
  
  me->SetStats(false);
  //me->Draw("axis");
  
  //m_bBlank->SetX1(0.5);  // Already set
  //m_bBlank->SetY1(0.5);
  m_bBlank->SetX2(m_fPosZeroX + m_fWHist);
  m_bBlank->SetY2(m_fPosZeroY + m_fHHist);
  m_bBlank->SetFillStyle(1001);
  m_bBlank->Draw("");
  
  unsigned int status_all = 0, status_bad = 0;
  
  int nNumTotalCh = 0;
  for ( int j = 1 ; j <= nNbinsY ; j++ ) nNumTotalCh += (int)( me->GetBinContent(0, j) + 0.5 );
  
  if ( nNumTotalCh > (int)m_listGEMBox.size() ) AddMoreGEMBox(nNumTotalCh);
  
  int nIdxBox = 0;
  float fHBox = m_fHHist / nNbinsY;
  for ( int nIdxLa = 1 ; nIdxLa <= nNbinsY ; nIdxLa++ ) {
    int nNumCh = (int)( me->GetBinContent(0, nIdxLa) + 0.5 );
    float fY1 = m_fPosZeroY + fHBox * ( nIdxLa - 1 ), fY2 = m_fPosZeroY + fHBox * nIdxLa;
    float fWBox = m_fWHist / nNumCh;
    for ( int nIdxCh = 1 ; nIdxCh <= nNumCh ; nIdxCh++ ) {
      float fX1 = m_fPosZeroX + fWBox * ( nIdxCh - 1 ), fX2 = m_fPosZeroX + fWBox * nIdxCh;
      auto boxCurr = m_listGEMBox[ nIdxBox ];
      auto texCurr = m_listGEMText[ nIdxBox ];
      float fVal = me->GetBinContent(nIdxCh, nIdxLa);
      
      boxCurr->SetX1(fX1);
      boxCurr->SetX2(fX2);
      boxCurr->SetY1(fY1);
      boxCurr->SetY2(fY2);
      SetColor(fVal, boxCurr, status_all, status_bad);
      boxCurr->Draw("l");
      
      texCurr->SetText(0.5 * ( fX1 + fX2 ), 0.5 * ( fY1 + fY2 ), Form("%i", nIdxCh));
      texCurr->Draw();
      
      nIdxBox++;
    }
  }
  
  printLegendBox(0, "OK/No Data", COLOR_WHITE);
  printLegendBox(1, "OK/Data", COLOR_GREEN);
  printLegendBox(2, "Error", COLOR_RED);
  printLegendBox(3, "Warning", COLOR_YELLOW);
}


void SummaryChamber::printLegendBox(const unsigned int& number, const std::string title, int color) {
  Float_t fRatioY = 1.0 / 24.0;
  Int_t nNumItem = 4;
  Float_t fBasisX = m_fPosZeroX + m_fWHist + 1.00;
  Float_t fBasisY = m_fPosZeroY + m_fHHist * 0.50 + 0.5 * ( 2 * nNumItem - 1 ) * fRatioY * m_fHHist;
  
  Float_t fX1 = fBasisX;
  Float_t fX2 = fBasisX + 0.07 * m_fWHist;
  Float_t fY1 = fBasisY - ( number + 1 ) * fRatioY * m_fHHist;
  Float_t fY2 = fBasisY -   number       * fRatioY * m_fHHist;
  
  m_bLegend[ number ]->SetX1(fX1);
  m_bLegend[ number ]->SetX2(fX2);
  m_bLegend[ number ]->SetY1(fY1);
  m_bLegend[ number ]->SetY2(fY2);
  m_bLegend[ number ]->SetFillColor(color);
  m_bLegend[ number ]->Draw("l");
  
  m_tLegend[ number ]->SetText(0.5 * ( fX1 + fX2 ), 0.5 * ( fY1 + fY2 ), title.c_str());
  m_tLegend[ number ]->Draw();
}
