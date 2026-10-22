from colorama import Fore, Style, init


from calc import data
from calc import ui


"""Подключи стороннюю библиотеку через uv add. Добавь в проект любую библиотеку
(например, rich или colorama) и примени её в выводе своей программы.
Загляни в pyproject.toml и объясни в комментарии в коде, что там появилось и зачем это нужно."""

"""В pyproject.toml добавилась версия colorama, это нужно, чтобы при передаче этого файла
другому разработчику, он знал, какие библиотеки и в каких версиях нужно скачать"""

init(autoreset=True) # нужен чтобы автоматически сбрасывать цвет текста после каждого вызова


def main() -> None:
    """Запрашивает у пользователя, что нужно сделать, вызывает нужную функцию
    и выводит на экран нужный результат"""
    while True:
        print(f"""
        {Fore.YELLOW}Меню:{Style.RESET_ALL}
        {Fore.GREEN}1{Style.RESET_ALL} - Сумма чисел a и b
        {Fore.GREEN}2{Style.RESET_ALL} - Разность чисел a и b
        {Fore.GREEN}3{Style.RESET_ALL} - Деление чисел a и b
        {Fore.GREEN}4{Style.RESET_ALL} - Умножение чисел a и b
        {Fore.GREEN}5{Style.RESET_ALL} - Возведение a в степень b
        {Fore.RED}6{Style.RESET_ALL} - Выход
        """)
        
        choice = input("Выберите действие ")
        if choice == "1":
            num = ui.entering_numbers()
            print(f"{num[0]} + {num[1]} = {data.addition(num[0], num[1])}")
            
        elif choice == "2":
            num = ui.entering_numbers()
            print(f"{num[0]} - {num[1]} = {data.subtraction(num[0], num[1])}")
        
        elif choice == "3":
            num = ui.entering_numbers()
            print(f"{num[0]} / {num[1]} = {data.division(num[0], num[1])}")

        elif choice == "4":
            num = ui.entering_numbers()
            print(f"{num[0]} * {num[1]} = {data.multiplication(num[0], num[1])}")
            
        elif choice == "5":
            num = ui.entering_numbers()
            print(f"{num[0]} ** {num[1]} = {data.exponentiation(num[0], num[1])}")

        elif choice == "6":
            print("Завершение работы")
            break

        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main()