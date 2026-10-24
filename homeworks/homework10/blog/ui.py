from rich.console import Console
from rich.table import Table

from . import data
"""Если импорт внутри одного пакета, то программа не падает, а если из корневого main - то падает
То есть, если относительная ссылка из корневого main - не знает, какой файл импортировать,
и выдает ошибку. Либо импортирует какой-то другой файл с таким же названием, а там таких функций нет"""


console = Console()


def create_post_menu() -> None:
    """Запрашивает у пользователя название, автора и текст статьи
    вызывает функцию "Добавить статью" и выводит название добавленной статьи"""
    title = input("Введите название статьи ")
    author = input("Введите имя автора ")
    text = input("Введите текст статьи ")
    
    data.create_post(title, author, text)
    console.print(f"[green]Статья {title} сохранена[/green]")
    
    
def show_posts_menu() -> None:
    articles = data.list_posts()
    
    if not articles:
        console.print("[red]Статей нет[/red]")
        return

    table = Table(title="Статьи блога")
    table.add_column("Заголовок")
    table.add_column("Автор")
    table.add_column("Текст")

    for article in articles:
        table.add_row(article["title"], article["author"], article["text"])

    console.print(table)


def find_posts_menu() -> None:
    """Запрашивает у пользователя название статьи, по которому будем искать статью
    Если статьи найдены - выводит их"""
    title_for_search = input("Введите название статьи для поиска ")
    articles_finded = data.find_post(title_for_search)
    
    if not articles_finded:
        console.print("[red]Статей нет[/red]")
        return

    table = Table(title="Статьи блога")
    table.add_column("Заголовок")
    table.add_column("Автор")
    table.add_column("Текст")

    table.add_row(articles_finded["title"], articles_finded["author"], articles_finded["text"])

    console.print(table)

