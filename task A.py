import spacy

# Загрузим модель spaCy
nlp = spacy.load("en_core_web_sm")

# Входной текст
text = """Polls had predicted Bolsonaro's performance to be lower ahead of the first round, but they were, within the margin of error, accurate in the percentage of votes that Lula da Silva could receive. Now, in this final stage of a deeply polarized contest, some of the research institutes that conduct these polls are drawing attention to the choices being made by women voters."""

# Обрабатываем текст с помощью spaCy
doc = nlp(text)

# Функция для замены именованных сущностей на ссылки
def replace_with_link(text):
    result = text
    for ent in doc.ents:
        # Отфильтровываем только сущности типа PERSON, ORG, GPE
        if ent.label_ in ["PERSON", "ORG", "GPE"]:
            # Строим URL для Wikipedia
            wiki_url = f"https://en.wikipedia.org/wiki/{ent.text.replace(' ', '_')}"
            # Заменяем сущность на HTML-ссылку
            result = result.replace(ent.text, f'<a href="{wiki_url}">{ent.text}</a>')
    return result

# Применяем функцию
html_result = replace_with_link(text)

# Выводим результат
print(html_result)
