from h15_blog import Author, Category, Post


def main() -> None:
    anna = Author(name="Анна", email="anna@mail.ru")
    anton = Author(name="Антон", email="anton@gmail.com")

    news_category = Category(title="Новости")
    it_category = Category(title="ИТ")
    
    post1 = Post(
            title="Новости Python",
            text="Вышла новая версия Python",
            author=anna,
            category=news_category
        )
    
    post2 = Post(
            title="Django",
            text="Знакомство с Django",
            author=anton,
            category=it_category
        )
    
    print("Заголовок с @property:")
    print(post1.title)
    print(post1.title_length)
    print(post1.slug)
    
    try:
        post2.title = "В чем преимущества Django"
    except ValueError as e:
        print(e)

    print("Измененный заголовок:")
    print(post2.title)
    print(post2.title_length)
    print(post2.slug)


if __name__ == "__main__":
    main()
