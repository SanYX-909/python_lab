import ifcopenshell

file_path = r"C:\Users\66910\ifc\Example_1.ifc"

model = ifcopenshell.open(file_path)

doors = model.by_type("IfcDoor")

min_width = 800  # например, 800 мм — граница

narrow_doors = []

for door in doors:
    name = door.Name
    width = getattr(door, "OverallWidth", None)
    height = getattr(door, "OverallHeight", None)

    # Проверка на None (чтобы не падало)
    if width is not None:
        width_mm = round(width * 1000)  # IFC часто в метрах → переводим в мм

        # Условие узких дверей
        if width_mm < min_width:
            narrow_doors.append((name, width_mm, height))

        print("Дверь:", name, "Ширина", width_mm, "мм", "Высота", height)

# Вывод узких дверей
print("\n=== УЗКИЕ ДВЕРИ ===")

for name, width, height in narrow_doors:
    print("Дверь:", name, "Ширина", width, "мм", "Высота", height)

print("\nКоличество узких дверей:", len(narrow_doors))