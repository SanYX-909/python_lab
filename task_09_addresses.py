# Задача 9: Очистка адресов

addresses = [
    " г. Санкт-Петербург, Невский проспект, д. 28 ",
    "г.Санкт-Петербург,ул.Рубинштейна,д.15",
    " г. Санкт-Петербург, Лиговский проспект, д. 50 ",
    "г Санкт-Петербург,пр.Энгельса,д.120",
    " г. Санкт-Петербург, ул. Савушкина, д. 10 "
]

# Вывод исходных данных
print("Исходные адреса:")
for addr in addresses:
    print(addr)

    cleaned_addresses = []

for addr in addresses:
    # Убираем пробелы по краям
    addr = addr.strip()

    # Добавляем пробелы после запятых
    addr = addr.replace(",", ", ")

    # Убираем двойные пробелы
    addr = addr.replace("  ", " ")

    cleaned_addresses.append(addr)

print("\nОчищенные адреса:")
for addr in cleaned_addresses:
    print(addr)

    normalized_addresses = []

for addr in cleaned_addresses:
    addr = addr.replace("г.", "г. ")
    addr = addr.replace("г ", "г. ")
    normalized_addresses.append(addr)

print("\nНормализованные адреса:")
for addr in normalized_addresses:
    print(addr)