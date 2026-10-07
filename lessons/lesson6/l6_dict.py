from pprint import pprint

user = {
    "name" : "Алена",
    "age" : 42,
    "city": "Нижний Новгород",
}

print(user["name"])
print(user.get("phone", "Нет телефона"))
print("name" in user)
print("phone" in user)

#user["email"] = "alenavk@yandex.ru" #добавляем новое значение в словарь
user["age"] = 33
pprint(user)

password = user.pop("email", "Не задан")
print(password)

for key, value in user.items():
    print(f"{key}: {value}")
