# Задача 10: Склад (финальная версия)

warehouse = {
    "Газоблок": {"quantity": 320, "price": 950.0, "min_quantity": 200},
    "Краска": {"quantity": 45, "price": 1200.0, "min_quantity": 50},
    "Плитка": {"quantity": 120, "price": 1800.0, "min_quantity": 100},
    "Гипсокартон": {"quantity": 60, "price": 400.0, "min_quantity": 70},
    "Профиль": {"quantity": 25, "price": 300.0, "min_quantity": 30}
}

print("=== СОСТОЯНИЕ СКЛАДА ===\n")

total_value = 0

for name, data in warehouse.items():
    quantity = data["quantity"]
    price = data["price"]
    min_q = data["min_quantity"]

    item_total = quantity * price
    total_value += item_total

    # Определение статуса
    if quantity < min_q:
        status = "❗ НИЖЕ МИНИМУМА"
    else:
        status = "OK"

    print(f"{name}:")
    print(f"  Количество: {quantity}")
    print(f"  Цена: {price} руб")
    print(f"  Минимум: {min_q}")
    print(f"  Стоимость: {item_total} руб")
    print(f"  Статус: {status}")
    print()

print("=== ИТОГО ===")
print("Общая стоимость склада:", round(total_value, 2), "руб")