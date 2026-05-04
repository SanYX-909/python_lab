# Задача 2: Параметры помещения

# Размеры комнаты (в метрах)
length = 5.0
width = 4.0
height = 2.7

# Расчёты
floor_area = length * width  # площадь пола
wall_area = 2 * (length + width) * height  # площадь стен
volume = length * width * height  # объём

# Стоимость покраски (125 руб за м²)
paint_price_per_m2 = 125
paint_cost = wall_area * paint_price_per_m2

# Округление
floor_area = round(floor_area, 2)
wall_area = round(wall_area, 2)
volume = round(volume, 2)
paint_cost = round(paint_cost, 2)

# Вывод
print("=== ПАРАМЕТРЫ ПОМЕЩЕНИЯ ===")
print("Длина:", length, "м")
print("Ширина:", width, "м")
print("Высота:", height, "м")
print()
print("Площадь пола:", floor_area, "м²")
print("Площадь стен:", wall_area, "м²")
print("Объём:", volume, "м³")
print("Стоимость покраски:", paint_cost, "руб")
print("Расчёт завершён")

# Комментарий:
# Использованы стандартные формулы для расчёта площади и объёма