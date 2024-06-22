# MathCAT #

* Autor: Neil Soiffer
* Compatibilidad con NVDA: 2018.1 o posterior (no probado en versiones
  anteriores)
* Descargar [versión estable][1]

MathCAT is designed to eventually replace MathPlayer because MathPlayer is
no longer supported. MathCAT generates speech and braille from MathML. The
speech for math produced by MathCAT is enhanced with prosody so that it
sounds more natural. The speech can be navigated in three modes using the
same commands as MathPlayer. In addition, the navigation node is indicated
on a braille display. Both Nemeth and UEB technical are supported.

MathCat tiene varias opciones de configuración que controlan la voz, la
navegación y el braille. Muchas de ellas pueden configurarse en el diálogo
de opciones de MathCat (en el menú Preferencias de NVDA). Para más
información sobre estos ajustes, consulta la [documentación de
MathCat](https://nsoiffer.github.io/MathCAT/users.html).  La documentación
incluye un enlace a [una tabla que enumera todas las órdenes de navegación
de MathCat](https://nsoiffer.github.io/MathCAT/nav-commands.html).

Nota: MathCat es una biblioteca general para generar voz y braille a partir
de MathML. Es usada por otros proyectos de tecnologías de asistencia además
de NVDA. Para información general sobre el proyecto MathCat, consulta la
[página principal de documentación de
MathCat](https://nsoiffer.github.io/MathCAT).


Quién debería usar MathCat:

* Quien necesite Braille Nemeth de alta calidad (el Nemeth de MathPlayer se
  basa en la generación Nemeth de Liblouis, que tiene una importante
  cantidad de fallos técnicamente complicados de corregir).
* Those who need UEB technical braille, CMU (Spanish/Portuguese), German
  LaTeX, ASCIIMath, or Vietnamese braille
* Quien quiera probar nuevas tecnologías y esté dispuesto a ayudar
  informando de fallos
* Quien use Eloquence como voz

Quién no debería usar MathCat:

* Anyone who uses MathPlayer with a language that is not yet supported by
  MathCAT (translations exist for Chinese (Traditional), Spanish, Indonesian
  and Vietnamese; translations will be coming in the future) and are not
  comfortable with speech in one of the supported languages.
* Cualquiera que prefiera Access8Math a MathPlayer (por la voz u otras
  funciones)

Las reglas del habla de MathCat no son todavía tan extensas como las de
MathPlayer -- esa puede ser otra razón para seguir con MathPlayer. MathCat
se está usando como un banco de pruebas para MathML 4, que permite a los
autores expresar su intención de tal forma que las notaciones ambiguas se
verbalicen correctamente sin tener que adivinarlas. Me he esperado antes de
añadir muchas reglas, ya que la arquitectura de MathCat se centra en usar e
inferir la intención del autor, y esto aún no está completamente
establecido.

## Registro de actualización de MathCat

### Version 0.6.3
* All the language and braille Rule files are zipped up per directory and unzipped on demand.
  * This currently saves ~5mb when Rules.zip is unzipped, and will save even more as more languages and braille codes are added.
  * This is in preparation for MathCAT being built into NVDA 2024.3
* Added new preference `DecimalSeparator`.
  * The default value is `Auto`, with other values being ".", ",", and "Custom". The first three values set `DecimalSeparators` and `BlockSeparators`.
  * `Auto` sets those preferences based on the value of the `Language` pref. For some language such as Spanish, `,` is used in some countries and `.` is used in others. In this case, it is best to set the language to also include the country code (e.g, `es-es` or `es-mx`) to ensure the right value is used.
* Added Swedish to supported languages.
* Added more Unicode chars to include both all Unicode chars marked as "Sm" and those with a mathclass (except Alphabetic and Glyph classes) in the Unicode standard.
* After changing how prefs work in a previous version, I forgot to change `MathRate` and `PauseFactor` to be numbers, not strings.
* Fixed bug in the braille Rules (missed change from earlier) where a third argument should have been given to say to look in the _Braille_ `definitions.yaml` files and not the speech ones when looking up the value of a definition.
* Cleaned up use of `definitions.yaml`.
* Fixed some bugs in the MathML cleanup for "," decimal separators.
* Found a bug in braille highlighting when nothing is highlighted (maybe never happens which is why I didn't see it in practice?)
* Fixed "Describe" mode so that it works -- it is still very minimal and probably not useful yet
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

### Versión 0.5.0
* Se añade código braille LaTeX en alemán. Al contrario que otros códigos
  braille, este genera caracteres ASCII y usa la tabla de salida braille
  actual para transcribirlos.
* Se añade código braille ASCIIMath (experimental). Al igual que el código
  braille LaTeX, genera caracteres ASCII y usa la tabla braille de salida
  actual para transcribirlos.
* Se añade la preferencia "CopyAs", que soporta copiar como MathML, LaTeX o
  ASCIIMath usando control+c cuando el foco está sobre contenido MathML
  (como antes). El nodo que tiene el foco se copia. Nota: esto sólo se lista
  en el archivo prefs.yaml y no se expone en el diálogo de preferencias de
  MathCat (todavía).

### Versión 0.4.2
* Se corrige el cambio de idioma cuando los cambios de voz y el idioma de
  MathCat se configuran en "Automático"
* Se añaden más comprobaciones de impedimentos para mejorar la lectura
  cuando no está configurada para personas ciegas
* Nemeth: corrección de "~" cuando no es parte de un mrow
* UEB: se añaden caracteres, corrección de espaciado en "~", prefijo if,
  prefijo xor,
* Limpieza de MathML en vocales acentuadas (principalmente en vietnamita)
* Reescritura importante del código que lee y actualiza las preferencias con
  mucha más celeridad. Se añade la preferencia `CheckRuleFiles` para
  controlar para qué archivos se buscan actualizaciones
* Se añaden dos nuevas llamadas de interfaz que permiten configurar la
  posición de navegación a partir del cursor braille (todavía no forman
  parte del complemento MathCat)

### Versión 0.3.11
* Se actualiza a Python 3.11 y se comprueba el funcionamiento en NVDA 2024.1
* Se corrigen fallos en el braille y la voz vietnamitas, en su mayoría de
  química.
* Se corrige un fallo en braille cuando el código braille y el idioma
  dependiente no coinciden (concretamente, braille vietnamita y voz
  vietnamita)
* Se corrige un fallo con los espacios en blanco en HTML dentro de los
  tokens
* Se mejora la detección de números romanos


### Versión 0.3.9
* Se añade traducción al chino tradicional (gracias a Hon-Jang Yang)
* Se corrige un fallo con la navegación en la base de una expresión escrita
  que tiene paréntesis
* Ha cambiado significativamente el manejo de los espacios en
  blanco. Principalmente afecta a la salida braille (espacios y detección de
  "omisión").
* Mejorado el reconocimiento de química
* Correcciones en el braille UEB que aparecieron al añadir ejemplos de
  química
* Correcciones en UEB al añadir paréntesis auxiliares en algunos casos


### Versión 0.3.8
Braille: * Dialog has been internationalized for several languages (many
thanks to the translators!)  * Initial implementation of CMU -- the braille
code used in Spanish and Portuguese speaking countries * Fix some UEB bugs
and added some characters for UEB * Significant improvements to Vietnamese
braille

Other fixes: * Change relative rate dialog slider to have a maximum value of
100% (now only allows setting slower rates). Also, added step sizes so it is
easier to raise/lower the rate significantly.  * Fix eSpeak bug that
sometimes cut off speech when the relative rate was changed * Improvements
to Vietnamese speech * Fixed bug with OneCore voices saying "a" * Fixed some
navigation bugs when `AutoZoomOut` is False (not the default)  * Fix
updating around language changes and some other dialog changes so they take
effect immediately upon clicking "Apply" or "OK".  * Added an "Use Voice's
Language" option so that out of the box, MathCAT will speak in the right
language (if there is a translation)  * Several improvements for cleaning up
poor MathML code

### Versión 0.3.3
This release has a number of bug fixes in it. The major new features and bug
fixes are: * Added Spanish Translation (thanks to Noelia Ruiz and María Allo
Roldán)  * Modified navigation so that it starts zoomed in one level * Added
cntrl+alt+arrow as a way to navigate tabular structures. These keys should
be more memorable because they are used for table navigation in NVDA.  *
Worked around NVDA bug for eSpeak voices that caused them to slow down when
the relative MathRate was set to be slower than the text speech rate.  *
Worked around a OneCore voice problem so that they will speak the long 'a'
sound.

Hay montones de pequeños retoques en la voz y algunos fallos corregidos en
Nemeth y UEB.

Nota: ahora hay una opción para obtener braille estándar vietnamita en la
salida braille. Este trabajo todavía está en progreso y tiene demasiados
fallos como para usarlo para otra cosa que no sean pruebas. Espero que la
próxima versión de MathCat contenga una implementación fiable.

### Versión 0.2.5
* Más mejoras en química
* Correcciones en Nemeth:
* * Added "omission" rules
* * Added some rules for English Language Indicators
* * Added more cases where the Mulitpurpose indicator is needed
* * Fixes related to Nemeth and punctuation

### Versión 0.2
* Muchos fallos corregidos
* Mejoras en la voz
* Una opción en las preferencias para controlar la duración de las pausas
  (funciona con los cambios relativos de velocidad de la voz en matemáticas)
* Soporte para reconocer notación química y verbalizarla adecuadamente
* Traducciones al indonesio y al vietnamita

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=mathcat
