# Structure du diaporama — EPIE Formation · Espace RH (8 slides)

Style conseillé : fond blanc, titres en bleu EPIE (#1f7fa8), accents verts (#5d9b31), une seule idée par slide, captures d'écran grandes et lisibles.

---

## Slide 1 — Titre

**« Espace RH — l'outil interne de gestion des ressources humaines »**

- Sous-titre : *EPIE Formation · 100 % local · développé en interne*
- Ton nom, ta fonction, la date
- **Visuel** : capture de la page de connexion (sobre, avec le wordmark EPIE)

---

## Slide 2 — Le problème aujourd'hui

**« La gestion RH actuelle nous fait perdre du temps et de la fiabilité »**

- Demandes de congé sur papier / Word : circuit lent, perte de traçabilité
- Soldes CP recalculés à la main → erreurs de décompte (week-ends, jours fériés)
- Informations dispersées dans plusieurs fichiers Excel non synchronisés
- Fins de contrat (CDD, alternances) suivies de mémoire
- Aucune trace de qui a validé quoi, ni quand
- **Visuel** : photo d'un formulaire papier ou schéma « avant » (flèches entre papier, mails, Excel)

---

## Slide 3 — La solution

**« Une application web unique, sur notre réseau, pour les trois profils »**

- Un seul outil : annuaire, congés, absences, comptes, journal d'audit
- 3 espaces distincts : Directeur (pilotage), RH (gestion), Employé (self-service)
- Décompte automatique en **jours ouvrés**, jours fériés français inclus
- Développée en interne : zéro licence, zéro cloud, évolutive selon nos besoins
- **Visuel** : capture du tableau de bord Directeur (plein écran)

---

## Slide 4 — Fonctionnalités principales

**« Du dépôt de la demande à l'export comptable »**

- Demande de congé en 30 s ; approbation / refus motivé en 1 clic
- Contrôle automatique du solde : impossible d'approuver sans jours disponibles
- Alertes fins de contrat à 60 jours ; ancienneté et âge calculés automatiquement
- Journal des absences et retards avec justification
- Import / export Excel compatible avec nos outils actuels (paie, comptabilité)
- **Visuel** : capture de la liste des congés avec la colonne « Jours ouvrés » + le message « Solde insuffisant »

---

## Slide 5 — Sécurité & RGPD

**« Les données RH restent chez nous, protégées et tracées »**

- Hébergement 100 % local : aucune donnée ne quitte le réseau de l'entreprise
- Mots de passe chiffrés (hachage salé standard) + blocage après 5 tentatives
- Sessions limitées à 8 h ; changement de mot de passe forcé à la première connexion
- Journal d'audit : chaque action sensible est horodatée et consultable par la direction
- Sauvegarde automatique et horodatée de la base à chaque démarrage
- **Visuel** : capture de l'onglet Journal d'audit

---

## Slide 6 — Démo live

**« Voyons-le fonctionner » (15 minutes)**

- Parcours Directeur : tableau de bord → approbation → cas « solde insuffisant » → audit → export
- Parcours RH : gestion quotidienne congés / absences, import Excel
- Parcours Employé : ma fiche, ma demande de congé, mes absences
- *(Garder cette slide affichée pendant la démo — suivre SCENARIO_DEMO.md)*
- **Visuel** : les 3 vignettes d'écrans (dashboard, liste congés, espace employé)

---

## Slide 7 — Roadmap

**« Une base solide, des évolutions déjà identifiées »**

- Court terme : compteur RTT séparé, calendrier visuel des congés de l'équipe
- Moyen terme : emails automatiques d'approbation / refus, messagerie interne
- Plus tard : suivi de tâches, planning formateurs / salles
- Les priorités seront ajustées selon les retours du pilote
- **Visuel** : frise chronologique simple en 3 colonnes

---

## Slide 8 — Prochaines étapes & décision

**« Ce dont j'ai besoin pour avancer »**

- Validation d'un **pilote de 3-4 semaines** avec un petit groupe (RH + 3-4 volontaires)
- Un poste ou mini-serveur dédié sur le réseau interne
- Import de l'annuaire réel (fichier Excel existant) et création des comptes
- Point de retour d'expérience à l'issue du pilote → décision de généralisation
- **Visuel** : aucun — slide de conclusion épurée, tes coordonnées

---

## Conseils de présentation

- 20 minutes au total : 5 de slides (1-5), 15 de démo (6), 2 de conclusion (7-8)
- Faire les captures d'écran **après** avoir rempli la base avec les données de démo, en français, fenêtre à 100 %
- Présenter comme « version pilote prête à tester », pas comme produit fini
- Répéter la démo au moins deux fois avec SCENARIO_DEMO.md
