def entering_numbers() -> list:
    """Запрашивает у пользователя числа и возвращает список с числами
    Альтернатива - писать 5 функций, которые отличаются только вызванной функцией из data"""
    a = int(input("Введите первое целое число "))
    b = int(input("Введите второе целое число "))

    numbers = []
    
    if type(a) != int or type(b) != int:
        print("Неправильный тип числа")
        return

    numbers.append(a)
    numbers.append(b)
    return numbers


if __name__ == "__main__":
    num = entering_numbers()
    print(num[0], num[1])