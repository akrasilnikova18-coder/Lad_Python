import csv


rows = [
    ["title", "author", "views"],
    ["Моя первая статья", "Алина", 100],
    ["Моя вторая статья", "Игорь", 94],
    ["Моя третья статья", "Антон", 108],
]

with open("articles.csv", "w", encoding="cp1251", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)

with open("articles.csv", "r", encoding="cp1251") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
