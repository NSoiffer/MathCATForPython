# MathCAT

* Author: Neil Soiffer
* NVDA compatibility: 2018.1 or later (untested in earlier versions)
* Download [stable version][1]

MathCAT is designed to eventually replace MathPlayer because MathPlayer is no longer supported. MathCAT generates speech and braille from MathML. The speech for math produced by MathCAT is enhanced with prosody so that it sounds more natural. The speech can be navigated in three modes using the same commands as MathPlayer. In addition, the navigation node is indicated on a braille display. Both Nemeth and UEB technical are supported.

MathCAT has a number of configuration options that control speech, navigation, and braille.
Many of these can be set in the MathCAT settings dialog (found NVDA Preferences menu).
For more information on these settings, see the [MathCAT documentation](https://nsoiffer.github.io/MathCAT/users.html).
The documentation includes a link to [a table listing all of the navigation commands in MathCAT](https://nsoiffer.github.io/MathCAT/nav-commands.html).

Note: MathCAT is a general library for generating speech and braille from MathML. It is used by other AT projects besides NVDA. For information on the MathCAT project in general, see the main [MathCAT Documentation page](https://nsoiffer.github.io/MathCAT).


Who should use MathCAT:

* Those who use the following spoken or braille Languages:
  * Languages: Chinese (Taiwan), English, Finnish, Indonesian, Spannish, Swedish, Vietnamese
  * Braille: CMU (Portugese, Spanish), Finnish AsciiMath, LaTeX (as used in German braille), Nemeth, Swedish, UEB, Vietnamese
* Those who need high quality Nemeth braille (MathPlayer's Nemeth is based on liblouis' Nemeth generation which has a number of significant bugs that are technically difficult to fix).
* Those who want to try out the latest technology and are willing to help by reporting bugs
* Those who use Eloquence as a voice

Who should NOT use MathCAT:

* Anyone who uses MathPlayer with a language that is not yet supported by MathCAT and are not comfortable with speech in one of the supported languages.
* Anyone who prefers Access8Math to MathPlayer (for speech or other features)

MathCAT's rules for speech are not yet as extensive as MathPlayer's rules although they are getting close -- that may be another reason to stick with MathPlayer. MathCAT is being used as a testbed for ideas for MathML 4 that allow authors to express their intent so that ambiguous notations can be spoken correctly and not guessed at. I have held off on adding too many rules since the architecture of MathCAT is centered around using and inferring author intent and these are not fully settled yet.

## MathCAT Update Log

### Version 0.6.8

Lots of changes because it has been a while since the last official release.

#### Speech

* Added "LiteralSpeak" style that does not infer what the meaning of the math and therefore, how that meaning spoken.
* Added Swedish to supported languages.
* Added Finnish to supported languages.
* For Vietnamese, added optional pitch change and beep for capital letters
* MathCAT will switch the voice when reading math if a different language from the current voice was set in the preference dialog.
* Added a en-UK variant with some British ways to speak bracketing chars.
* Added English rules for div, grad, and curl (calculus)
* Added English rule for $P(A|B)$ so that | is spoken as "given"
* In terse mode, integer subscripts are spoken as "x 1" instead of "x sub 1".
* Changed the speech for ≈ from "congruent to" to "approximately equal to"
* Added inference for cross-product and dot-product
* Added inference for div, grad, and curl
* Added special speech for zero, identity, and diagonal matrices in English
* Be more restrictive when inferring a table 
* Changed speech for the general cases of `mover` and `munder` from "modified x with y above it" to "quantity x with y above it"
* Improved rule for {} so that it isn't always spoken as "set of ...". It could just be bracketing chars.
* Tweaked the speech for ∈ inside of a set so that the word "is" is dropped when part of a set -- "the set of all x is an element of ..." sounds poor.
* Improved rule for chemistry recognition for atomic numbers.
* Update to speech hint property names in the proposed MathML Core property list
* Add speech for coordinates ("the point at 1 comma 2")
* Added pauses for a ","
* Added speech for units (e.g., "km", "in") -- won't work for single letter units such as "m" and "s" unless marked as a unit
* Terse mode now says "of" for functions except for trig/log functions. It was a little too terse before.

#### Navigation

* Added "Speech" to copy menu when navigating so that you can copy out the text used to speak the focus point in the expression being explored.
* Substantial rewrite of the navigation rules so that follow the inferred meaning. For example, if MathCAT says "absolute value of x" and you "zoom in", then you move to the "x", not to a vertical bar. As another example, if MathCAT determines that a table consists of rows of equations, navigation won't concatenate the columns so that the table acts like there is only one column.
* "Speak Overview" didn't do anything (fixed). Overviews remain under-developed.

#### Braille

* Added support for Finnish version of AsciiMath braille.
* Added support for Swedish braille.
* Added support for Vietnamese accents position for Vietnamese braille vowel "rhymes".
* Added preferences so that Nemeth users can remap typeforms (e.g, map BlackBoard Bold to a different character).
* Changed Blackboard typeform indicator to reuse italic indicator instead of reusing the script indicator. By changing the Nemeth typeform values in NVDA's addon subdirectory `addons\MathCAT\globalPlugins\MathCAT\Rulesprefs.yaml or adding it to `%AppData%\MathCAT\prefs.yaml`, you can restore the old mapping.

#### Other

* All the language and braille Rule files are zipped up per directory and unzipped on demand.
  * This currently saves ~5mb when Rules.zip is unzipped, and will save even more as more languages and braille codes are added.
  * If you know certain languages or braille code will definitely be used (e.g., it is the default), then the files in those directories can be manually unzipped to save a few tens of milliseconds the first time the language/braille code by that user.
* Added new preference DecimalSeparator.
  * The default value is Auto, with other values being ".", ",", and "Custom". The first three values set DecimalSeparators and BlockSeparators.
  * Auto sets those preferences based on the value of the Language pref. For some language such as Spanish, , is used in some countries and . is used in others. In this case, it is best to set the language to also include the country code (e.g, es-es or es-mx) to ensure the right value is used.
* Added more Unicode chars to include both all Unicode chars marked as "Sm" and those with a mathclass (except Alphabetic and Glyph classes) in the Unicode standard.
* Add support for some (upcoming) new Unicode characters (equilibrium arrows and others) used in Chemistry into UEB and Nemeth
* Fixed a bug with double-struck numbers for Nemeth.
* Several fixes for recognizing chemistry.

#### Fixes

* Setting .
* Fixed sans-serif indicator for Nemeth braille.
* Fixed a bug where empty cells in a table that is piecewise, m:system-of-equations or lines were spoken.
* Fixed bug where open/closed intervals were inferred when brackets/parens were nested (can't be an interval).
* Fixed a bug in UEB where passage mode should have been used for capitals.
* Fixed a crash with UEB in certain conditions with runs of capital letters.
* Fixed bug in Navigation of tables (previously reported "Error in Navigation").
* Fixed bug moving to previous/next column in tables when at a table row level.
* Fixed bug when trying to correct bad MathML representation of chemistry inside of the base of a script.
* Fixed Vietnamese braille for "/".
* In the dialog code, the file location and %APPDATA% are now used to find the Rules and prefs files.
* After changing how prefs work in a previous version, I forgot to change MathRate and PauseFactor to be numbers, not strings.
* Fixed bug in the braille Rules (missed change from earlier) where a third argument should have been given to say to look in the Braille definitions.yaml files and not the speech ones when looking up the value of a definition.
* Cleaned up use of definitions.yaml.
* Fixed some bugs in the MathML cleanup for "," decimal separators.
* Found a bug in braille highlighting when nothing is highlighted (maybe never happens which is why I didn't see it in practice?)
* Fixed "Describe" mode so that it works -- it is still very minimal and probably not useful yet
* Add space after math speech to work around a MS Word bug that concatinates the next character in the text onto the math.

### Version 0.5.6

* Added Copy As... to the MathCAT dialog (in the "Navagation" pane).
* Fixed a bug where the language reverted to English when changing speech styles.
* Fixed a bug with navigation and braille
* Fixed some Asciimath spacing problems.
* Improved chemistry recognition
* Updated MathCAT to new BANA Nemeth chemistry spec (still only single line and special case style/font changes not handled)
* Fix a crash when non-ASCII digits (e.g., bold digits) are used in numbers
* Don't use italic indicators in braille codes when the math alphanumeric italic chars are used
* Some other smaller bug fixes that weren't reported by users

### Version 0.5.0
* Added German LaTeX braille code. Unlike other braille codes, this generates ASCII chars and uses the current braille output table to translate the characters to braille.
* Added (expermental) ASCIIMath braille code. Like the LaTeX braille code, this generates ASCII chars and uses the current braille output table to translate the characters to braille.
* Added "CopyAs" preference that supports copying as MathML, LaTeX, or ASCIIMath using cntl+C when focused on MathML (as before). The currently focused node is copied. Note: this is only listed in the prefs.yaml file and is not exposed (yet) in the MathCAT Preferences dialog.

### Version 0.4.2
* Fixed language switching when voice changes and MathCAT language is "Auto"
* Added more checks for $Impairments to improve reading when it is not set for those who are blind
* Nemeth: fix for "~" when it isn't part of an mrow
* UEB: character additions, "~" spacing fix if prefix, xor fix, 
* MathML cleanup for accented vowels (mainly for Vietnamese)
* Major rewrite of preference reading/updating code with big speedup -- added `CheckRuleFiles` pref to control which files are checked for updates
* Added two new interface calls -- enables setting the navigaton location from the braille cursor (not part of MathCAT addon yet)

### Version 0.3.11
* Upgraded to python 3.11 and verified working with NVDA 2024.1
* Fix bugs in Vietnamese braille and also in Speech, mostly for chemistry.
* Fix broken braille when braille code and dependent language don't match (specifically Vietnam braille and Vietnamese speech)
* Fix whitespace bug in HTML inside of tokens
* Improve roman numeral detection


### Version 0.3.9
* Added Traditional Chinese translation (thanks to Hon-Jang Yang)
* Fixed bug with navigating into the base of a scripted expression that has parenthesis
* Significantly changed the way whitespace is handled. This mainly affects braille output (spaces and "omission" detection).
* Improved recognition of chemistry
* UEB braille fixes that came up from adding chemistry examples
* UEB fixes for adding auxillary parenthesis in some cases


### Version 0.3.8
Braille:
* Dialog has been internationalized for several languages (many thanks to the translators!)
* Initial implementation of CMU -- the braille code used in Spanish and Portuguese speaking countries
* Fix some UEB bugs and added some characters for UEB
* Significant improvements to Vietnamese braille

Other fixes:
* Change relative rate dialog slider to have a maximum value of 100% (now only allows setting slower rates). Also, added step sizes so it is easier to raise/lower the rate significantly.
* Fix eSpeak bug that sometimes cut off speech when the relative rate was changed
* Improvements to Vietnamese speech
* Fixed bug with OneCore voices saying "a"
* Fixed some navigation bugs when `AutoZoomOut` is False (not the default)
* Fix updating around language changes and some other dialog changes so they take effect immediately upon clicking "Apply" or "OK".
* Added an "Use Voice's Language" option so that out of the box, MathCAT will speak in the right language (if there is a translation)
* Several improvements for cleaning up poor MathML code

### Version 0.3.3
This release has a number of bug fixes in it. The major new features and bug fixes are:
* Added Spanish Translation (thanks to Noelia Ruiz and  María Allo Roldán)
* Modified navigation so that it starts zoomed in one level
* Added cntrl+alt+arrow as a way to navigate tabular structures. These keys should be more memorable because they are used for table navigation in NVDA.
* Worked around NVDA bug for eSpeak voices that caused them to slow down when the relative MathRate was set to be slower than the text speech rate.
* Worked around a OneCore voice problem so that they will speak the long 'a' sound.

There are lots of small tweaks to the speech and some bug fixes for both Nemeth and UEB.

Note: there is now an option to get Vietnam's braille standard as braille output. This is still a work in progress and is too buggy to be used other than for testing. I expect the next MathCAT release will contain a reliable implementation.

### Version 0.2.5
* More improvements chemistry
* Fixes for Nemeth:
* * Added "omission" rules
* * Added some rules for English Language Indicators
* * Added more cases where the Mulitpurpose indicator is needed
* * Fixes related to Nemeth and punctuation

### Version 0.2
* Lots of bug fixes
* Improvements to speech
* A preference setting to control the duration of pausing (works with changes to relative speech rate for math)
* Support to recognize chemistry notation and speak it appropriately
* Translations to Indonesian and Vietnamese

