import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# NLTK için gerekli olan dil kaynağını indiriyoruz. Kelimeleri ayırmak için kullanılıyor
# nltk.download('punkt')

# Normalizasyon işlemi
def normalize_ingredient(malzemeler):
    normalized_units = {
        'yarım': '',    
        'büyük boy': '', 
        'küçük boy': '', 
        'isteğe bağlı': '', 
        'adedi': '', 
        'adet': '',
        'paket': '',
        'su bardağı' :'',
        'çay bardağı':'',
        'yemek kaşığı':'',
        'tatlı kaşığı':'',
        'çay kaşığı':'',
        'rendesi': '',
        'kızartmak için': '',
        'dal':'',
        'tutam':'',
        'hamur için':'',
        'iç harcı için':'',
        'demet':'',
        'taze':'',
        'tercihen dönerlik':'',
        '/':'',
        '()':'',
        'gram':'',
        'litre':''
    }

    units_and_numbers = r"\b\d+([.,]\d+)?\b"


    malzemeler = malzemeler.lower() 
    for unit, replacement in normalized_units.items():
        malzemeler = malzemeler.replace(unit, replacement)

    tokens = word_tokenize(malzemeler, language='turkish')

    cleaned_tokens = [token for token in tokens if not re.match(units_and_numbers, token)]

    cleaned_text = " ".join(cleaned_tokens)
    return cleaned_text

def clean_ingredient(malzemeler):
    return normalize_ingredient(malzemeler)

df = pd.read_json('./recipe.json')

df['cleaned_ingredients'] = df['malzemeler'].apply(lambda x: [clean_ingredient(malzemeler) for malzemeler in x])

all_ingredients = set(malzemeler for ingredients_list in df['cleaned_ingredients'] for malzemeler in ingredients_list)

ingredients_df = pd.DataFrame({
    malzemeler: df['cleaned_ingredients'].apply(lambda x: int(malzemeler in x))
    for malzemeler in all_ingredients
})

ingredients_df = ingredients_df.loc[:, ~ingredients_df.columns.duplicated()]

result_df = pd.concat([df.drop(columns=['malzemeler', 'cleaned_ingredients']), ingredients_df], axis=1)

result_df.to_csv('recipes.csv', encoding='utf-8', index=False)

