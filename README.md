# **SIGESR Database Management Project**

Ce projet vise à concevoir un système de gestion décentralisé pour les préinscriptions et inscriptions académiques des étudiants des universités publiques du Sénégal.

## **Contexte du projet**
Le Système Informatique de Gestion de l’Enseignement Supérieur et de la Recherche (SIGESR) souhaite :
- Optimiser la gestion des étudiants à travers quatre zones géographiques.
- Offrir un système robuste pour les inscriptions, préinscriptions et statistiques complexes.

## **Objectifs**
1. Concevoir une base de données relationnelle pour gérer les données des étudiants, formations, et zones.
2. Implémenter une fragmentation adaptée (horizontale, verticale, mixte) pour la répartition des données.
3. Développer une couche logicielle pour faciliter l'accès aux données de manière transparente pour l'utilisateur final.

## **Travail Réalisé**

### **1. Modélisation**
- **Schéma Entité-Association (EA)** : Défini pour représenter les relations entre étudiants, formations, filières, et zones. (voir.pdf)
- **Modèle logique des données** : Création des relations et des attributs basés sur les besoins identifiés.(voir.pdf)

### **2. Création de la Base de Données**
- Tables SQL pour gérer les données globales.
- Déclencheurs et vues matérialisées pour préserver l'intégrité des données et automatiser les mises à jour.

### **3. Fragmentation des Données**
- Décomposition des données en fragments horizontaux et verticaux par zone (Nord, Centre, Cap-Vert, Sud).
- Répartition stratégique des données pour optimiser les performances.

### **4. Couche Logicielle**
- Développement d'une interface utilisateur pour saisir et exécuter des requêtes locales et globales.

## **Fonctionnalités Clés**
1. Gestion des inscriptions et préinscriptions.
3. Requêtes spécifiques, telles que :
   - Étudiants inscrits à la filière MIC de Saint-Louis en 2019/2020.
   - Filières avec plus de 1 000 préinscriptions en 2019/2020.
   - Top 3 des ENO ayant le meilleur taux de réussite.

## **Technologies Utilisées**
- **Base de données** : SQL (tables, vues matérialisées, déclencheurs).
- **Langage de développement** : ( Python,html.).
- **Outils collaboratifs** : Google Meet, Google Drive.

## **Structure des Fichiers**
- `fichier.sql` : Contient les scripts pour la création des tables et l'insertion des données.
- `synonymes.sql` : Requêtes pour la gestion des liens et des synonymes.
- `declencheurs_materializedView.sql` : Scripts pour les déclencheurs et les vues matérialisées.
- `Requete.sql` : Requêtes pour la gestion des données.
- `Rapport.pdf` : Documentation avec captures d'écran des étapes de configuration et tests.
