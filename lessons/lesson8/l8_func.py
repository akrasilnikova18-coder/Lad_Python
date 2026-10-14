def greet(name: str) -> None: #какой тип данных принимаем и возвращаем
    """Функция выводит приветствие по имени"""
    print(f"Привет, {name}")


def user_info(name: str, age: int) -> None:
    """Функция выводит имя и возраст пользователя"""
    print(f"Имя {name}, возраст {age}")


def greet_full(name: str, greeting: str = "Привет")-> None: #все значения по умолчанию именованные
    print(f"{greeting}, {name}")


greet("Анна")
greet(name = "Джим")

user_info("Мария", 25)
user_info(age = 36, name = "Джон")

greet_full("Иван")
greet_full("Анна", greeting="Hello")
