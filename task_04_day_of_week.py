# Задача 4: День недели

# Ввод числа
day_number = int(input("Введите число от 1 до 7: "))

# Определение дня недели
if day_number == 1:
    day = "Понедельник"
elif day_number == 2:
    day = "Вторник"
elif day_number == 3:
    day = "Среда"
elif day_number == 4:
    day = "Четверг"
elif day_number == 5:
    day = "Пятница"
elif day_number == 6:
    day = "Суббота"
elif day_number == 7:
    day = "Воскресенье"
else:
    day = "Некорректный ввод"

print("День недели:", day)

# Определение типа дня
if day_number in [6, 7]:
    day_type = "Выходной"
elif 1 <= day_number <= 5:
    day_type = "Рабочий день"
else:
    day_type = ""

print("Тип дня:", day_type)