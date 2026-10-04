# **Фильтрация строк через comprehension.** Заведите список из 8–10 строк (например, названий категорий блога).
# Через list comprehension: а) отфильтруйте строки длиннее 5 символов;
# б) постройте список из длин всех строк (`len`);
# в) постройте список строк с первой буквой в верхнем регистре (`capitalize()`). Выведите каждый результат.

titles = ["python", "django", "java script", "java", "sql", "php", "c++", "rust", "cotlin"]

#список со строками длиннее 5 символов
long_titles = [title for title in titles if len(title) > 5]
print(f"Категории длиннее 5 символов: {long_titles}")

#список из длин всех строк
len_titles = [len(title) for title in titles]
print(f"Длины всех строк: {len_titles}")

#все строки с заглавной буквы
capitalized_titles = [title.upper() if title == "sql" or title == "php" else title.capitalize() for title in titles]
print(f"Все строки с заглавной буквы: {capitalized_titles}")