from datetime import datetime
import locale # Чтобы месяц выводил на русском языке


"""Звёздочка (самостоятельное изучение datetime): изучи официальную документацию Python
по модулю datetime. Напиши программу, которая выводит текущую дату в трёх разных форматах:
28.08.2026, 2026-08-28, 28 августа 2026. Используй strftime() с подстановками %d, %m, %Y, %B.
Полезно: datetime.datetime.now(), now.strftime("%d.%m.%Y"), datetime.strptime(...)."""

locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")

now = datetime.now()

months = [
    "января", "февраля", "марта", "апреля",
    "мая", "июня", "июля", "августа",
    "сентября", "октября", "ноября", "декабря"
]

print(now.strftime("%d.%m.%Y"))
print(now.strftime("%Y-%m-%d"))
print(f"{now.day} {months[now.month - 1]} {now.year}") # Иначе выводил "октябрь" в именительном падеже
# now.month возвращает номер месяца от 1 до 12, а в списке нумерация от 0, поэтому минус 1
