class ValidationError(Exception):
    """Ошибка валидации данных"""


def create_post(title: str, body: str) -> dict:
    if not title.strip():
        raise ValidationError("Заголовок не должен быть пустым")
    if not body.strip() or len(body.strip()) < 15:
        raise ValidationError("Текст поста не должен быть пустым или короче 15 символов")
    return {
        "title": title,
        "body": body,
    }

if __name__ == "__main__":

    title_text = "Занимательная алгебра"
    body_text = "Это мой"

    try:
        print(create_post(title_text, body_text))
    except ValidationError as e:
        print(f"Не удалось создать пост, ошибка: {e}")
