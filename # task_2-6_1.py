# task_2-6_1
pH =float(input("Введите значение pH:"))
if pH > 7:
    print("Щелочная среда")
elif pH == 7:
    print("Нейтральная среда")
else:
    print("Кислотная среда")

# task_2-6_2
temp = float(input("Какая температура листа сейчас? "))

if temp < 5:
    print("Слишком холодно. Фотосинтез почти не идёт.")
elif 5 <= temp <= 25:
    print("Оптимально для растений с C3-метаболизмом")
elif 25 < temp <= 35:
    print("Хорошо для растений C4-метаболизмом")
else:
    print("It's hot as hell! Cool down, bro.")

# task_2-6_3
phenotype_donor = input("Введите группу крови донора:").upper()
phenotype_patient = input("Введите группу крови пациента:").upper()
if phenotype_donor == "I" and (phenotype_patient == "I" or phenotype_patient == "II" or phenotype_patient == "III" or phenotype_patient == "IV"):
   print(f"Возможно переливание пациенту с {phenotype_patient} группой крови.")
elif phenotype_donor == "II":
    if phenotype_patient == "II" or phenotype_patient == "IV":
        print(f"Возможно переливание пациенту с {phenotype_patient} группой крови.")
    else:
        print(f"Невозможно переливание пациенту с {phenotype_patient} группой крови.")
elif phenotype_donor == "III":
    if phenotype_patient == "III" or phenotype_patient == "IV":
        print(f"Возможно переливание пациенту с {phenotype_patient} группой крови.")
    else:
        print(f"Невозможно переливание пациенту с {phenotype_patient} группой крови.")
elif phenotype_donor == "IV":
    if phenotype_patient == "IV":
        print(f"Возможно переливание пациенту с {phenotype_patient} группой крови.")
    else:
        print(f"Невозможно переливание пациенту с {phenotype_patient} группой крови.")
else:
   print("Таких групп крови не существует, переливание невозможно.")

# task_2-6_4
print("«Витязь на распутье»")
print("=" * 50)

print("\nНадпись на камне:")
print("  • Налево пойдёшь — коня потеряешь")
print("  • Направо пойдёшь — голову потеряешь")
print("  • Прямо пойдёшь — счастье найдешь")

way = input("\nКуда поедет витязь? (налево/направо/прямо) ").lower()

if way == "налево":
    print("Витязь поехал налево.")
    print("Конь витязя умер")

elif way == "направо":
    print("Витязь поехал направо.")
    print("Витязь умер")

elif way == "прямо":
    print("Витязь поехал прямо")
    print("Витязь счастлив")

else:
    print("Витязь думает")