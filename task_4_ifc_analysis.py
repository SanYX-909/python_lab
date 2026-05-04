import ifcopenshell


file_path = r"C:\Users\66910\ifc\Example_1.ifc"

model = ifcopenshell.open(file_path)


storeys = model.by_type("IfcBuildingStorey")
# walls
# doors
# window

print("Схема IFC:", model.schema)
print("Этажей:", len(storeys))

# дополнить код, распечатав значения количества стен, дверей, окон

walls = model.by_type("IfcWall")
doors = model.by_type("IfcDoor")
windows = model.by_type("IfcWindow")

print("Стен:", len(walls))
print("Дверей:", len(doors))
print("Окон:", len(windows))