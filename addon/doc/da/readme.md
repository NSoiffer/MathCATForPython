# MathCAT #

* Forfatter: Neil Soiffer
* NVDA compatibility: 2018.1 or later (untested in earlier versions)
* Download [stabil version][1]

MathCAT er designet til at erstatte MathPlayer, fordi MathPlayer ikke
længere understøttes. MathCAT genererer tale og punkt fra MathML. Talen til
matematik produceret af MathCAT er forbedret med prosodi, så den lyder mere
naturlig. Talen kan navigeres i tre tilstande ved hjælp af de samme
kommandoer som MathPlayer. Derudover er navigationsknuden vist på et
punktdisplay. Både Nemeth og UEB teknisk understøttes.

MathCAT har en række konfigurationsmuligheder, der styrer tale, navigation
og punkt. Mange af disse kan indstilles i MathCAT-indstillingsdialogen
(findes i meNVDA-menuen>Opsætning). For mere information om disse
indstillinger, læs
[MathCAT-dokumentationen](https://nsoiffer.github.io/MathCAT/users.html).
Dokumentationen indeholder et link til [en tabel med alle
navigationskommandoer i
MathCAT](https://nsoiffer.github.io/MathCAT/nav-commands.html).

Bemærk: MathCAT er et generelt bibliotek til generering af tale og punkt fra
MathML. Dette bruges af andre lignende projekter udover NVDA. For
information om MathCAT-projektet, se
[MathCAT-dokumentationssiden](https://nsoiffer.github.io/MathCAT).


Hvem bør bruge MathCAT:

* Dem, der har brug for Nemeth-braille af høj kvalitet (MathPlayers Nemeth
  er baseret på liblouis' Nemeth-generation, som har en række væsentlige
  fejl, som er teknisk svære at rette).
* Dem, der har brug for UEB teknisk braille
* Dem, der ønsker at prøve den nyeste teknologi og er villige til at hjælpe
  ved at rapportere fejl
* Dem, der bruger Eloquence som stemme

Hvem bør IKKE bruge MathCAT:

* Enhver, der bruger MathPlayer med et andet sprog end engelsk
  (oversættelser findes til indonesisk og vietnamesisk; oversættelser er
  sandsynlige i fremtiden)
* Enhver, der bruger MathPlayer med et ikke-Nemeth/ikke-UEB brailleoutput
  (kontakt mig, hvis du vil hjælpe med en brailleoversættelse)
* Enhver, der foretrækker Access8Math frem for MathPlayer (til tale eller
  andre funktioner)

MathCATs regler for tale er endnu ikke så omfattende som MathPlayers regler
- det kan være endnu en grund til at holde sig til MathPlayer. MathCAT
bliver brugt som et testbed for ideer til MathML 4, der gør det muligt for
forfattere at udtrykke deres hensigt, så tvetydige notationer kan læses
korrekt og ikke gættes på. Jeg har holdt op med at tilføje for mange regler,
da arkitekturen i MathCAT er centreret omkring brug og udledning af
forfatterens hensigt, og disse er ikke helt afklarede endnu.

## MathCAT Update Log

### Version 0.2
* Masser af fejlrettelser
* Forbedringer af tale
* En præferenceindstilling til at kontrollere varigheden af pause (fungerer
  med ændringer af relativ talehastighed for matematik)
* Støtte til at genkende keminotation og tale den korrekt
* Oversættelser til indonesisk og vietnamesisk


### Version 0.2.5
* Flere forbedringer kemi
* Rettelser til Nemeth:

	* Added "omission" rules
	* Added some rules for English Language Indicators
	* Added more cases where the Mulitpurpose indicator is needed
	* Fixes related to Nemeth and punctuation


### Version 0.3.3
Denne udgivelse indeholder en række fejlrettelser. De vigtigste nye
funktioner og fejlrettelser er:

* Tilføjet spansk oversættelse (tak til Noelia Ruiz og María Allo Roldán)
* Ændret navigation, så den begynder at zoome i ét niveau
* Tilføjet cntrl+alt+pil som en måde at navigere i tabelstrukturer på. Disse
  taster burde være mere mindeværdige, fordi de bruges til tabelnavigation i
  NVDA.
* Virkede uden om NVDA-fejl for eSpeak-stemmer, der fik dem til at sænke
  farten, når den relative MathRate var indstillet til at være langsommere
  end teksttalehastigheden.
* Arbejdet med et OneCore-stemmeproblem, så de vil sige den lange 'a'-lyd.

Der er masser af små justeringer af talen og nogle fejlrettelser til både
Nemeth og UEB.

Bemærk: der er nu en mulighed for at få Vietnams braillestandard som
brailleoutput. Dette er stadig et igangværende arbejde og er for buggy til
at blive brugt andet end til test. Jeg forventer, at den næste
MathCAT-udgivelse vil indeholde en pålidelig implementering.

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
