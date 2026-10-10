point = (10, 20)
x, y = point
print(f"Значение x - {x}, значение y - {y}")

first, *rest = (10, 20, 30, 40) #переменные через запятую - это тоже кортеж. если один элемент - будет ругаться
print(first)
print(rest)

a, b = 1, 2
a, b = b, a
print(a, b)

pairs = [
    ("name", "Алена"),
    ("age", 42),
]

for key, value in pairs:
    print(f"Ключ: {key}, Значение: {value}")
