import json


# Профиль в JSON. Создать словарь с данными человека (имя, возраст, город, список любимых книг)
# и сохранить его в profile.json через json.dump с ensure_ascii=False и indent.
# Затем прочитать файл через json.load и вывести входящие в него данные.


person = {
    "name": "Алена",
    "age": 42,
    "city": "Нижний Новгород",
    "my_books": ["Властелин колец", "Записки о Шерлоке Холмсе", "Тайный город", "Ночной дозор",],
}


with open("person.json", "w", encoding="utf-8") as f:
    json.dump(person, f, ensure_ascii=False, indent=2)

with open("person.json", "r", encoding="utf-8") as f:
    person_info = json.load(f)
    print(f"Имя: {person_info["name"]}, Возраст: {person_info["age"]},"
          f" Город: {person_info["city"]}, Любимые книги: {person_info["my_books"]}")
