#ifndef GEMRenderPlugin_SummaryChamber_H
#define GEMRenderPlugin_SummaryChamber_H

/*
 * =====================================================================================
 *
 *       Filename:  GEMRenderPlugin_SummaryChamber.h*
 *       (the original: CSCRenderPlugin_ChamberMap.h)
 *
 *    Description:  Makes a real GEM map out of the dummy histogram.
 *                  For more description, see CSCRenderPlugin_ChamberMap.h
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

#include <math.h>
#include <unordered_map>
#include <string>
#include <iostream>
#include <bitset>
#include <TH1.h>
#include <TH2.h>
#include <TBox.h>
#include <TText.h>
#include <TPRegexp.h>
#include <TStyle.h>
#include <TCanvas.h>


struct ChamberID {
  Int_t nRegion;
  Int_t nStation;
  Int_t nLayer;
  Int_t nChamber;
  
  Bool_t bIsDouble;
  
  Int_t nIdx;
};


uint32_t ChIdToInt(ChamberID &id);


/**
 * @class SummaryChamber
 * @brief Class that draws GEM Map diagram
 */
class SummaryChamber {
  private:

    static const unsigned short COLOR_WHITE  = 0;
    static const unsigned short COLOR_GREEN  = 3;
    static const unsigned short COLOR_RED    = 2;
    static const unsigned short COLOR_BLUE   = 4;
    static const unsigned short COLOR_GREY   = 17;
    static const unsigned short COLOR_YELLOW = 5;
    
    std::vector<TBox  *> m_listGEMBox;
    std::vector<TText *> m_listGEMText;
    
    Float_t m_fPosZeroX, m_fPosZeroY;
    Float_t m_fWHist, m_fHHist;

    TBox*  m_bBlank;
    TBox*  m_bLegend[10];
    TText* m_tLegend[10];

  public:
    SummaryChamber();
    ~SummaryChamber();
    void AddMoreGEMBox(int nNumBox);
    void SetColor(float fVal, TBox *box, unsigned int &unStatusAll, unsigned int &unStatusBad);
    void drawStats(TH2*& me);

  private:
    void printLegendBox(const unsigned int& number, const std::string title, int color);

};

#endif
