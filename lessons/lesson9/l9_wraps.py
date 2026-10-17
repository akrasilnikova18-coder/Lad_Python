import time
import functools


def time_it(func):
    @functools.wraps(func) # для сохранения метаданных
    def wrapper(*args, **kwargs): # можно передавать любые аргументы
        start = time.perf_counter()
        result = func(*args, **kwargs) # выполняется переданная функция
        end = time.perf_counter()
        elapsed = end - start
        print(f"Функция {func.__name__} отработала за {elapsed:.6f} секунд") # не более 6 знаков после точки
        return result
    return wrapper


def logged(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов: {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"Результат: {func.__name__} - {result}")
        return result
    return wrapper


@logged # сначала таймер, потом логирование, снизу вверх
@time_it # это декорирование, сразу вызывает и функцию и таймер
def sum_of_list(numbers: list) -> int:
    return sum(numbers)


print(sum_of_list.__name__)


@time_it
def num_of_list(numbers: list) -> int:
    return min(numbers)


my_numbers = list(range(20))
print(sum_of_list(my_numbers))
print(num_of_list(my_numbers))
