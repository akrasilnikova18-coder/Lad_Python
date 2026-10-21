import functools
import time


"""Декоратор с «полезной нагрузкой». Напишите декоратор @time_it, но примените его к функции,
которая сортирует список (например, sorted(data)). Затем напишите функцию с тем же результатом,
но без декоратора, и сравните, насколько важно возвращать результат.
Подсказка: если забыть return result, функция вернёт None, и это сразу видно."""


def time_it(func):
    """Декоратор считает время выполнения функции"""

    @functools.wraps(func) # для сохранения метатегов функции
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Функция {func.__name__} отработала за {end - start:.6f} с.")
        #return result

    return wrapper


@time_it
def sort_list(numbers: list) -> list:
    """Возвращает отсортированный список по возрастанию"""
    return sorted(numbers)


def sort_list_reverse(numbers: list) -> list:
    """Возвращает отсортированный список по убыванию"""
    return sorted(numbers, reverse=True)


numbers = [40, 60, 50, 10, 38, 11, 12, 85, 77]
print(f"Исходный список: {numbers}")
print(f"Список, отсортированный по возрастанию: {sort_list(numbers)}")
print(f"Список, отсортированный по убыванию: {sort_list_reverse(numbers)}")

# Если не возвращать результат - функция вернет None (закомментировала в декораторе)