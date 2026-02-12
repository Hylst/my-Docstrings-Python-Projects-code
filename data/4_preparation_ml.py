# -*- coding: utf-8 -*-
"""
Prog 4 : Préparation et tri des données pour le machine learning
on doit nettoyer les données avant de les donner aux algos
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

def nettoyer_valeurs_manquantes(df):
    """
    Gère les NaN et les trucs qui manquent
    plusieurs stratégies possibles
    """
    print("\n=== Nettoyage des valeurs manquantes ===")
    print(f"valeurs manquantes avant :")
    print(df.isnull().sum())
    
    # stratégie simple : moyenne pour les nombres, mode pour le texte
    for col in df.columns:
        if df[col].dtype in ['float64', 'int64']:
            # remplace par la moyenne
            df[col].fillna(df[col].mean(), inplace=True)
        else:
            # remplace par la valeur la plus fréquente
            df[col].fillna(df[col].mode()[0], inplace=True)
    
    print(f"\nvaleurs manquantes après :")
    print(df.isnull().sum())
    
    return df

def supprimer_doublons(df):
    """vire les lignes en double si y'en a"""
    avant = len(df)
    df = df.drop_duplicates()
    après = len(df)
    
    print(f"\n{avant - après} doublons supprimés")
    return df

def normaliser_donnees(df, methode='standard'):
    """
    Normalise les données numériques
    important pour certains algos de ML comme SVM ou KNN
    """
    colonnes_num = df.select_dtypes(include=[np.number]).columns
    
    if methode == 'standard':
        # standardisation : moyenne=0, écart-type=1
        scaler = StandardScaler()
        print("\nnormalisation standard (z-score)")
    else:
        # normalisation min-max : entre 0 et 1
        scaler = MinMaxScaler()
        print("\nnormalisation min-max [0,1]")
    
    df[colonnes_num] = scaler.fit_transform(df[colonnes_num])
    
    return df, scaler

def encoder_variables_categorielles(df):
    """
    Transforme les variables texte en nombres
    le ML comprend que les chiffres
    """
    # one-hot encoding pour les variables catégorielles
    colonnes_cat = df.select_dtypes(include=['object']).columns
    
    if len(colonnes_cat) > 0:
        print(f"\nencodage de {len(colonnes_cat)} variables catégorielles")
        df = pd.get_dummies(df, columns=colonnes_cat, drop_first=True)
    
    return df

def separer_train_test(df, colonne_cible, test_size=0.2):
    """
    Sépare en ensemble d'entraînement et de test
    classique : 80% train, 20% test
    """
    # sépare X (features) et y (target)
    X = df.drop(colonne_cible, axis=1)
    y = df[colonne_cible]
    
    # split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42  # random_state pour reproductibilité
    )
    
    print(f"\n=== Séparation des données ===")
    print(f"taille train : {len(X_train)} ({(1-test_size)*100}%)")
    print(f"taille test : {len(X_test)} ({test_size*100}%)")
    
    return X_train, X_test, y_train, y_test

def traiter_outliers(df, colonnes, methode='iqr'):
    """
    Gère les valeurs aberrantes
    soit on les supprime soit on les plafonne
    """
    print("\n=== Traitement des outliers ===")
    
    for col in colonnes:
        if methode == 'iqr':
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1
            
            limite_basse = q1 - 1.5 * iqr
            limite_haute = q3 + 1.5 * iqr
            
            # plafonne les valeurs au lieu de les supprimer
            # comme ça on perd pas de données
            df[col] = df[col].clip(lower=limite_basse, upper=limite_haute)
            
            print(f"{col} : outliers plafonnés entre {limite_basse:.2f} et {limite_haute:.2f}")
    
    return df

def pipeline_complet(df, colonne_cible):
    """
    Pipeline de préparation complète
    enchaine toutes les étapes dans le bon ordre
    """
    print("=== DÉBUT DU PIPELINE DE PRÉPARATION ===\n")
    
    # 1. doublons
    df = supprimer_doublons(df)
    
    # 2. valeurs manquantes
    df = nettoyer_valeurs_manquantes(df)
    
    # 3. outliers (avant normalisation)
    colonnes_num = df.select_dtypes(include=[np.number]).columns
    colonnes_num = [c for c in colonnes_num if c != colonne_cible]  # pas la cible
    df = traiter_outliers(df, colonnes_num)
    
    # 4. encodage catégoriel
    df = encoder_variables_categorielles(df)
    
    # 5. normalisation (en dernier)
    df, scaler = normaliser_donnees(df, methode='standard')
    
    # 6. séparation train/test
    X_train, X_test, y_train, y_test = separer_train_test(df, colonne_cible)
    
    print("\n=== PIPELINE TERMINÉ ===")
    print(f"données prêtes pour le ML !")
    print(f"shape X_train : {X_train.shape}")
    print(f"shape X_test : {X_test.shape}")
    
    return X_train, X_test, y_train, y_test, scaler

if __name__ == "__main__":
    # créé des données de test avec des problèmes volontaires
    np.random.seed(42)
    
    data = {
        'temperature': list(np.random.normal(20, 5, 95)) + [None, None, None, 100, -50],  # NaN + outliers
        'humidite': list(np.random.normal(60, 15, 98)) + [None, None],
        'pression': np.random.normal(1013, 10, 100),
        'categorie': np.random.choice(['A', 'B', 'C'], 100),
        'cible': np.random.randint(0, 2, 100)  # variable binaire à prédire
    }
    
    df = pd.DataFrame(data)
    
    # rajoute des doublons
    df = pd.concat([df, df.iloc[:5]], ignore_index=True)
    
    print("données de test créées avec :")
    print("- valeurs manquantes")
    print("- doublons")
    print("- outliers")
    print("- variables catégorielles")
    
    # applique le pipeline
    X_train, X_test, y_train, y_test, scaler = pipeline_complet(df, 'cible')
    
    # sauvegarde les données nettoyées
    # pratique pour les réutiliser après
    pd.concat([X_train, y_train], axis=1).to_csv('donnees_train_clean.csv', index=False)
    pd.concat([X_test, y_test], axis=1).to_csv('donnees_test_clean.csv', index=False)
    
    print("\ndonnées nettoyées sauvegardées dans donnees_train_clean.csv et donnees_test_clean.csv")
