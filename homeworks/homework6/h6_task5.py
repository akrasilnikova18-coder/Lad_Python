# Словарь с defaultdict. Дан список кортежей [(имя, предмет, оценка), ...].
# Используя defaultdict(list), сгруппируйте оценки по именам студентов, а затем через defaultdict(list)
# или Counter выведите для каждого студента список его предметов и средний балл.
# (Подумайте: как посчитать средний балл, имея список оценок?)
from collections import defaultdict
from pprint import pprint

performance_journal = [
    ("Виктор", "Русский язык", "55",),
    ("Сергей", "Математика", "84",),
    ("Виктор", "Информатика", "78",),
    ("Сергей", "Химия", "98",),
    ("Сергей", "География", "34",),
]

#сгруппируйте оценки по именам студентов
#затем через defaultdict(list) или Counter выведите для каждого студента список его предметов и средний балл
student_grades = defaultdict(list)
student_subjects = defaultdict(list)

for line in performance_journal:
    student_grades[line[0]].append(line[2])
    student_subjects[line[0]].append(line[1])

print("\nПредметы для каждого студента")
for student, subjects in student_subjects.items():
    print(f"{student}: {subjects}")

middle_grade = 0
print("\nБаллы для каждого студента")
for student, grades in student_grades.items():
    print(f"{student}: {grades}")
    for grade in grades:
        middle_grade += int(grade)
    print(f"Студент: {student}, средний балл: {middle_grade // len(grades)}")



