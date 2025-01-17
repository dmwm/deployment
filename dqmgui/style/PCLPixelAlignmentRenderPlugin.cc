#include "DQM/DQMRenderPlugin.h"
#include "utils.h"
#include "TCanvas.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TProfile.h"
#include "TObjString.h"
#include "TProfile2D.h"
#include "TStyle.h"
#include "TGaxis.h"
#include "TPaveStats.h"
#include "TList.h"
#include "TLine.h"
#include "TString.h"
#include <cassert>

class PCLPixelAlignmentRenderPlugin : public DQMRenderPlugin
{
  std::array<double,6> sigCut_;
  std::array<double,6> cut_;
  std::array<double,6> maxMoveCut_;
  std::array<double,6> maxErrorCut_;

public:

  virtual void initialise (int, char **)
  {


  }

  virtual bool applies(const VisDQMObject &o, const VisDQMImgInfo &)
  {
    if(o.name.find( "SiPixelAli" ) != std::string::npos)return true;
    else return false;
  }

  virtual void preDraw(TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &, VisDQMRenderInfo &)
  {
    c->cd();

    // Check if HG alignment is used
    bool isHG = ((o.name.find( "SiPixelAliHG" ) != std::string::npos) || (o.name.find( "SiPixelAliHLTHG" ) != std::string::npos));


    if( dynamic_cast<TH1F*>( o.object ) )
    {
      if (isHG){
        this->preDrawTH1FHG( c, o );
      }else{
        this->preDrawTH1F( c, o );
      }
    }
    else if( dynamic_cast<TH2F*>( o.object ) )
    {
      this->preDrawTH2F( c, o );
    }
    else if( dynamic_cast<TProfile*>( o.object ) )
    {
      if (!isHG) this->preDrawTProfile( c, o );
    }
    else if( dynamic_cast<TProfile2D*>( o.object ) )
    {
      if (!isHG) this->preDrawTProfile2D( c, o );
    }
  }

  virtual void postDraw(TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &)
  {
    c->cd();

    if( dynamic_cast<TObjString*>( o.object ) ){
      if( o.name.find("SiPixelAli")!= std::string::npos){
        if(o.name.find("PedeExitCode") != std::string::npos){
          // Clear the default string from the canvas
          c->Clear();
          
          TObjString* tos = dynamic_cast<TObjString*>( o.object );
          auto exitCode = TString((tos->GetString())(0,6));
          TText *t = new TText(.5, .5, tos->GetString());
          t->SetTextFont(63);
          t->SetTextAlign(22);
          t->SetTextSize(18);
          // from Pede manual: http://www.desy.de/~kleinwrt/MP2/doc/html/exit_code_page.html
          // all exit codes <  10 are normal endings
          // all exit codes >= 10 indicated an aborted measurement
          if(exitCode.Atoi()>=10){
            t->SetTextColor(kRed);
          } else {
            t->SetTextColor(kGreen+2);
          }
          t->Draw();
        }
        if(o.name.find("IsVetoed") != std::string::npos){
          // Clear the default string from the canvas
          c->Clear();

          TObjString* tos = dynamic_cast<TObjString*>( o.object );
          auto strIsVetoed = TString((tos->GetString()));
          TText *t = new TText(.5, .5, strIsVetoed);
          t->SetTextFont(63);
          t->SetTextAlign(22);
          t->SetTextSize(50);
          // Print the three different options (Veto,Update,N/A) in three different colors
          if(strIsVetoed.Contains("Vetoed")){
            t->SetTextColor(kRed);
          } else if(strIsVetoed.Contains("Updated")){
            t->SetTextColor(kGreen+2);
          } else{
            t->SetTextColor(kGray+1);
          }
          t->Draw();
        }
      }
    }

    // Check if HG alignment is used
    bool isHG = ((o.name.find( "SiPixelAliHG" ) != std::string::npos) || (o.name.find( "SiPixelAliHLTHG" ) != std::string::npos));

    if( dynamic_cast<TH1F*>( o.object ) )
    {
      if (isHG){
          this->postDrawTH1FHG( c, o );
        }else{
          this->postDrawTH1F( c, o );
       }
    }
    else if( dynamic_cast<TH2F*>( o.object ) )
    {
      this->postDrawTH2F( c, o );
    }
    else if( dynamic_cast<TProfile*>( o.object ) )
    {
      if (!isHG) this->postDrawTProfile( c, o );
    }
    else if( dynamic_cast<TProfile2D*>( o.object ) )
    {
      if (!isHG) this->postDrawTProfile2D( c, o );
    }
  }

private:

  void preDrawTH1F(TCanvas *c, const VisDQMObject &o)
  {
    gStyle->SetCanvasBorderMode(0);
    gStyle->SetPadBorderMode(0);
    gStyle->SetPadBorderSize(0);

    gStyle->SetOptStat(111110);
    gStyle->SetTitleSize(0.06,"");
    gStyle->SetTitleX(0.18);


    TH1F* obj = dynamic_cast<TH1F*>( o.object );
    assert( obj );

    c->SetLogy(0);
    c->SetTopMargin(0.08);
    c->SetBottomMargin(0.14);
    c->SetLeftMargin(0.11);
    c->SetRightMargin(0.09);

    // dirty trick to ensure compatibility
    // with old histogram format

    const int& nBins = obj->GetNbinsX();
    if(nBins>11){
      for(size_t i=0;i<6;i++){
        cut_[i] = obj->GetBinContent(8+5*i);
        sigCut_[i] = obj->GetBinContent(9+5*i);
        maxMoveCut_[i] = obj->GetBinContent(10+5*i);
        maxErrorCut_[i] = obj->GetBinContent(11+5*i);
      }
    } else {

      for(size_t i=0;i<6;i++){
        cut_[i] = obj->GetBinContent(8);
        sigCut_[i] = obj->GetBinContent(9);
        maxMoveCut_[i] = obj->GetBinContent(10);
        maxErrorCut_[i] = obj->GetBinContent(11);
      }
    }

    obj->SetLineColor(kBlack);
    obj->SetLineWidth(2);
    obj->SetFillColor(kGreen+3);

    double max = -1000;
    double min = 1000;

    for (int i = 1; i < 7; i++){

      if (obj->GetBinContent(i) < min) min = obj->GetBinContent(i);
      if (obj->GetBinContent(i) > max) max = obj->GetBinContent(i);

      if (fabs(obj->GetBinContent(i)) > maxMoveCut_[i-1]) obj->SetFillColor(kRed);
      else if (obj->GetBinContent(i) > cut_[i-1]){

        if (obj->GetBinError(i) > maxErrorCut_[i-1]){
          obj->SetFillColor(kRed);
        }
        else if (fabs(obj->GetBinContent(i))/obj->GetBinError(i) > sigCut_[i-1]){

          obj->SetFillColor(kGreen+3);
        }
      }
    }

    obj->GetXaxis()->SetBinLabel(1,"FPIX(x+,z-)");
    obj->GetXaxis()->SetBinLabel(2,"FPIX(x-,z-)");
    obj->GetXaxis()->SetBinLabel(3,"BPIX(x+)");
    obj->GetXaxis()->SetBinLabel(4,"BPIX(x-)");
    obj->GetXaxis()->SetBinLabel(5,"FPIX(x+,z+)");
    obj->GetXaxis()->SetBinLabel(6,"FPIX(x-,z+)");

    obj->GetXaxis()->SetTitleSize(0.06);
    obj->GetXaxis()->SetLabelSize(0.06);
    obj->GetXaxis()->SetTitleOffset(1.05);
    obj->GetYaxis()->SetTitleOffset(0.95);
    obj->GetXaxis()->SetRangeUser(0,6);

    obj->GetYaxis()->SetTitleSize(0.06);
    obj->GetYaxis()->SetLabelSize(0.06);

    double maxCut_ = *std::max_element(cut_.begin(),cut_.end());

    obj->GetYaxis()->SetRangeUser(std::min(min-20,-maxCut_-20),std::max(max+20,maxCut_+20));

    obj->SetStats(kFALSE);
    obj->SetFillStyle(3017);
    obj->SetOption("histe");

  }

  void preDrawTH1FHG(TCanvas *c, const VisDQMObject &o)
  {
    gStyle->SetCanvasBorderMode(0);
    gStyle->SetPadBorderMode(0);
    gStyle->SetPadBorderSize(0);

    gStyle->SetOptStat(111110);
    gStyle->SetTitleSize(0.06,"");
    gStyle->SetTitleX(0.18);

    c->SetTopMargin(0.08);
    c->SetBottomMargin(0.14);
    c->SetLeftMargin(0.11);
    c->SetRightMargin(0.09);


    TH1F* obj = dynamic_cast<TH1F*>( o.object );
    assert( obj );

    int nBins = obj->GetNbinsX();

    double cutValue = obj->GetBinContent(nBins - 3);

    double max_ = -1;
    double min_ = 1;
    int alignableCount = 0;

    for (int i = 1; i <= nBins-5; i++){
      double content = obj->GetBinContent(i);

      if (content > max_){
        max_ = obj->GetBinContent(i);
      }
      if (content < min_){
        min_ = obj->GetBinContent(i);
      }
      alignableCount++;
    }

    obj->GetYaxis()->SetRangeUser(std::min(min_-20,-cutValue-20)*1.2,std::max(max_+20,cutValue+20)*1.2);
    obj->GetXaxis()->SetRangeUser(0,alignableCount);

    obj->SetMarkerStyle(20);
    obj->SetMarkerSize(0.6);
    obj->SetStats(kFALSE);
    obj->SetOption("PE");


  }



  void preDrawTH2F(TCanvas *, const VisDQMObject &o)
  {
    TH2F* obj = dynamic_cast<TH2F*>( o.object );
    assert( obj );

    if( o.name.find("SiPixelAli")!= std::string::npos && o.name.find("statusResults") != std::string::npos){
      gPad->SetGrid();
      dqm::utils::reportSummaryMapPalette(obj);
      obj->SetMarkerSize(1.5);
      obj->SetOption("colztext");
      return;
    }
  }

  void preDrawTProfile(TCanvas *, const VisDQMObject &o)
  {
    TProfile* obj = dynamic_cast<TProfile*>( o.object );
    assert( obj );

  }

  void preDrawTProfile2D(TCanvas *, const VisDQMObject &o)
  {
    TProfile2D* obj = dynamic_cast<TProfile2D*>( o.object );
    assert( obj );

  }

  void postDrawTH1F(TCanvas *, const VisDQMObject &o)
  {
    TH1F* obj = dynamic_cast<TH1F*>( o.object );
    assert( obj );

    gStyle->SetOptStat(111110);

    obj->SetStats( kFALSE );

    // dirty trick to ensure compatibility
    // with old histogram format

    const int& nBins = obj->GetNbinsX();
    if(nBins>11){
      for(size_t i=0;i<6;i++){
        cut_[i] = obj->GetBinContent(8+5*i);
        sigCut_[i] = obj->GetBinContent(9+5*i);
        maxMoveCut_[i] = obj->GetBinContent(10+5*i);
        maxErrorCut_[i] = obj->GetBinContent(11+5*i);
      }
    } else {

      for(size_t i=0;i<6;i++){
        cut_[i] = obj->GetBinContent(8);
        sigCut_[i] = obj->GetBinContent(9);
        maxMoveCut_[i] = obj->GetBinContent(10);
        maxErrorCut_[i] = obj->GetBinContent(11);
      }
    }

    TLine* line = new TLine();
    line->SetBit(kCanDelete);
    line->SetLineWidth(2);
    line->SetLineColor(kRed+2);

    for(size_t i=0;i<6;i++){
      line->DrawLine(i, cut_[i], i+1, cut_[i]);
      line->DrawLine(i, -cut_[i],i+1, -cut_[i]);
    }

    line->SetLineColor(kBlue+2);
    line->DrawLine(0, 0, 6, 0);

    TText* t_text = new TText();
    t_text->SetBit(kCanDelete);
    t_text->SetNDC(true);

    bool hitMax = false;
    bool moved = false;
    bool hitMaxError = false;
    bool sigMove = false;

    for (int i = 1; i < 7; i++){

      if (fabs(obj->GetBinContent(i)) > maxMoveCut_[i-1]){
        hitMax = true;
      }
      else if (fabs(obj->GetBinContent(i)) > cut_[i-1]){
        moved = true;
        if (obj->GetBinError(i) > maxErrorCut_[i-1]){
          hitMaxError = true;
        }
        else if (fabs(obj->GetBinContent(i))/obj->GetBinError(i) > sigCut_[i-1]){
          sigMove = true;
        }
      }
    }
    if (hitMax){
      obj->SetFillColor(kRed);
      t_text->DrawText(0.25,0.8, "Exceeds Maximum Movement");
    }
    else if (moved) {
      if (hitMaxError){
        obj->SetFillColor(kRed);
        t_text->DrawText(0.25,0.8, "Movement uncertainty exceeds maximum");
      }
      else if (sigMove){
        obj->SetFillColor(kOrange);
        t_text->DrawText(0.25,0.8, "Significant movement observed");
      }
    }
    else t_text->DrawText(0.25,0.8, "Movement within limits");

    return;
  }

    void postDrawTH1FHG(TCanvas *, const VisDQMObject &o)
  {
    TH1F* obj = dynamic_cast<TH1F*>( o.object );
    assert( obj );

    int nBins = obj->GetNbinsX();

    double cutValue = obj->GetBinContent(nBins - 3);
    double significance = obj->GetBinContent(nBins - 2);
    double maxMove = obj->GetBinContent(nBins - 1);
    double maxError = obj->GetBinContent(nBins);

    TLine* line = new TLine();
    line->SetBit(kCanDelete);
    line->SetLineWidth(2);
    line->SetLineColor(kRed+2);

    line->DrawLine(0, cutValue, nBins-5, cutValue);
    line->DrawLine(0, -cutValue, nBins-5, -cutValue);

    line->SetLineColor(kBlue+2);
    line->DrawLine(0, 0, nBins-5, 0);


    int alignableCount = 0; // number of alignables
    // THRESHOLD
    int aboveCutCount = 0; // number of alignables above threshold cut
    int aboveSigCount = 0; // number that fulfill prior condition and are significant
    // VETO
    int aboveMaxMoveCount = 0; // number outside movement bounds
    int aboveMaxErrorCount = 0; // number outside error bounds

    for (int i = 1; i <= nBins-5; i++){
      double content = obj->GetBinContent(i);
      double error = obj->GetBinError(i);
  
      if (content == 0 && error == 0){
        obj->SetBinContent(i, 0.00001);
        continue;
      }
  
      alignableCount++;
      if(std::abs(content) > maxMove){
        aboveMaxMoveCount++;
      }
      if(error > maxError){
        aboveMaxErrorCount++;
      }
      
      if(std::abs(content) >= cutValue){
        aboveCutCount++;
        if (std::abs(content/error) >= significance){
          aboveSigCount++;
        }
      }
      
    }

    double fraction = 0.25;
    bool aboveCut =       ((double)aboveCutCount / (double)alignableCount >= fraction ) ;
    bool aboveSig =       ((double)aboveSigCount / (double)alignableCount  >= fraction);
    bool vetoMaxMove =  aboveMaxMoveCount > 0;
    bool vetoMaxError = aboveMaxErrorCount > 0;

    TText* t_text = new TText();
    t_text->SetBit(kCanDelete);
    t_text->SetNDC(true);
    
    TString alignableType;
    std::string axisTitle = obj->GetXaxis()->GetTitle();
    if (axisTitle.find( "Panel" ) != std::string::npos){
      alignableType = "panels";
    }else{
      alignableType = "ladders";
    }
    
    if(vetoMaxMove){
      // Red, too large max error
      obj->SetMarkerColor(kRed);
      obj->SetLineColor(kRed);
      t_text->DrawText(0.13,0.87, "Movements exceed max movement, veto");
    }else if(vetoMaxError){
      // Red, too large max error
      obj->SetMarkerColor(kRed);
      obj->SetLineColor(kRed);
      t_text->DrawText(0.13,0.87, "Errors exceed max error, veto");
    }else if(aboveSig){
      // Orange
      obj->SetMarkerColor(kOrange);
      obj->SetLineColor(kOrange);
      t_text->DrawText(0.13,0.87, "Significant movements above threshold");
      t_text->DrawText(0.13,0.83, TString::Format("%.1f%% of %d aligned %s",100*((double)aboveSigCount / (double)alignableCount), alignableCount,alignableType.Data()));

    }else if(aboveCut){
      // Green, movements above threshold not significant
      obj->SetMarkerColor(kGreen+1);
      obj->SetLineColor(kGreen+1);
      t_text->DrawText(0.13,0.87, "Movements above threshold not significant");
      t_text->DrawText(0.13,0.83, TString::Format("Above significance: %.1f%% of %d aligned %s",100*((double)aboveSigCount / (double)alignableCount), alignableCount,alignableType.Data()));

    }else{
      // Grey, movements not above threshold
      obj->SetMarkerColor(kGray+2);
      obj->SetLineColor(kGray+2);
      t_text->DrawText(0.13,0.87, "Movements within threshold");
      t_text->DrawText(0.13,0.83, TString::Format("Above threshold: %.1f%% of %d aligned %s",100*((double)aboveCutCount / (double)alignableCount), alignableCount,alignableType.Data()));
    }


  }

  void postDrawTH2F(TCanvas *, const VisDQMObject &o)
  {
    TH2F* obj = dynamic_cast<TH2F*>( o.object );
    assert( obj );

    obj->SetStats( kFALSE );

  }

  void postDrawTProfile(TCanvas *, const VisDQMObject &o)
  {
    TProfile* obj = dynamic_cast<TProfile*>( o.object );
    assert( obj );

  }

void postDrawTProfile2D(TCanvas *, const VisDQMObject &o)
  {
    TProfile2D* obj = dynamic_cast<TProfile2D*>( o.object );
    assert( obj );

  }
};

static PCLPixelAlignmentRenderPlugin instance;
