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

def path_to_default_preferences():
    #the default preferences file is: C:\Users\<user-name>AppData\Roaming\\nvda\\addons\\mathCAT\\globalPlugins\\MathCAT\\Rules\\prefs.yaml
    return os.path.expanduser('~')+"\\AppData\\Roaming\\nvda\\addons\\mathCAT\\globalPlugins\\MathCAT\\Rules\\prefs.yaml"

def path_to_user_preferences_folder():
    #the user preferences file is stored at: C:\Users\<user-name>AppData\Roaming\MathCAT\prefs.yaml
    return os.path.expanduser('~')+"\\AppData\\Roaming\\MathCAT"

def path_to_user_preferences():
    #the user preferences file is stored at: C:\Users\<user-name>AppData\Roaming\MathCAT\prefs.yaml
    return path_to_user_preferences_folder() + "\\prefs.yaml"

def load_default_preferences():
    global user_preferences
    #load default preferences into the user preferences data structure (overwrites existing)
    if os.path.exists(path_to_default_preferences()):
        with open(path_to_default_preferences(), encoding='utf-8') as f:
            user_preferences = yaml.load(f, Loader=yaml.FullLoader)
    else:
        #default preferences file is NOT found
        wx.MessageBox(_(u"MathCat preferences file not found. The program will now exit."), "Error", wx.OK | wx.ICON_ERROR)
        os.sys.exit(-1)

def load_user_preferences():
    global user_preferences
    #merge user file values into the user preferences data structure
    if os.path.exists(path_to_user_preferences()):
        with open(path_to_user_preferences()) as f:
            # merge with the default preferences, overwriting with the user's values
            user_preferences.update(yaml.load(f, Loader=yaml.FullLoader))

def write_user_preferences():
    if not os.path.exists(path_to_user_preferences_folder()):
        #create a folder for the user preferences
        os.mkdir(path_to_user_preferences_folder())
    with open(path_to_user_preferences(), 'w') as f:
        #write values to the user preferences file, NOT the default
        yaml.dump(user_preferences, f)

class UserInterface(MathCATgui.MathCATPreferencesDialog):

    def GetLanguages(self):
        #clear the language choices
        self.m_choiceLanguage.Clear()
        #populate the language choices
        for f in os.listdir(path_to_languages_folder()):
            if os.path.isdir(path_to_languages_folder()+"\\"+f):
                self.m_choiceLanguage.Append(f)

    def GetSpeechStyles(self, this_SpeechStyle):
        #clear the SpeechStyle choices
        self.m_choiceSpeechStyle.Clear()
        #get the currently selected language
        this_language = self.m_choiceLanguage.GetStringSelection()
        this_path = os.path.expanduser('~')+"\\AppData\\Roaming\\nvda\\addons\\mathCAT\\globalPlugins\\MathCAT\\Rules\\Languages\\"+this_language+"\\*_Rules.yaml"
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
            UserInterface.GetSpeechStyles(self, user_preferences["Speech"]["SpeechStyle"])
            self.m_choiceSpeechAmount.SetSelection(Speech_Verbosity.index(user_preferences["Speech"]["Verbosity"]))
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

    def __init__(self,parent):
        #initialize parent class
        MathCATgui.MathCATPreferencesDialog.__init__(self,parent)

        # load in the system values followed by the user prefs (if any)
        load_default_preferences()
        load_user_preferences()

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

    def OnClickOK(self,event):
        UserInterface.get_ui_values(self)
        write_user_preferences()
        self.Destroy()
 
    def OnClickCancel(self,event):
        self.Destroy()
 
    def OnClickApply(self,event):
        UserInterface.get_ui_values(self)
        write_user_preferences()
 
    def OnClickReset(self,event):
        load_default_preferences()
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
        if keyCode == wx.WXK_RETURN:
            UserInterface.OnClickOK(self,event)
        event.Skip()
