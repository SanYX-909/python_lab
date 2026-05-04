# Задача 8: Работа с множествами

# Материалы на складе 1
warehouse_1 = {"Кирпич", "Цемент", "Песок", "Арматура"}

# Материалы на складе 2
warehouse_2 = {"Цемент", "Песок", "Бетон", "Гипс"}

# Вывод
print("Склад 1:", warehouse_1)
print("Склад 2:", warehouse_2)

# Общие материалы
common = warehouse_1 & warehouse_2

# Уникальные
only_1 = warehouse_1 - warehouse_2
only_2 = warehouse_2 - warehouse_1

print("\nОбщие материалы:", common)
print("Только на складе 1:", only_1)
print("Только на складе 2:", only_2)

# Объединение
all_materials = warehouse_1 | warehouse_2

print("\nВсе материалы:", all_materials)