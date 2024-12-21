import pandas as pd
import numpy as np
import pickle

def load_model(model_path="../models/knn_model.pkl"):
    try:
        with open(model_path, 'rb') as model_file:
            knn = pickle.load(model_file)
            print("Model başarıyla yüklendi.")
    except FileNotFoundError:
        print("Model dosyası bulunamadı. Lütfen modeli eğitin.")
        exit()
    return knn

def create_user_vector(X, kullanici_malzemeleri):
    return np.array([[1 if malzeme in kullanici_malzemeleri else 0 for malzeme in X.columns]])

def predict_recipes(knn, X, y, kullanici_vektoru, data):
    mesafeler, indeksler = knn.kneighbors(kullanici_vektoru)
    uygun_tarif_bulundu = False  

    for i, indeks in enumerate(indeksler[0]):
        benzerlik = 1 - mesafeler[0][i]
        if benzerlik >= 0.10:
            if(i==0):
                chat="Vermiş olduğunuz malzemelere uygun yemek tariflerini aşağıda verdim. Afiyet olsun :)\n" 
            tarif_adi = y.iloc[indeks]
            tarif_malzemeleri = X.columns[X.iloc[indeks] == 1].tolist() 
            chat+=f"\n{i+1}. {tarif_adi} (Benzerlik: {int(benzerlik * 100)}%)"
            chat+=f"\n   Malzemeler: {', '.join(tarif_malzemeleri)}"
            chat+=f"\n   Yapılışı: {data.iloc[indeks]['yapilis']}\n"

            uygun_tarif_bulundu = True 

    if not uygun_tarif_bulundu:
        chat="Maalesef, girdiğiniz malzemelere uygun bir tarif bulunamadı. Lütfen farklı malzemeler deneyin."
    return chat

def predict(ingredients):
    file_path = "../data/recipes.csv"
    data = pd.read_csv(file_path)

    y = data['yemekAdi']
    X = data.drop(columns=['yemekAdi', 'yapilis'])

    knn = load_model()

    kullanici_malzemeleri = [malzeme.strip() for malzeme in ingredients.split(',')]

    kullanici_vektoru = create_user_vector(X, kullanici_malzemeleri)

    return predict_recipes(knn, X, y, kullanici_vektoru, data)
