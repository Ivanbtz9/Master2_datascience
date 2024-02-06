# import numpy as np
import pandas as pd

from joblib import load
# import plotly.express as px
from dash import Dash, html, Input, Output, dcc

import dash_bootstrap_components as dbc

import plotly.express as px




app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP]) ##dbc 
#crée une instance de l'application Dash. __name__ est utilisé pour indiquer le nom du module actuel (c'est-à-dire le nom de ce fichier Python).
#external_stylesheets permet de spécifier des feuilles de style externes pour la mise en page de l'application.

linear_model = load("linear_model.joblib") #charge un model de regression linéaire

df = pd.read_csv("/home/ibotcazou/Bureau/Master_data_science/Master2_datascience/Informatique/machine_learning_operating/tp_dash/new_data.csv",index_col=0)

"""utilisateur est composée de plusieurs éléments HTML et composants Dash."""   

app.layout = html.Div(children=[ #contener , children arg de dash
    html.H6("Saisissez le texte de votre choix ci-dessous :"),#Titre 
    html.Div([ 
        "Input: ",
        dcc.Input(id='my-input', value='toto', type='text') #boite, valeur de base 
        ]),
    html.Br(),
    html.Div(id='my-output'), #contener
    html.Br(),
    html.H6("Scatter plot :"),#Titre 
    dcc.Dropdown(
        id='column-dropdown', #choisir la colonne 
        options=[{'label': col, 'value': col} for col in df.columns[:-1]],  # Options pour les colonnes Xi
        value=df.columns[0],  # Valeur par défaut (première colonne du DataFrame)
    ),
    # Ajoutez un composant dcc.Graph pour afficher le scatter plot
    dcc.Graph(id='scatter-plot'),
])


# Exemple de callback simple
""" @app.callback : Cette décoration indique que la fonction update_output_div est un callback. 
Les callbacks sont utilisés pour mettre à jour dynamiquement l'interface utilisateur en fonction de l'entrée de l'utilisateur."""

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
    
    
)
def update_output_div(input_value):
    try:
        input_value = float(input_value)
        return f'Output: {input_value**2}'
    except:
        return f'Output: {input_value}'


# Questions

# 0. Exécuter python app.py et tester le dashboard.

# 1. Définir un callback permettant de tracer un scatter plot (avec px.scatter(...))
# avec en abscisses une colonne Xi du dataframe df au choix de l'utilisateur
# (définie par un dropdown placé dans le layout ci-dessus)
# et en ordonnées la colonne y du dataframe df

@app.callback(
    Output('scatter-plot', 'figure'),
    Input('column-dropdown', 'value')   
    
)

def update_scatter_plot(selected_column_xi):
    # Créez un scatter plot avec Plotly Express en utilisant la colonne Xi sélectionnée
    fig = px.scatter(df, x=selected_column_xi, y='y', title=f'Scatter Plot: {selected_column_xi} vs. y')
    
    return fig


# 2. Définir un 2e callback permettant, à partir des valeurs de X0, X1, X2
# choisies avec 3 sliders placés dans le layout ci-dessus
# de calculer la prévision de y correspondante (en utilisant linear_model)
# et de l'afficher dans le dashboard




# Questions subsidiaires :
# 3. Tracer un histogramme de Xi (selon le choix du dropdown utilisé en 1.)
#
# 4. Modifier le graphe du 1er callback pour qu'il affiche le point (Xi, y_pred),
# où y_pred est calculé dans la question 2.
#
# 5. Aligner les 3 sliders sur la même ligne


if __name__ == '__main__':
    app.run_server(debug=True)
