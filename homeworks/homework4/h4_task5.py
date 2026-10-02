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
    else:
        print("Собака не найдена")
        
    if is_dog and is_dog+2 < len(my_email):
        print(my_email[is_dog+2])
        
        if my_email[is_dog+1].isalnum() and my_email[is_dog+2].isalnum() and (my_email[is_dog-1].isalnum() or my_email[is_dog-1] == ".") and (my_email[is_dog-2].isalnum() or my_email[is_dog-2] == "."):
            print(f"До и после собаки правильные символы: {is_dog+2}, {is_dog+1}, {is_dog-1}, {is_dog-2}")
            
            for number in range(is_dog, len(my_email)):
                if my_email.find("."):
                    is_point = my_email.find(".") + is_dog
                    print(f"В доменной части есть точка - символ {is_point}")
                    break
                    
                else:
                    print("Ошибка! В доменной части нет точки")
        else:
            print("Ошибка! До и после собаки есть недопустимые символы")
            
    else:
        print("Ошибка! Собаки нет или неправильные символы после собаки")
        
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
