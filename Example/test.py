# MathCAT add-on: generates speech, braille, and allows exploration of expressions written in MathML
# The goal of this add-on is to replicate/improve on the functionality of MathPlayer which has been discontinued.
# Author: Neil Soiffer
# Copyright: this file uses whatever GNU copyright that is required for NVDA addons
#   The code additionally makes use of the MathCAT library (written in Rust) which is covered by the MIT license
#   and also (obviously) requires external speech engines and braille drivers.


import os
import libmathcat

# import shutil
# if os.path.exists("libmathcat_py.pyd"):
# 	os.remove("libmathcat_py.pyd")
# shutil.copy("..\\target\\i686-pc-windows-msvc\\release\\libmathcat_py.dll", "libmathcat.pyd")


def SetMathCATPreferences():
    try:
        libmathcat.SetRulesDir(
            # this assumes the Rules dir is in the same dir a the library. Modify as needed
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "Rules")
        )
    except Exception as e:
        print("problem with finding the MathCAT rules", e)

    try:
        libmathcat.SetPreference("TTS", "none")
        libmathcat.SetPreference("Language", "en")  # Also "id" and "vi"
        libmathcat.SetPreference("SpeechStyle", "SimpleSpeak")  # Also "ClearSpeak"
        libmathcat.SetPreference("Verbosity", "Verbose")  # also terse "Terse"/"Medium"
        libmathcat.SetPreference("CapitalLetters_UseWord", "true")  # if "true", X => "cap x"
    except Exception as e:
        print("problem with setting a preference", e)


def SetMathMLForMathCAT(mathml: str):
    try:
        libmathcat.SetMathML(mathml)
    except Exception as e:
        print("problem with SetMathML", e)


def GetSpeech():
    try:
        return libmathcat.GetSpokenText()
    except Exception as e:
        return "problem with getting speech for MathML", e


SetMathCATPreferences()  # you only need to this once

print("Using MathCAT version '{}'".format(libmathcat.GetVersion()))

mathml = "<math><mfrac> <mn>1</mn> <mi>X</mi> </mfrac> </math>"
SetMathMLForMathCAT(mathml)
print("MathML: {}\nSpeech: '{}'".format(mathml, GetSpeech()))

mathml = "<math display='block'><mi>x</mi><mo>⨯</mo><mi>y</mi></math>"
SetMathMLForMathCAT(mathml)
print("MathML: {}\nSpeech: '{}'".format(mathml, GetSpeech()))

mathml = "<math><msup> <mi>x</mi> <mn>3</mn> </msup> </math>"
SetMathMLForMathCAT(mathml)
print("MathML: {}\nSpeech: '{}'".format(mathml, GetSpeech()))

mathml = "<math><msup intent='transpose:postfix($x)'> <mi arg='x'>x</mi> <mi>T</mi> </msup> </math>"
SetMathMLForMathCAT(mathml)
print("MathML: {}\nSpeech: '{}'".format(mathml, GetSpeech()))

mathml = "<math><mrow intent='_(x, $op)'><mo arg='op'>!</mo></mrow></math>"
SetMathMLForMathCAT(mathml)
print("MathML: {}\nSpeech: '{}'".format(mathml, GetSpeech()))

mathml = "<math intent=':structure'><mrow><mo>\
  (</mo><mfrac linethickness='0'><mn arg='n'>7</mn><mn arg='m'>3</mn></mfrac><mo>)</mo></mrow></math>"
SetMathMLForMathCAT(mathml)
print("MathML: {}\nSpeech (no inference): '{}'".format(mathml, GetSpeech()))
