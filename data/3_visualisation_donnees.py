# -*- coding: utf-8 -*-
"""
Prog 3 : Visualisation des données
Pour le rendu à faire avec de beaux graphiques via matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# config 
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

def graphique_distribution(df, colonne):
    """
    Fait un histogramme pour voir la distribution
    + une courbe de densité parce que ça fait pro...
    """
    plt.figure()
    
    # histogramme
    plt.hist(df[colonne], bins=30, alpha=0.7, color='skyblue', edgecolor='black')
    
    plt.title(f'Distribution de {colonne}')
    plt.xlabel(colonne)
    plt.ylabel('fréquence')
    plt.grid(True, alpha=0.3)
    
    # sauvegarde
    nom_fichier = f'histo_{colonne}.png'
    plt.savefig(nom_fichier, dpi=300, bbox_inches='tight')
    print(f"graphique sauvegardé : {nom_fichier}")
    plt.close()

def graphique_boite(df):
    """
    Boxplot pour toutes les variables
    pratique pour voir les outliers d'un coup
    """
    colonnes_num = df.select_dtypes(include=[np.number]).columns
    
    plt.figure()
    df[colonnes_num].boxplot()
    plt.title('Boîtes à moustaches')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.savefig('boxplots.png', dpi=300)
    print("boxplots sauvegardés")
    plt.close()

def graphique_correlation(df):
    """
    Heatmap de corrélation
    c'est stylé et ça impressionne toujours...
    """
    colonnes_num = df.select_dtypes(include=[np.number]).columns
    corr = df[colonnes_num].corr()
    
    plt.figure()
    # annot=True pour afficher les valeurs
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0,
                square=True, linewidths=1)
    plt.title('Matrice de corrélation')
    plt.tight_layout()
    
    plt.savefig('heatmap_correlation.png', dpi=300)
    print("heatmap sauvegardée")
    plt.close()

def graphique_scatter(df, col_x, col_y):
    """
    Nuage de points pour voir la relation entre 2 variables
    """
    plt.figure()
    plt.scatter(df[col_x], df[col_y], alpha=0.6, color='coral')
    
    # ajoute une ligne de tendance c'est la classe
    z = np.polyfit(df[col_x], df[col_y], 1)
    p = np.poly1d(z)
    plt.plot(df[col_x], p(df[col_x]), "r--", alpha=0.8, label='tendance')
    
    plt.xlabel(col_x)
    plt.ylabel(col_y)
    plt.title(f'{col_y} en fonction de {col_x}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.savefig(f'scatter_{col_x}_{col_y}.png', dpi=300, bbox_inches='tight')
    print(f"scatter plot sauvegardé")
    plt.close()

def graphique_evolution(df, colonne_temps, colonne_valeur):
    """
    Graphique temporel si on a des dates
    pas sûr que ça serve mais au cas où
    """
    plt.figure()
    plt.plot(df[colonne_temps], df[colonne_valeur], marker='o', linestyle='-')
    plt.xlabel(colonne_temps)
    plt.ylabel(colonne_valeur)
    plt.title(f'Évolution de {colonne_valeur}')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    plt.savefig('evolution_temporelle.png', dpi=300)
    print("graphique temporel sauvegardé")
    plt.close()

# fonction pour tout faire d'un coup
def faire_tous_les_graphiques(df):
    """génère tous les graphiques standard"""
    colonnes_num = df.select_dtypes(include=[np.number]).columns
    
    print("génération des graphiques...")
    
    # distributions
    for col in colonnes_num:
        graphique_distribution(df, col)
    
    # boxplots
    graphique_boite(df)
    
    # heatmap
    graphique_correlation(df)
    
    # scatter plots pour les premières variables
    if len(colonnes_num) >= 2:
        graphique_scatter(df, colonnes_num[0], colonnes_num[1])
    
    print("tous les graphiques sont prêts !")

if __name__ == "__main__":
    # crée des données de test
    np.random.seed(42)
    data = {
        'temperature': np.random.normal(20, 5, 100),
        'humidite': np.random.normal(60, 15, 100),
        'pression': np.random.normal(1013, 10, 100),
        'vent': np.random.exponential(10, 100)
    }
    df = pd.DataFrame(data)
    
    # génère tout
    faire_tous_les_graphiques(df)
