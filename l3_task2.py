from random import randint


secret = randint(1, 11)
attempt = 0

while True:
    guess = int(input("Введите загаданное число от 1 до 10 "))
    attempt += 1
    
    if guess < secret:
        print(f"Пользователь ввел число {guess}, оно меньше загаданного")
        continue
    
    if guess > secret:
        print(f"Пользователь ввел число {guess}, оно больше загаданного")
        continue

    print(f"Пользователь угадал число за {attempt} попыток")
    break
