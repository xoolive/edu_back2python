# Séminaire de reprise en main de Python

## Mise en place de l'environnement

Il est demandé d'installer un environnement Anaconda depuis le [lien suivant](https://www.anaconda.com/products/individual). Il est fortement probable que la version la plus adaptée à votre machine soit la version 64 bits.

Depuis une console Anaconda (Windows) ou un terminal (MacOS, Linux), si l'outil
`git` n'est pas accessible, vous pouvez l'installer avec l'outil conda:

```sh
conda install git
```

Vous pouvez alors télécharger les notebooks qui seront mis à jour avant les
prochaines séances.

```sh
git clone https://github.com/letstrythat/back2python
cd back2python
```

Avant chaque séance, il conviendra de télécharger les nouveaux notebooks:

```sh
git pull
```
 
## Déroulement des séances

Lancer un environnement Jupyter:

```sh
jupyter lab
```

puis déroulez les notebooks dans l'ordre:

0. Types et arithmétique de base
1. NumPy et Matplotlib
2. Pandas

Les notebooks suivants seront mis en ligne avant le prochain séminaire. Il n'est
pas nécessaire de finir les notebooks avant une séance donnée, il est bien
entendu que chacun avance à son propre rythme.


Les solutions aux exercices sont fournis, mais nous avons suffisamment de temps
pour faire de notre mieux avant de charger les solutions. Les encadrants sont là
pour aider !
