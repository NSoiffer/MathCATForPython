# MathCAT #

* Autor: Neil Soiffer
* NVDA-Kompatibilität: 2018.1 oder neuer (nicht getestet in älteren
  Versionen)
* [Stabile Version herunterladen][1]

MathCAT wurde entwickelt, um MathPlayer zu ersetzen, da der MathPlayer nicht
mehr unterstützt wird. MathCAT generiert Ausgaben über die Sprachausgabe und
in Braille aus MathML. Die von MathCAT erzeugte Sprache für Mathematik wird
durch Prosodie verbessert, so dass sie natürlicher klingt. Die Sprache kann
in drei Modi mit denselben Befehlen wie MathPlayer navigiert werden. Darüber
hinaus wird der Navigationsknoten auf einer Braillezeile angezeigt. Sowohl
Nemeth- als auch UEB-Technik werden unterstützt.

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
* Diejenigen, die technische Braille-Schrift UEB, CMU
  (Spanisch/Portugiesisch), deutsches LaTeX, ASCIIMath oder vietnamesische
  Braille-Schrift benötigen
* Diejenigen, die die neueste Technologie ausprobieren wollen und bereit
  sind, durch die Meldung von Fehlern zu helfen
* Diejenigen, die eine Eloquence-Stimme benutzen

Wer sollte MathCAT NICHT benutzen:

* Alle, die den MathPlayer mit einer Sprache verwendet, die noch nicht von
  MathCAT unterstützt wird (Übersetzungen gibt es für Chinesisch
  (traditionell), Spanisch, Indonesisch und Vietnamesisch; Übersetzungen
  werden in Zukunft folgen) und wer mit den unterstützten Sprachen (noch)
  nicht vertraut ist.
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

### Version 0.6.3

* Alle Sprach- und Braille-Regeldateien werden in ein Verzeichnis gepackt
  und bei Bedarf entpackt.

	* Dies spart derzeit ~5 MB, wenn Rules.zip entpackt wird, und wird noch
	  mehr sparen, wenn mehr Sprachen und Braille-Codes hinzugefügt werden.
	* Dies ist eine Vorbereitung für die Integration von MathCAT in NVDA 2024.3

* Neue Einstellung `DecimalSeparator` hinzugefügt.

	* Der Standardwert ist `Auto`, andere Werte sind ".", "," und "Custom". Die
	  ersten drei Werte legen `DecimalSeparators` und `BlockSeparators` fest.
	* Der Wert von `Auto` setzt diese Einstellungen auf der Grundlage des
	  Wertes der Voreinstellung "Sprache". Für einige Sprachen, wie
	  z.B. Spanisch, wird `,` in einigen Ländern und `.` in anderen
	  verwendet. In diesem Fall ist es am besten, die Sprache so einzustellen,
	  dass sie auch den Ländercode enthält (z. B. `es-es` oder `es-mx`), um
	  sicherzustellen, dass der richtige Wert verwendet wird.

* Schwedisch wurde zu den unterstützten Sprachen hinzugefügt.
* Es wurden weitere Unicode-Zeichen hinzugefügt, um sowohl alle
  Unicode-Zeichen, die als "Sm" gekennzeichnet sind, als auch diejenigen mit
  einer mathematischen Klasse (mit Ausnahme der Klassen Alphabetic und
  Glyph) in den Unicode-Standard aufzunehmen.
* Nachdem ich die Funktionsweise der Voreinstellungen in einer früheren
  Version geändert hatte, hatte ich vergessen, `MathRate` und `PauseFactor`
  in Zahlen und nicht in Strings zu ändern.
* Fehler in den Braille-Regeln behoben (verpasste Änderung von früher), wo
  ein drittes Argument hätte angegeben werden müssen, um zu sagen, dass in
  den _Braille_ `definitions.yaml`-Dateien und nicht in den Sprachdateien
  nachgeschaut werden soll, wenn der Wert einer Definition gesucht wird.
* Die Verwendung der Datei `definitions.yaml` wurde bereinigt.
* Einige Fehler in der MathML-Bereinigung für "," Dezimaltrennzeichen wurden
  behoben.
* Ich habe einen Fehler in der Braille-Hervorhebung gefunden, wenn nichts
  hervorgehoben ist (vielleicht passiert das nie, weshalb ich es in der
  Praxis nicht gesehen habe?)
* Der "Beschreibungs"-Modus wurde so korrigiert, dass er funktioniert - er
  ist immer noch sehr minimal und wahrscheinlich noch nicht nützlich
* Minimale unterstützte Version neu festgelegt

### Version 0.5.6
* Ein Dialogfeld für Kopieren als... zum MathCAT-Dialog hinzugefügt (im
  Bereich "Navigation").
* Ein Fehler wurde behoben, bei dem die Sprache beim Wechsel des Sprachstils
  auf Englisch zurückgesetzt wurde.
* Fehler bei der Navigation und in Braille behoben
* Einige Probleme mit den ASCIIMath-Abständen wurden behoben.
* Verbesserte Erkennung von chemischen Formeln
* MathCAT wurde auf die neue BANA-Nemeth-Chemie-Spezifikation aktualisiert
  (immer noch nur einzeilig und Änderungen der Schriftart/Schriftart für
  Sonderfälle werden nicht berücksichtigt)
* Behebung eines Absturzes, wenn Nicht-ASCII-Ziffern (z. B. fette Ziffern)
  in Zahlen verwendet werden
* Keine kursiven Indikatoren in Braille-Codes verwenden, wenn die
  mathematischen alphanumerischen kursiven Zeichen verwendet werden.
* Einige andere kleinere Fehlerbehebungen, die nicht von Benutzern gemeldet
  wurden

### Version 0.5.0
* Deutscher LaTeX-Braille-Code hinzugefügt. Im Gegensatz zu anderen
  Braille-Codes erzeugt dieser ASCII-Zeichen und verwendet die aktuelle
  Braille-Ausgabetabelle, um die Zeichen in Braille zu übersetzen.
* Ein (experimenteller) ASCIIMath-Braille-Code wurde hinzugefügt. Wie der
  LaTeX-Braille-Code erzeugt dieser ASCII-Zeichen und verwendet die aktuelle
  Braille-Ausgabetabelle, um die Zeichen in Braille zu übersetzen.
* Neue Einstellung "Kopieren als", die das Kopieren als MathML, LaTeX oder
  ASCIIMath mit cntl+C unterstützt, wenn der Fokus auf MathML liegt (wie
  zuvor). Der aktuell fokussierte Knoten wird kopiert. Hinweis: Diese
  Einstellung wird nur in der prefs.yaml-Datei aufgeführt und ist (noch)
  nicht im Dialogfeld für die MathCAT-Einstellungen sichtbar.

### Version 0.4.2
* Sprachumschaltung behoben, wenn die Stimme wechselt und die
  MathCAT-Sprache auf "Auto" eingestellt ist
* Weitere Überprüfungen für $Impairments hinzugefügt, um das Lesen zu
  verbessern, wenn es für Blinde nicht gesetzt ist
* Nemeth: Korrektur für "~", wenn es nicht Teil eines Mrows ist
* UEB: Zeichen hinzugefügt, "~"-Abstand korrigiert, wenn Präfix, xor
  korrigiert,
* MathML-Bereinigung für akzentuierte Vokale (hauptsächlich für
  Vietnamesisch)
* Umfassende Überarbeitung des Codes zum Lesen und Aktualisieren von
  Präferenzen mit großer Geschwindigkeitssteigerung -- Hinzufügen der
  Präferenz `CheckRuleFiles`, um zu kontrollieren, welche Dateien auf
  Aktualisierungen geprüft werden
* Zwei neue Interface-Aufrufe hinzugefügt -- ermöglicht das Setzen der
  Navigationsposition des Braille-Cursors (noch nicht Teil von MathCAT)

### Version 0.3.11
* Aktualisiert auf Python 3.11 und Überprüfung, ob es mit NVDA 2024.1
  kompatibel ist
* Behebung von Fehlern in Braille in Vietnamesisch und auch in der
  Sprachausgabe, vor allem für Chemie.
* Fehlerhafte Braille-Ausgaben korrigiert, wenn Braille-Code und abhängige
  Sprache nicht übereinstimmen (insbesondere vietnamesische Braille-Schrift
  und vietnamesische Sprache)
* Whitespace-Fehler in HTML innerhalb von Token behoben
* Verbesserung der Erkennung römischer Ziffern


### Version 0.3.9
* Übersetzung für traditionelles Chinesisch hinzugefügt (Dank an Hon-Jang
  Yang)
* Fehler beim Navigieren in die Basis eines geskripteten Ausdrucks mit
  Klammern behoben
* Die Art und Weise, wie Leerzeichen behandelt werden, wurde erheblich
  geändert. Dies betrifft vor allem die Braille-Ausgabe (Leerzeichen und
  Erkennung von "Auslassungen").
* Verbesserte Erkennung von chemischen Formeln
* UEB-Braille-Korrekturen, die sich aus dem Hinzufügen von Chemie-Beispielen
  ergeben haben
* UEB-Korrekturen für das Hinzufügen von Hilfsklammern in einigen Fällen


### Version 0.3.8

Braille:

* Das Dialogfeld wurde für mehrere Sprachen internationalisiert (vielen Dank
  an die Übersetzer!)
* Erstmalige Einführung von CMU - dem Braille-Code, der in spanisch- und
  portugiesischsprachigen Ländern verwendet wird
* Behebung einiger UEB-Fehler und Hinzufügen einiger UEB-Zeichen
* Signifikante Verbesserungen in Braille für Vietnamesisch

Weitere Korrekturen:

* Der Schieberegler des Dialogs "Relative Rate" hat nun einen Maximalwert
  von 100 % (jetzt können nur noch langsamere Raten eingestellt
  werden). Außerdem wurden Schrittgrößen hinzugefügt, damit es einfacher
  ist, die Rate deutlich zu erhöhen/verringern.
* Fehler mit der eSpeak behoben, der manchmal die Sprache abschnitt, wenn
  die relative Rate geändert wurde
* Verbesserungen der vietnamesischen Sprache
* Fehler bei den OneCore-Stimmen behoben, die "a" sagen
* Einige Navigationsfehler behoben, wenn "AutoZoomOut" auf "False" gesetzt
  ist (nicht der Standard)
* Die Aktualisierung von Änderungen bei den Sprachen und einigen anderen
  Änderungen bei Dialogfeldern wurde korrigiert, so dass sie sofort wirksam
  werden, wenn Sie auf "Übernehmen" oder "OK" klicken.
* Die Option "Sprache der Stimme verwenden" wurde hinzugefügt, so dass
  MathCAT von Anfang an in der richtigen Sprache spricht (wenn es eine
  Übersetzung gibt)
* Mehrere Verbesserungen zur Bereinigung von schlechtem MathML-Code

### Version 0.3.3
Diese Version enthält eine Reihe von Fehlerkorrekturen. Die wichtigsten
neuen Funktionen und Fehlerkorrekturen sind:

* Spanische Übersetzung hinzugefügt (Dank an Noelia Ruiz und María Allo
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

### Version 0.2.5
* Weitere Verbesserungen in Chemie
* Korrekturen für Nemeth:

	* Regeln für "Auslassungen" hinzugefügt
	* Einige Regeln für englische Sprachindikatoren hinzugefügt
	* Weitere Fälle, in denen der Mehrzweck-Indikator benötigt wird, wurden
	  hinzugefügt
	* Korrekturen im Zusammenhang mit Nemeth und Zeichensetzung

### Version 0.2
* Viele Fehlerkorrekturen
* Verbesserungen für die Sprachausgabe
* Eine Einstellung zur Steuerung der Dauer von Pausen (funktioniert mit
  Änderungen der relativen Sprechgeschwindigkeit für Mathematik)
* Unterstützung bei der Erkennung der chemischen Notation und deren
  korrekten Aussprache
* Übersetzungen ins Indonesische und Vietnamesische

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=mathcat
