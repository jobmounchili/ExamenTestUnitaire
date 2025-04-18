# Wordle - Jeu de Deviner des Mots

Ce projet est une implémentation du célèbre jeu **Wordle** en Python. Le but du jeu est de deviner un mot cible en un maximum de 6 tentatives. Chaque tentative fournit un retour visuel indiquant si les lettres sont correctes et bien placées.

## Fonctionnalités

- Devinez un mot de 5 lettres en 6 tentatives maximum.
- Retour visuel pour chaque tentative :
  - **Green** : Lettre correcte et bien placée.
  - **Yellow** : Lettre correcte mais mal placée.
  - **Gray** : Lettre incorrecte.
- Gestion des statistiques :
  - Nombre de victoires.
  - Série de victoires consécutives.
  - Moyenne des tentatives par partie.
- Validation des mots à partir d'une liste prédéfinie.
- Simulation de parties via des tests unitaires.

## Prérequis

- Python 3.10 ou supérieur.
- Bibliothèque `pytest` pour exécuter les tests unitaires.

## Installation

1. Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone https://github.com/jobmounchili/ExamenTestUnitaire.git
   python -m venv ExamenTestUnitaire
   cd ExamenTestUnitaire
   ```
2. Linux 
    ```bash
    source bin/activate
    ```
3. Windows
    ```bash
    source Scripts/activate
    ```

4. Installez les dépendances nécessaires (si applicable) :
    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

### Lancer l'application

Pour démarrer le jeu, exécutez simplement le fichier principal :
    ```bash
    python src/main.py
    ```

### Lancer les tests

Pour exécuter les tests unitaires et vérifier le bon fonctionnement du code, utilisez la commande suivante :
    ```bash
    py -m pytest
    ```