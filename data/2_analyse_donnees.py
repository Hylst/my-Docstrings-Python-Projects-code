# -*- coding: utf-8 -*-
"""
Prog 2 : Analyse des données
Pour le tp de stats descriptives
pour calculs basiques genre moyenne, médiane...
"""

import pandas as pd
import numpy as np

def charger_donnees(fichier):
    """charge le csv, rien de fou"""
    try:
        df = pd.read_csv(fichier)
        print(f"fichier chargé : {len(df)} lignes")
        return df
    except:
        print("erreur le fichier existe pas")
        return None

def stats_basiques(df, colonne):
    """
    Calcule les stats de base
    moyenne médiane écart type etc
    """
    print(f"\n=== Stats pour {colonne} ===")
    print(f"moyenne : {df[colonne].mean():.2f}")
    print(f"médiane : {df[colonne].median():.2f}")
    print(f"min : {df[colonne].min():.2f}")
    print(f"max : {df[colonne].max():.2f}")
    print(f"écart-type : {df[colonne].std():.2f}")
    
    # les quartiles aussi 
    q1 = df[colonne].quantile(0.25)
    q3 = df[colonne].quantile(0.75)
    print(f"Q1 (25%) : {q1:.2f}")
    print(f"Q3 (75%) : {q3:.2f}")

def detecter_valeurs_aberrantes(df, colonne):

    # Trouve les valeurs bizarres avec la méthode IQR

    q1 = df[colonne].quantile(0.25)
    q3 = df[colonne].quantile(0.75)
    iqr = q3 - q1
    
    # formule qu'on a appris : valeur aberrante si en dehors de [Q1-1.5*IQR, Q3+1.5*IQR]
    limite_basse = q1 - 1.5 * iqr
    limite_haute = q3 + 1.5 * iqr
    
    aberrantes = df[(df[colonne] < limite_basse) | (df[colonne] > limite_haute)]
    
    print(f"\nValeurs aberrantes détectées : {len(aberrantes)}")
    if len(aberrantes) > 0:
        print(aberrantes)

def analyser_correlations(df):
    """
    regarde si y'a des corrélations entre les variables
    utile pour après quand on fera du ML
    """
    # prend que les colonnes numériques sinon ça plante
    colonnes_num = df.select_dtypes(include=[np.number]).columns
    
    print("\n=== Matrice de corrélation ===")
    corr = df[colonnes_num].corr()
    print(corr)
    
    # trouve les corrélations fortes (>0.7 ou <-0.7)
    print("\ncorrélations fortes :")
    for i in range(len(corr.columns)):
        for j in range(i+1, len(corr.columns)):
            if abs(corr.iloc[i,j]) > 0.7:
                print(f"{corr.columns[i]} <-> {corr.columns[j]} : {corr.iloc[i,j]:.2f}")

# pour créer des données de test rapidement
def creer_donnees_test():
    """génère un csv de test au cas où"""
    np.random.seed(42)  # pour que ce soit reproductible
    
    data = {
        'temperature': np.random.normal(20, 5, 100),  # moyenne 20, écart-type 5
        'humidite': np.random.normal(60, 15, 100),
        'pression': np.random.normal(1013, 10, 100),
        'vent': np.random.exponential(10, 100)  # distribution exponentielle pour le vent
    }
    
    df = pd.DataFrame(data)
    df.to_csv('donnees_test.csv', index=False)
    print("données de test créées")

if __name__ == "__main__":
    # test avec des données random
    creer_donnees_test()
    
    # charge et analyse
    df = charger_donnees('donnees_test.csv')
    
    if df is not None:
        # analyse chaque colonne
        for col in df.select_dtypes(include=[np.number]).columns:
            stats_basiques(df, col)
            detecter_valeurs_aberrantes(df, col)
        
        # corrélations
        analyser_correlations(df)
