# RfDomoticz

## Introduction

L'idée de RfDomoticz est de regroupé tous les objets communiquant par radio-fréquence dans une seule interface et ainsi se passer des multiples télécommandes qui les utilisent.

### Pourquoi se débarassez des télécommandes ?

Premièrement car on ne sais jamais ou on les as rangés,
puis si on a plus besoin des télécommandes car ons sais envoyé le signal qui fait réagir cette objet les utilisations sont multiples :
* Intégration Google Home / Amazon Echo
* Crées ses propres objets connéctés (avec des prises rf)
* ect..

## Matériel

* Raspberry pi
* Recepteur / Emmeteur  RF 433
* télécommande RF 433 (Garage, prise connecté...)

# Python

Pour réalisez ce projet j'ai crée une interface python afin de gérer de manière facile les signaux recue et emis par le raspberry, afin de pouvoir communiquez avec celui-ci le logiciel python écoute et reçois des informations sur le port 6666.

## Imports

Interface graphique : kivy
*  Linux : https://kivy.org/docs/installation/installation-windows.html
* Mac os : https://kivy.org/docs/installation/installation-osx.html
* Linux :
https://kivy.org/docs/installation/installation-linux.html

Pourquoi kivy ? car celui-ci permet de crée des interface graphique assez facilement avec l'utilisation de fichier .kv dans lequel on décrit l'interface en yaml et celui-ci nous le transforme en python.

Avis après utilisation :
J'ai essayé plusieur framework avant de partir sur kivy, effectivement dessiner l'interface parrais tres simple au début surtout si on fais du mobile mais on se rend vite compte qu'il est très limité et qu'il est difficile d'y faire plus que des interface simples.

yaml parser : pyyaml
* https://pyyaml.org/wiki/PyYAML

`` pip install pyyaml``


## Vidéo démo : 
