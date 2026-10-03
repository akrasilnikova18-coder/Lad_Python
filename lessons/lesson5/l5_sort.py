prices = [4567, 9867, 3473, 1256, 8764]
prices.sort()
print(f"По возрастанию: {prices}")

prices.sort(reverse=True)
print(f"По убыванию: {prices}")

prices = [4567, 9867, 3473, 1256, 8764]
sorted_prices = sorted(prices)
print(f"Исходный список: {prices}")
print(f"Отсортированный список: {sorted_prices}")

print(f"Сумма всех элементов списка - {sum(prices)}")
print(f"Минимальный элемент в списке - {min(prices)}")
print(f"Максимальный элемент в списке - {max(prices)}")

affordable = [number for number in sorted_prices if number <= 5000]
print(f"Доступные суммы: {affordable}")

prices_strings = [str(number) for number in sorted_prices]
print(prices_strings)

affordable.reverse()
print(affordable)
