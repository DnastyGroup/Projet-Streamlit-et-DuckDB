# Projet de Groupe 4 : Créez une Application Web Interactive avec Git, Streamlit et DuckDB
Ce projet vise à développer une application web interactive utilisant Streamlit pour l'interface utilisateur et DuckDB pour la gestion des données. L'application permettra aux utilisateurs de téléverser des fichiers CSV contenant des données de ventes, de stocker ces données dans une base DuckDB, et de visualiser diverses analyses à travers des KPIs et des graphiques.

# Installation et Exécution

## Prérequis
- Python 3.8 ou supérieur
- pip

## Installation
1. Clonez ce dépôt :
   ```
   git clone https://github.com/DnastyGroup/Projet-de-Groupe-4-Cr-ez-une-Application-Web-Interactive-avec-Git-Streamlit-et-DuckDB.git
   cd Projet-de-Groupe-4-Cr-ez-une-Application-Web-Interactive-avec-Git-Streamlit-et-DuckDB
   ```

2. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```

## Exécution
Lancez l'application Streamlit :
```
streamlit run app.py
```

L'application sera accessible à l'adresse http://localhost:8501

## Description des Fonctionnalités
- Téléversement de fichiers CSV contenant des données de ventes
- Stockage des données dans une base DuckDB
- Calcul et affichage de 4 KPIs : Ventes Totales, Ventes Moyennes par Transaction, Nombre de Transactions, Région avec les Plus Hautes Ventes
- 4 visualisations : Évolution des Ventes dans le Temps, Ventes par Région, Top 10 Produits par Ventes, Distribution des Montants de Ventes
- Filtres dynamiques par date, région et produit

## Répartition des Tâches
- Membre 1 : Développement de l'interface Streamlit et téléversement de fichiers
- Membre 2 : Intégration de DuckDB et écriture des requêtes SQL
- Membre 3 : Création des visualisations et KPIs
- Membre 4 : Tests, documentation et gestion Git

Jeux de données :
Chaque groupe se verra attribuer une thématique parmi celles listées ci-dessous, chacune accompagnée d'un jeu de données permettant une analyse approfondie.

https://www.kaggle.com/datasets/urvishahir/electric-vehicle-specifications-dataset-2025?select=electric_vehicles_spec_2025.csv.csv
https://www.kaggle.com/datasets/michaelhakim/walmart-sales-analysis?select=Walmart_sales_analysis.csv
https://www.kaggle.com/datasets/nimishasen27/spotify-dataset
https://www.kaggle.com/datasets/abhinavrongala/netflix-datasets-evaluation?select=Netflix+Datasets+Evaluation+MS+Excel.csv
https://www.kaggle.com/datasets/harishthakur995/mcdonald-vs-burger-king
https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset
https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance
https://www.kaggle.com/datasets/lainguyn123/student-performance-factors
https://www.kaggle.com/datasets/shariful07/student-mental-health?select=Student+Mental+health.csv
https://www.kaggle.com/datasets/shivamb/amazon-prime-movies-and-tv-shows
https://www.kaggle.com/datasets/zeesolver/consumer-behavior-and-shopping-habits-dataset
https://www.kaggle.com/datasets/arianazmoudeh/airbnbopendata
📬 Soumission
Envoyez votre livrable avec intitulé MBAESG_EVALUATION_MANAGEMENT_OPERATIONNEL à l'adresse suivante : axel@logbrain.fr
