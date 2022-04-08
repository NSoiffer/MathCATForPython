# MathCAT add-on: generates speech, braille, and allows exploration of expressions written in MathML
# The goal of this add-on is to replicate/improve upon the functionality of MathPlayer which has been discontinued.
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
import winUser                              # clipboard manipultation
from ctypes import windll                   # register clipboard formats

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

RE_MP_SPEECH = re.compile(
    # Break.
    r"<break time='(?P<break>\d+)ms'/> ?"
    # Pronunciation of characters.
    r"|<say-as interpret-as='characters'>(?P<char>[^<]+)</say-as> ?"
    # Specific pronunciation.
    r"|<phoneme alphabet='ipa' ph='(?P<ipa>[^']+)'> (?P<phonemeText>[^ <]+)</phoneme> ?"
    # Prosody.
    r"|<prosody(?: pitch='(?P<pitch>\d+)%')?(?: volume='(?P<volume>\d+)%')?(?: rate='(?P<rate>\d+)%')?> ?"
    r"|(?P<prosodyReset></prosody>) ?"
    # Other tags, which we don't care about.
    r"|<[^>]+> ?"
    # Commas indicating pauses in navigation messages.
    r"| ?(?P<comma>,) ?"
    # Actual content.
    r"|(?P<content>[^<,]+)")

PROSODY_COMMANDS = {
    "pitch": PitchCommand,
    "volume": VolumeCommand,
    "rate": RateCommand,
}

def  ConvertSSMLTextForNVDA(text, language=""):
    # MathCAT's default rate is 180 wpm.
    # Assume that 0% is 80 wpm and 100% is 450 wpm and scale accordingly.
    synth = getSynth()
    wpm = synth._percentToParam(synth.rate, 80, 450)
    breakMulti = 180.0 / wpm
    synthConfig = config.conf["speech"][synth.name]
    out = []
    if language:
        out.append(LangChangeCommand(language))
    resetProsody = set()
    for m in RE_MP_SPEECH.finditer(text):
        if m.lastgroup == "break":
            out.append(BreakCommand(time=int(m.group("break")) * breakMulti))
        elif m.lastgroup == "char":
            # get the NVDA settings for what to do for a capital char and apply them
            ch = m.group("char")
            if ch.isupper():
                if synthConfig["sayCapForCapitals"]:
                    out.append(_(u"cap"))           # capital letter prefix
                out.append(PitchCommand(multiplier=int(synthConfig["capPitchChange"])))
                if synthConfig["beepForCapitals"]:
                    out.append(BeepCommand(2000, 50))
            out.extend((CharacterModeCommand(True), ch, CharacterModeCommand(False)))
            if ch.isupper():
                out.append(PitchCommand(multiplier=1))
        elif m.lastgroup == "comma":
            out.append(BreakCommand(time=100))
        elif m.lastgroup in PROSODY_COMMANDS:
            command = PROSODY_COMMANDS[m.lastgroup]
            out.append(command(multiplier=int(m.group(m.lastgroup)) / 100.0))
            resetProsody.add(command)
        elif m.lastgroup == "prosodyReset":
            for command in resetProsody:
                out.append(command(multiplier=1))
            resetProsody.clear()
        elif m.lastgroup == "phonemeText":
            out.append(PhonemeCommand(m.group("ipa"), text=m.group("phonemeText")))
        elif m.lastgroup == "content":
            # MathCAT puts out spaces between words, the speak command seems to want to glom the strings together at times,
            #  so we need to add individual " "s to the output
            out.append(" ")
            out.append(m.group(0))
            out.append(" ")

    if language:
        out.append(LangChangeCommand(None))
    return out

class MathCATInteraction(mathPres.MathInteractionNVDAObject):
    # Put MathML on the clipboard using the two formats below (defined by MathML spec)
    # We use both formats because some apps may only use one or the other
    # Note: filed https://github.com/nvaccess/nvda/issues/13240 to make this usable outside of MathCAT
    CF_MathML = windll.user32.RegisterClipboardFormatW("MathML")
    CF_MathML_Presentation = windll.user32.RegisterClipboardFormatW("MathML Presentation")
    # log.info("2**** MathCAT registering data formats: CF_MathML %x, CF_MathML_Presentation %x" % (CF_MathML, CF_MathML_Presentation))

    def __init__(self, provider=None, mathMl=None):
        super(MathCATInteraction, self).__init__(provider=provider, mathMl=mathMl)
        provider._setSpeechLanguage(mathMl)
        try:
            libmathcat.SetMathML(mathMl)
        except Exception as e:
            speech.speakMessage(_("Illegal MathML found: see NVDA error log for details"))
            log.error(e)

    def reportFocus(self):
        super(MathCATInteraction, self).reportFocus()
        try:
            speech.speak(ConvertSSMLTextForNVDA(libmathcat.GetSpokenText(),
                        self.provider._language))
        except Exception as e:
            log.error(e)
            speech.speakMessage(_("Error in speaking math: see NVDA error log for details"))


    def getBrailleRegions(self, review=False):
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

    def getScript(self, gesture):
        # Pass most keys to MathCAT. Pretty ugly.
        if isinstance(gesture, KeyboardInputGesture) and "NVDA" not in gesture.modifierNames and (
            gesture.mainKeyName in {
                "leftArrow", "rightArrow", "upArrow", "downArrow",
                "home", "end",
                "space", "backspace", "enter",
            }
            # or len(gesture.mainKeyName) == 1
        ):
            return self.script_navigate
        return super().getScript(gesture)

    def script_navigate(self, gesture):
        # log.info("***MathCAT script_navigate")
        try:
            if gesture != None:
                modNames = gesture.modifierNames
                text = libmathcat.DoNavigateKeyPress(gesture.vkCode,
                    "shift" in modNames, "control" in modNames, "alt" in modNames, False)
                speech.speak(ConvertSSMLTextForNVDA(text, self.provider._language))
            
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
        gesture="kb:control+c",
    )
    def script_rawdataToClip(self, gesture):
        try:
            mathml = libmathcat.GetNavigationMathML()[0]
            if not re.match(self._startsWithMath, mathml):
                mathml = "<math>" + mathml + "</math>"  # copy will fix up namespacing
            self._copyToClipAsMathML(mathml)
            ui.message(_("copy"))
        except Exception as e:
            log.error(e)
            speech.speakMessage(_("unable to copy math: see NVDA error log for details"))


     # not a perfect match sequence, but should capture normal MathML
    _mathTagHasNameSpace = re.compile("<math .*?xmlns.+?>")
    def _wrapMathMLForClipBoard(self, text: str) -> str:
        # cleanup the MathML a little
        mathml_with_ns = text.replace(" data-changed='added'", "").replace(" data-id-added='true'", "")
        if not re.match(self._mathTagHasNameSpace, text):
            mathml_with_ns = mathml_with_ns.replace('math', 'math xmlns="http://www.w3.org/1998/Math/MathML"', 1)
        return '<?xml version="1.0"?>' + mathml_with_ns

    from typing import Any, Optional
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
        try:
            with winUser.openClipboard(mainFrame.Handle):
                winUser.emptyClipboard()
                self._setClipboardData(self.CF_MathML, self._wrapMathMLForClipBoard(text))
                self._setClipboardData(self.CF_MathML_Presentation, self._wrapMathMLForClipBoard(text))
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

    def _setClipboardData(self, format,data):
        # Need to support MathML Presentation, so this copied from winUser.py and the first two lines are commented out
        # For now only unicode is a supported format
        # if format!=CF_UNICODETEXT:
        #     raise ValueError("Unsupported format")
        from textUtils import WCHAR_ENCODING
        from ctypes import c_wchar
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
            raise ctypes.WinError()
        # NULL the global memory handle so that it is not freed at the end of scope as the clipboard now has it.
        h.forget()

class MathCAT(mathPres.MathPresentationProvider):
    def __init__(self):
        # super(MathCAT, self).__init__(*args, **kwargs)

        try:
            # IMPORTANT -- SetRulesDir must be the first call to libmathcat
            rules_dir = path.join( path.dirname(path.abspath(__file__)), "Rules")
            log.info("MathCAT Rules dir: %s" % rules_dir)
            libmathcat.SetRulesDir(rules_dir)
            libmathcat.SetPreference("TTS", "SSML")

        except Exception as e:
            log.error(e)
            speech.speakMessage(_("MathCAT initialization failed: see NVDA error log for details"))


        # store mathcontent for navigation and copy
        mathcontent = None   

    def getSpeechForMathMl(self, mathml):
        self._setSpeechLanguage(mathml)
        try:
            libmathcat.SetMathML(mathml)
            mathcontent = mathml
        except Exception as e:
            log.error(e)
            speech.speakMessage(_("Illegal MathML found: see NVDA error log for details"))
            libmathcat.SetMathML("<math></math>")    # set it to something
        try:
            return ConvertSSMLTextForNVDA(libmathcat.GetSpokenText())
        except Exception as e:
            log.error(e)
            speech.speakMessage(_("Error in speaking math: see NVDA error log for details"))
            return [""]


    def getBrailleForMathMl(self, mathml):
        # log.info("***MathCAT getBrailleForMathMl")
        try:
            libmathcat.SetMathML(mathml)
        except Exception as e:
            log.error(e)
            speech.speakMessage(_("Illegal MathML found: see NVDA error log for details"))
            libmathcat.SetMathML("<math></math>")    # set it to something
        try:
            return libmathcat.GetBraille("")
        except Exception as e:
            log.error(e)
            speech.speakMessage(_("Error in brailling math: see NVDA error log for details"))
            return ""


    def interactWithMathMl(self, mathMl):
        MathCATInteraction(provider=self, mathMl=mathMl).setFocus()
        MathCATInteraction(provider=self, mathMl=mathMl).script_navigate(None)

    def _setSpeechLanguage(self, mathMl):
        lang = mathPres.getLanguageFromMath(mathMl)
        if not lang:
            lang = speech.getCurrentLanguage()
        try:
            libmathcat.SetPreference("Language", lang.replace("_", "-"))
            self._language = lang
        except Exception as e:
            log.error(e)
            speech.speakMessage(_("MathCAT does not support language %s: see NVDA error log for details" % lang))

