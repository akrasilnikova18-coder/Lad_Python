import json


"""
post = {
    "title": "Моя первая статья",
    "author": "Анна",
    "tags": ["Python", "JSON", "файлы"],
    "published": True,
    "views": 120,
}

with open("post.json", "w", encoding="utf-8") as f:
    json.dump(post, f, ensure_ascii=False, indent=2)

with open("post.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
"""

text = """
{
  "title": "Моя первая статья",
  "author": "Анна",
  "tags": [
    "Python",
    "JSON",
    "файлы"
  ],
  "published": true,
  "views": 120
}
"""

json_string = json.loads(text)

print(f"Заголовок: {json_string["title"]}")
print(f"Теги: {json_string["tags"]}")
print(f"Опубликовано: {json_string["published"]}")
