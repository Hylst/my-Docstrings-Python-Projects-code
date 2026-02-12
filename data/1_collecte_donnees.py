# -*- coding: utf-8 -*-
"""
Prog 1 : Récupération de données depuis une API
Pour le cours de data science sur Kaggle
"""

import requests
import json
import pandas as pd
from datetime import datetime

# bon alors ici je vais chercher des données météo parce que c'est gratuit
# faudra changer l'api key si tu veux l'utiliser pour de vrai

def recuperer_donnees_meteo(ville):
    """
    Récupère les données météo pour une ville
    j'utilise une api random que j'ai trouvé sur internet
    """
    # normalement faut une clé API mais flemme de m'inscrire
    # donc je vais juste simuler avec des données fictives pour l'exemple
    
    # api_key = "ta_cle_ici"  # faut s'inscrire sur openweathermap
    # url = f"http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}"
    
    # comme j'ai pas d'api key je simule juste
    donnees_test = {
        'ville': ville,
        'temperature': 15.5,
        'humidite': 65,
        'pression': 1013,
        'vent': 12.3,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    return donnees_test

def sauvegarder_en_csv(donnees, nom_fichier):
    """
    Sauvegarde les données dans un csv
    plus pratique pour après
    """
    df = pd.DataFrame([donnees])  # faut mettre entre [] sinon ça marche pas
    
    # si le fichier existe déjà on rajoute à la fin
    try:
        df_existant = pd.read_csv(nom_fichier)
        df = pd.concat([df_existant, df], ignore_index=True)
    except:
        pass  # si erreur c'est que le fichier existe pas encore
    
    df.to_csv(nom_fichier, index=False)
    print(f"données sauvegardées dans {nom_fichier}")

# le main comme le prof nous a montré
if __name__ == "__main__":
    villes = ['Paris', 'Lyon', 'Marseille', 'Toulouse']
    
    print("début de la collecte...")
    
    for ville in villes:
        print(f"récupération pour {ville}")
        donnees = recuperer_donnees_meteo(ville)
        sauvegarder_en_csv(donnees, 'donnees_meteo.csv')
    
    print("c'est bon tout est récupéré !")
    
    # affiche un aperçu
    df = pd.read_csv('donnees_meteo.csv')
    print("\naperçu des données:")
    print(df.head())
