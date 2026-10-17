import time


def time_it(func):
    def wrapper(*args, **kwargs): # можно передавать любые аргументы
        start = time.perf_counter()
        result = func(*args, **kwargs) # выполняется переданная функция
        end = time.perf_counter()
        elapsed = end - start
        print(f"Функция {func.__name__} отработала за {elapsed:.6f} секунд") # не более 6 знаков после точки
        return result
    return wrapper


@time_it # это декорирование, сразу вызывает и функцию и таймер
def sum_of_list(numbers: list) -> int:
    return sum(numbers)


@time_it
def num_of_list(numbers: list) -> int:
    return min(numbers)


my_numbers = list(range(100))
print(sum_of_list(my_numbers))
print(num_of_list(my_numbers))

# my_decor = time_it(sum_of_list)
# print(my_decor(my_numbers))
