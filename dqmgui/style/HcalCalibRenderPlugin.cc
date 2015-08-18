/*
 *	file:			HcalCalibRenderPlugin.cc
 *	author:			Viktor Khristenko
 */

//	DQM includes
#include "DQM/DQMRenderPlugin.h"

//	User includes
#include "HcalObjectCustomizer.h"

//	ROOT includes
#include "TCanvas.h"
#include "TText.h"
#include "TColor.h"

//	std includes
#include <cstring>

// Render Plugin Class for Hcal Calib
class HcalCalibRenderPlugin : public DQMRenderPlugin
{
	public:
		virtual void initialise(int, char**)
		{
			//	Initialize the Customizer
			_customizer.initialize_Type(hcaldqm::kHcalCalib);
			_customizer.initialize_ColorSchemes();
			_customizer.initialize_Filters();
		}

		//	if returns true, preDraw and then postDraw will be executed.
		//	Check if we should draw this object
		virtual bool applies(VisDQMObject const& o, 
			VisDQMImgInfo const&)
		{
			//	return true only if that is Hcal/ or HcalCalib/
			return o.name.find("HcalCalib/")!=std::string::npos;
		}

		//	if applies gives true - execute just before calling 
		//	TObject::Draw()
		virtual void preDraw(TCanvas *c, VisDQMObject const& object,
			VisDQMImgInfo const& iinfo, VisDQMRenderInfo &rinfo)
		{
			//	Check that the Object exists and inherits from TH1
			if (!object.object || !object.object->InheritsFrom(TH1::Class()))
				                    return;

			//	Apply Standard Customizations
			_customizer.preDraw_Standard(c);

			//	Identify the Class of the Object and customize accordingly
			if (object.object->IsA()==TH1D::Class())
			{
				_customizer.customize_1D(hcaldqm::kTH1D, c,
					object, iinfo, rinfo);
			}
			else if (object.object->IsA()==TH1F::Class())
			{
				_customizer.customize_1D(hcaldqm::kTH1F, c,
					object, iinfo, rinfo);
			}
			else if (object.object->IsA()==TH2D::Class())
			{
				_customizer.customize_2D(hcaldqm::kTH2D, c,
					object, iinfo, rinfo);
			}
			else if (object.object->IsA()==TH2F::Class())
			{
				_customizer.customize_2D(hcaldqm::kTH2D, c,
					object, iinfo, rinfo);
			}
			else if (object.object->IsA()==TProfile::Class())
			{
				_customizer.customize_1D(hcaldqm::kTProfile, c,
					object, iinfo, rinfo);
			}
			else if (object.object->IsA()==TProfile2D::Class())
			{
				_customizer.customize_2D(hcaldqm::kTProfile2D, c,
					object, iinfo, rinfo);
			}
			else if (object.object->IsA()==TH3D::Class())
				return;
			else 
				return;

			return;
		}
		//	is called right after TObject::Draw()
		virtual void postDraw(TCanvas * c, VisDQMObject const& object,
			VisDQMImgInfo const& info)
		{
			_customizer.postDraw_Standard(c, object, info);
		}
	protected:
		//	A wrapper around the Plugins...
		hcaldqm::HcalObjectCustomizer		_customizer;
};

static HcalCalibRenderPlugin instance;
