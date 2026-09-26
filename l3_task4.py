posts = [
    "Погода в Нижнем Новгороде",
    "Занимательная астрономия",
    "Изучаем Питон",
]

print("Свежие посты:")
for number, title in enumerate(posts, start=1):
    print(f"{number}. {title}")

print("\nКарточка статьи:")

for title in posts:
    print(f"Заголовок статьи: {title} - {len(title)} символов")

print("\nПоиск:")
if "Занимательная астрономия" in posts:
    print("Пост 'Занимательная астрономия' есть в списке")
else:
    print("Такой статьи нет")
