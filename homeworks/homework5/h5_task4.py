#**Цены и «доступность».** Дан список цен. Порог вводится с клавиатуры.
# Через comprehension постройте список флагов `True`/`False` — цена меньше порога.
# Посчитайте, сколько цен ниже порога (`sum(flags)`), и выведите среднюю цену только по «доступным» позициям.

prices = [2567, 1965, 4589, 10009, 12045, 5645, 6543, 8754, 1245]

#список флагов `True`/`False` — цена меньше порога
price_threshold = int(input("Введите максимальный порог цены: "))
is_affordable = [price < price_threshold for price in prices]
print(f"Список цен: {prices}\nДоступные ли цены: {is_affordable}")

#сколько цен ниже порога sum(flags) и выведите среднюю цену только по «доступным» позициям
sum_flags = 0

for flag in is_affordable:
    if flag:
        sum_flags += 1

print(f"Доступных цен: {sum_flags}")

middle_affordable_prices = [price for price in prices if price < price_threshold]
print(f"Доступные цены: {middle_affordable_prices}, "
      f"средняя цена по доступным позициям: {sum(middle_affordable_prices) // len(middle_affordable_prices)}")
