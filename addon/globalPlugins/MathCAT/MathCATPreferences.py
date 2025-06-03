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
from collections.abc import Callable
from .MathCAT import convertSSMLTextForNVDA
from speech import speak
from zipfile import ZipFile

addonHandler.initTranslation()
_ = gettext.gettext

# two constants to scale "PauseFactor"
# these work out so that a slider that goes [0,14] has value ~100 at 7 and ~1000 at 14
PAUSE_FACTOR_SCALE: float = 9.5
PAUSE_FACTOR_LOG_BASE: float = 1.4

# initialize the user preferences tuples
userPreferences: dict[str, dict[str, int | str | bool]] = {}
# Speech_Language is derived from the folder structures
Speech_DecimalSeparator = ("Auto", ".", ",", "Custom")
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
Navigation_CopyAs = ("MathML", "LaTeX", "ASCIIMath", "Speech")
Braille_BrailleNavHighlight = ("Off", "FirstChar", "EndPoints", "All")


class UserInterface(MathCATgui.MathCATPreferencesDialog):
	def __init__(self, parent):
		# initialize parent class
		MathCATgui.MathCATPreferencesDialog.__init__(self, parent)

		# load the logo into the dialog
		fullPathToLogo: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo.png")
		if os.path.exists(fullPathToLogo):
			self._bitmapLogo.SetBitmap(wx.Bitmap(fullPathToLogo))

		# load in the system values followed by the user prefs (if any)
		UserInterface.loadDefaultPreferences()
		UserInterface.loadUserPreferences()

		# hack for "CopyAs" because its location in the prefs is not yet fixed
		if "CopyAs" not in userPreferences["Navigation"]:
			userPreferences["Navigation"]["CopyAs"] = (
				userPreferences["Other"]["CopyAs"] if "CopyAs" in userPreferences["Other"] else "MathML"
			)
		UserInterface.validateUserPreferences()

		if "NVDAAddOn" in userPreferences:
			# set the categories selection to what we used on last run
			self._listBoxPreferencesTopic.SetSelection(userPreferences["NVDAAddOn"]["LastCategory"])
			# show the appropriate dialogue page
			self._simplebookPanelsCategories.SetSelection(self._listBoxPreferencesTopic.GetSelection())
		else:
			# set the categories selection to the first item
			self._listBoxPreferencesTopic.SetSelection(0)
			userPreferences["NVDAAddOn"] = {"LastCategory": "0"}
		# populate the languages and braille codes
		UserInterface.getLanguages(self)
		UserInterface.getBrailleCodes(self)
		# set the ui items to match the preferences
		UserInterface.setUIValues(self)

	@staticmethod
	def pathToLanguagesFolder() -> str:
		# the user preferences file is stored at: MathCAT\Rules\Languages
		return os.path.join(os.path.dirname(os.path.abspath(__file__)), "Rules", "Languages")

	@staticmethod
	def pathToBrailleFolder() -> str:
		# the user preferences file is stored at: MathCAT\Rules\Languages
		return os.path.join(os.path.dirname(os.path.abspath(__file__)), "Rules", "Braille")

	@staticmethod
	def languagesDict() -> dict[str, str]:
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
			"it": "Italiano",
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

	def getRulesFiles(
		self,
		pathToDir: str,
		processSubDirs: Callable[[str, str], list[str]] | None,
	) -> list[str]:
		language: str = os.path.basename(pathToDir)
		ruleFiles: list[str] = [
			os.path.basename(file) for file in glob.glob(os.path.join(pathToDir, "*_Rules.yaml"))
		]
		for dir in os.listdir(pathToDir):
			if os.path.isdir(os.path.join(pathToDir, dir)):
				if processSubDirs:
					ruleFiles.extend(processSubDirs(dir, language))

		if len(ruleFiles) == 0:
			# look in the .zip file for the style files, including regional subdirs -- it might not have been unzipped
			try:
				zip_file: ZipFile = ZipFile(f"{pathToDir}\\{language}.zip", "r")
				for file in zip_file.namelist():
					if file.endswith("_Rules.yaml"):
						ruleFiles.append(file)
					elif zip_file.getinfo(file).is_dir() and processSubDirs:
						ruleFiles.extend(processSubDirs(dir, language))
			except Exception as e:
				log.debugWarning(f"MathCAT Dialog: didn't find zip file {zip_file}. Error: {e}")

		return ruleFiles

	def getLanguages(self) -> None:
		def addRegionalLanguages(subDir: str, language: str) -> list[str]:
			# the language variants are in folders named using ISO 3166-1 alpha-2
			# codes https://en.wikipedia.org/wiki/ISO_3166-2
			# check if there are language variants in the language folder
			if subDir != "SharedRules":
				languagesDict: dict[str, str] = UserInterface.languagesDict()
				# add to the listbox the text for this language variant together with the code
				regionalCode: str = language + "-" + subDir.upper()
				if languagesDict.get(regionalCode, "missing") != "missing":
					self._choiceLanguage.Append(f"{languagesDict[regionalCode]} ({language}-{subDir})")
				elif languagesDict.get(language, "missing") != "missing":
					self._choiceLanguage.Append(f"{languagesDict[language]} ({regionalCode})")
				else:
					self._choiceLanguage.Append(f"{language} ({regionalCode})")
				return [os.path.basename(file) for file in glob.glob(os.path.join(subDir, "*_Rules.yaml"))]
			return []

		# initialise the language list
		languagesDict: dict[str, str] = UserInterface.languagesDict()
		# clear the language names in the dialog
		self._choiceLanguage.Clear()
		# Translators: menu item -- use the language of the voice chosen in the NVDA speech settings dialog
		# "Auto" == "Automatic" -- other items in menu are "English (en)", etc., so this matches that style
		self._choiceLanguage.Append(_("Use Voice's Language (Auto)"))
		# populate the available language names in the dialog
		# the implemented languages are in folders named using the relevant ISO 639-1
		#   code https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
		languageDir: str = UserInterface.pathToLanguagesFolder()
		for language in os.listdir(languageDir):
			pathToLanguageDir: str = os.path.join(UserInterface.pathToLanguagesFolder(), language)
			if os.path.isdir(pathToLanguageDir):
				# only add this language if there is a xxx_Rules.yaml file
				if len(self.getRulesFiles(pathToLanguageDir, addRegionalLanguages)) > 0:
					# add to the listbox the text for this language together with the code
					if languagesDict.get(language, "missing") != "missing":
						self._choiceLanguage.Append(languagesDict[language] + " (" + language + ")")
					else:
						self._choiceLanguage.Append(language + " (" + language + ")")

	def getLanguageCode(self) -> str:
		langSelection: str = self._choiceLanguage.GetStringSelection()
		langCode: str = langSelection[langSelection.find("(") + 1 : langSelection.find(")")]
		return langCode

	def getSpeechStyles(self, thisSpeechStyle: str):
		"""Get all the speech styles for the current language.
		This sets the SpeechStyles dialog entry"""
		from speech import getCurrentLanguage

		def getSpeechStyleFromDirectory(dir: str, lang: str) -> list[str]:
			r"""Get the speech styles from any regional dialog, from the main language, dir and if there isn't from the zip file.
			The 'lang', if it has a region dialect, is of the form 'en\uk'
			The returned list is sorted alphabetically"""
			# start with the regional dialect, then add on any (unique) styles in the main dir
			mainLang: str = lang.split("\\")[0]  # does the right thing even if there is no regional directory
			allStyleFiles: list[str] = []
			if lang.find("\\") >= 0:
				allStyleFiles: list[str] = [
					os.path.basename(name) for name in glob.glob(dir + lang + "\\*_Rules.yaml")
				]
			allStyleFiles.extend(
				[os.path.basename(name) for name in glob.glob(dir + mainLang + "\\*_Rules.yaml")],
			)
			allStyleFiles = list(set(allStyleFiles))  # make them unique
			if len(allStyleFiles) == 0:
				# look in the .zip file for the style files -- this will have regional variants, but also have that dir
				try:
					zipFilePath: str = dir + mainLang + "\\" + mainLang + ".zip"
					zipFile: ZipFile = ZipFile(zipFilePath, "r")  # file might not exist
					allStyleFiles = [
						name.split("/")[-1] for name in zipFile.namelist() if name.endswith("_Rules.yaml")
					]
				except Exception as e:
					log.debugWarning(f"MathCAT Dialog: didn't find zip file {zipFile}. Error: {e}")
			allStyleFiles.sort()
			return allStyleFiles

		# clear the SpeechStyle choices
		self._choiceSpeechStyle.Clear()
		# get the currently selected language code
		languageCode: str = UserInterface.getLanguageCode(self)

		if languageCode == "Auto":
			# list the speech styles for the current voice rather than have none listed
			languageCode = getCurrentLanguage().lower().replace("_", "-")
		languageCode = languageCode.replace("-", "\\")

		languagePath = UserInterface.pathToLanguagesFolder() + "\\"
		# log.info(f"languagePath={languagePath}")
		# populate the m_choiceSpeechStyle choices
		allStyleFiles = [
			# remove "_Rules.yaml" from the list
			name[: name.find("_Rules.yaml")]
			for name in getSpeechStyleFromDirectory(languagePath, languageCode)
		]
		# There isn't a LiteralSpeak rules file since it has no language-specific rules. We add it at the end.
		# Translators: at the moment, do NOT translate this string as some code specifically looks for this name.
		allStyleFiles.append("LiteralSpeak")
		for name in allStyleFiles:
			self._choiceSpeechStyle.Append((name))
		try:
			# set the SpeechStyle to the same as previous
			self._choiceSpeechStyle.SetStringSelection(
				thisSpeechStyle if thisSpeechStyle in allStyleFiles else allStyleFiles[0],
			)
		except Exception as e:
			log.exception(
				f"MathCAT: An exception occurred in GetSpeechStyles evaluating set SetStringSelection: {e}",
			)
			# that didn't work, choose the first in the list
			self._choiceSpeechStyle.SetSelection(0)

	def getBrailleCodes(self) -> None:
		# initialise the braille code list
		self._choiceBrailleMathCode.Clear()
		# populate the available braille codes in the dialog
		# the dir names are used, not the rule file names because the dir names have to be unique
		pathToBrailleFolder: str = UserInterface.pathToBrailleFolder()
		for brailleCode in os.listdir(pathToBrailleFolder):
			pathToBrailleCode: str = os.path.join(pathToBrailleFolder, brailleCode)
			if os.path.isdir(pathToBrailleCode):
				if len(self.getRulesFiles(pathToBrailleCode, None)) > 0:
					self._choiceBrailleMathCode.Append(brailleCode)

	def setUIValues(self) -> None:
		# set the UI elements to the ones read from the preference file(s)
		try:
			self._choiceImpairment.SetSelection(
				Speech_Impairment.index(userPreferences["Speech"]["Impairment"]),
			)
			try:
				langPref: str = userPreferences["Speech"]["Language"]
				self._choiceLanguage.SetSelection(0)
				i: int = 1  # no need to test i == 0
				while i < self._choiceLanguage.GetCount():
					if f"({langPref})" in self._choiceLanguage.GetString(i):
						self._choiceLanguage.SetSelection(i)
						break
					i += 1
			except Exception as e:
				log.exception(
					f"MathCAT: An exception occurred in setUIValues ('{userPreferences['Speech']['Language']}'): {e}",
				)
				# the language in the settings file is not in the folder structure, something went wrong,
				# set to the first in the list
				self._choiceLanguage.SetSelection(0)
			try:
				# now get the available SpeechStyles from the folder structure and set to the preference setting is possible
				self.getSpeechStyles(str(userPreferences["Speech"]["SpeechStyle"]))
			except Exception as e:
				log.exception(f"MathCAT: An exception occurred in set_ui_values (getting SpeechStyle): {e}")
				self._choiceSpeechStyle.Append(
					"Error when setting SpeechStyle for " + self._choiceLanguage.GetStringSelection(),
				)
			# set the rest of the UI elements
			self._choiceDecimalSeparator.SetSelection(
				Speech_DecimalSeparator.index(userPreferences["Other"]["DecimalSeparator"]),
			)
			self._choiceSpeechAmount.SetSelection(
				Speech_Verbosity.index(userPreferences["Speech"]["Verbosity"]),
			)
			self._sliderRelativeSpeed.SetValue(userPreferences["Speech"]["MathRate"])
			pause_factor = (
				0
				if int(userPreferences["Speech"]["PauseFactor"]) <= 1
				else round(
					math.log(
						int(userPreferences["Speech"]["PauseFactor"]) / PAUSE_FACTOR_SCALE,
						PAUSE_FACTOR_LOG_BASE,
					),
				)
			)
			self._sliderPauseFactor.SetValue(pause_factor)
			self._checkBoxSpeechSound.SetValue(userPreferences["Speech"]["SpeechSound"] == "Beep")
			self._choiceSpeechForChemical.SetSelection(
				Speech_Chemistry.index(userPreferences["Speech"]["Chemistry"]),
			)

			self._choiceNavigationMode.SetSelection(
				Navigation_NavMode.index(userPreferences["Navigation"]["NavMode"]),
			)
			self._checkBoxResetNavigationMode.SetValue(userPreferences["Navigation"]["ResetNavMode"])
			self._choiceSpeechAmountNavigation.SetSelection(
				Navigation_NavVerbosity.index(userPreferences["Navigation"]["NavVerbosity"]),
			)
			if userPreferences["Navigation"]["Overview"]:
				self._choiceNavigationSpeech.SetSelection(1)
			else:
				self._choiceNavigationSpeech.SetSelection(0)
			self._checkBoxResetNavigationSpeech.SetValue(userPreferences["Navigation"]["ResetOverview"])
			self._checkBoxAutomaticZoom.SetValue(userPreferences["Navigation"]["AutoZoomOut"])
			self._choiceCopyAs.SetSelection(
				Navigation_CopyAs.index(userPreferences["Navigation"]["CopyAs"]),
			)

			self._choiceBrailleHighlights.SetSelection(
				Braille_BrailleNavHighlight.index(userPreferences["Braille"]["BrailleNavHighlight"]),
			)
			try:
				braillePref: str = userPreferences["Braille"]["BrailleCode"]
				i = 0
				while braillePref != self._choiceBrailleMathCode.GetString(i):
					i = i + 1
					if i == self._choiceBrailleMathCode.GetCount():
						break
				if braillePref == self._choiceBrailleMathCode.GetString(i):
					self._choiceBrailleMathCode.SetSelection(i)
				else:
					self._choiceBrailleMathCode.SetSelection(0)
			except Exception as e:
				log.exception(f"MathCAT: An exception occurred while trying to set the Braille code: {e}")
				# the braille code in the settings file is not in the folder structure, something went wrong,
				# set to the first in the list
				self._choiceBrailleMathCode.SetSelection(0)
		except KeyError as err:
			print("Key not found", err)

	def getUIValues(self) -> None:
		global userPreferences
		# read the values from the UI and update the user preferences dictionary
		userPreferences["Speech"]["Impairment"] = Speech_Impairment[self._choiceImpairment.GetSelection()]
		userPreferences["Speech"]["Language"] = self.getLanguageCode()
		userPreferences["Other"]["DecimalSeparator"] = Speech_DecimalSeparator[
			self._choiceDecimalSeparator.GetSelection()
		]
		userPreferences["Speech"]["SpeechStyle"] = self._choiceSpeechStyle.GetStringSelection()
		userPreferences["Speech"]["Verbosity"] = Speech_Verbosity[self._choiceSpeechAmount.GetSelection()]
		userPreferences["Speech"]["MathRate"] = self._sliderRelativeSpeed.GetValue()
		pfSlider: int = self._sliderPauseFactor.GetValue()
		pauseFactor: int = (
			0 if pfSlider == 0 else round(PAUSE_FACTOR_SCALE * math.pow(PAUSE_FACTOR_LOG_BASE, pfSlider))
		)  # avoid log(0)
		userPreferences["Speech"]["PauseFactor"] = pauseFactor
		if self._checkBoxSpeechSound.GetValue():
			userPreferences["Speech"]["SpeechSound"] = "Beep"
		else:
			userPreferences["Speech"]["SpeechSound"] = "None"
		userPreferences["Speech"]["Chemistry"] = Speech_Chemistry[
			self._choiceSpeechForChemical.GetSelection()
		]
		userPreferences["Navigation"]["NavMode"] = Navigation_NavMode[
			self._choiceNavigationMode.GetSelection()
		]
		userPreferences["Navigation"]["ResetNavMode"] = self._checkBoxResetNavigationMode.GetValue()
		userPreferences["Navigation"]["NavVerbosity"] = Navigation_NavVerbosity[
			self._choiceSpeechAmountNavigation.GetSelection()
		]
		userPreferences["Navigation"]["Overview"] = self._choiceNavigationSpeech.GetSelection() != 0
		userPreferences["Navigation"]["ResetOverview"] = self._checkBoxResetNavigationSpeech.GetValue()
		userPreferences["Navigation"]["AutoZoomOut"] = self._checkBoxAutomaticZoom.GetValue()
		userPreferences["Navigation"]["CopyAs"] = Navigation_CopyAs[self._choiceCopyAs.GetSelection()]

		userPreferences["Braille"]["BrailleNavHighlight"] = Braille_BrailleNavHighlight[
			self._choiceBrailleHighlights.GetSelection()
		]
		userPreferences["Braille"]["BrailleCode"] = self._choiceBrailleMathCode.GetStringSelection()
		if "NVDAAddOn" not in userPreferences:
			userPreferences["NVDAAddOn"] = {"LastCategory": "0"}
		userPreferences["NVDAAddOn"]["LastCategory"] = self._listBoxPreferencesTopic.GetSelection()

	@staticmethod
	def pathToDefaultPreferences() -> str:
		return os.path.join(os.path.dirname(os.path.abspath(__file__)), "Rules", "prefs.yaml")

	@staticmethod
	def pathToUserPreferencesFolder() -> str:
		# the user preferences file is stored at: C:\Users\<user-name>AppData\Roaming\MathCAT\prefs.yaml
		return os.path.join(os.path.expandvars("%APPDATA%"), "MathCAT")

	@staticmethod
	def pathToUserPreferences() -> str:
		# the user preferences file is stored at: C:\Users\<user-name>AppData\Roaming\MathCAT\prefs.yaml
		return os.path.join(UserInterface.pathToUserPreferencesFolder(), "prefs.yaml")

	@staticmethod
	def loadDefaultPreferences() -> None:
		global userPreferences
		# load default preferences into the user preferences data structure (overwrites existing)
		if os.path.exists(UserInterface.pathToDefaultPreferences()):
			with open(
				UserInterface.pathToDefaultPreferences(),
				encoding="utf-8",
			) as f:
				userPreferences = yaml.load(f, Loader=yaml.FullLoader)

	@staticmethod
	def loadUserPreferences() -> None:
		global userPreferences
		# merge user file values into the user preferences data structure
		if os.path.exists(UserInterface.pathToUserPreferences()):
			with open(UserInterface.pathToUserPreferences(), encoding="utf-8") as f:
				# merge with the default preferences, overwriting with the user's values
				userPreferences.update(yaml.load(f, Loader=yaml.FullLoader))

	@staticmethod
	def validate(
		key1: str,
		key2: str,
		validValues: list[str | bool],
		defaultValue: str | bool,
	) -> None:
		global userPreferences
		try:
			if validValues == []:
				# any value is valid
				if userPreferences[key1][key2] != "":
					return

			else:
				# any value in the list is valid
				if userPreferences[key1][key2] in validValues:
					return
		except Exception as e:
			log.exception(f"MathCAT: An exception occurred in validate: {e}")
			# the preferences entry does not exist
		if key1 not in userPreferences:
			userPreferences[key1] = {key2: defaultValue}
		else:
			userPreferences[key1][key2] = defaultValue

	@staticmethod
	def validateInt(
		key1: str,
		key2: str,
		validValues: list[int],
		defaultValue: int,
	) -> None:
		global userPreferences
		try:
			# any value between lower and upper bounds is valid
			if (
				int(userPreferences[key1][key2]) >= validValues[0]
				and int(userPreferences[key1][key2]) <= validValues[1]
			):
				return
		except Exception as e:
			log.exception(f"MathCAT: An exception occurred in validateInt: {e}")
			# the preferences entry does not exist
		if key1 not in userPreferences:
			userPreferences[key1] = {key2: defaultValue}
		else:
			userPreferences[key1][key2] = defaultValue

	@staticmethod
	def validateUserPreferences():
		# check each user preference value to ensure it is present and valid, set default value if not
		#  Speech:
		# Impairment: Blindness       # LearningDisability, LowVision, Blindness
		UserInterface.validate(
			"Speech",
			"Impairment",
			["LearningDisability", "LowVision", "Blindness"],
			"Blindness",
		)
		#   Language: en                # any known language code and sub-code -- could be en-uk, etc
		UserInterface.validate("Speech", "Language", [], "en")
		#    Verbosity: Medium           # Terse, Medium, Verbose
		UserInterface.validate("Speech", "Verbosity", ["Terse", "Medium", "Verbose"], "Medium")
		#    MathRate: 100               # Change from text speech rate (%)
		UserInterface.validateInt("Speech", "MathRate", [0, 200], 100)
		#    PauseFactor: 100            # TBC
		UserInterface.validateInt("Speech", "PauseFactor", [0, 1000], 100)
		#  SpeechSound: None           # make a sound when starting/ending math speech -- None, Beep
		UserInterface.validate("Speech", "SpeechSound", ["None", "Beep"], "None")
		#    SpeechStyle: ClearSpeak     # Any known speech style (falls back to ClearSpeak)
		UserInterface.validate("Speech", "SpeechStyle", [], "ClearSpeak")
		#    SubjectArea: General        # FIX: still working on this
		UserInterface.validate("Speech", "SubjectArea", [], "General")
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
		#  CopyAs: MathML        # MathML, LaTeX, ASCIIMath, Speech
		UserInterface.validate("Navigation", "CopyAs", ["MathML", "LaTeX", "ASCIIMath", "Speech"], "MathML")
		# Braille:
		#  BrailleNavHighlight: EndPoints
		# Highlight with dots 7 & 8 the current nav node -- values are Off, FirstChar, EndPoints, All
		UserInterface.validate(
			"Braille",
			"BrailleNavHighlight",
			["Off", "FirstChar", "EndPoints", "All"],
			"EndPoints",
		)
		#  BrailleCode: "Nemeth"                # Any supported braille code (currently Nemeth, UEB, CMU, Vietnam)
		UserInterface.validate("Braille", "BrailleCode", [], "Nemeth")

	@staticmethod
	def writeUserPreferences() -> None:
		# Language is special because it is set elsewhere by SetPreference which overrides the user_prefs -- so set it here
		from . import libmathcat_py as libmathcat

		try:
			libmathcat.SetPreference("Language", userPreferences["Speech"]["Language"])
		except Exception as e:
			log.exception(
				f'Error in trying to set MathCAT "Language" preference to "{userPreferences["Speech"]["Language"]}": {e}',
			)
		if not os.path.exists(UserInterface.pathToUserPreferencesFolder()):
			# create a folder for the user preferences
			os.mkdir(UserInterface.pathToUserPreferencesFolder())
		with open(UserInterface.pathToUserPreferences(), "w", encoding="utf-8") as f:
			# write values to the user preferences file, NOT the default
			yaml.dump(userPreferences, stream=f, allow_unicode=True)

	def onRelativeSpeedChanged(self, event: wx.ScrollEvent) -> None:
		rate: int = self._sliderRelativeSpeed.GetValue()
		# Translators: this is a test string that is spoken. Only translate "the square root of x squared plus y squared"
		text: str = _("<prosody rate='XXX%'>the square root of x squared plus y squared</prosody>").replace(
			"XXX",
			str(rate),
			1,
		)
		speak(convertSSMLTextForNVDA(text))

	def onPauseFactorChanged(self, event: wx.ScrollEvent) -> None:
		rate: int = self._sliderRelativeSpeed.GetValue()
		pfSlider = self._sliderPauseFactor.GetValue()
		pauseFactor = (
			0 if pfSlider == 0 else round(PAUSE_FACTOR_SCALE * math.pow(PAUSE_FACTOR_LOG_BASE, pfSlider))
		)
		text: str = _(
			# Translators: this is a test string that is spoken. Only translate "the fraction with numerator"
			# and other parts NOT inside '<.../>',
			"<prosody rate='{rate}%'>the fraction with numerator <break time='{pause_factor_300}ms'/>\
                <mark name='M63i335o-4'/> <say-as interpret-as='characters'>x</say-as> to the <mark name='M63i335o-5'/>\
                <say-as interpret-as='characters'>n</say-as> <phoneme alphabet='ipa' ph='θ'>-th</phoneme>\
                power <break time='{pause_factor_128}ms'/> <mark name='M63i335o-6'/> plus  <mark name='M63i335o-7'/>1\
                <break time='{pause_factor_300}ms'/> and denominator <mark name='M63i335o-10'/>\
                <say-as interpret-as='characters'>x</say-as> to the <mark name='M63i335o-11'/>\
                <say-as interpret-as='characters'>n</say-as> <phoneme alphabet='ipa' ph='θ'>-th</phoneme>power\
                <break time='{pause_factor_128}ms'/> <mark name='M63i335o-12'/> minus  <mark name='M63i335o-13'/>1\
                <break time='{pause_factor_600}ms'/>end fraction <break time='{pause_factor_150}ms'/>",
		).format(
			rate=rate,
			pause_factor_128=128 * pauseFactor // 100,
			pause_factor_150=150 * pauseFactor // 100,
			pause_factor_300=300 * pauseFactor // 100,
			pause_factor_600=600 * pauseFactor // 100,
		)
		speak(convertSSMLTextForNVDA(text))

	def onClickOK(self, event: wx.CommandEvent) -> None:
		UserInterface.getUIValues(self)
		UserInterface.writeUserPreferences()
		self.Destroy()

	def onClickCancel(self, event: wx.CommandEvent) -> None:
		self.Destroy()

	def onClickApply(self, event: wx.CommandEvent) -> None:
		UserInterface.getUIValues(self)
		UserInterface.writeUserPreferences()

	def onClickReset(self, event: wx.CommandEvent) -> None:
		UserInterface.loadDefaultPreferences()
		UserInterface.validateUserPreferences()
		UserInterface.setUIValues(self)

	def onClickHelp(self, event: wx.CommandEvent) -> None:
		webbrowser.open("https://nsoiffer.github.io/MathCAT/users.html")

	def onListBoxCategories(self, event: wx.CommandEvent) -> None:
		# the category changed, now show the appropriate dialogue page
		self._simplebookPanelsCategories.SetSelection(self._listBoxPreferencesTopic.GetSelection())

	def onLanguage(self, event: wx.CommandEvent) -> None:
		# the language changed, get the SpeechStyles for the new language
		UserInterface.getSpeechStyles(self, self._choiceSpeechStyle.GetStringSelection())

	def mathCATPreferencesDialogOnCharHook(self, event: wx.KeyEvent) -> None:
		# designed choice is that Enter is the same as clicking OK, and Escape is the same as clicking Cancel
		keyCode: int = event.GetKeyCode()
		if keyCode == wx.WXK_ESCAPE:
			UserInterface.onClickCancel(self, event)
			return
		if keyCode == wx.WXK_RETURN:
			UserInterface.onClickOK(self, event)
		if keyCode == wx.WXK_TAB:
			if event.GetModifiers() == wx.MOD_CONTROL:
				# cycle the category forward
				newCategory: int = self._listBoxPreferencesTopic.GetSelection() + 1
				if newCategory == 3:
					newCategory = 0
				self._listBoxPreferencesTopic.SetSelection(newCategory)
				# update the ui to show the new page
				UserInterface.onListBoxCategories(self, event)
				# set the focus into the category list box
				self._listBoxPreferencesTopic.SetFocus()
				# jump out so the tab key is not processed
				return
			if event.GetModifiers() == wx.MOD_CONTROL | wx.MOD_SHIFT:
				# cycle the category back
				newCategory: int = self._listBoxPreferencesTopic.GetSelection() - 1
				if newCategory == -1:
					newCategory = 2
				self._listBoxPreferencesTopic.SetSelection(newCategory)
				# update the ui to show the new page
				UserInterface.onListBoxCategories(self, event)
				# update the ui to show the new page
				self._listBoxPreferencesTopic.SetFocus()
				# jump out so the tab key is not processed
				return
			if event.GetModifiers() == wx.MOD_NONE and (
				MathCATgui.MathCATPreferencesDialog.FindFocus() == self._listBoxPreferencesTopic
			):
				if self._listBoxPreferencesTopic.GetSelection() == 0:
					self._choiceImpairment.SetFocus()
				elif self._listBoxPreferencesTopic.GetSelection() == 1:
					self._choiceNavigationMode.SetFocus()
				elif self._listBoxPreferencesTopic.GetSelection() == 2:
					self._choiceBrailleMathCode.SetFocus()
				return
			if (event.GetModifiers() == wx.MOD_SHIFT) and (
				MathCATgui.MathCATPreferencesDialog.FindFocus() == self._buttonOK
			):
				if self._listBoxPreferencesTopic.GetSelection() == 0:
					self._choiceSpeechForChemical.SetFocus()
				elif self._listBoxPreferencesTopic.GetSelection() == 1:
					self._choiceSpeechAmountNavigation.SetFocus()
				elif self._listBoxPreferencesTopic.GetSelection() == 2:
					self._choiceBrailleHighlights.SetFocus()
				return
		# continue handling keyboard event
		event.Skip()
