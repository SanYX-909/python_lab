# Задача 10: Система учета склада (обновленная версия)

warehouse = {
    "Ламинат": {"quantity": 85, "price": 1350.00, "min_quantity": 60},
    "Краска": {"quantity": 40, "price": 2200.00, "min_quantity": 50},
    "Шпаклевка": {"quantity": 25, "price": 480.00, "min_quantity": 30},
    "Плитка": {"quantity": 120, "price": 1750.00, "min_quantity": 100},
    "Профиль": {"quantity": 18, "price": 320.00, "min_quantity": 25}
}

print("=" * 70)
print("СИСТЕМА УЧЁТА СКЛАДА")
print("=" * 70)

print("Материал   | Кол-во | Цена    | Мин. | Стоимость")
print("-" * 70)

total_value = 0
most_expensive = ("", 0)
critical = []

for name, data in warehouse.items():
    q = data["quantity"]
    p = data["price"]
    m = data["min_quantity"]

    cost = q * p
    total_value += cost

    # Самый дорогой материал (по общей стоимости)
    if cost > most_expensive[1]:
        most_expensive = (name, cost)

    # Критические остатки
    warning = ""
    if q < m:
        warning = "⚠ КРИТИЧНО!"
        critical.append(f"{name}: {q} < {m}")

    print(f"{name:10} | {q:6} | {p:7.2f} | {m:4} | {cost:10.2f} {warning}")

print("-" * 70)
print(f"ОБЩАЯ СТОИМОСТЬ: {total_value:.2f} руб")

print(f"Самый дорогой: {most_expensive[0]} ({most_expensive[1]:.2f} руб)")

print("\n⚠ КРИТИЧЕСКИЕ ОСТАТКИ:")
if critical:
    for item in critical:
        print("-", item)
else:
    print("Нет")

# === Выдача материала ===
print("\n=== ВЫДАЧА МАТЕРИАЛА ===")

material = "Краска"
issued = 15

if material in warehouse:
    before = warehouse[material]["quantity"]
    warehouse[material]["quantity"] -= issued
    after = warehouse[material]["quantity"]

    print(f"✓ Выдано {issued} единиц '{material}'")
    print(f"Остаток: {before} → {after}")
else:
    print("Материал не найден")