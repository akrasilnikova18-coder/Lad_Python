import pprint
from collections import defaultdict, Counter

posts = [
    {"title": "Введение в Python", "category": "python", "tags": ["python", "basics"]},
    {"title": "Советы по Django", "category": "django", "tags": ["django", "python", "web"]},
    {"title": "Знакомство с PostgreSQL", "category": "sql", "tags": ["sql", "postgres"]},
    {"title": "Модели Django на практике", "category": "django", "tags": ["django", "models", "python"]},
]

#pprint.pprint(posts)

for post in posts:
    print(f"[{post["category"]}] {post["title"]} - Теги: {", ".join(post["tags"])}")

by_category = defaultdict(list)

for post in posts:
    by_category[post["category"]].append(post["title"])

print("\nПосты по категориям")

for category, title in by_category.items():
    print(f"[{category}] {title}")

tag_counter = Counter()
for post in posts:
    tag_counter.update(post["tags"])

print("\nТОП3 тега")
for tag, count in tag_counter.most_common(3):
    print(f"[{tag}] {count}")
