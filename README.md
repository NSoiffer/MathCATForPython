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

* Those who need high quality Nemeth braille (MathPlayer's Nemeth is based on liblouis' Nemeth generation which has a number of significant bugs that are technically difficult to fix).
* Those who need UEB technical braille
* Those who want to try out the latest technology and are willing to help by reporting bugs
* Those who use Eloquence as a voice

Who should NOT use MathCAT:

* Anyone who uses MathPlayer with a non-English language (translations exist for Indonesian and Vietnamese; translations will be coming in the future)
* Anyone who uses MathPlayer with a non-Nemeth/non-UEB braille output (contact me if you want to help out with a braille translation)
* Anyone who prefers Access8Math to MathPlayer (for speech or other features)

MathCAT's rules for speech are not yet as extensive as MathPlayer's rules -- that may be another reason to stick with MathPlayer. MathCAT is being used as a testbed for ideas for MathML 4 that allow authors to express their intent so that ambiguous notations can be spoken correctly and not guessed at. I have held off on adding too many rules since the architecture of MathCAT is centered around using and inferring author intent and these are not fully settled yet.

## MathCAT Update Log

### Version 0.2
* Lots of bug fixes
* Improvements to speech
* A preference setting to control the duration of pausing (works with changes to relative speech rate for math)
* Support to recognize chemistry notation and speak it appropriately
* Translations to Indonesian and Vietnamese


### Version 0.2.5
* More improvements chemistry
* Fixes for Nemeth:
* * Added "omission" rules
* * Added some rules for English Language Indicators
* * Added more cases where the Mulitpurpose indicator is needed
* * Fixes related to Nemeth and punctuation


### Version 0.3.3
This release has a number of bug fixes in it. The major new features and bug fixes are:
* Added Spanish Translation (thanks to Noelia Ruiz and  María Allo Roldán)
* Modified navigation so that it starts zoomed in one level
* Added cntrl+alt+arrow as a way to navigate tabular structures. These keys should be more memorable because they are used for table navigation in NVDA.
* Worked around NVDA bug for eSpeak voices that caused them to slow down when the relative MathRate was set to be slower than the text speech rate.
* Worked around a OneCore voice problem so that they will speak the long 'a' sound.

There are lots of small tweaks to the speech and some bug fixes for both Nemeth and UEB.

Note: there is now an option to get Vietnam's braille standard as braille output. This is still a work in progress and is too buggy to be used other than for testing. I expect the next MathCAT release will contain a reliable implementation.

### Version 0.3.7
Braille:
* Dialog has been internationalized (many thanks to the translators!)
* Initial implementation of CMU -- braille code used in Spain and several Portuguese speaking countries
* Significant improvements to Vietnamese braille
* Change relative rate dialog slider to have a maximum value of 100% (now only allows setting slower rates). Also, added step sizes so it is easier to raise/lower the rate significantly.
* Fix some UEB bugs and added some characters for UEB

Other fixes:
* Improvements to Vietnamese speech
* Fixed bug with OneCore voices saying "a"
* Fixed some navigation bugs when `AutoZoomOut` is False (not the default)
* Fix updating around language changes and some other dialog changes so they take effect immediately upon clicking "Apply" or "OK".

