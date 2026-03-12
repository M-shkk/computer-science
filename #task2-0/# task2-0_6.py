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

    print("Содержимое файла:")
with open("output.txt", "r", encoding="utf-8") as файл:
    print(файл.read())