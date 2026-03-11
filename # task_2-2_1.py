# task_2-2_1
curse_name = "Информатика"
number_stage = 2
quantity = 9
print(f"Название курса: {name_course}, номер текущего этапа: {number_stage}, количество выполненных задач: {quantity}")

# task_2-2_2
user_input = input("Введите текст: ")
processed_input = user_input.upper()

print(user_input, processed_input, sep=" -> ")

# task_2-2_3
device_name = input("Введите название прибора:")
inventory_number = input("Введите инвентарный номер:")
device_status = input("Исправен прибор \"да/нет\"?")
quantity = input("Назовите количество приборов:")
print(f"Название прибора:\t{name_device}")
print(f"Инвентарный номер прибора:\t{inventory_number}")
print(f"Исправность прибора:\t{device_status}")
print(f"Количество приборов:\t{quantity}")

name_reagent = input("Введите название реактива:")
quantity = input("Введите количество реактива:")
print(f"Реактив {name_reagent} поступил на склад в количестве {quantity} шт")
