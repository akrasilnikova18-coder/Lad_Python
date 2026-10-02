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

    if my_email.find("@") != -1:
        is_dog = my_email.find("@")
        print(f"Собака найдена - символ {is_dog}")
        
        my_email = my_email.split("@")
        print(my_email)
        
        if my_email[1].find(".") != -1:
            print(f"В доменной части есть точка")
        else:
            print("Ошибка! В доменной части нет точки")

        if (my_email[0].isalnum() or my_email[0] == ".") and (my_email[1].isalnum() or my_email[0] == "."):
            print(f"Email содержит буквенные значения: {my_email[0]}, {my_email[1]}")
        else:
            print("Ошибка! Email содержит не только буквенные значения")

    else:
        print("Собака не найдена")

    if my_email[-1].isalpha or my_email[-2].isalpha:
        print("На конце email буквенные символы")
    else:
        print("Ошибка! На конце email не буквенные символы")
        
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
