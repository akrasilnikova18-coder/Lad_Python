from collections import namedtuple

from lessons.lesson6.l6_blog import category

Post = namedtuple("Post", ["title", "category", "year"])
posts = [
    Post("Модели Django", "IT", "2025"),
    Post("Индексы в Postgee SQL", "DB", "2024"),
    Post("View-функции", "Django", "2026"),
    Post("Транзакции", "DB", "2025"),
]

posts.append(Post("Формы и валидация", "Django", "2026"))

print("\nВсе статьи:")
for post in posts:
    print(f"[{post.year}] - {post.title} - {post.category}")

sorted_posts = sorted(posts, key=lambda post: post.year)

print("\nСтатьи по годам:")
for post in sorted_posts:
    print(f"[{post.year}] - {post.title} - {post.category}")

category = "DB"
matching = [post for post in posts if post.category == category]

print("\nСтатьи по категории:")
for post in matching:
    print(f"[{post.year}] - {post.title} - {post.category}")

number = 10
even_or_odd = [print("Число четное") if number % 2 == 0 else print("Число нечетное")]

odd_or_even = ("even", "odd")[number % 2] #в качестве ключа математическое выражение - 0 или 1
print(odd_or_even)
