import json
from pathlib import Path


DATA_FILE = Path("articles.json")

def load_articles() -> list:
    if not DATA_FILE.exists():
        return []
    
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
    

def save_articles(articles: list) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)
        

def main() -> None:
    articles = load_articles()
    title = input("Введите название статьи ")
    author = input("Введите автора ")
    new_post = {
        "title": title,
        "author": author,
    }

    articles.append(new_post)
    save_articles(articles)
    print("Статья сохранена")

    print("\nТекущий список статей:")
    for article in enumerate(articles, start=1):
        print(f"{article[0]}. {article[1]['title']} - {article[1]['author']}")


if __name__ == "__main__":
    main()