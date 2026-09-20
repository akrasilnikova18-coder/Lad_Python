name = "Алена"
age = 42
height = 1.71
is_student = True
nothing = None

print(name, age, height, is_student, nothing)

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

year = int("2026")
print(year + 1)

name = input("Привет! Как тебя зовут? ")
age = int(input("Сколько тебе лет? "))
next_year_age = age + 1

print(f"Привет, {name}! В следующем году тебе будет {next_year_age}.")
print("Привет, {0}! В следующем году тебе будет {1}.".format(name, next_year_age))

next_year_string = "Привет, {name}! В следующем году тебе будет {next_year_age}."

print(next_year_string.format(name=name, next_year_age=next_year_age))