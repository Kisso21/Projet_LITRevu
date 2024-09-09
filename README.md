
# LITReview

**LITReview** est une application web basée sur Django, conçue pour partager et publier des critiques de livres, films et autres médias.

## Table des matières

- [Aperçu du projet](#aperçu-du-projet)
- [Fonctionnalités](#fonctionnalités)
- [Pré-requis](#pré-requis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Comptes de test](#comptes-de-test)
- [Structure du projet](#structure-du-projet)
- [Syntaxe Markdown](#syntaxe-markdown)
- [Licence](#licence)

## Aperçu du projet

LITReview permet aux utilisateurs de publier des critiques et de demander des retours sur des œuvres littéraires, cinématographiques ou autres. L’application est conçue pour être simple d’utilisation, tout en offrant une interface responsive accessible depuis des plateformes de bureau et mobiles.

## Fonctionnalités

L'application offre plusieurs fonctionnalités pour faciliter la gestion et le partage des critiques :

- **Gestion des utilisateurs :**
  - Inscription et authentification utilisateur.
  - Connexion et déconnexion sécurisées.
  
- **Création et gestion des critiques :**
  - Publication de critiques textuelles sur des livres.
  - Ajout d'une note ou d'une évaluation lors de la publication de critiques.
  - Visualisation des critiques publiées par d'autres utilisateurs.

- **Demandes de critiques :**
  - Fonctionnalité permettant aux utilisateurs de demander une critique sur un livre.
  - Les autres utilisateurs peuvent répondre aux demandes de critique avec leurs propres avis.

- **Suivi des utilisateurs et des critiques :**
  - Fonctionnalité de "suivi" pour permettre aux utilisateurs de suivre les critiques d'autres utilisateurs.

- **Interface utilisateur responsive :**
  - Une interface utilisateur responsive pour un accès optimal sur différents appareils (ordinateurs, tablettes, smartphones).

- **Recherche et filtres :**
  - Moteur de recherche intégré pour retrouver un utilisateurs et le "suivre"

- **Administration :**
  - Tableau de bord d'administration pour gérer les utilisateurs, critiques, et demandes.
  - Modification et suppression des critiques par les administrateurs.
  - Gestion des comptes utilisateur par l'administrateur

## Installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/votre-utilisateur/LITReview.git
    cd LITReview
    ```

2. Créez un environnement virtuel et activez-le :
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows, utilisez `venv\Scriptsctivate`
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

4. Appliquez les migrations de la base de données :
    ```bash
    python manage.py migrate
    ```

5. Lancez le serveur de développement :
    ```bash
    python manage.py runserver
    ```

6. Ouvrez votre navigateur et accédez à l'adresse `http://127.0.0.1:8000`.

## Utilisation

- Après le lancement de l'application, inscrivez-vous ou connectez-vous.
- Les utilisateurs peuvent créer, consulter et éditer leurs critiques.
- L'application permet également de demander des retours sur les critiques à d'autres utilisateurs.

## Comptes de test

Voici les identifiants et mots de passe pour les comptes administrateur et de test :

- **Compte administrateur :**
    - Identifiant : `Admin`
    - Mot de passe : `Bonjour21!`
  
- **Comptes de test :**
    - Compte test 1 : `OC_TEST1`, mot de passe : `Bonjour55!`
    - Compte test 2 : `OC_TEST2`, mot de passe : `Bonjour55!`
    - Compte test 3 : `OC_TEST3`, mot de passe : `Bonjour55!`


# LITReview

**LITReview** est une application web basée sur Django, conçue pour partager et publier des critiques de livres, films et autres médias.

## Table des matières

- [Aperçu du projet](#aperçu-du-projet)
- [Fonctionnalités](#fonctionnalités)
- [Pré-requis](#pré-requis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Comptes de test](#comptes-de-test)
- [Structure du projet](#structure-du-projet)
- [Syntaxe Markdown](#syntaxe-markdown)
- [Licence](#licence)

## Aperçu du projet

LITReview permet aux utilisateurs de publier des critiques et de demander des retours sur des œuvres littéraires, cinématographiques ou autres. L’application est conçue pour être simple d’utilisation, tout en offrant une interface responsive accessible depuis des plateformes de bureau et mobiles.

## Fonctionnalités

L'application offre plusieurs fonctionnalités pour faciliter la gestion et le partage des critiques :

- **Gestion des utilisateurs :**
  - Inscription et authentification utilisateur.
  - Connexion et déconnexion sécurisées.
  - Modification des informations de profil utilisateur.
  
- **Création et gestion des critiques :**
  - Publication de critiques textuelles sur des livres, films, ou tout autre média.
  - Ajout d'une note ou d'une évaluation lors de la publication de critiques.
  - Visualisation des critiques publiées par d'autres utilisateurs.

- **Demandes de critiques :**
  - Fonctionnalité permettant aux utilisateurs de demander une critique sur un livre ou un film.
  - Les autres utilisateurs peuvent répondre aux demandes de critique avec leurs propres avis.

- **Suivi des utilisateurs et des critiques :**
  - Fonctionnalité de "suivi" pour permettre aux utilisateurs de suivre les critiques d'autres utilisateurs.
  - Notifications lorsqu'une nouvelle critique est publiée par un utilisateur suivi.

- **Interface utilisateur responsive :**
  - Une interface utilisateur responsive pour un accès optimal sur différents appareils (ordinateurs, tablettes, smartphones).

- **Recherche et filtres :**
  - Moteur de recherche intégré pour retrouver des critiques par titre, auteur, ou catégorie.
  - Filtres pour affiner les recherches par type de média, date de publication ou note.

- **Sécurité et permissions :**
  - Système de permissions pour limiter l'accès aux fonctionnalités administratives.
  - Protection des données utilisateur avec une gestion sécurisée des mots de passe.

- **Administration :**
  - Tableau de bord d'administration pour gérer les utilisateurs, critiques, et demandes.
  - Modification et suppression des critiques par les administrateurs.
  - Gestion des comptes utilisateur par l'administrateur (suspension, réactivation, suppression).

## Pré-requis

- Python 3.8+
- Django 3.2+
- Autres dépendances (indiquées dans le fichier `requirements.txt`)

## Installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/votre-utilisateur/LITReview.git
    cd LITReview
    ```

2. Créez un environnement virtuel et activez-le :
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows, utilisez `venv\Scriptsctivate`
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

4. Appliquez les migrations de la base de données :
    ```bash
    python manage.py migrate
    ```

5. Lancez le serveur de développement :
    ```bash
    python manage.py runserver
    ```

6. Ouvrez votre navigateur et accédez à l'adresse `http://127.0.0.1:8000`.

## Utilisation

- Après le lancement de l'application, inscrivez-vous ou connectez-vous.
- Les utilisateurs peuvent créer, consulter et éditer leurs critiques.
- L'application permet également de demander des retours sur les critiques à d'autres utilisateurs.

## Comptes de test

Voici les identifiants et mots de passe pour les comptes administrateur et de test :

- **Compte administrateur :**
    - Identifiant : `Admin`
    - Mot de passe : `Bonjour21!`
  
- **Comptes de test :**
    - Compte test 1 : `OC_TEST1`, mot de passe : `Bonjour55!`
    - Compte test 2 : `OC_TEST2`, mot de passe : `Bonjour55!`
    - Compte test 3 : `OC_TEST3`, mot de passe : `Bonjour55!`
