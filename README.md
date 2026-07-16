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
- 📊 **Dashboard** — statistiques, graphiques, alertes fins de contrat
- 👥 **Annuaire RH** — fiches collaborateurs avec ancienneté, solde CP, date de naissance
- 🌴 **Congés** — demandes numériques, approbation en 1 clic, note de refus
- 📋 **Absences** — journal avec durée de retard, justification
- 📥 **Import Excel** — import en masse des collaborateurs et congés/absences via fichier .xlsx
- 📤 **Export Excel** — export formaté annuaire / congés / absences
- 🔑 **Gestion des comptes** — création, modification, réinitialisation mot de passe

### Types de contrats supportés
CDI · CDD · Alternant · Autoentrepreneur · Stagiaire · Contrat pro

### Types de congés
Congés payés · RTT · Maladie · Congé maternité · Congé paternité · Demi-journée · Autorisation d'absence · Congé exceptionnel

---

## 🚀 Installation

### Prérequis
- Python 3.10 ou supérieur ([télécharger](https://www.python.org/downloads/))
- Cocher **"Add Python to PATH"** lors de l'installation Windows

### Lancement rapide (Windows)
```bash
# Double-cliquez sur lancer.bat
# OU depuis un terminal :
pip install -r requirements.txt
python app.py
```

### Installation propre avec environnement virtuel (recommandé)
```bash
git clone https://github.com/Ckebdi/epie-crm.git
cd epie-crm
python -m venv .venv
# Windows :
.venv\Scripts\activate
# macOS / Linux :
source .venv/bin/activate
pip install -r requirements.txt
python app.py
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

> ⚠️ **Changez les mots de passe par défaut** dès la mise en production depuis l'onglet *Comptes & Accès*. Un changement de mot de passe est exigé à la première connexion.

Les logins employés sont générés automatiquement : `première lettre du prénom + nom` en minuscules (ex : Amina Benali → `abenali`).

---

## 📁 Structure du projet

```
epie_crm/
├── app.py                  # Backend Flask (routes API, logique métier)
├── epie_crm.db             # Base de données SQLite (créée au premier lancement, non versionnée)
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
- **Authentification** : sessions Flask (expiration 8 h) · mots de passe PBKDF2-SHA256 salés (migration automatique des anciens comptes) · blocage 15 min après 5 échecs
- **Hébergement** : réseau local (aucun cloud nécessaire)

---

## 💾 Sauvegardes

La base SQLite est sauvegardée automatiquement :

- **À chaque démarrage** du serveur : copie horodatée dans `backups/` (ex. `backups/epie_crm_20260715_083000.db`)
- **À la demande** : bouton *Sauvegarder la base* dans la barre latérale (Directeur uniquement, action tracée dans le journal d'audit)
- **Rotation automatique** : les 30 copies les plus récentes sont conservées, les plus anciennes supprimées
- La copie utilise l'API de sauvegarde de SQLite : elle est fiable même pendant que l'application tourne

**Restaurer une sauvegarde** : arrêter le serveur, remplacer `epie_crm.db` par la copie choisie (renommée `epie_crm.db`), relancer.

> Le dossier `backups/` n'est jamais versionné sur git. Pensez à copier régulièrement ce dossier sur un second support (disque réseau interne, clé USB).

---

## 📋 Roadmap

- [x] Décompte des congés en jours ouvrés + jours fériés français
- [x] Renforcement sécurité (hash PBKDF2 salé, blocage après 5 échecs de connexion, session 8 h)
- [x] Journal d'audit des actions sensibles (onglet Directeur)
- [ ] Calendrier visuel des congés de l'équipe
- [ ] Messagerie interne entre collaborateurs
- [ ] Assignation et suivi de tâches
- [ ] Envoi d'emails automatiques (approbation, refus)
- [ ] Module planning formateurs / salles

---

## 📖 Exploitation & passation

Pour le service informatique ou un repreneur : voir **`GUIDE_EXPLOITATION.md`**
(démarrage/arrêt, gestion des comptes, `reset_password.py` en cas de mot de passe perdu,
restauration des sauvegardes, dépannage, déploiement ailleurs, précautions OVH/hébergement externe).

---

## 📝 Licence

Usage interne — Epie Formation · Saint-Denis (93)
