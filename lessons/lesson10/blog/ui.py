from rich.console import Console
from rich.table import Table

from blog import data


console = Console()


def create_post_menu() -> None:
    title = input("Введите название статьи ")
    author = input("Введите имя автора ")
    text = input("Введите текст статьи ")

    data.create_post(title, author, text) # обращаемся к импортируемой функции
    console.print(f"[green]Статья {title} сохранена[/green]")


def show_posts_menu() -> None:
    posts = data.list_posts()
    if not posts:
        console.print("[yellow]Статей нет[/yellow]")
        return
    #for post in posts:
        #print(f"Заголовок: {post["title"]}, Автор: {post["author"]}, Текст: {post["text"]}")
    table = Table(title="Статьи блога")
    table.add_column("Заголовок")
    table.add_column("Автор")
    table.add_column("Текст")

    for post in posts:
        table.add_row(post["title"], post["author"], post["text"])

    console.print(table)

if __name__ == "__main__":
    print("Добро пожаловать!")

