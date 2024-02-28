import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def replace_random_value(df):
    """permet de remplacer les valeur nulle
    par une valeur aléatoire de la colonne"""
    for col in df.columns:
        values_col = df[col].dropna().values #récupère les valeurs non nulles
        if df[col].isnull().sum() > 0: #vérifie si il ya un Nan dans la colonne
            # met une valeur aléatoire si elle est nulle 
            df[col] = df[col].apply(lambda x: np.random.choice(values_col) if pd.isnull(x) else x)
    return df

def normalisation_df(df):
    """Standardise les données, recentre et réduit"""
    return (df -df.mean(axis=0))/df.std(axis=0)

def scatter_plot_cause_effet(data,target,display=True):
    """Permet d'afficher les relations entre deux variables
    causes/effet dans un repère 2D"""
    for index, row in target.iterrows(): # permet d'ittérer sur les lignes et index (data.iterrows())
        source_var = row.iloc[0]
        target_var = row.iloc[1]

        # Sélection des données pour les variables source et cible
        x = data[source_var]
        y = data[target_var]
        
        if display:
            # Création du nuage de points
            plt.figure(figsize=(8, 6))
            plt.scatter(x, y)
            plt.title(f'Nuage de points : {source_var} → {target_var}')
            plt.xlabel(source_var)
            plt.ylabel(target_var)
            plt.show()

def find_cycle(target,data):
    """Affiche en fonction de la matrice d'adjacence d'un graphe
    si il y a des cycles dans le graphe en comparant avec les valeurs
    propres de la matrice d'adjacence"""

    unique_values = pd.unique(target.values.ravel('K'))
    #Le paramètre 'K' dans la méthode .ravel() spécifie que l'aplatissement 
    #doit être fait en suivant l'ordre de stockage en mémoire

    mapping = {value: i for i, value in enumerate(unique_values)}
    for col in target.columns:
        target[col] = target[col].map(mapping)
        
    N = len(data.columns)
    ajacent_matrix = np.zeros((N,N))
    for index,row in target.iterrows():
        try:
            i = row.iloc[0]
            j = row.iloc[1]
            ajacent_matrix[i,j]=1
        except:
            print(row.iloc[0][1:],row.iloc[1][1:])
            
    # Calculer les valeurs propres de la matrice d'adjacence avec leur multiplicité
    eigenvals = np.linalg.eigvals(ajacent_matrix)
    # Vérifier si l'une des valeurs propres est nulle (ou très proche de zéro) et renvoie un Booleen 
    all_eigen_values_null = np.isclose(eigenvals, 0).all()
    
    if all_eigen_values_null:
        print(f"Il n'y a pas de cycle dans le graphe")
    else:
        print("Il y a au moins un cycle dans le graphe")
        
    return eigenvals,all_eigen_values_null