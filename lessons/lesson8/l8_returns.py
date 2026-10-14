def add(a: int, b: int) -> int:
    """Возвращает сумму двух чисел"""
    return a + b


def print_sum(a: int, b: int) -> None:
    """Выводит сумму сложения, но не возвращает ее"""
    print(f"Сумма: {a + b}")


total = add(30,40)
print(total)

result_print = print_sum(a=50, b=100)
print(result_print)


message = "Глобальная"

def show_message() -> None:
    print(message)


def make_local() -> None:
    message = "Локальная"
    print(message)


show_message()
make_local()
print(message)


counter = 0


def increment_counter() -> None:
    global counter
    counter += 1

increment_counter()
increment_counter()
print(counter)
