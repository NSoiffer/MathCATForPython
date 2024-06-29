# MathCAT #

* Tekijä: Neil Soiffer
* Yhteensopivuus: NVDA 2018.1 tai uudempi (ei testattu aiemmissa versioissa)
* Lataa [vakaa versio][1]

MathCAT is designed to eventually replace MathPlayer because MathPlayer is
no longer supported. MathCAT generates speech and braille from MathML. The
speech for math produced by MathCAT is enhanced with prosody so that it
sounds more natural. The speech can be navigated in three modes using the
same commands as MathPlayer. In addition, the navigation node is indicated
on a braille display. Both Nemeth and UEB technical are supported.

MathCATissa on useita asetusvaihtoehtoja, jotka ohjaavat puhetta,
navigointia ja pistekirjoitusta. Monia näistä voidaan määrittää MathCATin
asetusvalintaikkunassa (löytyy NVDA:n Asetukset-valikosta). Lisätietoja saat
[MathCATin
dokumentaatiosta](https://nsoiffer.github.io/MathCAT/users.html).
Dokumentaatiossa on linkki [taulukkoon, jossa luetellaan kaikki MathCATin
navigointikomennot](https://nsoiffer.github.io/MathCAT/nav-commands.html).

MathCAT on yleiskirjasto, joka tuottaa puhetta ja pistekirjoitusta
MathML-muodosta. Sitä käytetään NVDA:n lisäksi myös muissa
apuvälineteknologisissa projekteissa. Yleistä tietoa MathCAT-projektista on
[MathCATin dokumentaatiosivulla](https://nsoiffer.github.io/MathCAT).


Kenen tulisi käyttää MathCATia:

* Käyttäjien, jotka tarvitsevat korkealaatuista Nemeth-pistekirjoitusta
  (MathPlayerin Nemeth perustuu liblouisin Nemeth-sukupolveen, jossa on
  useita merkittäviä bugeja, joita on teknisesti vaikea korjata).
* Those who need UEB technical braille, CMU (Spanish/Portuguese), German
  LaTeX, ASCIIMath, or Vietnamese braille
* Käyttäjien, jotka haluavat kokeilla uusinta teknologiaa ja ovat valmiita
  auttamaan ilmoittamalla bugeista
* Käyttäjien, jotka käyttävät puhesyntetisaattorina Eloquencea

Kenen EI tulisi käyttää MathCATia:

* Anyone who uses MathPlayer with a language that is not yet supported by
  MathCAT (translations exist for Chinese (Traditional), Spanish, Indonesian
  and Vietnamese; translations will be coming in the future) and are not
  comfortable with speech in one of the supported languages.
* Kaikkien, jotka pitävät enemmän Access8Mathista kuin MathPlayerista
  (puheen tai muiden ominaisuuksien vuoksi).

MathCATin puhesäännöt eivät ole vielä yhtä kattavia kuin MathPlayerissa
(tämä voi olla toinen syy MathPlayerissa pysymiseen). MathCATia käytetään
MathML 4 -ideoiden testausalustana, jonka avulla tekijät voivat ilmaista
tarkoituksensa, jotta moniselitteiset merkinnät voidaan puhua oikein eikä
arvailla. Olen viivytellyt liian monien sääntöjen lisäämistä, koska
MathCATin arkkitehtuuri keskittyy käyttöön ja tekijän tarkoituksen
päättelemiseen, eikä niitä ole vielä täysin ratkaistu.

## MathCATin päivitysloki

### Version 0.6.3

* All the language and braille Rule files are zipped up per directory and
  unzipped on demand.

	* This currently saves ~5mb when Rules.zip is unzipped, and will save even
	  more as more languages and braille codes are added.
	* This is in preparation for MathCAT being built into NVDA 2024.3

* Added new preference `DecimalSeparator`.

	* The default value is `Auto`, with other values being ".", ",", and
	  "Custom". The first three values set `DecimalSeparators` and
	  `BlockSeparators`.
	* `Auto` sets those preferences based on the value of the `Language`
	  pref. For some language such as Spanish, `,` is used in some countries
	  and `.` is used in others. In this case, it is best to set the language
	  to also include the country code (e.g, `es-es` or `es-mx`) to ensure the
	  right value is used.

* Added Swedish to supported languages.
* Added more Unicode chars to include both all Unicode chars marked as "Sm"
  and those with a mathclass (except Alphabetic and Glyph classes) in the
  Unicode standard.
* After changing how prefs work in a previous version, I forgot to change
  `MathRate` and `PauseFactor` to be numbers, not strings.
* Fixed bug in the braille Rules (missed change from earlier) where a third
  argument should have been given to say to look in the _Braille_
  `definitions.yaml` files and not the speech ones when looking up the value
  of a definition.
* Cleaned up use of `definitions.yaml`.
* Fixed some bugs in the MathML cleanup for "," decimal separators.
* Found a bug in braille highlighting when nothing is highlighted (maybe
  never happens which is why I didn't see it in practice?)
* Fixed "Describe" mode so that it works -- it is still very minimal and
  probably not useful yet
* Fixed minimum supported version

### Version 0.5.6
* Added Copy As... to the MathCAT dialog (in the "Navagation" pane).
* Fixed a bug where the language reverted to English when changing speech
  styles.
* Fixed a bug with navigation and braille
* Fixed some Asciimath spacing problems.
* Improved chemistry recognition
* Updated MathCAT to new BANA Nemeth chemistry spec (still only single line
  and special case style/font changes not handled)
* Fix a crash when non-ASCII digits (e.g., bold digits) are used in numbers
* Don't use italic indicators in braille codes when the math alphanumeric
  italic chars are used
* Some other smaller bug fixes that weren't reported by users

### Versio 0.5.0
* Lisätty saksalainen LaTeX-pistekirjoitusmerkistö. Toisin kuin muut
  pistekirjoitusmerkistöt, tämä tuottaa ASCII-merkkejä ja käyttää
  senhetkistä pistetulostustaulukkoa merkkien kääntämiseen
  pistekirjoitukseksi.
* Lisätty kokeellinen ASCIIMath-pistekirjoitusmerkistö. Kuten
  LaTeX-merkistö, tämäkin tuottaa ASCII-merkkejä ja  käyttää senhetkistä
  pistetulostustaulukkoa merkkien kääntämiseen pistekirjoitukseksi.
* Lisätty "CopyAs"-asetus, joka tukee kopiointia MathML-, LaTeX- tai
  ASCIIMath-muodossa Ctrl+C-näppäinkomentoa käyttäen kohdistuksen ollessa
  MathML:ssä (kuten aiemmin). Aktiivisena oleva solmu kopioidaan. Huom:
  Asetus on toistaiseksi muutettavissa vain prefs.yaml-tiedostossa eikä sitä
  vielä näytetä MathCATin asetusvalintaikkunassa.

### Versio 0.4.2
* Korjattu kielen vaihtaminen kun puheääni vaihtuu ja MathCATin kielenä on
  "Automaattinen"
* Lisätty tarkistuksia $Impairments-muuttujalle lukemisen parantamiseksi
  silloin, kun se on määritetty muita kuin sokeita varten.
* Nemeth: Korjaus "~":lle, kun se ei ole osa mrow:ta
* UEB: Merkkejä lisätty, "~":n välilyönnin korjaus jos etuliitteenä,
  xor-korjaus
* MathML:n siistiminen korostetuille vokaaleille (pääasiassa
  vietnamilaisille).
* Suuri osa asetusten luku- ja päivityskoodista kirjoitettu uudestaan, mikä
  nopeutti koodia huomattavasti – lisätty ``CheckRuleFiles``-asetus
  säätelemään, mitkä tiedostot tarkistetaan päivitysten varalta
* Lisätty kaksi uutta rajapintakutsua: mahdollistaa navigointisijainnin
  asettamisen pistekohdistimesta (ei vielä osa MathCAT-lisäosaa)

### Versio 0.3.11
* Päivitetty python versioksi 3.11 ja varmistettu toimivuus NVDA 2024.1:n
  kanssa
* Korjattu pääasiassa kemiaan liittyviä bugeja vietnaminkielisessä
  pistekirjoituksessa ja puheessa.
* Korjattu rikkoutuva pistekirjoitus, kun pistemerkistö ja siihen liittyvä
  kieli eivät täsmää (erityisesti Vietnamilainen pistekirjoitus ja puhe)
* Korjattu tyhjän tilan bugi HTML:n sisällä olevissa merkeissä
* Paranneltu roomalaisten numeroiden tunnistusta


### Versio 0.3.9
* Lisätty perinteisen kiinan käännös (kiitos Hon-Jang Yangille)
* Korjattu bugi navigoitaessa skriptatun lausekkeen sulkeita sisältävään
  perusosaan
* Muutettu merkittävästi tapaa, jolla tyhjätilaa käsitellään. Tämä vaikuttaa
  pääasiassa pistekirjoitustulosteeseen (välilyönnit ja "jättämisen"
  havaitseminen).
* Kemiallisten merkintöjen tunnistusta paranneltu
* Tehty UEB-pistekirjoituksen korjauksia, joiden tarve ilmeni kemiallisten
  kaavojen esimerkkejä lisättäessä
* Korjauksia UEB:lle apusulkeita lisättäessä joissakin tapauksissa


### Versio 0.3.8

Pistekirjoitus:

* Valintaikkuna on käännetty useille kielille (kiitokset kääntäjille!)
* Alustava toteutus Espanjassa ja useissa portugalinkielisissä maissa
  käytettävälle CMU-pistekirjoitusmerkistölle
* Korjattu UEB:n bugeja ja lisätty merkkejä
* Merkittäviä parannuksia vietnamilaiseen pistekirjoitukseen

Muita korjauksia:

* Muutettu suhteellisen nopeuden liukusäädintä siten, että sen enimmäisarvo
  on 100 % (sallii nyt vain hitaampien nopeuksien asettamisen). Lisätty myös
  askelkokoja, jotta nopeuden merkittävä nostaminen/laskeminen olisi
  helpompaa.
* Korjattu eSpeakin bugi, joka katkaisi toisinaan puheen, kun suhteellista
  nopeutta muutettiin
* Parannuksia vietnaminkieliseen puheeseen
* Korjattu OneCore-äänien bugi, joka sai ne sanomaan "a"
* Korjattu navigoinnin bugeja, joita esiintyi kun automaattinen
  loitontaminen ei ole käytössä (ei oletuksena)
* Korjattu kielen vaihtamisen ja muutaman muun valintaikkunan muutosten
  päivittämistä siten, että muutokset tulevat voimaan heti Käytä- tai
  OK-painiketta painettaessa.
* Lisätty "Käytä äänen kieltä" -asetus, jotta MathCAT puhuu oletusarvoisesti
  oikealla kielellä (jos käännös on saatavilla)
* Useita parannuksia huonon MathML-koodin siistimiseksi

### Versio 0.3.3
Tähän versioon on tehty useita bugikorjauksia. Merkittävimpiä uusia
ominaisuuksia ja bugikorjauksia ovat:

* Lisätty espanjankielinen käännös (kiitos Noelia Ruizille ja María Allo
  Roldánille)
* Muutettu navigointia siten, että se alkaa zoomattuna yhden tason lähemmäs
* Lisätty Ctrl+Alt+Nuolinäppäimet taulukkomaisissa rakenteissa
  navigoimiseen. Näiden näppäinyhdistelmien pitäisi olla helpommin
  muistettavat, koska niitä käytetään NVDA:ssa taulukkonavigointiin.
* Korjattu eSpeak-äänien NVDA-bugi, joka aiheutti niiden hidastumisen, kun
  suhteellinen matematiikkapuheen nopeus oli asetettu tekstipuheen nopeutta
  hitaammaksi.
* Tähän on tehty useita bugikorjauksia. Merkittävimmät uudet ominaisuudet ja
  bugikorjaukset ovat: * Lisätty espanjankielinen käännös (kiitos Noelia
  Ruizille ja María Allo Roldánille)  * Muutettu navigointia siten, että se
  alkaa zoomattuna yhden tason lähemmäs * Lisätty Ctrl+Alt+Nuolinäppäimet
  taulukkomaisissa rakenteissa navigoimiseen. Näiden näppäinyhdistelmien
  pitäisi olla helpommin muistettavat, koska niitä käytetään NVDA:ssa
  taulukkonavigointiin. * Korjattu eSpeak-äänien NVDA-bugi, joka aiheutti
  niiden hidastumisen, kun suhteellinen matematiikkapuheen nopeus oli
  asetettu tekstipuheen nopeutta hitaammaksi. * Korjattu OneCore-ääniä
  koskeva ongelma, jotta ne lausuisivat pitkän a-äänteen.

Paljon pieniä hienosäätöjä puheeseen ja bugikorjauksia sekä Nemethiin että
UEB:hen.

Huom: Nyt on käytettävissä vaihtoehto, jolla saa vietnamilaisen
pistekirjoitusstandardin pistekirjoituksen tuottamiseen. Tämä on edelleen
keskeneräinen ja liian virhealtis käytettäväksi muuhun kuin
testaamiseen. Seuraavassa MathCATin versiossa pitäisi jo olla luotettava
toteutus.

### Versio 0.2.5
* Lisää parannuksia kemiallisiin merkintöihin
* Korjauksia Nemeth-merkintöihin:

	* Added "omission" rules
	* Added some rules for English Language Indicators
	* Added more cases where the Mulitpurpose indicator is needed
	* Fixes related to Nemeth and punctuation

### Versio 0.2
* Paljon bugikorjauksia
* Parannuksia puheeseen
* Asetus tauon keston säätämiseen (toimii matematiikkapuheen suhteellisen
  nopeuden muutosten kanssa)
* Tuki kemiallisten merkintöjen tunnistamiselle ja niiden asianmukaiselle
  puhumiselle
* Käännökset indonesiaksi ja vietnamiksi

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=mathcat
