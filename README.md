## Installation

### Prérequis

- Python 3.10+ installé sur votre machine
- pip (gestionnaire de paquets Python)
- Git (optionnel, pour cloner le dépôt)

### 1. Cloner le dépôt

```bash
git clone https://github.com/Ckebdi/epie-crm.git
cd epie-crm
```

> Si vous avez reçu le projet par zip, décompressez l’archive puis placez‑vous dans le dossier `epie-crm`.

### 2. Créer un environnement virtuel

```bash
python -m venv .venv
```

Activer l’environnement virtuel :

- Sous Windows :

```bash
.venv\Scripts\activate
```

- Sous macOS / Linux :

```bash
source .venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer les variables (si nécessaire)

Si le projet utilise des identifiants (base de données, API, etc.), renseignez-les dans un fichier `.env` ou dans le fichier de configuration prévu à cet effet (voir la section Configuration du code si besoin).

## Lancement de l’application

### Lancement via la commande Python

Depuis la racine du projet :

```bash
python app.py
```

L’application démarre en mode développement.  
Par défaut, elle est accessible à l’adresse suivante dans votre navigateur :

```text
http://127.0.0.1:5000
```

(adresse à adapter si un autre port est configuré dans `app.py`).

### Lancement via le script Windows

Sous Windows, vous pouvez aussi utiliser le script fourni :

```bash
lancer.bat
```

Ce script active l’environnement virtuel (si configuré) et démarre automatiquement l’application Flask.

## Tests

Si des tests automatisés sont fournis, vous pouvez les exécuter avec :

```bash
pytest
```

(adaptez la commande si un autre framework de tests est utilisé).
