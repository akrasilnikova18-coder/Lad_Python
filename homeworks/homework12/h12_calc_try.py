# Защищённый калькулятор. Напишите программу, которая запрашивает два числа
# и выводит их сумму, разность, произведение и частное. Оберните вычисления в try/except так,
# чтобы: при делении на ноль (ZeroDivisionError) программа не «падала», а выводила
# «Деление на ноль невозможно»; при невалидном вводе (ValueError) — просила ввести число заново.
# Используйте else для вывода результата и finally для сообщения «Вычисления завершены».

while True:
    try:
        number1 = int(input("Введите первое целое число "))
        number2 = int(input("Введите второе целое число "))
        division = number1 // number2
    
    except ZeroDivisionError:
        print("На ноль делить нельзя. Делим на 5.")
        division = number1 // 5
        continue

    except ValueError as error:
        print("Введено не число. Попробуйте еще раз. Оба числа считаем как две единицы")
        summa = 2
        difference = 0
        multiplication = 1
        division = 1
        continue

    else:
        summa = number1 + number2
        difference = number1 + number2
        multiplication = number1 * number2
        
    finally:
        print(f"Вычисления завершены. Результаты:\n"
              f"Деление: {division}. Умножение: {multiplication}\n"
              f"Сумма: {summa}. Разность: {difference}\n"
        )

    break