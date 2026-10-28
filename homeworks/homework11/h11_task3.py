import csv


# Экспорт статей в CSV. Взять список словарей (заголовок, автор, просмотры)
# и записать его в blog.csv через csv.writer. Потом прочитать файл через csv.reader
# и вывести каждую строку. Убедиться, что CSV корректно открывается в табличном редакторе.

articles = [
    ["title", "author", "views"],
    ["Манулы в Московском зоопарке", "Игорь", 115],
    ["Как выращивать герани", "Алина", 34],
    ["Что едят манулы", "Алла", 234],
]

with open("blog.csv", "w", encoding="cp1251", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(articles)

with open("blog.csv", "r", encoding="cp1251", newline="") as f:
    read_articles = csv.reader(f)
    for row in read_articles:
        print(row)
