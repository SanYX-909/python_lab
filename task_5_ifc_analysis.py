import ifcopenshell


file_path = r"C:\Users\66910\ifc\Example_1.ifc"

model = ifcopenshell.open(file_path)

doors = model.by_type("IfcDoor")

min_width = 0   # задать значение которые позволит разделить двери на узкие и нормальные

narrow_doors = []

for door in doors:
    name = door.Name
    width = getattr(door, "OverallWidth", None)
    heigth = getattr(door, "OverallHeight", None)

    # добавить условие если ширина меньше минимальной - добавить в список узких дверей

    print("Дверь:", name, "Ширина", round(width), "Высота", heigth)

# код для построчного вывода узких дверей, в таком же формате, как и нормальных