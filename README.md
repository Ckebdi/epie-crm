<<<<<<< HEAD
# 🎓 Epie Formation — CRM Ressources Humaines

Application web de gestion RH développée pour **Epie Formation**, organisme de formation professionnelle basé à Saint-Denis (93).

> Projet interne · Python + Flask + SQLite · Zéro dépendance cloud

---

## ✨ Fonctionnalités

### 3 niveaux d'accès
| Rôle | Accès |
|------|-------|
| **Directeur** | Tout voir, approuver/refuser congés, gérer les comptes |
| **RH** | Annuaire complet, gestion congés & absences, export Excel |
| **Employé** | Sa fiche, ses congés, ses absences uniquement |

### Modules
- 📊 **Dashboard** — statistiques, graphiques, alertes fins de contrat, anniversaires
- 👥 **Annuaire RH** — fiches collaborateurs avec ancienneté, solde CP, date de naissance
- 🌴 **Congés** — demandes numériques (fini le Word imprimé !), approbation en 1 clic, note de refus
- 📋 **Absences** — journal avec durée de retard, justification
- 📥 **Import Excel** — import en masse des collaborateurs via fichier .xlsx
- 📤 **Export Excel** — export formaté annuaire / congés / absences
- 🔑 **Gestion des comptes** — création, modification, réinitialisation mot de passe

### Types de contrats supportés
CDI · CDD · Alternant · Autoentrepreneur · Stagiaire · Contrat pro

### Types de congés
Congés payés · RTT · Maladie · Congé maternité · Congé paternité · Demi-journée · Autorisation d'absence · Congé exceptionnel

---

## 🚀 Installation

### Prérequis
- Python 3.8 ou supérieur ([télécharger](https://www.python.org/downloads/))
- Cocher **"Add Python to PATH"** lors de l'installation Windows

### Lancement rapide (Windows)
```bash
# Double-cliquez sur lancer.bat
# OU depuis un terminal :
pip install flask openpyxl
python app.py
```

### Lancement (Linux / Mac)
```bash
pip3 install flask openpyxl
python3 app.py
```

L'application démarre sur **http://localhost:5000**

Sur le réseau local, accessible via **http://[IP_DU_SERVEUR]:5000**

---

## 🔐 Comptes par défaut

| Login | Mot de passe | Rôle |
|-------|-------------|------|
| `directeur` | `epie2024` | Directeur |
| `rh` | `rh2024` | Responsable RH |
| `cmeziane` | `epie123` | Employé (exemple) |

> ⚠️ **Changez les mots de passe par défaut** dès la mise en production depuis l'onglet *Comptes & Accès*.

Les logins employés sont générés automatiquement : `première lettre du prénom + nom` en minuscules (ex: Amina Benali → `abenali`).

---

## 📁 Structure du projet

```
epie_crm/
├── app.py                  # Backend Flask (routes API, logique métier)
├── epie_crm.db             # Base de données SQLite (créée au premier lancement)
├── requirements.txt        # Dépendances Python
├── lancer.bat              # Script de lancement Windows
├── templates/
│   ├── index.html          # Interface principale (JS vanilla)
│   └── login.html          # Page de connexion
└── README.md
```

---

## 🗄️ Modèle de données

```sql
employees   -- Collaborateurs (CDI, CDD, alternants, etc.)
users       -- Comptes de connexion avec rôles
conges      -- Demandes de congé et autorisations d'absence
absences    -- Journal des absences et retards
```

---

## 🛠️ Stack technique

- **Backend** : Python 3 · Flask · SQLite3
- **Frontend** : HTML/CSS/JS vanilla (zéro framework)
- **Export/Import** : openpyxl
- **Authentification** : sessions Flask + SHA-256
- **Hébergement** : réseau local (aucun cloud nécessaire)

---

## 📋 Roadmap

- [ ] Messagerie interne entre collaborateurs
- [ ] Assignation et suivi de tâches
- [ ] Calendrier visuel des congés de l'équipe
- [ ] Envoi d'emails automatiques (approbation, refus)
- [ ] Module planning formateurs / salles
- [ ] Synchronisation avec SoWeSign (API)

---

## 📝 Licence

Usage interne — Epie Formation · Saint-Denis (93)
=======
## Overview

This project is an internal CRM prototype developed for EPIE as part of a data and process automation initiative. The application is built with Python and Flask, and focuses on centralizing client information, follow‑ups, and key indicators in a simple web interface. It is designed as a lightweight proof of concept that can be extended with additional features such as authentication, reporting, and integration with existing tools.
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
>>>>>>> c80b8385c394015b27f7f094b98e9ec452a5d9e8
