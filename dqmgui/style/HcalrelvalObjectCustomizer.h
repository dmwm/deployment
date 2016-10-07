/*
 *	file:			        HcalrelvalObjectCustomizer.h
 *	original author:		Viktor Khristenko
 *	modified by:			Shubham Pandey (shubham.pandey@cern.ch)
 *      Description:                    Header file for HcalrelvalRenderPlugin.cc
 */

//	ROOT Includes
#include "TCanvas.h"
#include "TText.h"
#include "TColor.h"
#include "TROOT.h"
#include "TH1.h"
#include "TH1D.h"
#include "TH1F.h"
#include "TH2.h"
#include "TH2D.h"
#include "TH2F.h"
#include "TProfile.h"
#include "TProfile2D.h"
#include "TH3D.h"
#include "TStyle.h"
#include "TGaxis.h"
#include "TText.h"
#include "TLine.h"
#include "TPaletteAxis.h"

//	STD includes
#include <string>
#include <vector>



#include <dirent.h>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <map>
#include <cstdio>
using namespace std;


//	hcaldqm includes

//	hcaldqm namespace for HcalObjectCustomization API
namespace hcaldqm
{
  
  //	Render Types: 2 so far
  enum RenderType
  {
    kHcal		= 0,
    kHcalCalib	= 1,
    nRenderType = 2
  };
  
  //	Specifies the ROOT Class Type
  enum ROOTType
  {
    kTH1D		= 0,
    kTH1F		= 1,
    kTH2D		= 2,
    kTH2F		= 3,
    kTProfile	= 4,
    kTProfile2D = 5,
    kTH3D		= 6,
    kInvalid	= 7,
    nROOTTypes	= 8
  };
  
  //	Specifies the TObject bits convention
  int const bitshift = 19;
  enum ObjectBits
  {
    kAxisLogx		= 0,
    kAxisLogy		= 1,
    kAxisLogz		= 2,
    kAxisLS			= 3,
    kAxisFlag		= 4,
    nObjectBits = 5
  };
  
  //	Summary Detector Status Constants
  //	to be used in the next iteration of cmssw
  enum State
  {
    fNONE = 0,
    fNCDAQ = 1,
    fNA = 2,
    fGOOD = 3,
    fPROBLEMATIC = 4,
    fBAD = 5,
    fRESERVED = 6,
    nState = 7
  };



  //To be used for weblogs
  struct logs {
    std::string name;
    int y;
    int m;
    int d;
  };


  
  //	Class HcalrelvalObjectCustomizer
  class HcalrelvalObjectCustomizer
  {
  public: 
  HcalrelvalObjectCustomizer():_type(kHcal), _verbosity(0)
      {}
    ~HcalrelvalObjectCustomizer() {}
    
    //	Apply standard customizations for Styles or Canvas or anything 
    //	Apply standard customizations for all of the objects
    void preDraw_Standard(TCanvas *c)
    {
      if (_verbosity>0)
	std::cout << "Calling preDraw_Standard" << std::endl;
      gStyle->Reset("Default");
      gStyle->SetCanvasColor(10);
      gStyle->SetPadColor(10);
      gStyle->SetFillColor(10);
      gStyle->SetStatColor(10);
      gStyle->SetTitleFillColor(10);
      gStyle->SetOptTitle(kTRUE);
      gStyle->SetTitleBorderSize(0);
      gStyle->SetOptStat(kFALSE);
      gStyle->SetStatBorderSize(1);
      gROOT->ForceStyle();
      
      TGaxis::SetMaxDigits(4);
      c->Draw();
      
    }
    
    void postDraw_Standard(TCanvas*, VisDQMObject const&,  VisDQMImgInfo const&)
    {}
    
    //	Initialize all the Color Schemes
    void initialize_ColorSchemes()
    {
      //	summary
      _n_summary = nState - fNONE;
      _colors_summary[0] = kWhite;
      _colors_summary[1] = kGray;
      _colors_summary[2] = kWhite;
      _colors_summary[3] = kGreen;
      _colors_summary[4] = kYellow;
      _colors_summary[5] = kRed;
      _colors_summary[6] = kBlack;
      _contours_summary[0] = fNONE;
      _contours_summary[1] = fNCDAQ;
      _contours_summary[2] = fNA;
      _contours_summary[3] = fGOOD;
      _contours_summary[4] = fPROBLEMATIC;
      _contours_summary[5] = fBAD;
      _contours_summary[6] = fRESERVED;
      _contours_summary[7] = nState;
    }
    
    //	Initialize Filters - Names for Searching
    void initialize_Filters()
    {}
    
    //	Initialize Render Type
    void initialize_Type(RenderType type)
    {
      _type = type;
    }
    
    //	Customize 1D
    void pre_customize_1D(hcaldqm::ROOTType type, TCanvas* c,
			  VisDQMObject const& o,
			  VisDQMImgInfo const& ii,
			  VisDQMRenderInfo &ri)
    {
      if (_verbosity>0)
	std::cout << "Calling customize_1D" << std::endl;

      //spandey: Basic cosmetics
      c->cd();	
      c->GetPad(0)->SetFillColor(kCyan-10);
      c->GetPad(0)->SetGridx();
      c->GetPad(0)->SetGridy();


      //Get appropriate ranges according to the last loaded sample
      hist_range values = driver(o.object->GetName());
      
      if (values.xmax > 0 || values.xmin != 0)  //change xAxis range
        ((TH1F*)o.object)->GetXaxis()->SetRangeUser(values.xmin, values.xmax);


      //yAxis range, log_flag etc                                                                                                                                       
      if (values.ymin != 0) ((TH1F*)o.object)->SetMinimum(values.ymin);
      if (values.ymax > 0) ((TH1F*)o.object)->SetMaximum(values.ymax); 
      if (values.log_flag) {
	c->GetPad(0)->SetLogy();
	if (values.ymax < 0)
	  ((TH1F*)o.object)->SetMaximum((((TH1F*)o.object)->GetMaximum())*5);
	
      }

      //cosmetics      
      if ((type == kTH1F) || (type == kTH1D)) {
	((TH1F*)o.object)->SetLineStyle(2);
	((TH1F*)o.object)->SetLineWidth(2);
	if (values.chi2_flag) {
	  ((TH1F*)o.object)->SetFillColor(42);
	  ((TH1F*)o.object)->SetLineColor(kBlack);
	}
	else
	  ((TH1F*)o.object)->SetLineColor(kPink);

	ri.drawOptions = "hist";
	c->Modified();
      }
      
      

      //	by default
      
      
      //	further customization
      this->pre_customize_ByName(c, o, ii, ri);
      this->pre_customize_ByBits(type, c, o, ii, ri);
      
      //	for 1D Profiles
      //	NOTE: for profiles always hide non occupied xbins
      //	independent of the type of the axis (LS or not...)
      if (type==kTProfile)
	{

	  TProfile *obj = dynamic_cast<TProfile*>(o.object);
	  bool foundfirst = false;
	  int first = 1;
	  int last = 1;
	  for (int i=first; i<=obj->GetNbinsX(); i++)
	    {
	      if (!foundfirst && obj->GetBinContent(i)!=0)
		{
		  first = i;
		  foundfirst = true;
		}
	      if (obj->GetBinContent(i)!=0)
		last = i+1;
	    }
	  if (last-first>=1)
	    obj->GetXaxis()->SetRange(first, last);
	  
	  //cosmetics
	  obj->SetErrorOption("");
	  obj->SetMarkerStyle(20);
	  obj->SetLineColor(kGreen+2);
	  obj->SetLineStyle(1);
	  obj->SetLineWidth(1);
	  obj->SetMarkerColor(kGreen+2);
	  obj->SetMarkerStyle(22);
	  obj->SetMarkerSize(1.0);
	  ri.drawOptions = "hist pl";
	  c->Modified();
	}
    }
    
    //	Customize 2D
    void pre_customize_2D(hcaldqm::ROOTType type, TCanvas* c, VisDQMObject const& o, VisDQMImgInfo const& ii, VisDQMRenderInfo &ri)
    {
      if (_verbosity>0)
	std::cout << "Calling customize_2D" << std::endl;
      
      //	By default 
      //	1) colz
      //	2) No Statistics for 2D plots
      //	3) z plot range (min, max)
      //	4) Set Rainbow Palette(1 is for Rainbow Color Map)
      ri.drawOptions = "colz";
      ((TH2*)o.object)->SetStats(kFALSE);
      ((TH2*)o.object)->GetZaxis()->SetRangeUser(((TH2*)o.object)->GetMinimum(), ((TH2*)o.object)->GetMaximum());
      gStyle->SetPalette(1);
      
      //		
      this->pre_customize_ByName(c, o, ii, ri);
      this->pre_customize_ByBits(type, c, o, ii, ri);
    }
    
    //	post customize 1D
    void post_customize_1D(hcaldqm::ROOTType, TCanvas *, VisDQMObject const&, VisDQMImgInfo const&)
    {}
    
    //	post customize 2D
    void post_customize_2D(hcaldqm::ROOTType, TCanvas *, VisDQMObject const& o, VisDQMImgInfo const&)
    {
      if (_verbosity>0)
	std::cout << "Caliing post_customize_2D" << std::endl;
      
      TString fullpath(o.name.c_str());
      
      //	for summaries
      /*if (fullpath.Contains("Summary"))
	{
	gPad->Update();
	TBox *box_GOOD = new TBox(0.8, 0.8, 0.9, 0.9);
	box_GOOD->SetFillColor(kGreen);
	box_GOOD->Draw();
	}*/
    }
    
    //	Customize By Name
    void pre_customize_ByName(TCanvas* c, VisDQMObject const& o, VisDQMImgInfo const&, VisDQMRenderInfo & ri)
    {
      if (_verbosity>0)
	std::cout << "Calling customize_ByName" << std::cout;
      
      TString fullpath(o.name.c_str());
      
      //	for summaries
      if (fullpath.Contains("Summary"))
	{
	  ri.drawOptions = "col";
	  if (!fullpath.Contains("runSummary"))
	    c->SetGrid();
	  gStyle->SetPalette(_n_summary,
			     _colors_summary);
	  ((TH2*)o.object)->SetContour(_n_summary+1,  _contours_summary);
	}
    }
    
    //	Customize by Bits
    void pre_customize_ByBits(hcaldqm::ROOTType type, TCanvas*,
			      VisDQMObject const& o, VisDQMImgInfo const&,
			      VisDQMRenderInfo &)
    {
      if (_verbosity>0)
	std::cout << "Calling customize_ByBits" << std::endl;
      
      for (int i=0; i<nObjectBits; i++)
	{
	  if (!isBitSet(i, o.object))
	    continue;
	  
	  //	do based on which bit it is
	  switch (i)
	    {
	    case kAxisLogx:
	      gPad->SetLogx(1);
	      break;
	    case kAxisLogy:
	      gPad->SetLogy(1);
	      break;
	    case kAxisLogz:
	      gPad->SetLogz(1);
	      break;
	    case kAxisLS:
	      if (type==kTH2D || type==kTH2F)
		{
		  //	for 2D with X axis as LS
		  TH2 *obj = dynamic_cast<TH2*>(o.object);
		  bool foundfirst = false;
		  int first = 1;
		  int last = 1;
		  for (int i=first; i<=obj->GetNbinsX(); i++)
		    {
		      if (!foundfirst && 
			  obj->GetBinContent(i, 1)!=0)
			{
			  first = i;
			  foundfirst = true;
			}
		      if (obj->GetBinContent(i, 1)!=0)
			last = i+1;
		    }
		  if (last-first>=1)
		    obj->GetXaxis()->SetRange(first, last);
		}
	      else if ( type==kTH1F || type==kTH1D)
		{
		  //	for 1D with X axis as LS
		  TH1 *obj = dynamic_cast<TH1*>(o.object);
		  bool foundfirst = false;
		  int first = 1;
		  int last = 1;
		  for (int i=first; i<=obj->GetNbinsX(); i++)
		    {
		      if (!foundfirst && 
			  obj->GetBinContent(i)!=0)
			{
			  first = i;
			  foundfirst = true;
			}
		      if (obj->GetBinContent(i)!=0)
			last = i+1;
		    }
		  if (last-first>=1)
		    obj->GetXaxis()->SetRange(first, last);
		  obj->SetMarkerStyle(20);
		}
	      break;
	    case kAxisFlag:
	      break;
	    default:
	      break;
	    }
	}
    }






    /*
     *  Following functions are written by: Shubham Pandey (shubham.pandey@cern.ch)
     *
     */


    //Funtion to sort weblogs according to date
    logs sorts(std::vector<logs> ll) {
      //Sort according to year -> month -> date
      for(int i=0; i<(int)ll.size()-1; i++){
	for(int j=i+1; j<(int)ll.size(); j++){
	  if( ll[i].y < ll[j].y ) {
	    swap(ll.at(i),ll.at(j));
	  }
	  else if ( ll[i].y == ll[j].y ) {
	    if( ll[i].m < ll[j].m )
	      swap(ll.at(i),ll.at(j));
	    else if ( ll[i].m == ll[j].m ) {
	      if( ll[i].d < ll[j].d )
		swap(ll.at(i),ll.at(j));
	      else
		continue;
	    }
	    else
	      continue;
	  }
	  else
	    continue;
	             
	}
      }

      return ll.at(0); //return latest weblog
    }



    //Latest weblog contains name of loaded sample
    //Function to get the name of sample loaded
    int get_sample(char *f)
    {
      FILE * fp;
      char * line = NULL;
      size_t len = 0;
      ssize_t read;
  
      std::string sample;
      int range_code = -1;  //rangeMediumData = 0, rangeLow = 1, rangeMedium = 2, rangeHigh = 3
  
      fp = std::fopen(f, "r");
      if (fp == NULL)
	exit(EXIT_FAILURE);
  
      while ((read = getline(&line, &len, fp)) != -1) {
	std::string tmp = (std::string)line;
	if (tmp.find("/dqm/relval/plotfairy/archive/") != std::string::npos) {
	  if (tmp.find("/RelValTTbar_13/") != std::string::npos)  range_code = 2;   //sample = "TTbar"
	  else if (tmp.find("/RelValQCD_Pt_80_120_13/") != std::string::npos)   range_code = 2; //sample = "LowPtQCD"
	  else if (tmp.find("/RelValQCD_Pt_3000_3500_13/") != std::string::npos) range_code = 3; //sample = "HighPtQCD"
	  else if (tmp.find("/RelValMinBias_13/") != std::string::npos)   range_code = 1; //sample = "MinBias"
	  else if (tmp.find("/JetHT/") != std::string::npos) range_code = 0; //sample = "JetHT"
	  else if (tmp.find("/ZeroBias/") != std::string::npos) range_code = 0; //sample = "ZeroBias"
	  else  range_code = 0; //sample = "Other than standard samples" //Default case, range = rangeMediumData
	}
      }
  
      fclose(fp);
      if (line)
	free(line);
  
      return range_code;

    }

    //This is the driver function
    // This function calls sorts(), get_sample() function
    hist_range driver(std::string hist_name) {
      DIR *dir;
      struct dirent *ent;
      bool flag = false;
      std::vector<std::string> f_name;
      std::vector<logs> weblogs;
      char year[5], month[3], day[3];
      char directory[] = "/tmp/spandey/testGui/logs/dqmgui/relval/";   //This path of "weblog Directory" has to be changed when implemented on central server

      /* Get all the files and directories within directory */
      if ((dir = opendir (directory)) != NULL) {
	while ((ent = readdir (dir)) != NULL) {
	  std::string f = (std::string)ent->d_name;
	  if (f.find("weblog") != std::string::npos) {
	    for (int i = 7, j = 0; i <= 14; i++, j++) {   //loop to separate out year, date  and month from the weblog name
	      if(i <= 10)
		year[j] = f[i];
	      if((i == 11) || (i == 12))
		month[j-4] = f[i];
	      if( i > 12)
		day[j-6] = f[i];
	    }
	    flag = true;
	    logs tmp;
	    tmp.name = f;
	    tmp.y = atoi(year);
	    tmp.m = atoi(month);
	    tmp.d = atoi(day);
	    weblogs.push_back(tmp);  //contains full name of weblog along with year, date and month separately
	  }
	}

	closedir (dir);
      }
      else {
	/* could not open directory */
	perror ("");
	//return EXIT_FAILURE;
	exit(EXIT_FAILURE);

      }
      if(!flag)
	printf("\n Directory Not found");

      logs recent = this->sorts(weblogs);
      char file_name[100];
      int i1;
      for(i1 = 0; i1 < (int)recent.name.size(); i1++) {
	file_name[i1] = recent.name[i1];
      }
      file_name[i1] = '\0';

      char strtmp[100] = "";
      strcat(strtmp,directory);
      char* full_path = strcat(strtmp,file_name);
      int ii = this->get_sample(full_path);
      std::vector< std::map<std::string, hist_range> > vec ;

      //initializes all maps from HcalrelvalMaps.h file
      vec.push_back(map0());   
      vec.push_back(map1());
      vec.push_back(map2());
      vec.push_back(map3());
      std::map<std::string, hist_range>::iterator search = vec[ii].find(hist_name);
      hist_range foobar;
      if (search != vec[ii].end()) {
	foobar = search->second;
      }
      else {
	std::cout<<"Key:"<<hist_name<<" Not Found!!\n";
      }

      return foobar;
    }




    /*
     *  End of functions
     *
     */



    
  protected:
    bool isBitSet(int ibit, TObject* o)
    {
      return o->TestBit(BIT(ibit+bitshift));
    }
    
    
    
    // Some members....
  protected:
    RenderType			_type;
    int					_verbosity;
    
    /*
     *	Declare all the colors/contours
     */
    //	summary
    unsigned int _n_summary;
    Int_t _colors_summary[10];
    Double_t _contours_summary[10];
  };
}
