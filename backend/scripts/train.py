import pandas as pd
import pickle
from sklearn.neighbors import NearestNeighbors

def train_model(X, model_path="models/knn_model.pkl"):
    knn = NearestNeighbors(n_neighbors=3, metric='jaccard')
    knn.fit(X.values)
    

    with open(model_path, 'wb') as model_file:
        pickle.dump(knn, model_file)
        print("Model başarıyla eğitildi ve kaydedildi.")

if __name__ == "__main__":
    file_path = "data/recipes.csv"
    data = pd.read_csv(file_path)

    X = data.drop(columns=['yemekAdi', 'yapilis'])

    train_model(X)
