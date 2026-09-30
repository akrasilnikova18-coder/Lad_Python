raw_age = (input("Сколько тебе лет? ")).strip()

if raw_age.isdigit():
    age = int(raw_age)
    print(f"Вы ввели возраст: {age}")
else:
    print("Ошибка! Возраст должен быть числом")

login = (input("Введите логин: ")).strip()

if login and login.isalnum():
    print(f"Логин принят: {login}")
else:
    print("Ошибка! Логин должен содержать буквы и цифры")

fullname = (input("Введите ФИО: ")).strip()
parts = fullname.split()

if len(parts) == 3:
    surname, firstname, middlename = parts
    print(f"Фамилия: {surname}, Имя: {firstname}, Отчество: {middlename}")
else:
    print("ФИО не полное")
