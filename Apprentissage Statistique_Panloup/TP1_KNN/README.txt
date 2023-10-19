# Le premier fichier: Exercice_3.ipynb

Indication : assurez-vous de changer les variables path_train et path_test dans le code avec 'mnist_train.csv' et 'mnist_test.csv' si les données se trouvent dans le même répertoire.

- La première partie présente les questions de l'exercice 3 du TP1_KNN.

- Une partie deux est réservée à l'application Grid_search_CV du module Sklearn. Cette fonctionnalité permet de trouver le modèle le plus performant au sens de l'erreur moyenne de classification pour une famille de paramètres proposés en amont.

- Une partie est réservée à la réduction de dimension avec l'ACP et l'apprentissage d'un modèle KNN sur ces données de plus petite dimension. Le résultat n'est pas très bon mais le temps d'entraînement est bien plus rapide.

- La dernière partie est réservée à la réduction de dimension avec la méthode UMAP et l'apprentissage d'un modèle KNN sur ces données de plus petite dimension. Le résultat est équivalent voire meilleur selon les données d'entraînement et de test, de plus le temps d'entraînement est bien plus rapide. Le seul inconvénient est qu'il n'existe pas de fonction explicite pour modifier les nouvelles données et ainsi faire de la prédiction future.

# Le second fichier: Exploration_personnelle_exo_3.ipynb

- Ce notebook est une initiative personnelle de recherche. J'ai essayé de grouper par catégories les données d'entraînement.
J'ai regardé par groupe et par pixel la valeur moyenne qui lui était attribuée. J'ai ensuite normalisé pour avoir une mesure de probabilité associée à chaque classe (0,1,...,9). Enfin pour chaque photo test, j'ai normalisé les valeurs pour obtenir probabilité. Enfin, j'ai mis en place un critère d'attribution d'une classe en utilisant les "distances" sur un ensemble de probabilité (divergence de Kulback Leiber, variation totale et autres...). Les résultats ne sont vraiment pas bons, cependant je partage cette recherche pour vous montrer mon travail sur cette voie.
