import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif

def filter_feature_selection(data, target_column, k_features):
    # Remplacer les valeurs non numériques par la moyenne de la colonne respective
    data = data.apply(pd.to_numeric, errors='coerce')
    data = data.fillna(data.mean())

    # Séparer les fonctionnalités et la cible
    X = data.drop(target_column, axis=1)
    y = data[target_column]

    # Utiliser SelectKBest avec la corrélation de Pearson comme mesure
    selector = SelectKBest(score_func=f_classif, k=k_features)
    X_new = selector.fit_transform(X, y)

    # Afficher les colonnes sélectionnées
    selected_columns = X.columns[selector.get_support()]
    print("Colonnes sélectionnées:", selected_columns)

    # Retourner le nouvel ensemble de données avec les caractéristiques sélectionnées
    selected_data = pd.DataFrame(data=X_new, columns=selected_columns)
    selected_data[target_column] = y  # Ajouter la colonne cible
    return selected_data

# Fonction pour charger les données à partir d'un fichier XLSX
def load_data(file_path):
    data = pd.read_excel(file_path)
    return data

# Exemple d'utilisation
if __name__ == "__main__":
    # Entrer le chemin du fichier XLSX (remplacez cela par le chemin de votre fichier)
    file_path = input("Veuillez entrer le chemin vers le fichier XLSX : ")
    
    # Charger les données à partir du fichier XLSX
    data = load_data(file_path)

    # Entrer la colonne cible
    target_column = input("Veuillez entrer le nom de la colonne cible : ")

    # Entrer le nombre de caractéristiques à sélectionner
    k_features = int(input("Veuillez entrer le nombre de caractéristiques à sélectionner : "))

    # Appliquer la sélection des caractéristiques
    selected_data = filter_feature_selection(data, target_column, k_features)
    
    # Afficher l'ensemble de données résultant
    print("\nEnsemble de données après sélection des caractéristiques:")
    print(selected_data)
