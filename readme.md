# Intermediate concepts for Python

## Objectives for the seminar

This seminar has been designed to provide materials for a 3-session Python seminar. It consists of several Python scripts and Jupyter notebooks with self-contained solutions, designed for every participant **to proceed at their own pace**.

The participant is expected to have a basic command of programming languages, if possible with Python, and a decent scientific background with a good understanding of common algorithmic and programming design challenges.

After the seminar, the participant should be able to:

- attend applied mathematics, engineering or artificial intelligence classes which provide examples and exercices using Jupyter notebooks;
- write and run a Python script **outside the Jupyter environment**;
- **install and manage** a Python or Anaconda environment on their home computer.

Participants are considered consenting adults. Enough material is provided to get proficient quickly and ask questions when needed. Obviously, the more you more assiduous you are the better, but learning practices best suiting you are in your hands. In particular, it is perfectly acceptable:

- to peak into the solutions when you are stuck, or to read them thoroughly;
- to skip sections when it becomes overwhelming, or boring;
- to extend problems, find new issues and discuss them with your teacher assistant;
- to find issues in the provided materials;
- to fix them, see [how to create a pull request](https://help.github.com/en/articles/creating-a-pull-request).

## Setting up your environment

You will need to set up **by yourself** the following pieces:

- [Visual Studio Code](https://code.visualstudio.com/)

- an Anaconda distribution, from the [following link](https://www.anaconda.com/products/individual). In case the question arises, it is very likely that the best suited version for your needs is the 64 bits one. Anaconda is more than a Python distribution: it also provides additional dependencies you may need;

- understand that you will need a terminal for cloning learning materials, installing dependencies and more. You are required to not run the Anaconda navigator. **(⇐ Please read again)**.

  - MacOS and Linux users should be familiar with their usual terminal application;
  - MacOS users will probably need to install common tools and dependencies with [brew](https://brew.sh/);
  - Windows users should find out how to run the **Anaconda prompt**.

  You are expected to be familiar with the most basic shell commands to list a directory, create and move files, change permissions, etc.

  Please set up the following settings:

  ```
  conda config --set channel_priority strict
  conda config --add channels conda-forge
  ```

- the `git` (or `git.exe` for Windows users) program, for version control. Using Git falls out of scope of this seminar, but you are **strongly encouraged** to become proficient with it. You may find resources on [GitHub Learning Lab](https://lab.github.com/), e.g. the following course for [first-timers](https://lab.github.com/lmachens/git-and-github-first-timers).

  Try running `git --version`. If necessary, install `git`:

  | Operating system | Installation command   |
  | ---------------- | ---------------------- |
  | Windows          | `conda install git`    |
  | MacOS            | `brew install git`     |
  | Linux (Ubuntu)   | `sudo apt install git` |

- clone the resources for the seminar:

  ```sh
  git clone https://github.com/xoolive/pyseminar
  ```

  You may move the folder at any time if you prefer to keep things sorted differently on your computer.

  Before each session, it may be necessary to update the repository and get additional resources with fixes if errors were encountered in previous sessions. You should add the following options in order to avoid merging conflicts:

  ```sh
  git pull --rebase --autostash
  ```

## Déroulement des séances (change everything)

Lancer un environnement Jupyter:

```sh
jupyter lab
```

puis déroulez les notebooks dans l'ordre:

0. Types et arithmétique de base
1. NumPy et Matplotlib
2. Pandas
3. Les compréhensions de liste
4. Le protocole d'itération appliqué à Pandas
5. Programmation orientée objet et protocoles appliqués à Pandas
6. Programmation orientée objet et protocoles appliqués à la résolution de
   puzzles

Les notebooks suivants seront mis en ligne avant le prochain séminaire. Il n'est
pas nécessaire de finir les notebooks avant une séance donnée, il est bien
entendu que chacun avance à son propre rythme.

Les solutions aux exercices sont fournis, mais nous avons suffisamment de temps
pour faire de notre mieux avant de charger les solutions. Les encadrants sont là
pour aider !

## Errata

- Dans le notebook `02-pandas.ipynb`, corriger la ligne suivante dans la dernière cellule:

```python
from shapely.geometry import Polygon

shapes = {
    r.attributes['gn_a1_code'][3:]: [r.geometry]
    if type(r.geometry) == Polygon else r.geometry
    for r in shpreader.Reader(admin1_file).records()
    if r.attributes['adm0_a3'] == 'FRA'
    and r.attributes['gn_a1_code'][:2] == 'FR'
}
```

- Dans le notebook `04-pandas-iterate.ipynb`, corriger la solution:

```python
bigger_chunk.timestamp.astype(int).plot.hist(bins=100)
# corriger par la ligne suivante
bigger_chunk.timestamp.astype(np.int64).plot.hist(bins=100)
```
