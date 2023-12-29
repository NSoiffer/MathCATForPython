# -*- coding: UTF-8 -*-

import math
import wx
from . import MathCATgui
from . import yaml
import os
import glob
import webbrowser
import gettext
import addonHandler
from logHandler import log  # logging
from typing import Dict, Union
from .MathCAT import ConvertSSMLTextForNVDA
from speech import speak

addonHandler.initTranslation()
_ = gettext.gettext

# two constants to scale "PauseFactor"
# these work out so that a slider that goes [0,14] has value ~100 at 7 and ~1000 at 14
PAUSE_FACTOR_SCALE = 9.5
PAUSE_FACTOR_LOG_BASE = 1.4

# initialize the user preferences tuples
user_preferences: Dict[str, Dict[str, Union[int, str, bool]]] = {}
# Speech_Language is derived from the folder structures
Speech_Impairment = ("LearningDisability", "Blindness", "LowVision")
# Speech_SpeechStyle is derived from the yaml files under the selected language
Speech_Verbosity = ("Terse", "Medium", "Verbose")
Speech_SubjectArea = "General"
Speech_Chemistry = ("SpellOut", "Off")
Navigation_NavMode = ("Enhanced", "Simple", "Character")
# Navigation_ResetNavMode is boolean
# Navigation_OverView is boolean
Navigation_NavVerbosity = ("Terse", "Medium", "Verbose")
# Navigation_AutoZoomOut is boolean
Braille_BrailleNavHighlight = ("Off", "FirstChar", "EndPoints", "All")
Braille_BrailleCode = ("Nemeth", "UEB", "CMU", "Vietnam")


class UserInterface(MathCATgui.MathCATPreferencesDialog):
    def __init__(self, parent):
        # initialize parent class
        MathCATgui.MathCATPreferencesDialog.__init__(self, parent)

        # load the logo into the dialog
        full_path_to_logo = (
            os.path.expanduser("~") + "\\AppData\\Roaming\\nvda\\addons\\mathCAT\\globalPlugins\\MathCAT\\logo.png"
        )
        if os.path.exists(full_path_to_logo):
            self.m_bitmapLogo.SetBitmap(wx.Bitmap(full_path_to_logo))

        # load in the system values followed by the user prefs (if any)
        UserInterface.load_default_preferences()
        UserInterface.load_user_preferences()
        UserInterface.validate_user_preferences()

        if "MathCATPreferencesLastCategory" in user_preferences:
            # set the categories selection to what we used on last run
            self.m_listBoxPreferencesTopic.SetSelectionuser_preferences(["MathCATPreferencesLastCategory"])
            # show the appropriate dialogue page
            self.m_simplebookPanelsCategories.SetSelection(self.m_listBoxPreferencesTopic.GetSelection())
        else:
            # set the categories selection to the first item
            self.m_listBoxPreferencesTopic.SetSelection(0)
            user_preferences["MathCATPreferencesLastCategory"] = "0"
        # populate the languages
        UserInterface.GetLanguages(self)
        # set the ui items to match the preferences
        UserInterface.set_ui_values(self)

    @staticmethod
    def path_to_languages_folder():
        # the user preferences file is stored at: MathCAT\Rules\Languages
        return os.path.expanduser("~") + "\\AppData\\Roaming\\nvda\\addons\\mathCAT\\globalPlugins\\MathCAT\\Rules\\Languages"

    @staticmethod
    def LanguagesDict():
        languages = {
            "aa": "Afar",
            "ab": "Аҧсуа",
            "af": "Afrikaans",
            "ak": "Akana",
            "an": "Aragonés",
            "ar": "العربية",
            "as": "অসমীয়া",
            "av": "Авар",
            "ay": "Aymar",
            "az": "Azərbaycanca / آذربايجان",
            "ba": "Башҡорт",
            "be": "Беларуская",
            "bg": "Български",
            "bh": "भोजपुरी",
            "bi": "Bislama",
            "bm": "Bahamanian",
            "bn": "বাংলা",
            "bo": "བོད་ཡིག / Bod skad",
            "bs": "Bosanski",
            "ca": "Català",
            "ce": "Нохчийн",
            "ch": "Chamoru",
            "co": "Corsu",
            "cr": "Nehiyaw",
            "cs": "Česky",
            "cu": "словѣньскъ / slověnĭskŭ",
            "cv": "Чăваш",
            "cy": "Cymraeg",
            "da": "Dansk",
            "de": "Deutsch",
            "dv": "ދިވެހިބަސް",
            "dz": "རྫོང་ཁ",
            "ee": "Ɛʋɛ",
            "el": "Ελληνικά",
            "en": "English",
            "en-GB": "English, United Kingdom",
            "en-US": "English, United States",
            "eo": "Esperanto",
            "es": "Español",
            "fa": "فارسی",
            "fi": "Suomi",
            "fj": "Na Vosa Vakaviti",
            "fo": "Føroyskt",
            "fr": "Français",
            "fy": "Frysk",
            "ga": "Gaeilge",
            "gd": "Gàidhlig",
            "gl": "Galego",
            "gn": "Avañe'ẽ",
            "gu": "ગુજરાતી",
            "gv": "Gaelg",
            "ha": "هَوُسَ",
            "he": "עברית",
            "hi": "हिन्दी",
            "ho": "Hiri Motu",
            "hr": "Hrvatski",
            "ht": "Krèyol ayisyen",
            "hu": "Magyar",
            "hy": "Հայերեն",
            "hz": "Otsiherero",
            "ia": "Interlingua",
            "id": "Bahasa Indonesia",
            "ig": "Igbo",
            "ii": "ꆇꉙ / 四川彝语",
            "ik": "Iñupiak",
            "io": "Ido",
            "is": "Íslenska",
            "iu": "ᐃᓄᒃᑎᑐᑦ",
            "ja": "日本語",
            "jv": "Basa Jawa",
            "ka": "ქართული",
            "kg": "KiKongo",
            "ki": "Gĩkũyũ",
            "kj": "Kuanyama",
            "kk": "Қазақша",
            "km": "ភាសាខ្មែរ",
            "kn": "ಕನ್ನಡ",
            "ko": "한국어",
            "ks": "कॉशुर / کٲش",
            "ku": "Kurdî",
            "kv": "Коми",
            "kw": "Kernewek",
            "ky": "Kırgızca / Кыргызча",
            "la": "Latina",
            "lb": "Lëtzebuergesch",
            "lg": "Luganda",
            "li": "Limburgs",
            "ln": "Lingála",
            "lo": "ລາວ / Pha xa lao",
            "lt": "Lietuvių",
            "lv": "Latviešu",
            "mg": "Malagasy",
            "mh": "Kajin Majel / Ebon",
            "mk": "Македонски",
            "ml": "മലയാളം",
            "mn": "Монгол",
            "mo": "Moldovenească",
            "ms": "Bahasa Melayu",
            "mt": "bil-Malti",
            "my": "Myanmasa",
            "na": "Dorerin Naoero",
            "ne": "नेपाली",
            "ng": "Oshiwambo",
            "nl": "Nederlands",
            "nn": "Norsk (nynorsk)",
            "nr": "isiNdebele",
            "nv": "Diné bizaad",
            "ny": "Chi-Chewa",
            "oc": "Occitan",
            "oj": "ᐊᓂᔑᓈᐯᒧᐎᓐ / Anishinaabemowin",
            "om": "Oromoo",
            "os": "Иронау",
            "pa": "ਪੰਜਾਬੀ / پنجابی",
            "pi": "Pāli / पाऴि",
            "pl": "Polski",
            "ps": "پښتو",
            "pt": "Português",
            "qu": "Runa Simi",
            "rm": "Rumantsch",
            "ro": "Română",
            "ru": "Русский",
            "rw": "Kinyarwandi",
            "sa": "संस्कृतम्",
            "sc": "Sardu",
            "sd": "सिंधी / سنڌي",
            "se": "Davvisámegiella",
            "sg": "Sängö",
            "sh": "Srpskohrvatski / Српскохрватски",
            "si": "සිංහල",
            "sk": "Slovenčina",
            "sl": "Slovenščina",
            "sm": "Gagana Samoa",
            "sn": "chiShona",
            "so": "Soomaaliga",
            "sq": "Shqip",
            "sr": "Српски",
            "ss": "SiSwati",
            "st": "Sesotho",
            "su": "Basa Sunda",
            "sv": "Svenska",
            "sw": "Kiswahili",
            "ta": "தமிழ்",
            "tg": "Тоҷикӣ",
            "th": "ไทย / Phasa Thai",
            "ti": "ትግርኛ",
            "tk": "Туркмен / تركمن",
            "tl": "Tagalog",
            "to": "Lea Faka-Tonga",
            "tr": "Türkçe",
            "ts": "Xitsonga",
            "tt": "Tatarça",
            "tw": "Twi",
            "ty": "Reo Mā`ohi",
            "ug": "Uyƣurqə / ئۇيغۇرچە",
            "uk": "Українська",
            "ur": "اردو",
            "uz": "Ўзбек",
            "ve": "Tshivenḓa",
            "vi": "Tiếng Việt",
            "vo": "Volapük",
            "wa": "Walon",
            "wo": "Wollof",
            "xh": "isiXhosa",
            "yi": "ייִדיש",
            "yo": "Yorùbá",
            "za": "Cuengh / Tôô / 壮语",
            "zh": "中文",
            "zh-HANS": "Chinese, Simplified",
            "zh-HANT": "Chinese, Traditional",
            "zh-TW": "Chinese, Traditional, Taiwan",
            "zu": "isiZulu",
        }
        return languages

    def GetLanguages(self):
        # initialise the language list
        languages_dict = UserInterface.LanguagesDict()
        # clear the language names in the dialog
        self.m_choiceLanguage.Clear()
        # Translators: menu item -- use the language of the voice chosen in the NVDA speech settings dialog
        # "Auto" == "Automatic" -- other items in menu are "English (en)", etc., so this matches that style
        self.m_choiceLanguage.Append(_("Use Voice's Language (Auto)"))
        # populate the available language names in the dialog
        # the implemented languages are in folders named using the relevant ISO 639-1
        #   code https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
        for language in os.listdir(UserInterface.path_to_languages_folder()):
            if os.path.isdir(os.path.join(UserInterface.path_to_languages_folder(), language)):
                path_to_language_folder = os.path.join(UserInterface.path_to_languages_folder(), language)
                # only add this language if there is a xxx_Rules.yaml file
                files = glob.glob(os.path.join(path_to_language_folder, "*_Rules.yaml"))
                if files:
                    # add to the listbox the text for this language together with the code
                    if languages_dict.get(language, "missing") != "missing":
                        self.m_choiceLanguage.Append(languages_dict[language] + " (" + language + ")")
                    else:
                        self.m_choiceLanguage.Append(language + " (" + language + ")")
                # the language variants are in folders named using ISO 3166-1 alpha-2
                # codes https://en.wikipedia.org/wiki/ISO_3166-2
                # check if there are language variants in the language folder
                for variant in os.listdir(path_to_language_folder):
                    if os.path.isdir(os.path.join(path_to_language_folder, variant)):
                        if variant != "SharedRules":
                            # add to the listbox the text for this language variant together with the code
                            if languages_dict.get(language + "-" + variant.upper(), "missing") != "missing":
                                self.m_choiceLanguage.Append(
                                    languages_dict[language + "-" + variant.upper()] + " (" + language + "-" + variant + ")"
                                )
                            else:
                                if languages_dict.get(language, "missing") != "missing":
                                    self.m_choiceLanguage.Append(
                                        languages_dict[language] + " (" + language + "-" + variant + ")"
                                    )
                                else:
                                    self.m_choiceLanguage.Append(
                                        language + " (" + language + "-" + variant + ")"
                                    )

    def GetLanguageCode(self):
        lang_selection = self.m_choiceLanguage.GetStringSelection()
        lang_code = lang_selection[
            lang_selection.find("(") + 1: lang_selection.find(")")
        ]
        return lang_code

    def GetSpeechStyles(self, this_SpeechStyle: str):
        from speech import getCurrentLanguage

        # clear the SpeechStyle choices
        self.m_choiceSpeechStyle.Clear()
        # get the currently selected language code
        this_language_code = UserInterface.GetLanguageCode(self)
        log.info(
            f"\nthis lang={this_language_code}, getCurrentLanguage = {getCurrentLanguage()}"
        )

        if this_language_code == "Auto":
            # list the speech styles for the current voice rather than have none listed
            this_language_code = getCurrentLanguage().lower().replace("_", "-")
            # FIX: when dialog is aware of regional dialects, remove this next line that removes the dialect part
            this_language_code = this_language_code.split("-")[0]  # grab the first part

        this_path = (
            os.path.expanduser("~")
            + "\\AppData\\Roaming\\nvda\\addons\\MathCAT\\globalPlugins\\MathCAT\\Rules\\Languages\\"
            + this_language_code
            + "\\*_Rules.yaml"
        )
        # populate the m_choiceSpeechStyle choices
        for f in glob.glob(this_path):
            fname = os.path.basename(f)
            self.m_choiceSpeechStyle.Append((fname[: fname.find("_Rules.yaml")]))
        try:
            # set the SpeechStyle to the same as previous
            self.m_choiceSpeechStyle.SetStringSelection(this_SpeechStyle)
        except Exception as e:
            print(f"An exception occurred: {e}")
            # that didn't work, choose the first in the list
            self.m_choiceSpeechStyle.SetSelection(0)

    def set_ui_values(self):
        # set the UI elements to the ones read from the preference file(s)
        try:
            self.m_choiceImpairment.SetSelection(
                Speech_Impairment.index(user_preferences["Speech"]["Impairment"])
            )
            try:
                lang_pref = user_preferences["Speech"]["Language"]
                i = 0
                while "(" + lang_pref + ")" not in self.m_choiceLanguage.GetString(i):
                    i = i + 1
                    if i == self.m_choiceLanguage.GetCount():
                        break
                if "(" + lang_pref + ")" in self.m_choiceLanguage.GetString(i):
                    self.m_choiceLanguage.SetSelection(i)
                else:
                    self.m_choiceLanguage.SetSelection(0)
            except Exception as e:
                print(f"An exception occurred: {e}")
                # the language in the settings file is not in the folder structure, something went wrong,
                # set to the first in the list
                self.m_choiceLanguage.SetSelection(0)
            try:
                # now get the available SpeechStyles from the folder structure and set to the preference setting is possible
                self.GetSpeechStyles(user_preferences["Speech"]["SpeechStyle"])
            except Exception as e:
                print(f"An exception occurred: {e}")
                self.m_choiceSpeechStyle.Append(
                    "Error when setting SpeechStyle for " + self.m_choiceLanguage.GetStringSelection()
                )
            # set the rest of the UI elements
            self.m_choiceSpeechAmount.SetSelection(Speech_Verbosity.index(user_preferences["Speech"]["Verbosity"]))
            self.m_sliderRelativeSpeed.SetValue(user_preferences["Speech"]["MathRate"])
            pause_factor = (
                0
                if user_preferences["Speech"]["PauseFactor"] <= 1
                else round(
                    math.log(
                        user_preferences["Speech"]["PauseFactor"] / PAUSE_FACTOR_SCALE,
                        PAUSE_FACTOR_LOG_BASE,
                    )
                )
            )
            self.m_sliderPauseFactor.SetValue(pause_factor)
            self.m_checkBoxSpeechSound.SetValue(user_preferences["Speech"]["SpeechSound"] == "Beep")
            self.m_choiceSpeechForChemical.SetSelection(Speech_Chemistry.index(user_preferences["Speech"]["Chemistry"]))
            self.m_choiceNavigationMode.SetSelection(Navigation_NavMode.index(user_preferences["Navigation"]["NavMode"]))
            self.m_checkBoxResetNavigationMode.SetValue(user_preferences["Navigation"]["ResetNavMode"])
            self.m_choiceSpeechAmountNavigation.SetSelection(
                Navigation_NavVerbosity.index(user_preferences["Navigation"]["NavVerbosity"])
            )
            if user_preferences["Navigation"]["Overview"]:
                self.m_choiceNavigationSpeech.SetSelection(1)
            else:
                self.m_choiceNavigationSpeech.SetSelection(0)
            self.m_checkBoxResetNavigationSpeech.SetValue(user_preferences["Navigation"]["ResetOverview"])
            self.m_checkBoxAutomaticZoom.SetValue(user_preferences["Navigation"]["AutoZoomOut"])
            self.m_choiceBrailleHighlights.SetSelection(
                Braille_BrailleNavHighlight.index(user_preferences["Braille"]["BrailleNavHighlight"])
            )
            self.m_choiceBrailleMathCode.SetSelection(
                Braille_BrailleCode.index(user_preferences["Braille"]["BrailleCode"])
            )
        except KeyError as err:
            print("Key not found", err)

    def get_ui_values(self):
        global user_preferences
        # read the values from the UI and update the user preferences dictionary
        user_preferences["Speech"]["Impairment"] = Speech_Impairment[self.m_choiceImpairment.GetSelection()]
        user_preferences["Speech"]["Language"] = self.GetLanguageCode()
        user_preferences["Speech"]["SpeechStyle"] = self.m_choiceSpeechStyle.GetStringSelection()
        user_preferences["Speech"]["Verbosity"] = Speech_Verbosity[self.m_choiceSpeechAmount.GetSelection()]
        user_preferences["Speech"]["MathRate"] = self.m_sliderRelativeSpeed.GetValue()
        pf_slider = self.m_sliderPauseFactor.GetValue()
        pause_factor = (
            0
            if pf_slider == 0
            else round(PAUSE_FACTOR_SCALE * math.pow(PAUSE_FACTOR_LOG_BASE, pf_slider))
        )  # avoid log(0)
        user_preferences["Speech"]["PauseFactor"] = pause_factor
        if self.m_checkBoxSpeechSound.GetValue():
            user_preferences["Speech"]["SpeechSound"] = "Beep"
        else:
            user_preferences["Speech"]["SpeechSound"] = "None"
        user_preferences["Speech"]["Chemistry"] = Speech_Chemistry[self.m_choiceSpeechForChemical.GetSelection()]
        user_preferences["Navigation"]["NavMode"] = Navigation_NavMode[self.m_choiceNavigationMode.GetSelection()]
        user_preferences["Navigation"]["ResetNavMode"] = self.m_checkBoxResetNavigationMode.GetValue()
        user_preferences["Navigation"]["NavVerbosity"] = Navigation_NavVerbosity[
            self.m_choiceSpeechAmountNavigation.GetSelection()
        ]
        user_preferences["Navigation"]["Overview"] = self.m_choiceNavigationSpeech.GetSelection() != 0
        user_preferences["Navigation"]["ResetOverview"] = self.m_checkBoxResetNavigationSpeech.GetValue()
        user_preferences["Navigation"]["AutoZoomOut"] = self.m_checkBoxAutomaticZoom.GetValue()
        user_preferences["Braille"]["BrailleNavHighlight"] = (
            Braille_BrailleNavHighlight[self.m_choiceBrailleHighlights.GetSelection()]
        )
        user_preferences["Braille"]["BrailleCode"] = Braille_BrailleCode[self.m_choiceBrailleMathCode.GetSelection()]
        user_preferences["MathCATPreferencesLastCategory"] = self.m_listBoxPreferencesTopic.GetSelection()

    @staticmethod
    def path_to_default_preferences():
        # the default preferences file is:
        #   C:\Users\<user-name>AppData\Roaming\\nvda\\addons\\MathCAT\\globalPlugins\\MathCAT\\Rules\\prefs.yaml
        return (
            os.path.expanduser("~") + "\\AppData\\Roaming\\nvda\\addons\\MathCAT\\globalPlugins\\MathCAT\\Rules\\prefs.yaml"
        )

    @staticmethod
    def path_to_user_preferences_folder():
        # the user preferences file is stored at: C:\Users\<user-name>AppData\Roaming\MathCAT\prefs.yaml
        return os.path.expanduser("~") + "\\AppData\\Roaming\\MathCAT"

    @staticmethod
    def path_to_user_preferences():
        # the user preferences file is stored at: C:\Users\<user-name>AppData\Roaming\MathCAT\prefs.yaml
        return UserInterface.path_to_user_preferences_folder() + "\\prefs.yaml"

    @staticmethod
    def load_default_preferences():
        global user_preferences
        # load default preferences into the user preferences data structure (overwrites existing)
        if os.path.exists(UserInterface.path_to_default_preferences()):
            with open(
                UserInterface.path_to_default_preferences(), encoding="utf-8"
            ) as f:
                user_preferences = yaml.load(f, Loader=yaml.FullLoader)

    @staticmethod
    def load_user_preferences():
        global user_preferences
        # merge user file values into the user preferences data structure
        if os.path.exists(UserInterface.path_to_user_preferences()):
            with open(UserInterface.path_to_user_preferences(), encoding="utf-8") as f:
                # merge with the default preferences, overwriting with the user's values
                user_preferences.update(yaml.load(f, Loader=yaml.FullLoader))

    @staticmethod
    def validate(key1: str, key2: str, valid_values: list, default_value: Union[str, int, bool]):
        global user_preferences
        try:
            if valid_values is None:
                # any value is valid
                if user_preferences[key1][key2] != "":
                    return
            if (isinstance(valid_values[0]) == int) and (isinstance(valid_values[1]) == int):
                # any value between lower and upper bounds is valid
                if user_preferences[key1][key2] >= valid_values[0] and user_preferences[key1][key2] <= valid_values[1]:
                    return
            else:
                # any value in the list is valid
                if user_preferences[key1][key2] in valid_values:
                    return
        except Exception as e:
            print(f"An exception occurred: {e}")
            # the preferences entry does not exist
            pass
        if key1 not in user_preferences:
            user_preferences[key1] = {key2: default_value}
        else:
            user_preferences[key1][key2] = default_value

    @staticmethod
    def validate_user_preferences():
        # check each user preference value to ensure it is present and valid, set default value if not
        #  Speech:
        # Impairment: Blindness       # LearningDisability, LowVision, Blindness
        UserInterface.validate("Speech", "Impairment", ["LearningDisability", "LowVision", "Blindness"], "Blindness")
        #   Language: en                # any known language code and sub-code -- could be en-uk, etc
        UserInterface.validate("Speech", "Language", None, "en")
        #    Verbosity: Medium           # Terse, Medium, Verbose
        UserInterface.validate("Speech", "Verbosity", ["Terse", "Medium", "Verbose"], "Medium")
        #    MathRate: 100               # Change from text speech rate (%)
        UserInterface.validate("Speech", "MathRate", [0, 200], 100)
        #    PauseFactor: 100            # TBC
        UserInterface.validate("Speech", "PauseFactor", [0, 1000], 100)
        #  SpeechSound: None           # make a sound when starting/ending math speech -- None, Beep
        UserInterface.validate("Speech", "SpeechSound", ["None", "Beep"], "None")
        #    SpeechStyle: ClearSpeak     # Any known speech style (falls back to ClearSpeak)
        UserInterface.validate("Speech", "SpeechStyle", None, "ClearSpeak")
        #    SubjectArea: General        # FIX: still working on this
        UserInterface.validate("Speech", "SubjectArea", None, "General")
        #    Chemistry: SpellOut         # SpellOut (H 2 0), AsCompound (Water), Off (H sub 2 O)
        UserInterface.validate("Speech", "Chemistry", ["SpellOut", "Off"], "SpellOut")
        # Navigation:
        #  NavMode: Enhanced         # Enhanced, Simple, Character
        UserInterface.validate("Navigation", "NavMode", ["Enhanced", "Simple", "Character"], "Enhanced")
        #  ResetNavMode: false       # remember previous value and use it
        UserInterface.validate("Navigation", "ResetNavMode", [False, True], False)
        #  Overview: false             # speak the expression or give a description/overview
        UserInterface.validate("Navigation", "Overview", [False, True], False)
        #  ResetOverview: true        # remember previous value and use it
        UserInterface.validate("Navigation", "ResetOverview", [False, True], True)
        #  NavVerbosity: Medium        # Terse, Medium, Full (words to say for nav command)
        UserInterface.validate("Navigation", "NavVerbosity", ["Terse", "Medium", "Full"], "Medium")
        #  AutoZoomOut: true           # Auto zoom out of 2D exprs (use shift-arrow to force zoom out if unchecked)
        UserInterface.validate("Navigation", "AutoZoomOut", [False, True], True)
        # Braille:
        #  BrailleNavHighlight: EndPoints
        # Highlight with dots 7 & 8 the current nav node -- values are Off, FirstChar, EndPoints, All
        UserInterface.validate("Braille", "BrailleNavHighlight", ["Off", "FirstChar", "EndPoints", "All"], "EndPoints")
        #  BrailleCode: "Nemeth"                # Any supported braille code (currently Nemeth, UEB, CMU, Vietnam)
        UserInterface.validate("Braille", "BrailleCode", ["Nemeth", "UEB", "CMU", "Vietnam"], "Nemeth")

    @staticmethod
    def write_user_preferences():
        # Language is special because it is set elsewhere by SetPreference which overrides the user_prefs -- so set it here
        from . import libmathcat

        libmathcat.SetPreference("Language", user_preferences["Speech"]["Language"])
        if not os.path.exists(UserInterface.path_to_user_preferences_folder()):
            # create a folder for the user preferences
            os.mkdir(UserInterface.path_to_user_preferences_folder())
        with open(UserInterface.path_to_user_preferences(), "w", encoding="utf-8") as f:
            # write values to the user preferences file, NOT the default
            yaml.dump(user_preferences, stream=f, allow_unicode=True)

    def OnRelativeSpeedChanged(self, event):
        rate = self.m_sliderRelativeSpeed.GetValue()
        # Translators: this is a test string that is spoken. Only translate "the square root of x squared plus y squared"
        text = _("<prosody rate='XXX%'>the square root of x squared plus y squared</prosody>").replace("XXX", str(rate), 1)
        speak(ConvertSSMLTextForNVDA(text))

    def OnPauseFactorChanged(self, event):
        rate = self.m_sliderRelativeSpeed.GetValue()
        pf_slider = self.m_sliderPauseFactor.GetValue()
        pause_factor = 0 if pf_slider == 0 else round(PAUSE_FACTOR_SCALE * math.pow(PAUSE_FACTOR_LOG_BASE, pf_slider))
        # Translators: this is a test string that is spoken. Only translate "the fraction with numerator"
        # and other parts NOT inside '<.../>',
        text = _(
            "<prosody rate='{rate}%'>the fraction with numerator <break time='{pause_factor_300}ms'/>\
                <mark name='M63i335o-4'/> <say-as interpret-as='characters'>x</say-as> to the <mark name='M63i335o-5'/>\
                <say-as interpret-as='characters'>n</say-as> <phoneme alphabet='ipa' ph='θ'>-th</phoneme>\
                power <break time='{pause_factor_128}ms'/> <mark name='M63i335o-6'/> plus  <mark name='M63i335o-7'/>1\
                <break time='{pause_factor_300}ms'/> and denominator <mark name='M63i335o-10'/>\
                <say-as interpret-as='characters'>x</say-as> to the <mark name='M63i335o-11'/>\
                <say-as interpret-as='characters'>n</say-as> <phoneme alphabet='ipa' ph='θ'>-th</phoneme>power\
                <break time='{pause_factor_128}ms'/> <mark name='M63i335o-12'/> minus  <mark name='M63i335o-13'/>1\
                <break time='{pause_factor_600}ms'/>end fraction <break time='{pause_factor_150}ms'/>"
        ).format(
            rate=rate,
            pause_factor_128=128 * pause_factor // 100,
            pause_factor_150=150 * pause_factor // 100,
            pause_factor_300=300 * pause_factor // 100,
            pause_factor_600=600 * pause_factor // 100,
        )
        speak(ConvertSSMLTextForNVDA(text))

    def OnClickOK(self, event):
        UserInterface.get_ui_values(self)
        UserInterface.write_user_preferences()
        self.Destroy()

    def OnClickCancel(self, event):
        self.Destroy()

    def OnClickApply(self, event):
        UserInterface.get_ui_values(self)
        UserInterface.write_user_preferences()

    def OnClickReset(self, event):
        UserInterface.load_default_preferences()
        UserInterface.validate_user_preferences()
        UserInterface.set_ui_values(self)

    def OnClickHelp(self, event):
        webbrowser.open("https://nsoiffer.github.io/MathCAT/users.html")

    def OnListBoxCategories(self, event):
        # the category changed, now show the appropriate dialogue page
        self.m_simplebookPanelsCategories.SetSelection(self.m_listBoxPreferencesTopic.GetSelection())

    def OnLanguage(self, event):
        # the language changed, get the SpeechStyles for the new language
        UserInterface.GetSpeechStyles(self, self.m_choiceSpeechStyle.GetSelection())

    def MathCATPreferencesDialogOnCharHook(self, event: wx.KeyEvent):
        # designed choice is that Enter is the same as clicking OK, and Escape is the same as clicking Cancel
        keyCode = event.GetKeyCode()
        if keyCode == wx.WXK_ESCAPE:
            UserInterface.OnClickCancel(self, event)
            return
        if keyCode == wx.WXK_RETURN:
            UserInterface.OnClickOK(self, event)
        if keyCode == wx.WXK_TAB:
            if event.GetModifiers() == wx.MOD_CONTROL:
                # cycle the category forward
                new_category = self.m_listBoxPreferencesTopic.GetSelection() + 1
                if new_category == 3:
                    new_category = 0
                self.m_listBoxPreferencesTopic.SetSelection(new_category)
                # update the ui to show the new page
                UserInterface.OnListBoxCategories(self, event)
                # set the focus into the category list box
                self.m_listBoxPreferencesTopic.SetFocus()
                # jump out so the tab key is not processed
                return
            if event.GetModifiers() == wx.MOD_CONTROL | wx.MOD_SHIFT:
                # cycle the category back
                new_category = self.m_listBoxPreferencesTopic.GetSelection() - 1
                if new_category == -1:
                    new_category = 2
                self.m_listBoxPreferencesTopic.SetSelection(new_category)
                # update the ui to show the new page
                UserInterface.OnListBoxCategories(self, event)
                # update the ui to show the new page
                self.m_listBoxPreferencesTopic.SetFocus()
                # jump out so the tab key is not processed
                return
            if event.GetModifiers() == wx.MOD_NONE and (
                MathCATgui.MathCATPreferencesDialog.FindFocus() == self.m_listBoxPreferencesTopic
            ):
                if self.m_listBoxPreferencesTopic.GetSelection() == 0:
                    self.m_choiceImpairment.SetFocus()
                elif self.m_listBoxPreferencesTopic.GetSelection() == 1:
                    self.m_choiceNavigationMode.SetFocus()
                elif self.m_listBoxPreferencesTopic.GetSelection() == 2:
                    self.m_choiceBrailleMathCode.SetFocus()
                return
            if (event.GetModifiers() == wx.MOD_SHIFT) and (
                MathCATgui.MathCATPreferencesDialog.FindFocus() == self.m_buttonOK
            ):
                if self.m_listBoxPreferencesTopic.GetSelection() == 0:
                    self.m_choiceSpeechForChemical.SetFocus()
                elif self.m_listBoxPreferencesTopic.GetSelection() == 1:
                    self.m_choiceSpeechAmountNavigation.SetFocus()
                elif self.m_listBoxPreferencesTopic.GetSelection() == 2:
                    self.m_choiceBrailleHighlights.SetFocus()
                return
        # continue handling keyboard event
        event.Skip()
