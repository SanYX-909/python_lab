# Задача 8: Анализ заказов

# Материалы трех подрядчиков
contractor_1 = {"Ламинат", "Краска", "Шпаклевка", "Грунтовка"}
contractor_2 = {"Краска", "Плитка", "Грунтовка", "Клей"}
contractor_3 = {"Грунтовка", "Клей", "Гипсокартон", "Ламинат"}

print("Подрядчик 1:", contractor_1)
print("Подрядчик 2:", contractor_2)
print("Подрядчик 3:", contractor_3)

# 1. Все уникальные материалы
all_materials = contractor_1 | contractor_2 | contractor_3

# 2. Общие для всех
common_all = contractor_1 & contractor_2 & contractor_3

# 3. Только у первого
only_first = contractor_1 - contractor_2 - contractor_3

# 4. Ровно у двух
only_two = (
    (contractor_1 & contractor_2) |
    (contractor_1 & contractor_3) |
    (contractor_2 & contractor_3)
) - common_all

print("\n=== АНАЛИЗ ===")
print("Все уникальные:", all_materials)
print("Общие для всех:", common_all)
print("Только у первого:", only_first)
print("Ровно у двух:", only_two)