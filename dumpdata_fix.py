import json

# Попробуем открыть файл с кодировкой 'utf-8', игнорируя ошибки
with open("fixtures/goods/categories.json", "r", encoding="utf-8", errors="ignore") as file:
    data = json.load(file)

# Сохраняем данные с нужной кодировкой
with open("fixtures/goods/products_fixed.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Файл успешно преобразован и сохранён.")
