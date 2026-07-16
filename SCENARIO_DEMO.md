# Scénario de démonstration — EPIE Formation · Espace RH

Durée totale : **15 minutes** (7 + 4 + 3) + questions. À suivre à l'écran, sans improvisation.

---

## ✅ Préparation (15 min avant la réunion)

1. Lancer `lancer.bat`, vérifier que http://localhost:5000 répond
2. **Se connecter une fois avec chaque compte AVANT la démo** et définir les mots de passe (le changement est forcé à la première connexion) :
   - `directeur` / mot de passe choisi
   - `rh` / mot de passe choisi
   - `cmeziane` / mot de passe choisi
3. Vérifier l'état des données de démo :
   - la demande de **Camille Meziane** (Congés payés 07→11/04, solde 0) est **En attente** → c'est le cas « solde insuffisant »
   - **Thomas Girard** a un solde de 25 j → c'est le cas « approbation normale »
4. Navigateur : fenêtre propre, zoom 100 %, onglets fermés, notifications coupées
5. Ouvrir Excel en arrière-plan (pour l'étape export)
6. Garder ce document imprimé ou sur un second écran

---

## 👔 Parcours 1 — Directeur (~7 min)

| # | Écran | À faire / à montrer | À dire |
|---|-------|---------------------|--------|
| 1 | **Page de connexion** | Se connecter avec `directeur` | « Chaque collaborateur a un compte personnel. Les mots de passe sont chiffrés avec un standard bancaire, et après 5 tentatives ratées le compte est bloqué 15 minutes — on se protège contre les intrusions. » |
| 2 | **Tableau de bord** | Balayer les cartes stats, pointer **« Fins de contrat dans les 60 jours »** puis le badge **« Demandes en attente »** | « En un coup d'œil : l'effectif, les contrats qui arrivent à échéance — fini les CDD qu'on découvre expirés — et les demandes de congé à traiter. » |
| 3 | **Annuaire RH** | Taper un nom dans la recherche, filtrer par contrat, ouvrir une **Fiche** (Thomas Girard) | « Tout l'annuaire est centralisé : contrat, ancienneté calculée automatiquement, solde de congés, historique complet — plus de fichiers Excel éparpillés. » |
| 4 | **Congés — cas normal** | Bouton *Congé* → créer une demande **Congés payés** pour **Thomas Girard** du **lundi 20/07 au vendredi 24/07** → Approuver. Montrer la colonne **Jours ouvrés = 5** puis retourner sur sa fiche : solde 25 → 20 | « Le décompte est en **jours ouvrés** : week-ends et les 11 jours fériés français sont exclus automatiquement, y compris Pâques et l'Ascension qui changent chaque année. Le solde se met à jour tout seul. » |
| 5 | **Congés — solde insuffisant** | Sur la demande en attente de **Camille Meziane** (solde 0), cliquer **Approuver** → message d'erreur « Solde insuffisant : 0 j restants… » → cliquer **Refuser** avec le motif « Solde épuisé, à reporter sur la prochaine période » | « L'application **empêche** d'approuver un congé sans solde — c'est une erreur humaine classique qui coûte de vraies journées. Le refus est toujours motivé : le collaborateur voit le message sur son espace. » |
| 6 | **Journal d'audit** | Ouvrir l'onglet, montrer les lignes fraîches : approbation, refus, connexions. Utiliser le filtre | « Chaque action sensible est tracée : qui a approuvé quoi, quand, qui s'est connecté. C'est notre exigence de traçabilité RGPD, consultable uniquement par la direction. » |
| 7 | **Export Excel + Sauvegarde** | Cliquer *Export Excel*, ouvrir le fichier (3 onglets formatés). Puis cliquer *Sauvegarder la base* → toast de confirmation | « On reste compatible avec les outils existants : la comptabilité récupère un Excel propre en un clic. Et la base est sauvegardée automatiquement à chaque démarrage plus à la demande. » |

---

## 🗂️ Parcours 2 — RH (~4 min)

| # | Écran | À faire / à montrer | À dire |
|---|-------|---------------------|--------|
| 1 | **Connexion** | Se déconnecter, se connecter avec `rh` | « Le compte RH a exactement les droits dont il a besoin : gestion quotidienne, sans l'administration des comptes ni le journal d'audit. » |
| 2 | **Congés** | Montrer la liste complète, la colonne **Jours ouvrés**, approuver/refuser possible | « La RH traite les demandes au fil de l'eau ; le chiffre affiché est toujours le décompte réel en jours ouvrés, calculé par le serveur — pas de recalcul manuel. » |
| 3 | **Absences** | Bouton *Absence* → enregistrer un **Retard** de 15 min justifié « Transport » pour un collaborateur | « Retards et absences sont consignés avec durée et justification — utile pour les entretiens et les obligations de suivi. » |
| 4 | **Import / Export Excel** | Ouvrir *Import Excel* dans l'Annuaire (montrer la fenêtre, sans importer), puis *Export* | « Pour démarrer, on n'a pas tout ressaisi : l'annuaire existant s'importe en masse depuis Excel. L'export sert aux bilans et à la paie. » |

---

## 👤 Parcours 3 — Employé (~3 min)

| # | Écran | À faire / à montrer | À dire |
|---|-------|---------------------|--------|
| 1 | **Connexion** | Se connecter avec `cmeziane` | « Côté collaborateur, c'est volontairement minimal : il ne voit que **ses** données — cloisonnement strict appliqué par le serveur. » |
| 2 | **Ma fiche** | Montrer la synthèse (ancienneté, fin de contrat, solde avec jauge), cliquer *Modifier* (email/tél seulement) | « Chacun voit sa situation en temps réel : solde exact, fin de contrat. Il peut mettre à jour ses coordonnées, et rien d'autre. » |
| 3 | **Mes congés** | Montrer la notification de **refus avec motif** (celle créée au parcours 1), puis *Demande de congé* → demi-journée (créneau Matin) → soumettre | « La demande se fait en 30 secondes, y compris les demi-journées comptées 0,5 jour. Le collaborateur voit le statut et le motif d'un éventuel refus — plus de papier, plus de "je n'étais pas au courant". » |
| 4 | **Mes absences** | Montrer le tableau en lecture seule | « Ses absences enregistrées par la RH sont visibles en toute transparence, mais non modifiables. » |

---

## ❓ Questions probables — réponses prêtes

- **« Et si le PC serveur tombe en panne ? »** → Sauvegarde horodatée automatique à chaque démarrage + bouton, 30 copies conservées, restauration en 2 minutes. Le dossier `backups/` peut être répliqué sur le NAS interne.
- **« Où sont stockées les données ? »** → 100 % sur notre machine, sur notre réseau. Aucun cloud, aucun abonnement, rien ne sort de l'entreprise — argument RGPD fort.
- **« Qui voit quoi ? »** → 3 rôles étanches vérifiés côté serveur ; le journal d'audit trace les consultations sensibles.
- **« Combien ça coûte ? »** → Zéro licence. Python, Flask et SQLite sont libres et gratuits ; le seul coût est le poste qui l'héberge.
- **« Et les RTT / autres compteurs ? »** → Aujourd'hui seuls les congés payés décomptent le solde ; un compteur RTT séparé est dans la roadmap.
- **« On peut l'essayer ? »** → Proposer un pilote de 3-4 semaines avec un petit groupe avant généralisation.

---

## ⚠️ Pièges à éviter

- Ne pas faire la démo sur des **données réelles** — garder la base de démonstration
- Ne pas improviser de manipulation non répétée (import Excel réel notamment)
- Si une question dépasse le cadre : « bonne idée, je la note pour la roadmap » — et la noter réellement
