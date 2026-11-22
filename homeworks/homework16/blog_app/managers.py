import json
from datetime import datetime

from .models import Author, Category, Tag, Post


# Уникальность и валидация. Сделайте модель устойчивой:
# add_author/add_category/add_tag должны бросать ValueError,
# если объект с таким именем/названием уже есть;
# create_post должен бросать ValueError,
# если title пустой или если author/category переданы как None.
# Подсказка: это пересекается с занятием 12 (обработка исключений) —
# используйте raise ValueError(...) с понятным сообщением и обработайте его в main.py.


# Усложнить связи многие-ко-многим (теги).
# Сделайте Blog.add_tag_to_post(post, tag) возвращающим True, если тег был добавлен, и False, если такой тег у поста уже есть (без создания дубликата).
# Убедитесь, что при повторном добавлении не ломается согласованность Tag._posts (дубликат не появляется).
# Добавьте метод Blog.tags_of_post(post) — список названий тегов поста — и выведите его для каждого поста.


class Blog:
    def __init__(self) -> None:
        self._authors: list[Author] = []
        self._categories: list[Category] = []
        self._tags: list[Tag] = []
        self._posts: list[Post] = []
        self._next_ids: dict[str, int] = {"author": 1, "category": 1, "tag": 1, "post": 1}
        
    def new_id(self, kind: str) -> int:
        new_id = self._next_ids[kind]
        self._next_ids[kind] += 1
        return new_id

    def add_author(self, name: str) -> Author:
        if any(author.name == name for author in self._authors):
            raise ValueError(f"Автор с таким именем уже есть: {name}")

        author = Author(name=name, id=self.new_id(kind="author"))
        self._authors.append(author)
        return author
    
    def add_category(self, title: str) -> Category:
        if any(category.title == title for category in self._categories):
            raise ValueError(f"Категория с таким названием уже есть: {title}")

        category = Category(title=title, id=self.new_id(kind="category"))
        self._categories.append(category)
        return category
    
    def add_tag(self, title: str) -> Tag:
        if any(tag.title == title for tag in self._tags):
            raise ValueError(f"Тег с таким названием уже есть: {title}")

        tag = Tag(title=title, id=self.new_id(kind="tag"))
        self._tags.append(tag)
        return tag
    
    def create_post(self, title: str, content: str, author: Author, category: Category) -> Post | None:
        if not title or not author or not category:
            raise ValueError("Все поля обязательны для заполнения")
            return
        else:
            post = Post(
                title=title,
                content=content,
                author=author,
                category=category,
                id=self.new_id(kind="post"),
            )
            author.add_post(post)
            category.add_post(post)
            self._posts.append(post)
            return post

    def add_tag_to_post(self, post: Post, tag: Tag) -> bool:
        if tag in post.tags:
            return False

        post.add_tag(tag)
        return True

    def tags_of_post(self, post: Post) -> list[str]:
        return post.tag_titles
        
    @property
    def authors(self) -> list[Author]:
        return self._authors.copy()

    @property
    def categories(self) -> list[Category]:
        return self._categories.copy()

    @property
    def tags(self) -> list[Tag]:
        return self._tags.copy()

    @property
    def posts(self) -> list[Post]:
        return self._posts.copy()
    
    def posts_by_category(self, category: Category) -> list[Post]:
        return category.posts
    
    def posts_by_tag(self, tag: Tag) -> list[Post]:
        return tag.posts

    def posts_by_author(self, author: Author) -> list[Post]:
        return author.posts
    
    @staticmethod
    def _post_to_dict(post: Post) -> dict:
        return {
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "author_id": post.author.id,
            "category_id": post.category.id,
            "tag_ids": [tag.id for tag in post.tags],
            "created_at": post.created_at.isoformat(),
        }

    def save(self, path: str) -> None:
        data = {
            "authors": [{"id": author.id, "name": author.name} for author in self._authors],
            "categories": [{"id": category.id, "title": category.title} for category in self._categories],
            "tags": [{"id": tag.id, "title": tag.title} for tag in self._tags],
            "posts": [self._post_to_dict(post) for post in self._posts],
        }

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @classmethod
    def load(cls, path: str) -> "Blog":
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        blog = cls()

        authors = {author["id"]: Author(id=author["id"], name=author["name"]) for author in data["authors"]}
        categories = {category["id"]: Category(id=category["id"], title=category["title"]) for category in data["categories"]}
        tags = {tag["id"]: Tag(id=tag["id"], title=tag["title"]) for tag in data["tags"]}

        blog._authors = list(authors.values())
        blog._categories = list(categories.values())
        blog._tags = list(tags.values())

        for post_data in data["posts"]:
            post_author = authors[post_data["author_id"]]
            post_category = categories[post_data["category_id"]]

            post = Post(
                id=post_data["id"],
                title=post_data["title"],
                content=post_data["content"],
                author=post_author,
                category=post_category,
            )

            post.created_at = datetime.fromisoformat(post_data["created_at"])

            post_author.add_post(post)
            post_category.add_post(post)

            for tag_id in post_data["tag_ids"]:
                post.add_tag(tags[tag_id])

            blog._posts.append(post)

        blog._next_ids = {
            "author": max([author.id for author in blog.authors], default=0) + 1,
            "category": max([category.id for category in blog.categories], default=0) + 1,
            "tag": max([tag.id for tag in blog.tags], default=0) + 1,
            "post": max([post.id for post in blog.posts], default=0) + 1,
        }

        return blog

