# task_2-3_recipe
medium_name = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temp = input("Введите температуру стерилизации: ")

with open("recipe.txt", "w", encoding="utf-8") as card:
    card.write(medium_name + "\n")
    card.write(f"\tКонцентрация агара:\t{agar_concentration}%\n")
    card.write(f"\tТемпература стерилизации:\t{sterilization_tempreture}К\n")

print("Файл 'recipe.txt' успешно сформирован!")

#task_2-3_sensor
operator_name = input("Введите имя оператора: ")
pressure_sensor = input("Введите текущее значение датчика давления (Па): ")

with open("sensor_log.txt", "a", encoding="utf-8") as card:
    card.write(f"ОПЕРАТОР:\tЗНАЧЕНИЕ:\n{name_operator}\t{pressure_sensor} Па")

print("Данные успешно сохранены в sensor_log.txt")

# task_2-3_lab_journal
researcher = input("ФИО: ")
date = input("Дата: ")
experiment = input("Название эксперимента: ")
conclusion = input("Вывод: ")

print("\n┌" + "─" * 58 + "┐")
print("│         ЛАБОРАТОРНЫЙ ЖУРНАЛ          │")
print("├" + "─" * 58 + "┤")
print(f"│ ФИО:           {researcher:<40} │")
print(f"│ Дата:          {date:<40} │")
print(f"│ Эксперимент:   {experiment:<40} │")
print("├" + "─" * 58 + "┤")
print(f"│ ВЫВОД: {conclusion:<52} │")
print("└" + "─" * 58 + "┘")

with open("journal.txt", "w", encoding="utf-8") as card:
    card.write("┌" + "─" * 58 + "┐\n")
    card.write("│         ЛАБОРАТОРНЫЙ ЖУРНАЛ          │\n")
    card.write("├" + "─" * 58 + "┤\n")
    card.write(f"│ ФИО:           {researcher:<40} │\n")
    card.write(f"│ Дата:          {date:<40} │\n")
    card.write(f"│ Эксперимент:   {experiment:<40} │\n")
    card.write("├" + "─" * 58 + "┤\n")
    card.write(f"│ ВЫВОД: {conclusion:<52} │\n")
    card.write("└" + "─" * 58 + "┘\n")

print("\n✅ Данные сохранены в journal.txt")