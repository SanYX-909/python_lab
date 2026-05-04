# Задача 1: Паспорт объекта

# Переменные
student_name = "Кузьмин Александр Андреевич"
group_number = "3150801/10101"
project_name = "ЖК \"Шишкино\""
floors = 22
height = 72.6
is_residential = True
construction_year = 2024

# Вывод
print("=== ПАСПОРТ СТРОИТЕЛЬНОГО ОБЪЕКТА ===")
print("Составитель:", student_name)
print("Группа:", group_number)
print()
print("Объект:", project_name)
print("Этажность:", floors, "этажа")
print("Высота:", height, "м")

if is_residential:
    print("Тип: Жилой")
else:
    print("Тип: Нежилой")

print("Год постройки:", construction_year)

# Комментарий:
# Объект находится в вымышленном районе.
# Выбран ЖК, который я проектировал в университет в курсовом проекте.