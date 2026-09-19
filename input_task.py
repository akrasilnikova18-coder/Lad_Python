name = input("Привет! Как тебя зовут? ")
age = int(input("Сколько тебе лет? "))
next_year_age = age + 1

print(f"Привет, {name}! В следующем году тебе будет {next_year_age}.")
print("Привет, {0}! В следующем году тебе будет {1}.".format(name, next_year_age))

next_year_string = "Привет, {name}! В следующем году тебе будет {next_year_age}."

print(next_year_string.format(name=name, next_year_age=next_year_age))
