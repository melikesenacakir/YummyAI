import json

with open('data/recipe.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

def remove_duplicate_meals(data):
    seen = set()  
    result = []
    
    for item in data:
        yemek_adi = item['yemekAdi']
        if yemek_adi not in seen:
            result.append(item)
            seen.add(yemek_adi)
    
    return result

cleaned_data = remove_duplicate_meals(json_data)

with open('cleanedData.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_data, f, ensure_ascii=False, indent=2)

print("Temizlenen veriler 'cleanedData.json' dosyasına yazıldı.")