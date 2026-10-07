from collections import Counter

odd_squares = {number: number**2 for number in range(10) if number % 2 != 0}
print(odd_squares)

words = ["Python", "Django", "Web", "API", "Python"]
lenght_of_words = {word: len(word) for word in words}
print(lenght_of_words)

counter = Counter(words)
print(counter)
print(counter.most_common(2))

char_counter = Counter("Занимательная математика")
print(char_counter)
