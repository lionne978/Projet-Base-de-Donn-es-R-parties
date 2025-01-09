SIGESR Database Management Project
Ce projet vise à concevoir un système de gestion décentralisé pour les préinscriptions et inscriptions académiques des étudiants des universités publiques du Sénégal.

Contexte du projet
Le Système Informatique de Gestion de l’Enseignement Supérieur et de la Recherche (SIGESR) souhaite :

Optimiser la gestion des étudiants à travers quatre zones géographiques.
Offrir un système robuste pour les inscriptions, préinscriptions et statistiques complexes.
Objectifs
Concevoir une base de données relationnelle pour gérer les données des étudiants, formations, et zones.
Implémenter une fragmentation adaptée (horizontale, verticale, mixte) pour la répartition des données.
Développer une couche logicielle pour faciliter l'accès aux données de manière transparente pour l'utilisateur final.
Travail Réalisé
1. Modélisation
Schéma Entité-Association (EA) : Défini pour représenter les relations entre étudiants, formations, filières, et zones.
Modèle logique des données : Création des relations et des attributs basés sur les besoins identifiés.
2. Création de la Base de Données
Tables SQL pour gérer les données globales.
Déclencheurs et vues matérialisées pour préserver l'intégrité des données et automatiser les mises à jour.
3. Fragmentation des Données
Décomposition des données en fragments horizontaux et verticaux par zone (Nord, Centre, Cap-Vert, Sud).
Répartition stratégique des données pour optimiser les performances.
4. Couche Logicielle
Développement d'une interface utilisateur pour saisir et exécuter des requêtes locales et globales.
Fonctionnalités Clés
Gestion des inscriptions et préinscriptions.
Génération des statistiques complexes pour le ministère (passants, redoublants, taux de réussite).
Requêtes spécifiques, telles que :
Étudiants inscrits à la filière MIC de Saint-Louis en 2019/2020.
Filières avec plus de 1 000 préinscriptions en 2019/2020.
Top 3 des ENO ayant le meilleur taux de réussite.
Technologies Utilisées
Base de données : SQL (tables, vues matérialisées, déclencheurs).
Langage de développement : (Préciser ici : Python, Java, etc.).
Outils collaboratifs : Google Meet, Blackboard Collaborate.
Structure des Fichiers
Tables.sql : Contient les scripts pour la création des tables et l'insertion des données.
synonymes.sql : Requêtes pour la gestion des liens et des synonymes.
declencheurs_materializedView.sql : Scripts pour les déclencheurs et les vues matérialisées.
Requete.sql : Requêtes pour la gestion des données et les statistiques.
Rapport.pdf : Documentation avec captures d'écran des étapes de configuration et tests.
Installation et Configuration
Importer les scripts SQL dans un système de gestion de bases de données compatible.
Configurer les utilisateurs et les privilèges pour chaque zone.
Exécuter les tests et les requêtes fournies pour valider l'installation
