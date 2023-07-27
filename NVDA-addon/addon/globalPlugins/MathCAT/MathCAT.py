"""MathCAT add-on: generates speech, braille, and allows exploration of expressions written in MathML.
The goal of this add-on is to replicate/improve upon the functionality of MathPlayer which has been discontinued."""
# Author: Neil Soiffer
# Copyright: this file is copyright GPL2
#   The code additionally makes use of the MathCAT library (written in Rust) which is covered by the MIT license
#   and also (obviously) requires external speech engines and braille drivers.
#   The plugin also requires the use of a small python dll: python3.dll
#   python3.dll has "Copyright © 2001-2022 Python Software Foundation; All Rights Reserved"


# Note: this code is a lot of cut/paste from other code and very likely could be substantially improved/cleaned.
import braille                              # we generate braille
import globalVars
from keyboardHandler import KeyboardInputGesture  # navigation key strokes
from logHandler import log                  # logging
import mathPres                             # math plugin stuff
from os import path                         # set rule dir path
import re                                   # regexp patter match
import speech                               # speech commands
import config                               # look up caps setting
import ui                                   # copy message
from scriptHandler import script            # copy MathML via ctrl-c
from synthDriverHandler import getSynth     # speech engine param setting
import winUser                              # clipboard manipulation
import gettext
_ = gettext.gettext
from ctypes import windll                   # register clipboard formats
from typing import Any, Optional

from . import libmathcat

# speech/SSML processing borrowed from NVDA's mathPres/mathPlayer.py
from speech.commands import (
    BeepCommand,
    PitchCommand,
    VolumeCommand,
    RateCommand,
    LangChangeCommand,
    BreakCommand,
    CharacterModeCommand,
    PhonemeCommand,
)

RE_MATHML_SPEECH = re.compile(
    # Break.
    r"<break time='(?P<break>\d+)ms'/> ?"
    # Pronunciation of characters.
    r"|<say-as interpret-as='characters'>(?P<char>[^<]+)</say-as> ?"
    # Specific pronunciation.
    r"|<phoneme alphabet='ipa' ph='(?P<ipa>[^']+)'>(?P<phonemeText>[^ <]+)</phoneme> ?"
    # Prosody.
    r"|<prosody(?: pitch='(?P<pitch>\d+)%')?(?: volume='(?P<volume>\d+)%')?(?: rate='(?P<rate>\d+)%')?> ?"
    r"|(?P<prosodyReset></prosody>) ?"
    r"|<audio src='(?P<beep>beep.mp4)'>.*?</audio> ?" # hack for beeps
    # Other tags, which we don't care about.
    r"|<[^>]+> ?"
    # Actual content.
    r"|(?P<content>[^<]+)")

PROSODY_COMMANDS = {
    "pitch": PitchCommand,
    "volume": VolumeCommand,
    "rate": RateCommand,
}
RE_MATH_LANG = re.compile(r'''<math .*(xml:)?lang=["']([^'"]+)["'].*>''')
def getLanguageToUse(mathMl:str) -> str:
    """Get the language specified in a math tag if the language pref is Auto, else the language preference."""
    mathCATLanguageSetting = "Auto"
    try:
        # ignore regional differences if the MathCAT language setting doesn't have it.
        mathCATLanguageSetting = libmathcat.GetPreference("Language")
    except Exception as e:
        log.error(e)
    
    if mathCATLanguageSetting != 'Auto':
        return mathCATLanguageSetting
    
    languageMatch = RE_MATH_LANG.search(mathMl)
    language = languageMatch.group(2) if languageMatch else speech.getCurrentLanguage() # seems to be current voice's language
    language = language.lower().replace("_", "-")
    return language

def  ConvertSSMLTextForNVDA(text:str, language:str="") -> list:
    # MathCAT's default rate is 180 wpm.
    # Assume that 0% is 80 wpm and 100% is 450 wpm and scale accordingly.
    # log.info(f"Speech str: '{text}'")
    if language == "":    # shouldn't happen
        language = "en"   # fallback to what was being used

    mathCATLanguageSetting = "en"   # fallback in case GetPreference fails for unknown reasons
    try:
        mathCATLanguageSetting = libmathcat.GetPreference("Language")
    except Exception as e:
        log.error(e)    

    synth = getSynth()
    wpm = synth._percentToParam(synth.rate, 80, 450)
    breakMulti = 180.0 / wpm
    synthConfig = config.conf["speech"][synth.name]
    supported_commands = synth.supportedCommands
    use_break = BreakCommand in supported_commands
    use_pitch = PitchCommand in supported_commands
    use_rate = RateCommand in supported_commands
    use_volume = VolumeCommand in supported_commands
    use_phoneme = PhonemeCommand in supported_commands
    # as of 7/23, oneCore voices do not implement the CharacterModeCommand despite it being in supported_commands
    use_character = CharacterModeCommand in supported_commands and synth.name != 'oneCore'
    out = []
    if mathCATLanguageSetting != language:
        try:
            log.info(f"Setting language to {language}")
            libmathcat.SetPreference("Language", language)
            out.append(LangChangeCommand(language))
        except Exception as e:
            log.error(e) 
            language = mathCATLanguageSetting   # didn't do the 'append'

    resetProsody = []
    for m in RE_MATHML_SPEECH.finditer(text):
        if m.lastgroup == "break":
            if use_break:
                out.append(BreakCommand(time=int(int(m.group("break")) * breakMulti)))
        elif m.lastgroup == "char":
            ch = m.group("char")
            if use_character:
                out.extend((CharacterModeCommand(True), ch, CharacterModeCommand(False)))
            else:
                out.extend((" ", "eigh" if ch=="a" else ch, " "))
        elif m.lastgroup == "beep":
            out.append(BeepCommand(2000, 50))
        elif m.lastgroup == "pitch":
            if use_pitch:
                out.append(PitchCommand(multiplier=int(m.group(m.lastgroup))))
                resetProsody.append(PitchCommand)
        elif m.lastgroup in PROSODY_COMMANDS:
            command = PROSODY_COMMANDS[m.lastgroup]
            if command in supported_commands:
                out.append(command(multiplier=int(m.group(m.lastgroup)) / 100.0))
                resetProsody.append(command)
        elif m.lastgroup == "prosodyReset":
            # for command in resetProsody:    # only supported commands were added, so no need to check
            command = resetProsody.pop()
            out.append(command(multiplier=1))
        elif m.lastgroup == "phonemeText":
            if use_phoneme:
                out.append(PhonemeCommand(m.group("ipa"), text=m.group("phonemeText")))
            else:
                out.append(m.group("phonemeText"))
        elif m.lastgroup == "content":
            # MathCAT puts out spaces between words, the speak command seems to want to glom the strings together at times,
            #  so we need to add individual " "s to the output
            out.extend((" ", m.group(0), " "))
    if mathCATLanguageSetting != language:
        try:
            libmathcat.SetPreference("Language", mathCATLanguageSetting)
            out.append(LangChangeCommand(None))
        except Exception as e:
            log.error(e) 
        
    # log.info(f"Speech commands: '{out}'")
    return out

class MathCATInteraction(mathPres.MathInteractionNVDAObject):
    # Put MathML on the clipboard using the two formats below (defined by MathML spec)
    # We use both formats because some apps may only use one or the other
    # Note: filed https://github.com/nvaccess/nvda/issues/13240 to make this usable outside of MathCAT
    CF_MathML = windll.user32.RegisterClipboardFormatW("MathML")
    CF_MathML_Presentation = windll.user32.RegisterClipboardFormatW("MathML Presentation")
    # log.info("2**** MathCAT registering data formats: CF_MathML %x, CF_MathML_Presentation %x" % (CF_MathML, CF_MathML_Presentation))

    def __init__(self, provider=None, mathMl: Optional[str]=None):
        super(MathCATInteraction, self).__init__(provider=provider, mathMl=mathMl)
        self._language = getLanguageToUse(mathMl)
        self.init_mathml = mathMl


    def reportFocus(self):
        super(MathCATInteraction, self).reportFocus()
        try:
            text = libmathcat.DoNavigateCommand("ZoomIn")
            speech.speak(ConvertSSMLTextForNVDA(text, self._language))
        except Exception as e:
            log.error(e)
            speech.speakMessage(_("Error in starting navigation of math: see NVDA error log for details"))


    def getBrailleRegions(self, review: bool = False):
        # log.info("***MathCAT start getBrailleRegions")
        yield braille.NVDAObjectRegion(self, appendText=" ")
        region = braille.Region()
        region.focusToHardLeft = True
        # libmathcat.SetBrailleWidth(braille.handler.displaySize)
        try:
            region.rawText = libmathcat.GetBraille("")
        except Exception as e:
            log.error(e)
            speech.speakMessage(_("Error in brailling math: see NVDA error log for details"))
            region.rawText = ""

        # log.info("***MathCAT end getBrailleRegions ***")
        yield region

    def getScript(self, gesture: KeyboardInputGesture):
        # Pass most keys to MathCAT. Pretty ugly.
        if isinstance(gesture, KeyboardInputGesture) and "NVDA" not in gesture.modifierNames and (
            gesture.mainKeyName in {
                "leftArrow", "rightArrow", "upArrow", "downArrow",
                "home", "end",
                "space", "backspace", "enter",
                "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
            }
            # or len(gesture.mainKeyName) == 1
        ):
            return self.script_navigate
        return super().getScript(gesture)

    def script_navigate(self, gesture: KeyboardInputGesture):
        # log.info("***MathCAT script_navigate")
        try:
            if gesture != None:     # == None when initial focus -- handled in reportFocus()
                modNames = gesture.modifierNames
                text = libmathcat.DoNavigateKeyPress(gesture.vkCode,
                    "shift" in modNames, "control" in modNames, "alt" in modNames, False)
                speech.speak(ConvertSSMLTextForNVDA(text, self._language))
            
            # update the braille to reflect the nav position (might be excess code, but it works)
            nav_node = libmathcat.GetNavigationMathMLId()
            region = braille.Region()
            region.rawText = libmathcat.GetBraille(nav_node[0])
            region.focusToHardLeft = True
            region.update()
            braille.handler.buffer.regions.append(region)
            braille.handler.buffer.focus(region)
            braille.handler.buffer.update()
            braille.handler.update()
        except Exception as e:
            log.error(e)
            speech.speakMessage(_("Error in navigating math: see NVDA error log for details"))


    _startsWithMath = re.compile("\\s*?<math")
    @script(
        # For translators: Message to be announced during Keyboard Help
        description=_("Copy navigation focus to clipboard"), 
        # For translators: Name of the section in "Input gestures" dialog. 
        category = _("Clipboard"),
        gesture="kb:control+c",
    )
    def script_rawdataToClip(self, gesture: KeyboardInputGesture):
        try:
            mathml = libmathcat.GetNavigationMathML()[0]
            if not re.match(self._startsWithMath, mathml):
                mathml = "<math>\n" + mathml + "</math>"  # copy will fix up name spacing
            elif self.init_mathml != '':
                mathml = self.init_mathml
            self._copyToClipAsMathML(mathml)
            ui.message(_("copy"))
        except Exception as e:
            log.error(e)
            speech.speakMessage(_("unable to copy math: see NVDA error log for details"))


     # not a perfect match sequence, but should capture normal MathML
     # not a perfect match sequence, but should capture normal MathML
    _mathTagHasNameSpace = re.compile("<math .*?xmlns.+?>")
    _hasAddedId = re.compile(" id='[^'].+' data-id-added='true'")
    _hasDataAttr = re.compile(" data-[^=]+='[^']*'")
    def _wrapMathMLForClipBoard(self, text: str) -> str:
        # cleanup the MathML a little
        text = re.sub(self._hasAddedId, "", text)
        mathml_with_ns = re.sub(self._hasDataAttr, "", text)
        if not re.match(self._mathTagHasNameSpace, mathml_with_ns):
            mathml_with_ns = mathml_with_ns.replace('math', "math xmlns='http://www.w3.org/1998/Math/MathML'", 1)
        return mathml_with_ns

    def _copyToClipAsMathML(self, text: str, notify: Optional[bool] = False) -> bool:
        """Copies the given text to the windows clipboard.
        @returns: True if it succeeds, False otherwise.
        @param text: the text which will be copied to the clipboard
        @param notify: whether to emit a confirmation message
        """
        # copied from api.py and modified to use CF_MathML_Presentation 
        if not isinstance(text, str) or len(text) == 0:
            return False
        from api import getClipData
        import gui

        try:
            with winUser.openClipboard(gui.mainFrame.Handle):
                winUser.emptyClipboard()
                text = self._wrapMathMLForClipBoard(text)
                self._setClipboardData(self.CF_MathML, '<?xml version="1.0"?>' + text)
                self._setClipboardData(self.CF_MathML_Presentation, '<?xml version="1.0"?>' + text)
                self._setClipboardData(winUser.CF_UNICODETEXT, text)
            got = getClipData()
        except OSError:
            if notify:
                ui.reportTextCopiedToClipboard()  # No argument reports a failure.
            return False
        if got == text:
            if notify:
                ui.reportTextCopiedToClipboard(text)
            return True
        if notify:
            ui.reportTextCopiedToClipboard()  # No argument reports a failure.
        return False

    def _setClipboardData(self, format, data: str):
        # Need to support MathML Presentation, so this copied from winUser.py and the first two lines are commented out
        # For now only unicode is a supported format
        # if format!=CF_UNICODETEXT:
        #     raise ValueError("Unsupported format")
        from textUtils import WCHAR_ENCODING
        from ctypes import c_wchar, WinError
        import winKernel
        text = data
        bufLen = len(text.encode(WCHAR_ENCODING, errors="surrogatepass")) + 2
        # Allocate global memory
        h=winKernel.HGLOBAL.alloc(winKernel.GMEM_MOVEABLE, bufLen)
        # Acquire a lock to the global memory receiving a local memory address
        with h.lock() as addr:
            # Write the text into the allocated memory
            buf=(c_wchar*bufLen).from_address(addr)
            buf.value=text
        # Set the clipboard data with the global memory
        if not windll.user32.SetClipboardData(format,h):
            raise WinError()
        # NULL the global memory handle so that it is not freed at the end of scope as the clipboard now has it.
        h.forget()

class MathCAT(mathPres.MathPresentationProvider):
    def __init__(self):
        # super(MathCAT, self).__init__(*args, **kwargs)

        try:
            # IMPORTANT -- SetRulesDir must be the first call to libmathcat
            rules_dir = path.join( path.dirname(path.abspath(__file__)), "Rules")
            log.info(f"MathCAT installed. Using rules dir: {rules_dir}")
            libmathcat.SetRulesDir(rules_dir)
            libmathcat.SetPreference("TTS", "SSML")
        except Exception as e:
            log.error(e)
            speech.speakMessage(_("MathCAT initialization failed: see NVDA error log for details"))
        self._language = ""


    def getSpeechForMathMl(self, mathml: str):
        try:
            self._language = getLanguageToUse(mathml)
            libmathcat.SetMathML(mathml)
        except Exception as e:
            log.error(e)
            log.error(f"MathML is {mathml}")
            speech.speakMessage(_("Illegal MathML found: see NVDA error log for details"))
            libmathcat.SetMathML("<math></math>")    # set it to something
        try:
            synth = getSynth()
            synthConfig = config.conf["speech"][synth.name]
            supported_commands = synth.supportedCommands
            # Set preferences for capital letters
            libmathcat.SetPreference("CapitalLetters_Beep", "true" if synthConfig["beepForCapitals"] else "false")
            libmathcat.SetPreference("CapitalLetters_UseWord", "true" if synthConfig["sayCapForCapitals"] else "false")
            if PitchCommand in supported_commands:
                libmathcat.SetPreference("CapitalLetters_Pitch", str(synthConfig["capPitchChange"]))
            if self._add_sounds():
                return [BeepCommand(800,25)] + ConvertSSMLTextForNVDA(libmathcat.GetSpokenText(), self._language) + [BeepCommand(600,15)]
            else:
                return ConvertSSMLTextForNVDA(libmathcat.GetSpokenText(), self._language)

        except Exception as e:
            log.error(e)
            speech.speakMessage(_("Error in speaking math: see NVDA error log for details"))
            return [""]

    def _add_sounds(self):
        try:
            return libmathcat.GetPreference("SpeechSound") != "None"
        except:
            return False

    def getBrailleForMathMl(self, mathml: str):
        # log.info("***MathCAT getBrailleForMathMl")
        try:
            libmathcat.SetMathML(mathml)
        except Exception as e:
            log.error(e)
            log.error(f"MathML is {mathml}")
            speech.speakMessage(_("Illegal MathML found: see NVDA error log for details"))
            libmathcat.SetMathML("<math></math>")    # set it to something
        try:
            return libmathcat.GetBraille("")
        except Exception as e:
            log.error(e)
            speech.speakMessage(_("Error in brailling math: see NVDA error log for details"))
            return ""


    def interactWithMathMl(self, mathml: str):
        MathCATInteraction(provider=self, mathMl=mathml).setFocus()
        MathCATInteraction(provider=self, mathMl=mathml).script_navigate(None)
