#Домашнее задание 1.
#Задача 1. Создать программу, которая запрашивает имя и возраст, а затем выводит приветствие с возрастом через год (f-строка + преобразование типа).

name = input("Привет! Как тебя зовут? ")
age = int(input("Сколько тебе лет? "))
next_year_age = age + 1

print(f"Привет, {name}! В следующем году тебе будет {next_year_age}.")

#Задача 2.Вывести таблицу «фактов о себе»: год рождения, рост (float), любимое число, признак «люблю Python» (bool). Для каждого значения вывести тип через `type()`.
age = 42
height = 1.71
favorite_number = 8
is_like_python = True

print(f"Мой возраст - {age} лет")
print(f"Мой рост - {height} метр")
print(f"Мое любимое число - {favorite_number}")
print(f"Я люблю Питон - {is_like_python}")

print(type(age))
print(type(height))
print(type(favorite_number))
print(type(is_like_python))

#Задача 3. Сделать «калькулятор лет в днях»: считать возраст (int), вывести количество дней (`age * 365`), оформить в f-строке.
age = int(input("Сколько тебе лет? "))
age_in_days = age * 365

print(f"Тебе {age} лет, {age_in_days} дней.")

#Задача 4. добавить проверку — если пользователь ввёл не число, программа не должна «падать». Подсказка: поищите, как обработать ошибку при `int("abc")` (тема №12 — `try/except`, но попробуйте интуитивно).
#Ответ нашла в Интернете по типу ошибки "ValueError: invalid literal for int() with base 10: 'сорок'"

try:
    age = int(input("Сколько тебе лет? "))
    age_in_days = age * 365
    print(f"Тебе {age} лет, {age_in_days} дней.")
except ValueError:
    print("Ошибка! Введи корректное целое число.")
