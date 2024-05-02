# MathCAT #

* Autor: Neil Soiffer
* Compatibilidad con NVDA: 2018.1 o posterior (no probado en versiones
  anteriores)
* Descargar [versión estable][1]

MathCat está diseñado para sustituir eventualmente a MathPlayer, ya que este
último ya no está soportado. MathCat genera voz y braille desde MathML. La
voz producida por MathCat para las matemáticas se mejora con entonación para
que suene más natural. Se puede navegar por la voz con tres modos usando las
mismas órdenes que en MathPlayer. Además, el nodo de navegación se indica en
la pantalla Braille. Se soportan tanto Nemeth como UEB técnico.

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
* Quien necesite braille técnico UEB
* Quien quiera probar nuevas tecnologías y esté dispuesto a ayudar
  informando de fallos
* Quien use Eloquence como voz

Quién no debería usar MathCat:

* Cualquiera que use Math Player en idiomas distintos al inglés (existen
  traducciones a indonesio, vietnamita y español; las traducciones se irán
  haciendo en el futuro).
* Cualquiera que use MathPlayer con una salida braille sin Nemeth o UEB
  (contacta conmigo si quieres ayudar con una traducción braille)
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
Braille:

* Se ha internacionalizado el diálogo en varios idiomas (¡Muchas gracias a
  los traductores!)
* Implementación inicial de CMU, código braille usado en los países de habla
  hispana y portuguesa
* Se corrigen algunos fallos de UEB y se añaden algunos caracteres para UEB
* Mejoras importantes al braille vietnamita

Otras correcciones:

* Se cambia el deslizador del diálogo de velocidad relativa para que tenga
  un valor máximo del 100% (ahora sólo permite configurar velocidades
  menores). También se añaden pasos de tamaño para que sea más fácil
  aumentar o disminuir la velocidad significativamente.
* Se corrige un problema con Espeak que hacía que la voz se entrecortara al
  cambiar su velocidad relativa
* Mejoras en la voz vietnamita
* Corregido un fallo con las voces OneCore, que decían "a"
* Se corrigen algunos fallos de navegación cuando `AutoZoomOut` es falso (no
  el que hay por defecto)
* Se corrigen algunos cambios en los diálogos y en el idioma para que tengan
  efecto inmediato cuando se pulse "Aplicar" o "Aceptar".
* Se añade una opción "Usar idioma de la voz" para que MathCat hable en el
  idioma correcto desde el principio (si hay traducción)
* Varias mejoras al limpiar código MathML pobre

### Versión 0.3.3
Esta versión contiene bastantes correcciones de fallos. Las principales
funciones nuevas y correcciones son:

* Se ha añadido traducción al español (gracias a Noelia Ruiz y María Allo
  Roldán)
* Se modifica la navegación, de tal forma que ahora comienza ampliada en un
  nivel
* Se añade control+alt+flechas como mecanismo para navegar por estructuras
  tabulares. Estas teclas deberían ser más fáciles de memorizar, ya que se
  usan para navegar por tablas en NVDA.
* Corregido un fallo con las voces de Espeak que provocaba que se
  ralentizaran cuando la velocidad relativa matemática se configuraba para
  ser más lenta que la velocidad de verbalización del texto.
* Solucionado un problema con las voces OneCore, que deberían poder
  verbalizar el sonido de la 'a' larga.

Hay montones de pequeños retoques en la voz y algunos fallos corregidos en
Nemeth y UEB.

Nota: ahora hay una opción para obtener braille estándar vietnamita en la
salida braille. Este trabajo todavía está en progreso y tiene demasiados
fallos como para usarlo para otra cosa que no sean pruebas. Espero que la
próxima versión de MathCat contenga una implementación fiable.

### Versión 0.2.5
* Más mejoras en química
* Correcciones en Nemeth:

	* Añadidas reglas de "omisión"
	* Añadidas algunas reglas para los indicadores en inglés
	* Añadidos más casos donde es necesario el indicador Multipropósito
	* Correcciones relacionadas con Nemeth y la puntuación

### Versión 0.2
* Muchos fallos corregidos
* Mejoras en la voz
* Una opción en las preferencias para controlar la duración de las pausas
  (funciona con los cambios relativos de velocidad de la voz en matemáticas)
* Soporte para reconocer notación química y verbalizarla adecuadamente
* Traducciones al indonesio y al vietnamita

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=mathcat
