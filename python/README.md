Interprétation avec python
===========================

Prérequis
---------

Installer python : https://python.org

Plus de détails sur l'installation de python ici :
https://wiki.python.org/moin/BeginnersGuide/Download

Installer pip : https://pip.pypa.io/en/stable/installation/

pip est un gestionnaire de libraires pour python.

Exemples
========

Pour les exemples, nous avons besoin d'une librairie nommée **xtermcolor** qui permet d'afficher des couleurs dans le terminal.

Installer **xtermcolor** :
```bash
$ pip install xtermcolor
```

0-unicolor.py
-------------

Fichier exemple d'affichage d'une couleur unie dans le terminal
```bash
$ ./0-unicolor.py
```
![0-unicolor](results/0-unicolor.png)

1-random.py
-----------

Fichier exemple d'affichage d'une couleur aléatoire dans le terminal
```bash
$ ./1-random.py
```
![1-random](results/1-random.png)

2.1-gradient-horizontal.py
--------------------------

Fichier exemple d'affichage d'un dégradé aléatoire entre deux couleurs horizontal dans le terminal
```bash
$ ./2.1-gradient-horizontal.py
```
![2.1-gradient-horizontal](results/2.1-gradient-horizontal.png)

2.2-gradient-vertical.py
------------------------

Fichier exemple d'affichage d'un dégradé aléatoire entre deux couleurs vertical dans le terminal
```bash
$ ./2.1-gradient-vertical.py
```
![2.2-gradient-vertical](results/2.2-gradient-vertical.png)

2.3-gradient-rotation.py
------------------------

Fichier exemple d'affichage d'un dégradé aléatoire entre deux couleurs avec une rotation aléatoire dans le terminal
```bash
$ ./2.1-gradient-rotation.py
```
![2.3-gradient-rotation](results/2.3-gradient-rotation.png)


A-interpretation.py
-------------------

Entrée :
--------

N'importe quel fichier

Sortie :
--------

Chaque triplets d'octet du fichier d'entrée représente une couleur.

Exemple d'utilisation :
-----------------------

```bash
./A-interpretation.py ../demo-sources/images/joconde-de-vinci/joconde-de-vinci.bmp
```

B-interpretation.py
-------------------

Pour cet exemple, nous avons besoin d'une librairie nommée **pygame** qui est un moteur de jeux pour python.

Installer **pygame** :
```bash
$ pip install pygame
```

Entrée :
--------

N'importe quel fichier

Sortie :
--------

Le fichier en entrée est interprété comme étant un fichier audio au format wav.

Exemple d'utilisation :
-----------------------

```bash
./B-interpretation.py ../demo-sources/images/joconde-de-vinci/joconde-de-vinci.bmp
```


README.md
=========
Ce fichier

utils.py
========
Fonctions utilitaires
