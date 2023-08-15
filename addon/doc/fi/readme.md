# MathCAT #

* Tekijä: Neil Soiffer
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

### Versio 0.2
* Paljon bugikorjauksia
* Parannuksia puheeseen
* Asetus tauon keston säätämiseen (toimii matematiikkapuheen suhteellisen
  nopeuden muutosten kanssa)
* Tuki kemiallisten merkintöjen tunnistamiselle ja niiden asianmukaiselle
  puhumiselle
* Käännökset indonesiaksi ja vietnamiksi


### Versio 0.2.5
* Lisää parannuksia kemiallisiin merkintöihin
* Korjauksia Nemeth-merkintöihin:
* * Lisätty "jättösääntöjä"
* * Lisätty sääntöjä englannin kielen ilmaisimille
* * Lisätty enemmän tapauksia, joissa monitoimi-ilmaisinta tarvitaan
* * Nemeth-merkintöihin ja välimerkkeihin liittyviä korjauksia


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

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=mathcat
