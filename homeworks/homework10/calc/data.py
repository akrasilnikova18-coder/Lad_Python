"""Разбей программу на модули и добавь точку входа. Возьми любую небольшую программу
из прошлых занятий (например, «калькулятор» или «список дел») и разложи её на модули:
один файл — логика/данные, второй — интерфейс (ввод/вывод), третий — точка входа main.py
с if __name__ == "__main__":. Запусти через uv run python main.py"""


def addition(a: int, b: int) -> int:
    """Возвращает сумму двух чисел"""
    return a + b


def subtraction(a: int, b: int) -> int:
    """Возвращает разность двух чисел"""
    return a - b


def division(a: int, b: int) -> int | float | None:
    """Возвращает результат деления a на b"""
    if b == 0:
        print("Нельзя делить на ноль")
        return
    return a / b


def multiplication(a: int | float, b: int | float) -> int:
    """Возвращает результат умножения a на b"""
    return a * b


def exponentiation(a: int | float, b: int | float) -> int:
    """Возвращает результат возведения a в степень b"""
    return a ** b
