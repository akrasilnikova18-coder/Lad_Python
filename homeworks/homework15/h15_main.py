from h15_blog import Author, Category, Post


def main() -> None:
    anna = Author(name="Анна", email="anna@mail.ru")
    anton = Author(name="Антон", email="anton@gmail.com")

    news_category = Category(title="Новости")
    it_category = Category(title="ИТ")

    posts = [
        Post(
            title="Новости Python",
            text="Вышла новая версия Python",
            author=anna,
            category=news_category,
        ),
        Post(
            title="Обновление сайта",
            text="На сайте появились новые функции",
            author=anna,
            category=news_category,
        ),
        Post(
            title="Основы ООП",
            text="Изучаем классы и объекты",
            author=anton,
            category=it_category,
        ),
        Post(
            title="Django",
            text="Знакомство с Django",
            author=anton,
            category=it_category,
        ),
    ]

    # Выводим каждый блок категории отдельно
    for category in [news_category, it_category]:
        print(f"\n===== {category} =====")
        Post.find_for_category(posts, category.title)

    # Проверяем разницу между __str__ и __repr__
    print("\nОдин пост:")
    print(posts[0])

    print("\nСписок постов:")
    print(posts)

    # print(post) вызывает __str__, поэтому выводит красивую строку.
    # print(posts) выводит список объектов, для которых вызывается __repr__.


if __name__ == "__main__":
    main()

