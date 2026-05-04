# Задача 4: День недели

# Ввод числа
day_number = int(input("Введите число от 1 до 7: "))

# Определение дня недели
days = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье"
}

if day_number in days:
    day = days[day_number]
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