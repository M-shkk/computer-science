# task_2-4_calories
protein = float(input("Введите массу белков в продукте (г):"))
lipid = float(input("Введите массу жиров в продукте (г):"))
carbohydrate = float(input("Введите массу углеводов в продукте (г):"))
KAL = protein * 4 + lipid * 9 + carbohydrate * 4

print(f"Общая каллорийность продукта = {KAL} калл")

# task_2-4_bmi
weight = float(input("Введите свой вес (в кг):"))
height = float(input("Введите свой рост (в м):"))
bmi = weight / (height ** 2) 

print("--- Отчет о состоянии здоровья ---")
print(f"Рост:\t{weight}\nВес:\t{height}\nИндекс массы тела:\t{bmi:.2f}")

# task_2-4_pharmacy
quantity_capsules = int(input("Введите количество произведенных капсул:"))
capacity = int(input("Введите количество капсул в одной упаковке:"))
full_packaging = quantity_capsules // capacity
remains =  quantity_capsules % capacity
print("--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{full_packaging}\nОстаток капсул:\t{remains}")

# task_2-4_lab_assistant
volume = float(input("Введите объем раствора:"))
salt_mass = volume * 0.009
total_volume = volume

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ\n")
    file.write("-" * 25)
    file.write(f"\nОбщий объем:\t{total_volume} мл\nМасса соли:\t{salt_mass:.2f} г\nОбъем воды:\t{volume} мл")