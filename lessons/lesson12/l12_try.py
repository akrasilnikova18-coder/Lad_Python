while True:
    try:
        first_number = int(input("Введите первое целое число "))
        second_number = int(input("Введите второе целое число "))
        result = first_number // second_number
        
    except ZeroDivisionError:
        print("На ноль делить нельзя. Делим на 10.")
        result = first_number // 10
        
    except ValueError:
        print("Введено не число. Попробуйте еще раз.")
        continue

    else:
        print("Оба числа корректные, вычисляем.")

    print(f"Результат деления: {result}")
    break

        
    
    
   