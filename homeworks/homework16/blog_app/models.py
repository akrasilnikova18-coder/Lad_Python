from datetime import datetime


# Избежать повторов можно, добавив родительский класс
class PostContainer:
    """Базовый класс для объектов, содержащих посты."""

    def __init__(self, id: int) -> None:
        self.id = id
        self._posts: list["Post"] = []

    def add_post(self, post: "Post") -> None:
        if post not in self._posts:
            self._posts.append(post)

    @property
    def posts(self) -> list["Post"]:
        return self._posts.copy()

    def post_count(self) -> int:
        return len(self._posts)


class Author(PostContainer):
    def __init__(self, id: int, name: str) -> None:
        super().__init__(id)
        self.name = name

    def add_post(self, post: "Post") -> None:
        post.author = self
        super().add_post(post)

    def __str__(self) -> str:
        return f"Автор: имя {self.name}, ИД: {self.id}"

    def __repr__(self) -> str:
        return f"Author(id={self.id}, name={self.name!r})"


class Category(PostContainer):
    def __init__(self, id: int, title: str) -> None:
        super().__init__(id)
        self.title = title

    def add_post(self, post: "Post") -> None:
        post.category = self
        super().add_post(post)

    def __str__(self) -> str:
        return f"Категория: название {self.title}, ИД: {self.id}"

    def __repr__(self) -> str:
        return f"Category(id={self.id}, title={self.title!r})"


class Tag(PostContainer):
    def __init__(self, id: int, title: str) -> None:
        super().__init__(id)
        self.title = title

    def __str__(self) -> str:
        return f"Тег: название {self.title}, ИД: {self.id}"

    def __repr__(self) -> str:
        return f"Tag(id={self.id}, title={self.title!r})"


class Post:
    def __init__(
        self,
        id: int,
        title: str,
        content: str,
        author: Author,
        category: Category
    ) -> None:
        self.id = id
        self.title = title
        self.content = content
        self.author = author
        self.category = category

        self.tags: list[Tag] = []
        self.created_at = datetime.now()

    def add_tag(self, tag: Tag) -> None:
        if tag not in self.tags:
            self.tags.append(tag)
            tag.add_post(self)

    @property
    def tag_titles(self) -> list[str]:
        return [tag.title for tag in self.tags]

    def __str__(self) -> str:
        return (
            f"Пост: ИД - {self.id}, "
            f"Автор - {self.author.name}, "
            f"Название - {self.title}"
        )

    def __repr__(self) -> str:
        return (
            f"Post(id={self.id}, "
            f"title={self.title!r}, "
            f"content={self.content!r}, "
            f"author={self.author!r}, "
            f"category={self.category!r})"
        )
