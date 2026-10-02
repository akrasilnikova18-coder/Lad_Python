#Звёздочка (валидация телефона/email). Написать проверку корректности e-mail без регулярных выражений,
# только методами строк: есть ровно один @, слева и справа от него есть непробельные символы,
# в доменной части есть точка, домен заканчивается на 2+ буквы (endswith + проверка isalpha на суффиксе).
# Дополнительно — проверить номер телефона в формате +7-XXX-XXX-XX-XX: разбить по - на 5 частей,
# первая равна +7, остальные — isdigit() и нужной длины (len). Вывести True/False для нескольких примеров.

#валидация email

my_email = input("Введите email ")

if my_email:
    print(f"Введен email: {my_email}")

    is_dog = ""

    if (is_dog := my_email.find("@")) != -1:
        print(f"Собака найдена - символ {is_dog}")
        
        my_email = my_email.split("@")
        print(my_email)
        
        if my_email[0].isalnum():
            print(f"Первая часть email содержит буквенные значения: {my_email[0]}")
        else:
            print("Ошибка! Первая часть email содержит не только буквенные значения")
        
        if my_email[1].find(".") != -1:
            print(f"В доменной части есть точка")

            part2_email = my_email[1].split(".")
            print(part2_email)

            if part2_email[0].isalnum():
                print("Во второй части email есть только буквы и цифры")
            else:
                print("Ошибка! Во второй части email есть не только буквы и цифры")

            if part2_email[1].isalnum() and len(part2_email[1]) >= 2:
                print("На конце email есть только буквы и цифры, и он больше или равен двум символам")
            else:
                print(
                    "Ошибка! На конце email есть не только буквы и цифры и / или он меньше двух символов"
                )

        else:
            print("Ошибка! В доменной части нет точки")
            
    else:
        print("Собака не найдена")

else:
    print("Ошибка! Email не может быть пустым")
    
#валидация телефона

phone = input("Введите номер телефона в формате +7-XXX-XXX-XX-XX ")

if phone:
    phone = phone.split("-")
    print(phone)
    
    if len(phone) == 5:
        print("В номере телефона 5 частей")
        
        if (
            len(phone[1]) == 3
            and len(phone[2]) == 3
            and len(phone[3]) == 2
            and len(phone[4]) == 2
        ):
            print("Части 2-5 телефона правильной длины")
        else:
            print("Части 2-5 телефона неправильной длины")

        for number in range(1, 5):
            if phone[number].isdigit():
                print(f"Номер телефона правильный - {phone[number]}")
            else:
                print("Ошибка! В номере телефона не только цифры")
                break
        
    else:
        print("Ошибка! В номере телефона не 5 частей")

    if phone[0] == "+7":
        print("Телефон начинается с +7")
    else:
        print("Ошибка! Телефон должен начинаться с +7")

else:
    print("Ошибка! Телефон не может быть пустым")
