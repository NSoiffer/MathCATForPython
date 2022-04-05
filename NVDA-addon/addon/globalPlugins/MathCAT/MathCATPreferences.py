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
user_preferences = {}
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
            #set the rest of the UI elements
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

    def load_user_preferences():
        global user_preferences
        #merge user file values into the user preferences data structure
        if os.path.exists(UserInterface.path_to_user_preferences()):
            with open(UserInterface.path_to_user_preferences(), encoding='utf-8') as f:
                # merge with the default preferences, overwriting with the user's values
                user_preferences.update(yaml.load(f, Loader=yaml.FullLoader))

    def validate(key1, key2, valid_values, default_value):
        global user_preferences
        try:
            if valid_values == None:
                #any value is valid
                if user_preferences[key1][key2] != "":
                    return
            if (type(valid_values[0]) == int) and (type(valid_values[1]) == int):
                #any value between lower and upper bounds is valid
                if (user_preferences[key1][key2] >= valid_values[0]) and (user_preferences[key1][key2] <= valid_values[1]):
                    return
            else:
                #any value in the list is valid
                if user_preferences[key1][key2] in valid_values:
                    return
        except:
            #the preferences entry does not exist
            pass
        if not key1 in user_preferences:
            user_preferences[key1] = {key2: default_value}
        else:
            user_preferences[key1][key2] = default_value

    def validate_user_preferences():
        #check each user preference value to ensure it is present and valid, set default value if not
        #  Speech:
        #Impairment: Blindness       # LearningDisability, LowVision, Blindness
        UserInterface.validate("Speech", "Impairment", ["LearningDisability", "LowVision", "Blindness"], "Blindness")
    #   Language: en                # any known language code and sub-code -- could be en-uk, etc
        UserInterface.validate("Speech", "Language", None, "en")
        #    Verbosity: Medium           # Terse, Medium, Verbose
        UserInterface.validate("Speech", "Verbosity", ["Terse", "Medium", "Verbose"], "Medium")
        #    MathRate: 100               # Change from text speech rate (%)
        UserInterface.validate("Speech", "MathRate", [0,200], 100)
        #    SpeechStyle: ClearSpeak     # Any known speech style (falls back to ClearSpeak)
        UserInterface.validate("Speech", "SpeechStyle", None, "ClearSpeak")
        #    SubjectArea: General        # FIX: still working on this
        UserInterface.validate("Speech", "SubjectArea", None, "General")
        #    Chemistry: SpellOut         # SpellOut (H 2 0), AsCompound (Water), Off (H sub 2 O)
        UserInterface.validate("Speech", "Chemistry", ["SpellOut", "AsCompound", "Off"], "SpellOut")
        #Navigation:
        #  NavMode: Enhanced         # Enhanced, Simple, Character
        UserInterface.validate("Navigation", "NavMode", ["Enhanced", "Simple", "Character"], "Enhanced")
        #  ResetNavMode: false       # remember previous value and use it
        UserInterface.validate("Navigation", "ResetNavMode", [False, True], False)
            #  Overview: false             # speak the expression or give a description/overview
        UserInterface.validate("Navigation", "Overview", [False, True] ,False)
        #  ResetOverview: true        # remember previous value and use it
        UserInterface.validate("Navigation", "ResetOverview", [False, True], True)
        #  NavVerbosity: Medium        # Terse, Medium, Full (words to say for nav command)
        UserInterface.validate("Navigation", "NavVerbosity", ["Terse", "Medium", "Full"], "Medium")
        #  AutoZoomOut: true           # Auto zoom out of 2D exprs (use shift-arrow to force zoom out if unchecked)
        UserInterface.validate("Navigation", "AutoZoomOut", [False, True], True)
        #Braille:
        #  BrailleNavHighlight: EndPoints   # Highlight with dots 7 & 8 the current nav node -- values are Off, FirstChar, EndPoints, All
        UserInterface.validate("Braille", "BrailleNavHighlight", ["Off", "FirstChar", "EndPoints", "All"], "EndPoints")
        #  BrailleCode: "Nemeth"                # Any supported braille code (currently Nemeth, UEB)
        UserInterface.validate("Braille", "BrailleCode", ["Nemeth", "UEB"], "Nemeth")

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
        if keyCode == wx.WXK_TAB:
            if event.GetModifiers()  == wx.MOD_CONTROL:
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
            if event.GetModifiers()  == wx.MOD_CONTROL|wx.MOD_SHIFT:
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
                if self.m_listBoxPreferencesTopic.GetSelection() == 0:
                    self.m_choiceImpairment.SetFocus()
                elif self.m_listBoxPreferencesTopic.GetSelection() == 1:
                    self.m_choiceNavigationMode.SetFocus()
                elif self.m_listBoxPreferencesTopic.GetSelection() == 2:
                    self.m_choiceBrailleMathCode.SetFocus()
                return
            if (event.GetModifiers()  == wx.MOD_SHIFT) and (MathCATgui.MathCATPreferencesDialog.FindFocus() == self.m_buttonOK):
                if self.m_listBoxPreferencesTopic.GetSelection() == 0:
                    self.m_choiceSpeechForChemical.SetFocus()
                elif self.m_listBoxPreferencesTopic.GetSelection() == 1:
                    self.m_choiceSpeechAmountNavigation.SetFocus()
                elif self.m_listBoxPreferencesTopic.GetSelection() == 2:
                    self.m_choiceBrailleHighlights.SetFocus()
                return
        #continue handling keyboard event
        event.Skip()
          
