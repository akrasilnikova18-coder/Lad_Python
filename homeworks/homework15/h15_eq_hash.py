from h15_blog import Author, Category, Post


def main():
    anna = Author(name="Анна", email="anna@mail.ru")
    python = Category(title="Python")

    post1 = Post(title="Основы Python", text="Первый текст", author=anna, category=python)
    post2 = Post(title="Основы Python", text="Второй текст", author=anna, category=python)
    post3 = Post(title="ООП в Python", text="Третий текст", author=anna, category=python)

    # Проверяем сравнение
    print(post1 == post2)  # True, потому что одинаковые заголовки
    print(post1 == post3)  # False, потому что разные заголовки

    # Проверяем хеши
    print(hash(post1) == hash(post2))  # True, потому что одинаковые заголовки

    # Проверяем множество
    posts = {post1, post2, post3}

    print(len(posts))  # 2, потому что post1 и post2 имеют одинаковые заголовки. Метод __eq__ считает их равными, а __hash__ возвращает для них одинаковое хеш-значение.

    for post in posts:
        print(post)

    # Проверяем словарь
    posts_dict = {post1: "Первая статья"} # Используем post1 в качестве ключа 
    print(posts_dict[post2])

    # Происходит следующее:
    # 1. Python вычисляет hash(post2).
    # 2. Находит подходящее место в словаре, где хранится ключ с таким хешем.
    # 3. Проверяет равенство ключей с помощью __eq__ (если это разные объекты).
    # 4. Поскольку заголовки post1 и post2 одинаковые, они считаются равными.
    # 5. Python возвращает значение, сохранённое по ключу post1.
    # 6. Если обратиться через post3 - получим ошибку, потому что заголовки разные


if __name__ == "__main__":
    main()
