# MathCAT #

* Auteur : Neil Soiffer
* Compatibilité NVDA : 2018.1 ou version ultérieure (non testée dans les
  versions antérieures)
* Télécharger [version stable][1]

MathCAT est conçu pour éventuellement remplacer MathPlayer, car ce dernier
n'est plus pris en charge. MathCAT génère la parole et le braille à partir
de  MathML. La parole produite par MathCAT pour les mathématiques est
améliorée avec intonation afin qu'elle semble plus naturelle. Vous pouvez
naviguer dans la parole de trois façons en utilisant les mêmes commandes que
dans MathPlayer. De plus, le nœud de navigation est indiqué sur l'afficheur
braille. Nemeth et UEB technique sont pris en charge.

MathCAT a un certain nombre d'options de configuration qui contrôlent la
parole, la navigation et le braille. Beaucoup d'entre eux peuvent être
définis dans la boîte de dialogue des paramètres MathCAT (qui se trouve dans
le menu Préférences de NVDA). Pour plus d'informations sur ces paramètres,
consultez la [documentation
MathCAT](https://nsoiffer.github.io/mathcat/users.html). La documentation
comprend un lien vers [une table répertoriant toutes les commandes de
navigation dans
MathCAT](https://nsoiffer.github.io/MathCAT/nav-commands.html).

Remarque : MathCAT est une bibliothèque générale pour générer la parole et
le braille à partir de MathML. Il est utilisé par d'autres dans des projets
en plus de NVDA. Pour plus d'informations sur le projet MathCAT en général,
consultez la principale [page de documentation de
MathCAT](https://nsoiffer.github.io/MathCAT).


Qui devrait utiliser MathCAT :

* Ceux qui ont besoin de Nemeth Braille de haute qualité (Nemeth de
  MathPlayer est basé sur la génération Nemeth de liblouis qui a un certain
  nombre de bogues importants qui sont techniquement difficiles à corriger).
* Ceux qui ont besoin d'un braille technique UEB
* Ceux qui veulent essayer les dernières technologies et sont prêts à aider
  en signalant des bogues
* Ceux qui utilisent Eloquence comme voix

Qui ne devrait pas utiliser MathCAT :

* Quiconque utilise MathPlayer avec une langue non anglaise (des traductions
  existent pour les langues indonésiennes et vietnamiennes ; des traductions
  arrivent dans le futur)
* Quiconque utilise MathPlayer avec une sortie en braille sans Nemeth / sans
  UEB (contactez-moi si vous souhaitez vous aider avec une traduction en
  braille)
* Quiconque préfère Access8Math à MathPlayer (pour la parole ou d'autres
  fonctionnalités)

Les règles de la parole de MathCAT ne sont pas encore aussi étendues que
celles de MathPlayer - cela peut être une autre raison de continuer avec
MathPlayer. MathCAT est utilisé comme banque de test pour MathML 4, ce qui
permet aux auteurs d'exprimer leur intention afin que les notations ambiguës
soient verbalisées correctement sans avoir à les deviner. J'ai attendu avant
d'ajouter de nombreuses règles, car l'architecture de MathCAT se concentre
sur l'utilisation et la déduction de l'intention de l'auteur, et ce n'est
pas encore complètement établi.

## Mise à jour du Journal de MathCAT

### Version 0.2
* Beaucoup de correctifs de bogues
* Améliorations de la parole
* Un paramètre de préférence pour contrôler la durée de la pause (fonctionne
  avec le changement du débit relatif de la parole pour les mathématiques)
* Prise en charge de la reconnaissance de la notation chimique et à la
  verbaliser de manière appropriée
* Traductions vers indonésien et vietnamien


### Version 0.2.5
* Plus d'améliorations chimique
* Correction pour Nemeth :

	* Règles "omission" ajoutées
	* Ajout de quelques règles pour les indicateurs de langue Anglaise
	* Ajout de plus de cas où l'indicateur polyvalent est nécessaire
	* Correction liée à Nemeth et à la ponctuation


### Version 0.3.3
Cette version contient un certain nombre de corrections de bogues. Les
nouvelles fonctionnalités et correctifs de bogues sont :

* Ajout de la traduction en espagnol (grâce à Noelia Ruiz et María Allo
  Roldán)
* Navigation modifiée afin qu'elle démarre le zoom sur un niveau
* Ajout de ctrl+alt+flèche comme moyen de naviguer sur les structures
  tabulaires. Ces touches doivent être plus mémorables car elles sont
  utilisées pour la navigation de tableau dans NVDA.
* Travaillé autour du bogue de NVDA pour les voix eSpeak qui les ont amenés
  à ralentir lorsque le relatif MathRate  a été mis plus lentement que le
  débit de la parole de texte.
* Travaillé autour d'un problème de la voix OneCore afin qu'ils parlent le
  son long "a".

Il y a beaucoup de petits ajustements dans la parole et quelques corrections
de bogues pour Nemeth et UEB.

Remarque : il y a maintenant une option pour obtenir la norme en braille
Vietnamien comme sortie braille. Il s'agit toujours d'un travail en cours et
il y a trop de bogues pour être utilisé autrement que pour les tests. Je
m'attends à ce que la prochaine version de MathCAT contienne une
implémentation fiable.

### Version 0.3.8
Braille :

* Le dialogue s'est internationalisé (un grand merci aux traducteurs !)
* Mise en œuvre initiale de la CMU - code braille utilisé en Espagne et dans
  plusieurs pays Lusophones
* Améliorations significatives du braille Vietnamien
* Modifiez le curseur de la boîte de dialogue de débit relatif pour avoir
  une valeur maximale de 100 % (permet désormais uniquement de définir des
  débits  plus lents). En outre, des tailles de pas ont été ajoutées pour
  qu'il soit plus facile d'augmenter/diminuer le débit de manière
  significative.
* Correction de quelques bugs de l'UEB et ajout de quelques caractères pour
  l'UEB

Autres correctifs :

* Améliorations de la parole en Vietnamien
* Correction d'un bug avec les voix OneCore disant "a"
* Correction de quelques bugs de navigation lorsque `AutoZoomOut` est False
  (pas la valeur par défaut)
* Correction de la mise à jour autour des changements de langue et de
  certains autres changements de boîte de dialogue afin qu'ils prennent
  effet immédiatement après avoir cliqué sur "Appliquer" ou "OK".

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=mathcat
