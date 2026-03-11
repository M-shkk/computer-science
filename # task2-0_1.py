# task2-0_1
print('Hello World!')

# task2-0_2
print("Фамилия:" "Назатова", "Имя:" "Мария", "Группа:" "4731204/50003", "Год:" "2026")

# task2-0_3
print("04", "02", 2026, sep=".")

# task2-0_4
print("Предмет\tОценка\nМатематика\t5\nФизика\t4\nИнформатика\t5")

# task2-0_5
name = "Саша"
group = 1234
score = 5
print(f"Студент {name} из группы {group} получил {score} баллов")

# task2-0_6
name = "Назатова Мария"
age = 18
city = "Санкт-Петербург"
zodiac = "Близнецы"

with open("output.txt", "w", encoding="utf-8") as файл:
    print("Имя:", name, file=файл)
    print("Возраст:", age, "лет", file=файл)
    print("Город:", city, file=файл)
    print("Знак зодиака:", zodiac, file=файл)

print("Файл output.txt создан!")

print("\nСодержимое файла:")
with open("output.txt", "r", encoding="utf-8") as файл:
    print(файл.read())

# task_2-0_creative

print("Добро пожаловать!", end=" ")
год_обучения = 1
print("\nСтудент", год_обучения, "курса 2026", sep=" ")
print("*** Удачи в обучении! ***")
