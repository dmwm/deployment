#include "DQM/DQMRenderPlugin.h"
#include "TCanvas.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TProfile.h"
#include "TProfile2D.h"
#include "TStyle.h"
#include "TGaxis.h"
#include "TPaveStats.h"
#include "TList.h"
#include "TLine.h"
#include <cassert>

class PCLPixelAlignmentRenderPlugin : public DQMRenderPlugin
{
	double sigCut_;
	double cut_;
	double maxMoveCut_;
	double maxErrorCut_;
	
	
		
public:

  virtual void initialise (int, char **)
  {
	
	
  }

  virtual bool applies(const VisDQMObject &o, const VisDQMImgInfo &)
  {
    if(o.name.find( "SiPixelAli/" ) != std::string::npos)return true;
    else return false;
  }

  virtual void preDraw(TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &, VisDQMRenderInfo &)
  {
    c->cd();

    if( dynamic_cast<TH1F*>( o.object ) )
    {
      this->preDrawTH1F( c, o );
    }
    else if( dynamic_cast<TH2F*>( o.object ) )
    {
      this->preDrawTH2F( c, o );
    }
    else if( dynamic_cast<TProfile*>( o.object ) )
    {
      this->preDrawTProfile( c, o );
    }
    else if( dynamic_cast<TProfile2D*>( o.object ) )
    {
      this->preDrawTProfile2D( c, o );
    }
  }

  virtual void postDraw(TCanvas *c, const VisDQMObject &o, const VisDQMImgInfo &)
  {
    c->cd();

    if( dynamic_cast<TH1F*>( o.object ) )
    {
      this->postDrawTH1F( c, o );
    }
    else if( dynamic_cast<TH2F*>( o.object ) )
    {
      this->postDrawTH2F( c, o );
    }
    else if( dynamic_cast<TProfile*>( o.object ) )
    {
      this->postDrawTProfile( c, o );
    }
    else if( dynamic_cast<TProfile2D*>( o.object ) )
    {
      this->postDrawTProfile2D( c, o );
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

    cut_ = obj->GetBinContent(8);
    sigCut_ = obj->GetBinContent(9);
    maxMoveCut_ = obj->GetBinContent(10);
    maxErrorCut_ = obj->GetBinContent(11);


    obj->SetLineColor(kBlack);
    obj->SetLineWidth(2);
    obj->SetFillColor(kGreen+3);

    double max = -1000;
    double min = 1000;


    for (int i = 1; i < 7; i++){

    	if (obj->GetBinContent(i) < min) min = obj->GetBinContent(i);
    	if (obj->GetBinContent(i) > max) max = obj->GetBinContent(i);


	if (fabs(obj->GetBinContent(i)) > maxMoveCut_) obj->SetFillColor(kRed);
	else if (obj->GetBinContent(i) > cut_){

		if (obj->GetBinError(i) > maxErrorCut_){
			obj->SetFillColor(kRed);
		}
		else if (fabs(obj->GetBinContent(i))/obj->GetBinError(i) > sigCut_){

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
    obj->GetXaxis()->SetRangeUser(0,6);

    obj->GetYaxis()->SetTitleSize(0.06);
    obj->GetYaxis()->SetLabelSize(0.06);

    obj->GetYaxis()->SetRangeUser(std::min(min-20,-cut_-20),std::max(max+20,cut_+20));

    obj->SetStats(kFALSE);
    obj->SetFillStyle(3017);
    obj->SetOption("histe");
    
  }

  void preDrawTH2F(TCanvas *, const VisDQMObject &o)
  {
    TH2F* obj = dynamic_cast<TH2F*>( o.object );
    assert( obj );

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

    cut_ = obj->GetBinContent(8);
    sigCut_ = obj->GetBinContent(9);
    maxMoveCut_ = obj->GetBinContent(10);
    maxErrorCut_ = obj->GetBinContent(11);
                    
    TLine* line = new TLine();
    line->SetBit(kCanDelete);
    line->SetLineWidth(2);
    line->SetLineColor(kRed+2);
    line->DrawLine(0, cut_, 6, cut_);
    line->DrawLine(0, -cut_, 6, -cut_);
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

	if (fabs(obj->GetBinContent(i)) > maxMoveCut_){
		hitMax = true;	
	}		
	else if (obj->GetBinContent(i) > cut_){
		moved = true;
		if (obj->GetBinError(i) > maxErrorCut_){
			hitMaxError = true;
		}
		else if (fabs(obj->GetBinContent(i))/obj->GetBinError(i) > sigCut_){
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

  void postDrawTH2F(TCanvas *, const VisDQMObject &o)
  {
    TH2F* obj = dynamic_cast<TH2F*>( o.object );
    assert( obj );

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
