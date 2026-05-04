# Задача 7: Прайс-лист материалов

# Создание словаря
materials = {
    "Кирпич": 12.5,
    "Цемент": 450,
    "Песок": 800,
    "Арматура": 48000,
    "Бетон": 4200
}

# Вывод
print("Исходный список материалов:")
for name, price in materials.items():
    print(name, "-", price, "руб")

    # Добавление новых материалов
materials["Гипс"] = 300
materials["Дерево"] = 1500

# Изменение цены (+10%)
materials["Кирпич"] = materials["Кирпич"] * 1.1

print("\nПосле изменений:")
for name, price in materials.items():
    print(name, "-", round(price, 2), "руб")

    # Удаление одного материала
materials.pop("Песок")

# Расчет средней цены
average_price = sum(materials.values()) / len(materials)

print("\nПосле удаления:")
for name, price in materials.items():
    print(name, "-", round(price, 2), "руб")

print("\nСредняя цена:", round(average_price, 2), "руб")