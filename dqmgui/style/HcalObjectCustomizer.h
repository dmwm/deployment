/*
 *	file:			HcalObjectCustomizer.h
 *	author:			Viktor Khristenko
 *	Revision
 *	Description:	A wrapper around any Render Plugin.
 *		Created specifically for HcalRenderPlugin and 
 *		HcalCalibRenderPlugin. Provides object customization based on the 
 *		following hierarchical selections. 
 *		1) TObject::Class() -> TH1, TH2, TProfile, etc....
 *		=>	2.1) Based on the Object's name. See naming conventions
 *		=>	2.2) Based on the Bits of TObject using SetBit/TestBit
 *		Naming Conventions(or Name Filters):
 *			If such a filter is part of the ME name, then customization by name
 *			will be applied. These filters are GLOBAL/UNIQUE, namely that is 
 *			by the design...
 *			1) Summary - All MEs having "Summary" in their name 
 *				are used as Summary Plots and customized accordingly
 *			2) Map - All MEs like that are typically TH2D or PROF2D
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
		kLogx		= 0,
		kLogy		= 1,
		kLogz		= 2,
		nObjectBits = 3
	};

	//	Class HcalObjectCustomizer
	class HcalObjectCustomizer
	{
		public: 
			HcalObjectCustomizer():_type(kHcal), _verbosity(10)
			{}
			~HcalObjectCustomizer() {}

			//	Apply standard customizations for Styles or Canvas or anything 
			//	Apply standard customizations for all of the objects
			void preDraw_Standard(TCanvas *c)
			{
				if (_verbosity>0)
					std::cout << "Calling preDraw_Standard" << std::endl;

				c->cd();

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

			}

			void postDraw_Standard(TCanvas*, VisDQMObject const&,
				VisDQMImgInfo const&)
			{}

			//	Initialize all the Color Schemes
			void initialize_ColorSchemes()
			{}

			//	Initialize Filters - Names for Searching
			void initialize_Filters()
			{}

			//	Initialize Render Type
			void initialize_Type(RenderType type)
			{
				_type = type;
			}

			//	Customize 1D
			void customize_1D(hcaldqm::ROOTType, TCanvas* c, 
				VisDQMObject const& o,
				VisDQMImgInfo const& ii, VisDQMRenderInfo &ri)
			{
				if (_verbosity>0)
					std::cout << "Calling customize_1D" << std::endl;

				//	by default

				//	further customization
				this->customize_ByName(c, o, ii, ri);
				this->customize_ByBits(c, o, ii, ri);
			}

			//	Customize 2D
			void customize_2D(hcaldqm::ROOTType, TCanvas* c, 
				VisDQMObject const& o,
				VisDQMImgInfo const& ii, VisDQMRenderInfo &ri)
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
				((TH2*)o.object)->GetZaxis()->SetRangeUser(
					((TH2*)o.object)->GetMinimum(),
					((TH2*)o.object)->GetMaximum());
				gStyle->SetPalette(1);

				//		
				this->customize_ByName(c, o, ii, ri);
				this->customize_ByBits(c, o, ii, ri);
			}

			//	Customize By Name
			void customize_ByName(TCanvas*,
				VisDQMObject const& o, VisDQMImgInfo const&,
				VisDQMRenderInfo &)
			{
				if (_verbosity>0)
					std::cout << "Calling customize_ByName" << std::cout;

				TString fullpath(o.name.c_str());
				if (!fullpath.Contains("Summary") &&
					!fullpath.Contains("Map"))
					return;

				//	
			}

			//	Customize by Bits
			void customize_ByBits(TCanvas*,
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
						case kLogx:
							gPad->SetLogx(1);
							break;
						case kLogy:
							gPad->SetLogy(1);
							break;
						case kLogz:
							gPad->SetLogz(1);
							break;
						default:
							break;
					}
				}
			}

		protected:
			bool isBitSet(int ibit, TObject* o)
			{
				return o->TestBit(BIT(ibit+bitshift));
			}

			// Some members....
		protected:
			RenderType			_type;
			int					_verbosity;
	};
}
