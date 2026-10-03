posts = [
    ["2026-02-10", "Как установить uv", "Инструментарий"],
    ["2026-02-14", "Списки в Python", "Python"],
    ["2026-02-18", "Введение в Django", "Django"],
]

print("Добро пожаловать в блог CLI!")

while True:
    print(
        """
        Что делаем?
        1 - Добавить пост
        2 - Показать все посты
        3 - Отсортировать по дате
        4 - Отфильтровать по категории
        0 - Выйти
        """
    )
    
    choice = input("Ваш выбор: ")
    
    if choice == "1":
        new_date = input("Введите дату в формате ГГГГ-ММ-ДД: ")
        new_title = input("Введите заголовок: ")
        new_category = input("Введите категорию: ")
        
        posts.append([new_date, new_title, new_category])
        print(f"Пост \"{new_title}\" добавлен")
        
    elif choice == "2":
        print("\nВсе посты")
        for post in posts:
            print(f"{post[0]} - {post[1]} - {post[2]}")
    
    elif choice == "3":
        posts.sort()
        print("\nОтсортировано по дате:")
        for post in posts:
            print(f"{post[0]} - {post[1]} - {post[2]}")
            
    elif choice == "4":
        target = input("По какой категории отфильтровать? ")
        filtered = [post for post in posts if post[2] == target]
        print(f"\nПосты в категории {target}:")
        if filtered:
            for post in filtered:
                print(f"{post[0]} - {post[1]} - {post[2]}")
        else:
            print("Постов в категории нет")

    elif choice == "0":
        print("До свидания")
        break

    else:
        print("Не понял команду, попробуй еще раз")