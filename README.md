# Projet DVC Tweets Suspects

Exécuter `dvc repro` pour lancer le pipeline.

Ce projet consiste à développer une application de machine learning capable de détecter automatiquement des tweets suspects à partir de leur contenu textuel.

L’objectif est de classifier chaque tweet en deux catégories :
- 0 : Tweet non suspect
- 1 : Tweet suspect

Une interface web interactive a été développée avec Streamlit pour permettre des prédictions en temps réel.

---

## Objectifs

- Automatiser la détection de contenus suspects sur Twitter
- Appliquer les techniques de NLP
- Construire un pipeline complet de Machine Learning
- Déployer un modèle utilisable via une interface simple

---

##  Dataset

- text : contenu du tweet  
- label : 0 = non suspect, 1 = suspect  

---

##  Pipeline du projet

- Prétraitement : nettoyage, tokenisation, stopwords, lemmatisation  
- Vectorisation : TF-IDF / Bag of Words  
- Modélisation : Logistic Regression, Naive Bayes, Random Forest  
- Évaluation : Accuracy, Precision, Recall, F1-score  

---

##  Déploiement

Application Streamlit permettant :
- Saisie d’un tweet
- Prédiction instantanée
- Résultat affiché en temps réel

---

## Installation

```bash
git clone https://github.com/ton-utilisateur/tweet-suspect-detection.git

pip install -r requirements.txt
Lancer l’application
streamlit run app.py
Technologies
Python, Pandas, NumPy, Scikit-learn, NLTK, Streamlit
