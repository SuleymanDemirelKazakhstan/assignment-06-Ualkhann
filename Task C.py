import spacy
import pandas as pd
import os
from collections import defaultdict

nlp = spacy.load("en_core_web_sm")

categories = ['business', 'entertainment', 'politics', 'sport', 'tech']
data_path = "c:/Users/HP/Downloads/assignment-06-Ualkhann-main/assignment-06-Ualkhann-main/bbc-fulltext/bbc/" 

entity_counts = defaultdict(lambda: defaultdict(int))

for category in categories:
    category_path = f"{data_path}/{category}"
    for filename in os.listdir(category_path):
        file_path = f"{category_path}/{filename}"
        
        try:
            # Пробуем открыть файл с 'utf-8', но обрабатываем ошибки
            with open(file_path, "r", encoding="utf-8", errors="replace") as file:
                text = file.read()
        except Exception as e:
            print(f"Ошибка при чтении файла {filename}: {e}")
            continue

        # Обработка текста SpaCy
        doc = nlp(text)
        for ent in doc.ents:
            entity_key = f"{ent.text}_{ent.label_}"
            entity_counts[entity_key][category] += 1

# Преобразуем результат в DataFrame
result = pd.DataFrame(entity_counts).T.fillna(0).astype(int)
result.index.name = 'word'
result.reset_index(inplace=True)

# Сохраняем в CSV
result.to_csv("named_entities.csv", index=False)
print("CSV-файл сохранен как 'named_entities.csv'.")
