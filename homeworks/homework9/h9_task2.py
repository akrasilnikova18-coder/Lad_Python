import functools
import time


"""Декораторы @time_it и @logged. Напишите оба декоратора с @functools.wraps.
Примените @time_it к функции, рассчитывающей сумму элементов списка, и @logged к функции,
формирующей приветствие. Убедитесь, что метаданные (__name__, __doc__) сохранены
и что декораторы возвращают исходный результат функции (а не None)."""


def time_it(func):
    """Декоратор считает время выполнения функции"""

    @functools.wraps(func) # для сохранения метатегов функции
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Функция {func.__name__} отработала за {end - start:.6f} с.")
        return result

    return wrapper


def logged(func):
    """Декоратор модерирует (логирует) процесс выполнения функции: имя, аргументы, результат"""

    @functools.wraps(func) # для сохранения метатегов функции
    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"Завершение {func.__name__} -> {result}")
        return result

    return wrapper


@time_it
def sum_list(numbers: list) -> int:
    """Суммирует элементы списка"""
    return sum(numbers)


@logged
def greeting(name: str):
    """Возвращает текст приветствия"""
    return f"Добро пожаловать, {name}!"


print("\nРезультат работы функции суммы элементов списка")
numbers_list = range(10)
print(sum_list(numbers_list))
print(sum_list.__name__)
print(sum_list.__doc__)

print("\nРезультат работы функции приветствия")
print(greeting("Елена"))
print(greeting.__name__)
print(greeting.__doc__)
