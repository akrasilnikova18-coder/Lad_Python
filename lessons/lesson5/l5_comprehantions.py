numbers = list(range(1, 11))
sqarues = [num**2 for num in numbers]
print(f"Квадраты: {sqarues}")

even =[num for num in numbers if num % 2 == 0]
print(f"Четные числа: {even}")

prices = [4567, 9867, 3473, 1256, 8764]
flags = [number > 5000 for number in prices]
print(prices, flags)

categories = ['python', 'django', 'sql', 'docker']
titles = [word.capitalize() if word != 'sql' else word.upper() for word in categories]
print(titles)
