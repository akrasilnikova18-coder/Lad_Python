posts: list[dict] = []


def create_post(title: str, author: str, text: str) -> dict:
    post = {
        "title": title,
        "author": author,
        "text": text,
    }
    posts.append(post)
    return post


def list_posts() -> list[dict]:
    return posts


def find_post(title: str) -> dict | None:
    for post in posts:
        if post["title"] == title:
            return post
    return None

