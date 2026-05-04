print("Hello")
# Задача 1: Паспорт объекта

# Переменные
student_name = "Алекс"
group_number = "ИС-22-1"
project_name = "ЖК Солнечный"
floors = 9
height = 27.0
is_residential = True
construction_year = 2023

# Вывод
print("=== ПАСПОРТ СТРОИТЕЛЬНОГО ОБЪЕКТА ===")
print("Составитель:", student_name)
print("Группа:", group_number)
print()
print("Объект:", project_name)
print("Этажность:", floors, "этажей")
print("Высота:", height, "м")

if is_residential:
    print("Тип: Жилой")
else:
    print("Тип: Нежилой")

print("Год постройки:", construction_year)

# Комментарий:
# Объект находится в вымышленном районе.
# Выбран для примера.