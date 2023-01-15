# SAE3.2 : Empilement d’images astronomiques en Python

Auteurs : Samuel CARON, Ludovic GUYADER <br>
BUT2 Informatique TP APP

---


## Cahier des charges :

* <b>V1 - Interface graphique + empilement par moyenne</b> : qui possède une interface graphique, permet d'ouvrir un répertoire, de lire les images à l'intérieur, de les traiter (faire l'empilement par moyenne) et afficher le résultat.
* <b>V2 - Empilement par médiane</b> : comme V1 mais empilement par médiane.
* <b>V3 - Suppression des valeurs aberrantes</b> : V1 + V2 + supprimer les données incohérentes avant l'empilement.
* <b>V4 - Image en couleur</b> : gestion des images en couleur.
* <b>V5 - Recalage d'images</b> : recalage des images si nécessaire.


## Travaux réalisés : 

* <b>V1</b> : Fait ✅
* <b>V2</b> : Fait ✅
* <b>V3</b> : Fait ✅
* <b>V4</b> : Fait ✅ 
* <b>V5</b> : Non fait ❌ (Cependant, cette fonction permettrait de recaler des images si les dimensions sont différentes)

## Pré-requis de compilation :

Afin de lancer le projet, vous devez disposer des bibliothèques suivantes : 
* <b>Pyqt6</b> : pip install pyqt6
* <b>Astropy</b> : pip install astropy
* <b>Statistics</b> : pip install statistics
* <b>Matplolib</b> : pip install matplotlib
* <b>Numpy</b> : pip install numpy

## Conseil :

* Certains traitements peuvent être assez long (en minutes). Pour cela, vous êtes toujours averti lorsque le traitement est terminé grâce au terminal -> <b>PHOTO A JOUR</b>

* La suppression des valeurs aberrantes complexifie les calculs et ainsi ralentit le traitement des images. <br> Pour tester la fonctionnalité de cette option, nous vous recommandons de le faire sur des petites images en noir et blanc.

* Certaines images peuvent vous sembler toute noire. Ce n'est pas réellement le cas. Afin de mieux visualiser les images, n'hésitez pas à :
    * augmenter la luminosité de votre écran au maximum.
    * vous mettre sous votre couette.
    * placez votre tête à quelques centimètres de l'image.