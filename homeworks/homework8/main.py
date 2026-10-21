#**Задание на закрепление — мини-проект «Блог CLI».** Продолжите развивать консольную утилиту
# со статьями, вынося логику в функции. Проект (ветка `homework-8`, файл `main.py`)
# должен содержать и использовать описанные ниже функции.

articles = [
    {"title": "Среда обитания манулов", "category": "Манулы", "author": "Игорь", "rating": 5.3, "views": 165,},
    {"title": "Как выращивать розы", "category": "Садоводство", "author": "Анна", "rating": 3.6, "views": 15,},
    {"title": "Что едят манулы", "category": "Манулы", "author": "Антон", "rating": 4.8, "views": 1365,},
    {"title": "Панды в Московском зоопарке", "category": "Панды", "author": "Ирина", "rating": 6.0, "views": 5165,},
]

keys_list = ["title", "category", "author", "rating", "views"]


def create_article(title: str, category: str, author: str, rating: float, views: int) -> dict:
    """Новая статья. Создается словарь статьи и добавляется в список
    Проверку float пришлось сделать при вызове функции, в самой функции не работала"""
    article = {
        "title": title,
        "category": category,
        "author": author,
        "rating": rating,
        "views": views,
    }
    articles.append(article)
    return article


def show_articles(arlicles_list: list) -> None:
    """Выводит все статьи"""
    if not arlicles_list:
        print("Список статей пуст")
        return

    for num, article in enumerate(arlicles_list, start=1):
        print(f"{num}. Название: {article['title']}, Категория: {article['category']}, "
              f"Автор: {article['author']}, Рейтинг: {article['rating']}, Просмотров: {article['views']}")


def filter_by_category(articles_filtered: list, category: str) -> list:
    """Фильтрация по категории. Возвращает статьи выбранной категории"""
    return [article for article in articles_filtered if article["category"] == category]


def find_articles(articles_finded: list, query: str) -> list:
    """Поиск по заголовку / автору. Возвращает список найденных статей"""
    return [article for article in articles_finded if query in article["title"] or query in article["author"]]


def sort_articles(articles_list: list, key="rating", reverse=True, bonus="views") -> list:
    """Сортировка по заголовку / рейтингу / категории / просмотрам / автору. Возвращает отсортированный список
    Кортеж из двух полей решает задачу вторичной сортировки, потому что сначала статьи
    сравниваются по ключу, а потом, если ключи одинаковые - то по бонусу"""
    if key in keys_list:
        return sorted(articles_list, key=lambda a: (a[key], a.get(bonus, 0)), reverse=reverse)
    else:
        print("Неверное значение key")
        return


def show_help() -> None:
    """Показывает список доступных команд"""
    print("""
        Доступные команды:
        add - Добавить статью
        show - Показать все статьи
        filter - Отфильтровать статьи по категории
        find - Поиск по статьям
        sort - Отсортировать статьи по выбранному значению
        help - Показать справку
        exit - Выйти
    """)
    

print("Мини-проект блог CLI")
show_help()

while True:
    command = input("Введите команду: ").strip().lower()
    
    if command == "add":
        title = input("Введите название статьи: ")
        author = input("Введите имя автора: ")
        category = input("Введите категорию: ")
        views = int(input("Введите количество просмотров: "))

        try:
            rating = float(input("Введите рейтинг: "))
        except ValueError:
            print("Рейтинг должен быть типа float")
            continue
        
        if title and author and category and rating and views:
            create_article(title, category, author, rating, views)
            print("Статья добавлена")
        else: 
            print("Не указаны параметры статьи")
            continue
    
    elif command == "show":
        show_articles(articles)
        
    elif command == "filter":
        category = input("Введите категорию для фильтра: ")
        if category:
            filtered_articles = filter_by_category(articles, category)
            print(f"\nВ категории {category} {len(filtered_articles)} статей")
            show_articles(filtered_articles)
        else:
            print("Категория не выбрана")
            continue
            
    elif command == "find":
        query = input("Введите имя автора или название статьи, которое нужно найти: ")
        if query:
            articles_finded = find_articles(articles, query)
            if articles_finded:
                print("\nНайденные статьи:")
                show_articles(articles_finded)
            else: 
                print ("Статьи с таким автором или названием нет")
                continue
        else:
            print("Не введен параметр запроса")
            continue
            
    elif command == "sort":
        key = input(f"Поле для сортировки {keys_list} ")
        bonus = input(f"Введите второй параметр сортировки {keys_list} ")
        reverse = input("Сортировать по убыванию? ")
        
        if reverse:
            reverse = True
        else:
            reverse = False

        print("\nОтсортированные статьи:")
        sorted_article = sort_articles(articles, key, reverse)
        show_articles(sorted_article)
        
    elif command == "help":
        show_help()
        
    elif command == "exit":
        print("Выход из программы")
        break
        
    else:
        print("Команда неизвестна, введите help")


sorted_articles_for_rating = sort_articles(articles, key="rating", reverse=False)
print("\n Статьи с сортировкой по рейтингу")
show_articles(sorted_articles_for_rating)

sorted_articles_for_views = sort_articles(articles, key="views", reverse=True)
print("\n Статьи с сортировкой по числу просмотров")
show_articles(sorted_articles_for_views)


"""Коротко изучите по документации модуль `functools` (функции `lru_cache`, `partial`, `wraps`)
**или** базовое понятие **рекурсии** (функция, вызывающая саму себя, например, факториал
или поиск по вложенному списку). Опишите своими словами комментарием в коде,
что вы выбрали и зачем, и приведите рабочий пример. **Важно:** декораторы полноценно
разбираются на занятии 9 — сейчас просто «познакомьтесь» и зафиксируйте наблюдение."""

"""Рекурсия - это функция, которая вызывает саму себя. Она используется при решении простых задач,
которые можно разбить на задачи такого же типа. Важно! Нужно задать условие, при котором
функция останавливается, иначе она будет вызывать себя бесконечно"""

def countdown(n: int) -> int:
    """Функция обратного отсчета. Перебирает числа от заданного до нуля по убыванию
    Когда число становится равным 0, пишет старт. Альтернативный вариант - цикл с условием"""
    if n == 0:
        print("Старт!")
        return

    print(n)
    countdown(n - 1)

countdown(8)

# новый список и ключ сравниваем со списком!
# если в качестве аргумента в функцию передать список
    