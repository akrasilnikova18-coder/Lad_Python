from collections import namedtuple


#Каталог статей (namedtuple). Определить Post с полями title, category, year.
#Cоздать список из 4 статей. Реализовать: вывести все статьи,
#отсортировать по году по убыванию, найти и вывести статьи заданной категории,
#добавить новую статью. Оформить вывод через f-строки.

Post = namedtuple("Post", ["title", "category", "year"])

posts = [
    Post("Среда обитания манулов", "Манулы", "2023"),
    Post("Как выращивать розы", "Садоводство", "2024"),
    Post("Что едят манулы", "Манулы", "2026"),
    Post("Панды в Московском зоопарке", "Панды", "2025"),
]

#вывести все статьи
print("\nВсе статьи:")
for post in posts:
    print(f"[{post.year}] - Категория: {post.category} - Название: {post.title}")

#отсортировать по году по убыванию
print("\nСтатьи по годам по убыванию:")
sorted_posts = sorted(posts, key=lambda post: post.year, reverse=True)
for post in sorted_posts:
    print(f"[{post.year}] - Категория: {post.category} - Название: {post.title}")

#найти и вывести статьи заданной категории
print("\nСтатьи по категории:")
category = "Манулы"
for post in posts:
    if post.category == category:
        print(f"[{post.year}] - Категория: {post.category} - Название: {post.title}")

#добавить новую статью
posts.append(Post("Где живут слоны", "Слоны", "2024"))
print("\nВсе статьи вместе с новой:")
for post in posts:
    print(f"[{post.year}] - Категория: {post.category} - Название: {post.title}")
