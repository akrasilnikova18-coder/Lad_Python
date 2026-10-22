"""Напиши модуль utils.py и продемонстрируй разные способы импорта. Создай файл utils.py
с двумя-тремя полезными функциями (например, проверка чётности, преобразование строки в число
с обработкой ошибки). Затем в двух разных файлах-заготовках подключи его:
в первом — import utils, во втором — from utils import ... as ....
Обрати внимание на разницу в вызове."""


def even_number(number: int) -> bool:
    """Возвращает True, если число четное, и False, если число не четное"""
    return number % 2 == 0


def str_in_num(string_with_number: str) -> int:
    """Преобразует строку в число"""
    try:
        return int(string_with_number)
    except ValueError:
        print("Ошибка! Неправильный тип данных")
        return
    

if __name__ == "__main__":
    print(even_number(10))
    print(even_number(5))

    string_with_num = input("Введите число от 1 до 90 ")
    print(str_in_num(string_with_num))
