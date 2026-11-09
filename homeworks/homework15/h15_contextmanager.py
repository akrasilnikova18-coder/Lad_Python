from contextlib import contextmanager


# Модуль contextlib позволяет создавать собственные контекстные менеджеры
# с помощью декоратора @contextmanager.


@contextmanager
def open_log(filename: str):
    print(f"Открыли лог: {filename}")

    # yield временно приостанавливает выполнение функции и передаёт управление внутрь блока with.
    try:
        yield
    finally:
        print(f"Закрыли лог: {filename}")


with open_log("app.log"):
    print("Записываем информацию в лог")

# Результат:
# Открыли лог: app.log
# Записываем информацию в лог
# Закрыли лог: app.log