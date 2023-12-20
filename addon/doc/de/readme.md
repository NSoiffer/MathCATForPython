# MathCAT #

* Autor: Neil Soiffer
* NVDA-Kompatibilität: 2018.1 oder neuer (nicht getestet in älteren
  Versionen)
* [Stabile Version herunterladen][1]

MathCAT wurde entwickelt, um MathPlayer zu ersetzen, da MathPlayer nicht
mehr unterstützt wird. MathCAT generiert Sprache und Blindenschrift aus
MathML. Die von MathCAT erzeugte Sprache für Mathematik wird mit Prosodie
verbessert, damit sie natürlicher klingt. Die Sprache kann in drei Modi mit
denselben Befehlen wie MathPlayer bedient werden. Zusätzlich wird der
Navigationsbereich auf einer Braillezeile angezeigt. Sowohl Nemeth- als auch
UEB-Technik werden unterstützt.

MathCAT verfügt über eine Reihe von Konfigurationsoptionen, die die
Sprachausgabe, Navigation und die Braille-Ausgabe steuern. Viele dieser
Optionen können in den MathCAT-Einstellungen vorgenommen werden (zu finden
im NVDA-Menü). Weitere Informationen zu diesen Einstellungen finden Sie in
der
[MathCAT-Dokumentation](https://nsoiffer.github.io/MathCAT/users.html). Die
Dokumentation enthält einen Link zu [einer Tabelle mit allen
Navigationsbefehlen in
MathCAT](https://nsoiffer.github.io/MathCAT/nav-commands.html).

Hinweis: MathCAT ist eine allgemeine Bibliothek zur Erzeugung von Sprache
und Braille aus MathML. Sie wird neben NVDA auch von anderen AT-Projekten
verwendet. Informationen über das MathCAT-Projekt im Allgemeinen finden Sie
auf der [Dokumentationsseite für
MathCAT](https://nsoiffer.github.io/MathCAT).


Wer sollte MathCAT benutzen:

* Diejenigen, die eine hohe Qualität der Nemeth-Brailleschrift benötigen
  (die Nemeth-Schrift von MathPlayer basiert auf der Nemeth-Schrift von
  liblouis, die eine Reihe schwerwiegender Fehler aufweist, die technisch
  schwer zu beheben sind).
* Diejenigen, die die technische Braille-Schrift UEB benötigen
* Diejenigen, die die neueste Technologie ausprobieren wollen und bereit
  sind, durch die Meldung von Fehlern zu helfen
* Diejenigen, die eine Eloquence-Stimme benutzen

Wer sollte MathCAT NICHT benutzen:

* Alle, die MathPlayer außer in englischer Sprache verwenden (Übersetzungen
  für Indonesisch und Vietnamesisch sind vorhanden; weitere Übersetzungen
  werden in Zukunft folgen)
* Alle, die den MathPlayer mit einer Braille-Ausgabe außer Nemeth und UEB
  benutzt (kontaktiert mich, wenn ihr mit einer Braille-Übersetzung
  aushelfen wollt)
* Alle, die den Access8Math dem MathPlayer vorzieht (wegen der Sprache oder
  anderer Funktionen)

Die Sprachregeln von MathCAT sind noch nicht so umfangreich wie die von
MathPlayer - ein weiterer Grund, bei MathPlayer zu bleiben. MathCAT wird als
Testumgebung für Ideen für MathML 4 verwendet, mit denen die Autoren
mehrdeutige Notationen korregieren können und diese dann nicht mehr erraten
werden müssen. Ich habe mich noch etwas zurückgehalten, zu viele Regeln
hinzuzufügen, da sich die Architektur von MathCAT auf die Verwendung und
Ableitung von Autorenabsichten konzentriert und diese noch nicht vollständig
geklärt sind.

## Änderungsprotokoll für MathCAT

### Version 0.2
* Viele Fehlerkorrekturen
* Verbesserungen für die Sprachausgabe
* Eine Einstellung zur Steuerung der Dauer von Pausen (funktioniert mit
  Änderungen der relativen Sprechgeschwindigkeit für Mathematik)
* Unterstützung bei der Erkennung der chemischen Notation und deren
  korrekten Aussprache
* Übersetzungen ins Indonesische und Vietnamesische


### Version 0.2.5
* Weitere Verbesserungen in Chemie
* Korrekturen für Nemeth:

	* Added "omission" rules
	* Added some rules for English Language Indicators
	* Added more cases where the Mulitpurpose indicator is needed
	* Fixes related to Nemeth and punctuation


### Version 0.3.3
Diese Version enthält eine Reihe von Fehlerkorrekturen. Die wichtigsten
neuen Funktionen und Fehlerkorrekturen sind:

* Spanisch Übersetzung hinzugefügt (Dank an Noelia Ruiz und María Allo
  Roldán)
* Die Navigation wurde so geändert, dass sie um eine Ebene vergrößert
  startet.
* Strg+Alt+Pfeiltasten als Möglichkeit zur Navigation in tabellarischen
  Strukturen hinzugefügt. Diese Tasten sollten einprägsamer sein, da sie für
  die Tabellennavigation in NVDA verwendet werden.
* Ein NVDA-Fehler für eSpeak-Stimmen wurde behoben, der dazu führte, dass
  sie langsamer wurden, wenn die relative MathRate langsamer als die
  Sprachgeschwindigkeit im Text eingestellt war.
* Ein Problem mit Onecore-Stimmen korrigiert, damit sie auch ein langen
  A-Laut sprechen.

Es gibt viele kleine Verbesserungen für die Sprachausgabe und einige
Fehlerkorrekturen sowohl für Nemeth als auch für UEB.

Hinweis: Es gibt jetzt eine Option, um den vietnamesischen Braille-Standard
als Braille-Ausgabe zu erhalten. Diese ist noch in Arbeit und
fehleranfällig, um außer zum Testen verwendet zu werden. Die nächste
MathCAT-Version wird eine zuverlässige Implementierung enthalten.

### Version 0.3.8
Braille:

* Dialog has been internationalized (many thanks to the translators!)
* Initial implementation of CMU -- braille code used in Spain and several
  Portuguese speaking countries
* Significant improvements to Vietnamese braille
* Change relative rate dialog slider to have a maximum value of 100% (now
  only allows setting slower rates). Also, added step sizes so it is easier
  to raise/lower the rate significantly.
* Fix some UEB bugs and added some characters for UEB

Other fixes:

* Improvements to Vietnamese speech
* Fixed bug with OneCore voices saying "a"
* Fixed some navigation bugs when `AutoZoomOut` is False (not the default)
* Fix updating around language changes and some other dialog changes so they
  take effect immediately upon clicking "Apply" or "OK".

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=mathcat
