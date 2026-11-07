from l15_blog import Author, Post, Category, Comment


def main() -> None:
    author = Author(name="Anna", email="5677")
    news_category = Category(name="news")
    it_category = Category(name="IT")
    
    news_category.add(Post(title="Занимательная физика", author=author, content="Мой первый пост"))
    news_category.add(Post(title="Занимательная химия", author=author, content="Мой второй пост"))
    it_category.add(Post(title="Занимательная алгебра", author=author, content="Мой третий пост"))

    print("Посты категории Новости:")
    for post in news_category:
        print(post)

    print(f"Количество постов: {len(news_category)}")

    it_post = it_category[0]
    print(it_post.title)
    print(f"Этот пост есть в категории IT постов: {it_post in it_category}")

    for post in news_category:
        print(f"Заголовок: {post.title}, Длина: {post.title_length}, Ссылка: {post.slug}")


if __name__ == "__main__":
    main()
