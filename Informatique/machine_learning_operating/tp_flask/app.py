# import datetime
# from joblib import dump, load
from flask import Flask, request, jsonify
import pandas as pd
import datetime
import joblib
import json

app = Flask(__name__)

# Exemple d'une route GET simple :


@app.route("/route1", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

# Exercice 1 - Créer une route "/date" qui montre la date et l'heure du jour
# (utiliser datetime.datetime.now()).
@app.route("/date", methods=['GET'])
def today():
    return str(datetime.datetime.today()).split()[0]

# Exemple d'une route GET avec paramètres

@app.route("/print-param", methods=['GET']) #http://172.18.105.182:5000/print-param?param1=10&param2=Hello
def print_param():
    param1 = request.args.get("param1", default=42) #ceci est un dictionnaire
    param2 = request.args["param2"]
    print(type(param1), type(param2))
    return f"<p>{param1}: {param2}<p>"

# Exercice 2 - Créer une route qui affiche le carré d'un flottant passé en argument
# (que faire si l'utilisateur envoie une chaîne de caractères ou rien ?).

@app.route("/square", methods=['GET']) #http://172.18.105.182:5000/print-param?param1=10&param2=Hello
def square():
    try:
        param1 = float(request.args.get("param1", default=0)) #ceci est un dictionnaire
        square = param1**2
        return f"<p>Le carré de {param1} est : {square:.2f}<p>" #pour avoir chiffre derrière la virgule
    except Exception as e :
        return f"<p>Il faut entrer un nombre et non une chaine de caractères car il a cette erreur {e}<p>", 400 #pour renvoyer une erreur de type 400 

# Exemple d'une route POST
@app.route("/add-json-value", methods=['POST']) #une requete post ne peux pas se voir du navigateur
def add_json_value():
    json_data = request.json

    if json_data is not None:
        json_data['test'] = 'ok'
    else:
        json_data['test'] = 'error'

    return jsonify(json_data),200

# Pour tester cette requête, ouvrir un autre terminal et y taper la commande :
# python client.py -r add-json-value


# Exercice 3 - Créer une route 'predict' qui reçoit un JSON, calcule des prévisions
# à partir de ce JSON (et du modèle créé dans creation_modele.ipynb)
# et renvoie un JSON contenant les prévisions.
# Puis compléter le fichier client.py (fonction push_data_for_predict())
# pour envoyer une requête avec les nouvelles données (créées dans le notebook)
# afin de tester cette route.

# Exemple d'une route POST
@app.route("/predict", methods=['POST']) #une requete post ne peux pas se voir du navigateur
def prediction_json_value():
    json_data = request.json

    X = pd.DataFrame(json_data)
    if X.dtype != float:
            return f"Les données envoyée sont du type {X.dtype} cela ne peut pas fonctionner il faut entrer des nombres",400
    else:
        try:
            # Charger un modèle pré-entraîné depuis un fichier
            model = joblib.load('linear_model.joblib')
            # Utiliser le modèle pour effectuer des prédictions
            predictions = model.predict(X).tolist()

            predictions_json = json.dumps(predictions) #créer un json

            return jsonify(predictions_json),200
        except Exception as e:
            return f"Vous avez une erreur du type {e}",400
        
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
