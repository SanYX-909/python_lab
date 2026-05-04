# Задача 10: Склад

warehouse = {
    "Кирпич": {"quantity": 5000, "price": 12.5, "min_quantity": 1000},
    "Цемент": {"quantity": 120, "price": 450, "min_quantity": 50},
    "Песок": {"quantity": 8, "price": 800, "min_quantity": 10},
    "Арматура": {"quantity": 30, "price": 48000, "min_quantity": 20},
    "Бетон": {"quantity": 45, "price": 4200, "min_quantity": 15}
}

print("Склад:")
for name, data in warehouse.items():
    print(name, "-", data)

    print("\nТовары ниже минимального запаса:")

for name, data in warehouse.items():
    if data["quantity"] < data["min_quantity"]:
        print(name, "- осталось", data["quantity"])

        total_value = 0

for data in warehouse.values():
    total_value += data["quantity"] * data["price"]

print("\nОбщая стоимость склада:", total_value, "руб")

print("\n=== ДЕТАЛИ СКЛАДА ===")

for name, data in warehouse.items():
    total = data["quantity"] * data["price"]

    status = "OK"
    if data["quantity"] < data["min_quantity"]:
        status = "⚠️ МАЛО"

    print(f"{name}:")
    print(f"  Количество: {data['quantity']}")
    print(f"  Цена: {data['price']} руб")
    print(f"  Стоимость: {total} руб")
    print(f"  Статус: {status}")