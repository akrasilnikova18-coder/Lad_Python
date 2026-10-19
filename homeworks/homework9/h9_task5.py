import functools


"""Звёздочка. Декоратор с аргументами. Напишите декоратор @repeat(times), который вызывает функцию N
раз (@repeat(3)). Это потребует «фабрики декоратора»: repeat(times) возвращает декоратор,
а тот возвращает обёртку. Подсказка (та же логика, что в @api_view(["GET"])): `
`python def repeat(times): def decorator(func): @functools.wraps(func) def wrapper(args, *kwargs):
result = None for _ in range(times): result = func(args, *kwargs)
return result return wrapper return decorator `
Разберите каждую вложенную функцию и объясните комментарием,
почему цепочка «repeat(times) → decorator → wrapper`» нужна именно такая.
Проверьте на функции, печатающей текст."""


def repeat(times):
    """Фабрика декоратора, которая возвращает декоратор - нужна,
    так как нужно вызвать декоратор не один раз, а несколько"""

    def decorator(func):
        """Декоратор, который возвращает функцию три раза"""
        @functools.wraps(func)

        def wrapper(*args, **kwargs):
            result = None # чтобы не было ошибки, если будет указано количество повторений = отрицательное число

            for _ in range(times): # повторяет функцию заданное число раз
                result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator


@repeat(3) # повторяем функцию три раза
def greet(name: str):
    """Выводит приветствие"""
    print(f"Привет, {name}")


greet("Наталья")
