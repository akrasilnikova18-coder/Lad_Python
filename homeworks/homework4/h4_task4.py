#Поиск по блогу. Есть список заголовков постов. Вывести только те, что содержат слово "Python"
# (через find или in). Затем для каждого заголовка вывести его slug через написанную
# на занятии функцию build_slug.

def built_slug(title: str) -> str:
    result = title.lower()
    result = result.replace(" ", "-")

    clean = []
    for char in result:
        if char.isalnum() or char == "-":
            clean.append(char)
        else:
            clean.append("-")

    result = "".join(clean)

    while "--" in result:
        result = result.replace("--", "-")

    result = result.strip('-')
    return result

posts = [
    "Изучаем Python",
    "Занимательная   : астрономия",
    "Программирование   %% на Python!!!",
    "Из  жизни манулов",
    "Циклы    в Python",
]

print('Заголовки, которые содержат слово "Python"')
for title in posts:
    if "Python" in title:
        #print(f"{title}")
        print(built_slug(title))
