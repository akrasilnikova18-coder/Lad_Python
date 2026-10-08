#Dict comprehension + Counter. Для списка слов words:
# постройте словарь {слово: длина} через dict comprehension;
# посчитайте частоту встречаемости слов через Counter;
# выведите топ-3 самых частых слова через most_common(3).
from collections import Counter

words = ["Математика", "Физика", "Информатика", "Геометрия", "Физика", "Химия", "Математика", "Физика",]

# постройте словарь {слово: длина} через dict comprehension;
length_of_words = { word: len(word) for word in words }
print(length_of_words)

# посчитайте частоту встречаемости слов через Counter;
word_frequency = Counter(words)
print(word_frequency)

# выведите топ-3 самых частых слова через most_common(3)
print(f"Чаще всего встречаются: {word_frequency.most_common(3)}")
