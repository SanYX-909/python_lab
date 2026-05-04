# Задача 5: Калькулятор скидки

# Ввод данных
price = float(input("Введите цену товара: "))
quantity = int(input("Введите количество: "))

# Общая стоимость
total = price * quantity

print("Общая стоимость:", total, "руб")

# Определение скидки
if total < 1000:
    discount = 0
elif total <= 5000:
    discount = 5
else:
    discount = 10

# Расчет скидки
discount_amount = total * discount / 100
final_price = total - discount_amount

print("Скидка:", discount, "%")
print("Сумма скидки:", discount_amount, "руб")
print("Итого к оплате:", final_price, "руб")