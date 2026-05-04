# Задача 10: Система учета склада

warehouse = {
    "Кирпич": {"quantity": 5000, "price": 12.50, "min_quantity": 1000},
    "Цемент": {"quantity": 120, "price": 450.00, "min_quantity": 50},
    "Песок": {"quantity": 8, "price": 800.00, "min_quantity": 10},
    "Арматура": {"quantity": 30, "price": 48000.00, "min_quantity": 20},
    "Бетон": {"quantity": 45, "price": 4200.00, "min_quantity": 15}
}

print("=" * 65)
print("СИСТЕМА УЧЁТА СКЛАДА")
print("=" * 65)

print("Материал | Кол-во | Цена | Мин. | Стоимость")
print("-" * 65)

total_value = 0
most_expensive = ("", 0)
critical = []

for name, data in warehouse.items():
    q = data["quantity"]
    p = data["price"]
    m = data["min_quantity"]

    cost = q * p
    total_value += cost

    # Проверка самого дорогого
    if cost > most_expensive[1]:
        most_expensive = (name, cost)

    # Проверка критического остатка
    warning = ""
    if q < m:
        warning = "⚠ КРИТИЧНО!"
        critical.append(f"{name}: {q} < {m}")

    print(f"{name:8} | {q:6} | {p:6.2f} | {m:4} | {cost:10.2f} {warning}")

print("-" * 65)
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

material = "Цемент"
issued = 25

if material in warehouse:
    before = warehouse[material]["quantity"]
    warehouse[material]["quantity"] -= issued
    after = warehouse[material]["quantity"]

    print(f"✓ Выдано {issued} единиц '{material}'")
    print(f"Остаток: {before} → {after}")
else:
    print("Материал не найден")