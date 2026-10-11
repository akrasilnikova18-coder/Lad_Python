from collections import namedtuple, defaultdict, Counter

#Группировка по категории. Для того же каталога статей сгруппировать заголовки по категории
#с помощью defaultdict из collections, а затем посчитать количество статей в каждой категории через Counter.
#Вывести оба результата.

Post = namedtuple("Post", ["title", "category", "year"])

posts = [
    Post("Среда обитания манулов", "Манулы", "2023"),
    Post("Как выращивать розы", "Садоводство", "2024"),
    Post("Что едят манулы", "Манулы", "2026"),
    Post("Панды в Московском зоопарке", "Панды", "2025"),
]

#сгруппировать заголовки по категории c помощью defaultdict из collections
by_category = defaultdict(list)
for post in posts:
    by_category[post.category].append(post.title)

print("\nЗаголовки по категории")
for category, title in by_category.items():
    print(f"{category}: {title}")

#посчитать количество статей в каждой категории через Counter
article_in_categories = Counter(post.category for post in posts)
print(article_in_categories)
