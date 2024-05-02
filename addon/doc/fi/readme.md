# MathCAT #

* Tekijä: Neil Soiffer
* Yhteensopivuus: NVDA 2018.1 tai uudempi (ei testattu aiemmissa versioissa)
* Lataa [vakaa versio][1]

MathCAT on suunniteltu korvaamaan lopulta MathPlayerin, koska sitä ei enää
tueta. MathCAT luo MathML:stä puhetta ja pistekirjoitusta. MathCATin
tuottamaa matemaattista puhetta on paranneltu prosodialla, jotta se
kuulostaa luonnollisemmalta. Puhetta voidaan navigoida kolmessa eri tilassa
samoilla komennoilla kuin MathPlayerissa. Navigointisolmu näkyy lisäksi
pistenäytöllä. Sekä Némethiä että UEB:tä tuetaan.

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
* Käyttäjien, jotka tarvitsevat teknistä UEB-pistekirjoitusta.
* Käyttäjien, jotka haluavat kokeilla uusinta teknologiaa ja ovat valmiita
  auttamaan ilmoittamalla bugeista.
* Käyttäjien, jotka käyttävät puhesyntetisaattorina Eloquencea.

Kenen EI tulisi käyttää MathCATia:

* Kaikkien, jotka käyttävät MathPlayeria muulla kuin englannin kielellä
  (indonesian- ja vietnaminkieliset käännökset ovat käytettävissä, muita
  käännöksiä on tulossa myöhemmin).
* Kaikkien, jotka käyttävät MathPlayeria muulla kuin
  Nemeth/UEB-pistekirjoituksella (ota yhteyttä, jos haluat auttaa
  pistekirjoituskäännöksen tekemisessä).
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

### Versio 0.5.0
* Lisätty saksalainen LaTeX-pistekirjoitusmerkistö. Toisin kuin muut
  pistekirjoitusmerkistöt, tämä muodostaa ASCII-merkkejä ja käyttää
  senhetkistä pistetulostustaulukkoa merkkien kääntämiseen
  pistekirjoitukseksi.
* Lisätty kokeellinen ASCIIMath-pistekirjoitusmerkistö. Kuten
  LaTeX-merkistö, tämä muodostaa ASCII-merkkejä ja  käyttää senhetkistä
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
* Nemeth: Korjaus "~":lle, kun se ei ole osa mrow:ta.
* UEB: Merkkejä lisätty, "~":n välilyönnin korjaus jos etuliitteenä,
  xor-korjaus.
* MathML:n siistiminen korostetuille vokaaleille (pääasiassa
  vietnamilaisille).
* Huomattava uudelleenkirjoitus asetusten lukemis- ja päivityskoodille
  suurella nopeutuksella – lisätty ``CheckRuleFiles``-asetus säätelemään,
  mitkä tiedostot tarkistetaan päivitysten varalta.
* Added two new interface calls -- enables setting the navigaton location
  from the braille cursor (not part of MathCAT addon yet)

### Versio 0.3.11
* Upgraded to python 3.11 and verified working with NVDA 2024.1
* Fix bugs in Vietnamese braille and also in Speech, mostly for chemistry.
* Fix broken braille when braille code and dependent language don't match
  (specifically Vietnam braille and Vietnamese speech)
* Fix whitespace bug in HTML inside of tokens
* Improve roman numeral detection

### Versio 0.3.9
* Added Traditional Chinese translation (thanks to Hon-Jang Yang)
* Fixed bug with navigating into the base of a scripted expression that has
  parenthesis
* Significantly changed the way whitespace is handled. This mainly affects
  braille output (spaces and "omission" detection).
* Kemiallisten merkintöjen tunnistusta paranneltu
* UEB braille fixes that came up from adding chemistry examples
* UEB fixes for adding auxillary parenthesis in some cases

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
* Fix eSpeak bug that sometimes cut off speech when the relative rate was
  changed
* Parannuksia vietnaminkieliseen puheeseen
* Korjattu OneCore-äänien bugi, joka sai ne sanomaan "a"
* Korjattu navigoinnin bugeja, joita esiintyi kun automaattinen
  loitontaminen ei ole käytössä (ei oletuksena)
* Korjattu kielen vaihtamisen ja muutaman muun valintaikkunan muutosten
  päivittämistä siten, että muutokset tulevat voimaan heti Käytä- tai
  OK-painiketta painettaessa.
* Added an "Use Voice's Language" option so that out of the box, MathCAT
  will speak in the right language (if there is a translation)
* Several improvements for cleaning up poor MathML code

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

	* Lisätty "jättösääntöjä"
	* Lisätty sääntöjä englannin kielen ilmaisimille
	* Lisätty enemmän tapauksia, joissa monitoimi-ilmaisinta tarvitaan
	* Nemeth-merkintöihin ja välimerkkeihin liittyviä korjauksia

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
