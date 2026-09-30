post_text = "Привет"
is_published = True
is_premium = False
has_subscription = False

print("Есть ли статья для отображения: ", bool(post_text))

can_show = post_text and is_published and (is_premium or has_subscription)

if can_show:
    print(f"Показываем текст: {post_text}")
else:
    print("Пост скрыт")

author_name = input("Имя автора (можно пусто) ")
display_name = author_name or "Аноним"

print(f"Автор: {display_name}")

age = int(input("Сколько тебе лет? "))

if 0 <= age <= 100:
    print("Возраст корректен")
else:
    print("Возраст некорректен")
