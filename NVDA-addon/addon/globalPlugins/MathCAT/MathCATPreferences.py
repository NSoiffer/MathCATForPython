import wx
from . import MathCATgui
from . import yaml
import os
import glob
import sys
import webbrowser  
import gettext
_ = gettext.gettext

from logHandler import log                  # logging

# initialize the user preferences tuples
user_preferences = dict([("", "")])
#Speech_Language is derived from the folder structure
Speech_Impairment = ("LearningDisability", "Blindness", "LowVision")
#Speech_SpeechStyle is derived from the yaml files under the selected language
Speech_Verbosity = ("Terse", "Medium", "Verbose")
Speech_SubjectArea = ("General")
Speech_Chemistry = ("SpellOut", "AsCompound", "Off")
Navigation_NavMode = ("Enhanced", "Simple", "Character")
#Navigation_ResetNavMode is boolean
#Navigation_OverView is boolean
Navigation_NavVerbosity = ("Terse", "Medium", "Verbose")
#Navigation_AutoZoomOut is boolean

Braille_BrailleNavHighlight = ("Off", "FirstChar", "EndPoints", "All")
Braille_BrailleCode = ("Nemeth", "UEB")


class UserInterface(MathCATgui.MathCATPreferencesDialog):
    def __init__(self,parent):
        #initialize parent class
        MathCATgui.MathCATPreferencesDialog.__init__(self,parent)

        #load the logo into the dialog
        full_path_to_logo = os.path.expanduser('~')+"\\AppData\\Roaming\\nvda\\addons\\mathCAT\\globalPlugins\\MathCAT\\logo.png"
        if os.path.exists(full_path_to_logo):
            self.m_bitmapLogo.SetBitmap(wx.Bitmap(full_path_to_logo))

        # load in the system values followed by the user prefs (if any)
        UserInterface.load_default_preferences()
        UserInterface.load_user_preferences()
        UserInterface.validate_user_preferences()

        if "MathCATPreferencesLastCategory" in user_preferences:
            #set the categories selection to what we used on last run
            self.m_listBoxPreferencesTopic.SetSelection(user_preferences["MathCATPreferencesLastCategory"])
            #show the appropriate dialogue page
            self.m_simplebookPanelsCategories.SetSelection(self.m_listBoxPreferencesTopic.GetSelection())
        else:
            #set the categories selection to the first item
            self.m_listBoxPreferencesTopic.SetSelection(0)
            user_preferences["MathCATPreferencesLastCategory"]="0"
        #populate the languages
        UserInterface.GetLanguages(self)
        #set the ui items to match the preferences
        UserInterface.set_ui_values(self)

    def path_to_languages_folder():
        #the user preferences file is stored at: MathCAT\Rules\Languages
        return os.path.expanduser('~')+"\\AppData\\Roaming\\nvda\\addons\\mathCAT\\globalPlugins\\MathCAT\\Rules\\Languages"

    def GetLanguages(self):
        #clear the language choices
        self.m_choiceLanguage.Clear()
        #populate the language choices
        for f in os.listdir(UserInterface.path_to_languages_folder()):
            if os.path.isdir(UserInterface.path_to_languages_folder()+"\\"+f):
                self.m_choiceLanguage.Append(f)

    def GetSpeechStyles(self, this_SpeechStyle):
        #clear the SpeechStyle choices
        self.m_choiceSpeechStyle.Clear()
        #get the currently selected language
        this_language = self.m_choiceLanguage.GetStringSelection()
        this_path = os.path.expanduser('~')+"\\AppData\\Roaming\\nvda\\addons\\MathCAT\\globalPlugins\\MathCAT\\Rules\\Languages\\"+this_language+"\\*_Rules.yaml"
        #populate the m_choiceSpeechStyle choices
        for f in glob.glob(this_path):
            fname = os.path.basename(f)
            self.m_choiceSpeechStyle.Append((fname[:fname.find("_Rules.yaml")]))
        try:
            #set the SpeechStyle to the same as previous
            self.m_choiceSpeechStyle.SetStringSelection(this_SpeechStyle)
        except:
            #that didn't work, choose the first in the list
            self.m_choiceSpeechStyle.SetSelection(0)

    def set_ui_values(self):
        #set the UI elements to the ones read from the preference file(s)
        try:
            self.m_choiceImpairment.SetSelection(Speech_Impairment.index(user_preferences["Speech"]["Impairment"]))
            try:
                self.m_choiceLanguage.SetStringSelection(user_preferences["Speech"]["Language"])
            except:
                #the language in the settings file is not in the folder structure, something went wrong, set to the first in the list
                self.m_choiceLanguage.SetSelection(0)
            #now get the available SpeechStyles from the folder structure and set to the preference setting is possible
            self.GetSpeechStyles(user_preferences["Speech"]["SpeechStyle"])
            self.m_choiceSpeechAmount.SetSelection(Speech_Verbosity.index(user_preferences["Speech"]["Verbosity"]))
            self.m_sliderRelativeSpeed.SetValue(user_preferences["Speech"]["MathRate"])
            self.m_choiceSpeechForChemical.SetSelection(Speech_Chemistry.index(user_preferences["Speech"]["Chemistry"]))
            self.m_choiceNavigationMode.SetSelection(Navigation_NavMode.index(user_preferences["Navigation"]["NavMode"]))
            self.m_checkBoxResetNavigationMode.SetValue(user_preferences["Navigation"]["ResetNavMode"])
            self.m_choiceSpeechAmountNavigation.SetSelection(Navigation_NavVerbosity.index(user_preferences["Navigation"]["NavVerbosity"]))
            if user_preferences["Navigation"]["Overview"]:
                self.m_choiceNavigationSpeech.SetSelection(0)
            else:
                self.m_choiceNavigationSpeech.SetSelection(1)
            self.m_checkBoxResetNavigationSpeech.SetValue(user_preferences["Navigation"]["ResetOverview"])
            self.m_checkBoxAutomaticZoom.SetValue(user_preferences["Navigation"]["AutoZoomOut"])
            self.m_choiceBrailleHighlights.SetSelection(Braille_BrailleNavHighlight.index(user_preferences["Braille"]["BrailleNavHighlight"]))
            self.m_choiceBrailleMathCode.SetSelection(Braille_BrailleCode.index(user_preferences["Braille"]["BrailleCode"]))
        except KeyError as err:
            print('Key not found')
        		
    def get_ui_values(self):
        global user_preferences
        # read the values from the UI and update the user preferences dictionary
        user_preferences["Speech"]["Impairment"] = Speech_Impairment[self.m_choiceImpairment.GetSelection()]
        user_preferences["Speech"]["Language"] = self.m_choiceLanguage.GetStringSelection()
        user_preferences["Speech"]["SpeechStyle"] = self.m_choiceSpeechStyle.GetStringSelection()
        user_preferences["Speech"]["Verbosity"] = Speech_Verbosity[self.m_choiceSpeechAmount.GetSelection()]
        user_preferences["Speech"]["MathRate"] = self.m_sliderRelativeSpeed.GetValue()
        user_preferences["Speech"]["Chemistry"] = Speech_Chemistry[self.m_choiceSpeechForChemical.GetSelection()]
        user_preferences["Navigation"]["NavMode"] = Navigation_NavMode[self.m_choiceNavigationMode.GetSelection()]
        user_preferences["Navigation"]["ResetNavMode"] = self.m_checkBoxResetNavigationMode.GetValue()
        user_preferences["Navigation"]["NavVerbosity"] = Navigation_NavVerbosity[self.m_choiceSpeechAmountNavigation.GetSelection()]
        if self.m_choiceNavigationSpeech.GetSelection() == 0:
            user_preferences["Navigation"]["Overview"] = True
        else:
            user_preferences["Navigation"]["Overview"] = False
        user_preferences["Navigation"]["ResetOverview"] = self.m_checkBoxResetNavigationSpeech.GetValue()
        user_preferences["Navigation"]["AutoZoomOut"] = self.m_checkBoxAutomaticZoom.GetValue()
        user_preferences["Braille"]["BrailleNavHighlight"] = Braille_BrailleNavHighlight[self.m_choiceBrailleHighlights.GetSelection()]
        user_preferences["Braille"]["BrailleCode"] = Braille_BrailleCode[self.m_choiceBrailleMathCode.GetSelection()]
        user_preferences["MathCATPreferencesLastCategory"] = self.m_listBoxPreferencesTopic.GetSelection()

    def path_to_default_preferences():
        #the default preferences file is: C:\Users\<user-name>AppData\Roaming\\nvda\\addons\\MathCAT\\globalPlugins\\MathCAT\\Rules\\prefs.yaml
        return os.path.expanduser('~')+"\\AppData\\Roaming\\nvda\\addons\\MathCAT\\globalPlugins\\MathCAT\\Rules\\prefs.yaml"

    def path_to_user_preferences_folder():
        #the user preferences file is stored at: C:\Users\<user-name>AppData\Roaming\MathCAT\prefs.yaml
        return os.path.expanduser('~')+"\\AppData\\Roaming\\MathCAT"

    def path_to_user_preferences():
        #the user preferences file is stored at: C:\Users\<user-name>AppData\Roaming\MathCAT\prefs.yaml
        return UserInterface.path_to_user_preferences_folder() + "\\prefs.yaml"

    def load_default_preferences():
        global user_preferences
        #load default preferences into the user preferences data structure (overwrites existing)
        if os.path.exists(UserInterface.path_to_default_preferences()):
            with open(UserInterface.path_to_default_preferences(), encoding='utf-8') as f:
                user_preferences = yaml.load(f, Loader=yaml.FullLoader)
        else:
            #default preferences file is NOT found
            wx.MessageBox(_(u"MathCat preferences file not found. The program will now exit."), "Error", wx.OK | wx.ICON_ERROR)
            os.sys.exit(-1)

    def load_user_preferences():
        global user_preferences
        #merge user file values into the user preferences data structure
        if os.path.exists(UserInterface.path_to_user_preferences()):
            with open(UserInterface.path_to_user_preferences(), encoding='utf-8') as f:
                # merge with the default preferences, overwriting with the user's values
                user_preferences.update(yaml.load(f, Loader=yaml.FullLoader))

    def validate_user_preferences():
        global user_preferences
        #check each user preference value to ensure it is present and valid, set default value if not

        #  Speech:
        #Impairment: Blindness       # LearningDisability, LowVision, Blindness
        valid_test_passed = False
        try: 
            if user_preferences["Speech"]["Impairment"] in ["LearningDisability", "LowVision", "Blindness"]:
                valid_test_passed = True
        except:
            pass
        if not valid_test_passed:
            user_preferences["Speech"]["Impairment"] = "Blindness"

        #    Language: en                # any known language code and sub-code -- could be en-uk, etc
        valid_test_passed = False
        try: 
            if user_preferences["Speech"]["Language"] != "":
                valid_test_passed = True
        except:
            pass
        if not valid_test_passed:
            user_preferences["Speech"]["Language"] = "en"

        #    Verbosity: Medium           # Terse, Medium, Verbose
        valid_test_passed = False
        try: 
            if user_preferences["Speech"]["Verbosity"] in ["Terse", "Medium", "Verbose"]:
                valid_test_passed = True
        except:
            pass
        if not valid_test_passed:
            user_preferences["Speech"]["Verbosity"] = "Medium"

        #    MathRate: 100               # Change from text speech rate (%)
        valid_test_passed = False
        try: 
            if (user_preferences["Speech"]["MathRate"] > 0):
                valid_test_passed = True
        except:
            pass
        if not valid_test_passed:
            user_preferences["Speech"]["MathRate"] = 100

        #    SpeechStyle: ClearSpeak     # Any known speech style (falls back to ClearSpeak)
        valid_test_passed = False
        try: 
            if user_preferences["Speech"]["SpeechStyle"] != "":
                valid_test_passed = True
        except:
            pass
        if not valid_test_passed:
            user_preferences["Speech"]["SpeechStyle"] = "ClearSpeak"

        #    SubjectArea: General        # FIX: still working on this
        valid_test_passed = False
        try: 
            if user_preferences["Speech"]["SubjectArea"] != "":
                valid_test_passed = True
        except:
            pass
        if not valid_test_passed:
            user_preferences["Speech"]["SubjectArea"] = "General"

        #    Chemistry: SpellOut         # SpellOut (H 2 0), AsCompound (Water), Off (H sub 2 O)
        valid_test_passed = False
        try: 
            if user_preferences["Speech"]["Chemistry"] in ["SpellOut", "AsCompound", "Off"]:
                valid_test_passed = True
        except:
            pass
        if not valid_test_passed:
            user_preferences["Speech"]["Chemistry"] = "SpellOut"

        #Navigation:
        #  NavMode: Enhanced         # Enhanced, Simple, Character
        valid_test_passed = False
        try: 
            if user_preferences["Navigation"]["NavMode"] in ["Enhanced", "Simple", "Character"]:
                valid_test_passed = True
        except:
            pass
        if not valid_test_passed:
            user_preferences["Navigation"]["NavMode"] = "Enhanced"

        #  ResetNavMode: false       # remember previous value and use it
        valid_test_passed = False
        try: 
            if (user_preferences["Navigation"]["ResetNavMode"]) or (not user_preferences["Navigation"]["ResetNavMode"]) :
                valid_test_passed = True
        except:
            pass
        if not valid_test_passed:
            user_preferences["Navigation"]["ResetNavMode"] = False

        #  Overview: false             # speak the expression or give a description/overview
        valid_test_passed = False
        try: 
            if (user_preferences["Navigation"]["Overview"]) or True :
                valid_test_passed = True
        except:
            pass
        if not valid_test_passed:
            user_preferences["Navigation"]["Overview"] = False

        #  ResetOverview: true        # remember previous value and use it
        valid_test_passed = False
        try: 
            if (user_preferences["Navigation"]["ResetOverview"]) or True :
                valid_test_passed = True
        except:
            pass
        if not valid_test_passed:
            user_preferences["Navigation"]["ResetOverview"] = True

        #  NavVerbosity: Medium        # Terse, Medium, Verbose (words to say for nav command)
        valid_test_passed = False
        try: 
            if user_preferences["Navigation"]["NavVerbosity"] in ["Terse", "Medium", "Verbose"]:
                valid_test_passed = True
        except:
            pass
        if not valid_test_passed:
            user_preferences["Navigation"]["NavVerbosity"] = "Medium"

        #  AutoZoomOut: true           # Auto zoom out of 2D exprs (use shift-arrow to force zoom out if unchecked)
        valid_test_passed = False
        try: 
            if (user_preferences["Navigation"]["AutoZoomOut"]) or True :
                valid_test_passed = True
        except:
            pass
        if not valid_test_passed:
            user_preferences["Navigation"]["AutoZoomOut"] = True

        #Braille:
        #  BrailleNavHighlight: EndPoints   # Highlight with dots 7 & 8 the current nav node -- values are Off, FirstChar, EndPoints, All
        valid_test_passed = False
        try: 
            if user_preferences["Braille"]["BrailleNavHighlight"] in ["Off", "FirstChar", "EndPoints", "All"]:
                valid_test_passed = True
        except:
            pass
        if not valid_test_passed:
            user_preferences["Braille"]["BrailleNavHighlight"] = "EndPoints"

        #  BrailleCode: "Nemeth"                # Any supported braille code (currently Nemeth, UEB)
        valid_test_passed = False
        try: 
            if user_preferences["Braille"]["BrailleCode"] in ["Nemeth", "UEB"]:
                valid_test_passed = True
        except:
            pass
        if not valid_test_passed:
            user_preferences["Braille"]["BrailleCode"] = "Nemeth"

    def write_user_preferences():
        if not os.path.exists(UserInterface.path_to_user_preferences_folder()):
            #create a folder for the user preferences
            os.mkdir(UserInterface.path_to_user_preferences_folder())
        with open(UserInterface.path_to_user_preferences(), 'w', encoding="utf-8") as f:
            #write values to the user preferences file, NOT the default
            yaml.dump(user_preferences, stream=f, allow_unicode=True)

    def OnRelativeSpeedChanged( self, event ):
        from .MathCAT import ConvertSSMLTextForNVDA
        from  speech import speak
        rate = self.m_sliderRelativeSpeed.GetValue()
        text = _(u"<prosody rate='XXX%'>the square root of x squared plus y squared</prosody>").replace("XXX", str(rate), 1)
        speak( ConvertSSMLTextForNVDA(text) )

    def OnClickOK(self,event):
        UserInterface.get_ui_values(self)
        UserInterface.write_user_preferences()
        self.Destroy()
 
    def OnClickCancel(self,event):
        self.Destroy()
 
    def OnClickApply(self,event):
        UserInterface.get_ui_values(self)
        UserInterface.write_user_preferences()
 
    def OnClickReset(self,event):
        UserInterface.load_default_preferences()
        UserInterface.validate_user_preferences()
        UserInterface.set_ui_values(self)
 
    def OnClickHelp(self,event):
        webbrowser.open('https://nsoiffer.github.io/MathCAT/users.html')

    def OnListBoxCategories(self,event):
        #the category changed, now show the appropriate dialogue page
        self.m_simplebookPanelsCategories.SetSelection(self.m_listBoxPreferencesTopic.GetSelection())

    def OnLanguage(self,event):
        #the language changed, get the SpeechStyles for the new language
        UserInterface.GetSpeechStyles(self, self.m_choiceSpeechStyle.GetSelection())

    def MathCATPreferencesDialogOnCharHook(self,event):
        #designed choice is that Enter is the same as clicking OK, and Escape is the same as clicking Cancel
        keyCode = event.GetKeyCode()
        if keyCode == wx.WXK_ESCAPE:
            UserInterface.OnClickCancel(self,event)
            return
        if keyCode == wx.WXK_RETURN:
            UserInterface.OnClickOK(self,event)
        if keyCode == wx.WXK_TAB and (event.GetModifiers()  == wx.MOD_CONTROL):
            #cycle the category forward
            new_category = self.m_listBoxPreferencesTopic.GetSelection() + 1
            if new_category == 3:
                new_category = 0
            self.m_listBoxPreferencesTopic.SetSelection(new_category)
            #update the ui to show the new page
            UserInterface.OnListBoxCategories(self,event)
            #set the focus into the category list box
            self.m_listBoxPreferencesTopic.SetFocus()
            #jump out so the tab key is not processed
            return
        if keyCode == wx.WXK_TAB and (event.GetModifiers()  == wx.MOD_CONTROL|wx.MOD_SHIFT):
            #cycle the category back
            new_category = self.m_listBoxPreferencesTopic.GetSelection() - 1
            if new_category == -1:
                new_category = 2
            self.m_listBoxPreferencesTopic.SetSelection(new_category)
            #update the ui to show the new page
            UserInterface.OnListBoxCategories(self,event)
            #update the ui to show the new page
            self.m_listBoxPreferencesTopic.SetFocus()
            #jump out so the tab key is not processed
            return
        if (event.GetModifiers()  == wx.MOD_NONE) and (MathCATgui.MathCATPreferencesDialog.FindFocus() == self.m_listBoxPreferencesTopic):
            #user tabbed from into the paged content, set the focus on the first control
            if self.m_listBoxPreferencesTopic.GetSelection() == 0:
                self.m_choiceImpairment.SetFocus()
            elif self.m_listBoxPreferencesTopic.GetSelection() == 1:
                self.m_choiceNavigationMode.SetFocus()
            elif self.m_listBoxPreferencesTopic.GetSelection() == 2:
                self.m_choiceBrailleMathCode.SetFocus()
            return
        if (event.GetModifiers()  == wx.MOD_SHIFT) and (MathCATgui.MathCATPreferencesDialog.FindFocus() == self.m_buttonOK):
            #user shift+tabbed from into the paged content, set the focus on the last control
            if self.m_listBoxPreferencesTopic.GetSelection() == 0:
                self.m_choiceSpeechForChemical.SetFocus()
            elif self.m_listBoxPreferencesTopic.GetSelection() == 1:
                self.m_choiceSpeechAmountNavigation.SetFocus()
            elif self.m_listBoxPreferencesTopic.GetSelection() == 2:
                self.m_choiceBrailleHighlights.SetFocus()
            return
        #continue handling keyboard event
        event.Skip()
          
