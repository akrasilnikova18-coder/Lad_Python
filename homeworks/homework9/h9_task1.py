"""**Замыкания.** Напишите функцию `make_power(exponent)`, которая возвращает функцию `power(base)`
(вычисляет `base ** exponent`). Затем напишите `make_counter(start)` со `nonlocal`,
как на семинаре. Протестируйте обе и выведите результаты в консоль. Подсказка: возвращайте функцию,
а не результат её вызова."""


def make_power(exponent: int):
    """Возвращает функцию возведения числа в степень"""

    def power(base: int) -> int:
        return base ** exponent

    return power


def make_counter(start=0):
    """Возвращает функцию-счётчик с памятью между вызовами."""

    count = start  # переменная «запоминается» замыканием

    def increment(step=1):
        # nonlocal — разрешаем менять переменную из внешней функции
        nonlocal count
        count += step
        return count

    return increment


print("\nРезультат работы функции возведения в степень")
number_power = make_power(3) # все числа возводит в третью степень (куб)
print(number_power(2))
print(number_power(3))
print(number_power(4))
print(number_power(5))

print("\nРезультат работы функции-счетчика")
number_counter = make_counter(2)
print(number_counter(5))

number_counter1 = make_counter(8)
print(number_counter1(10))
