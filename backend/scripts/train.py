import pandas as pd
import pickle
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import KFold


def cross_validate_model(X, k=3, model_path="../models/knn_model.pkl"):
    kf = KFold(n_splits=k, shuffle=True, random_state=42)
    fold_scores = []

    for fold, (train_index, test_index) in enumerate(kf.split(X)):
        print(f"Fold {fold + 1}/{k}")

        X_train, X_test = X.iloc[train_index], X.iloc[test_index]

        knn = NearestNeighbors(n_neighbors=3, metric='cosine')
        knn.fit(X_train.values)

        distances, _ = knn.kneighbors(X_test.values)

        avg_distance = distances.mean()
        fold_scores.append(avg_distance)
        print(f"Fold {fold + 1} - Ortalama Mesafe: {avg_distance:.4f}\n")

    print(f"{k}-Fold Çapraz Doğrulama Ortalama Mesafe: {sum(fold_scores) / len(fold_scores):.4f}")

    knn.fit(X.values)
    with open(model_path, 'wb') as model_file:
        pickle.dump(knn, model_file)
        print("Son model başarıyla eğitildi ve kaydedildi.")


if __name__ == "__main__":
    file_path = "../data/recipes.csv"
    data = pd.read_csv(file_path)

    X = data.drop(columns=['yemekAdi', 'yapilis'])

    cross_validate_model(X)

