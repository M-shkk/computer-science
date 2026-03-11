# task_2-5_nucl_count 
dna = input("Введите последовательность ДНК:")
dnabig = dna.upper()
count_A = dnabig.count("A")
count_T = dnabig.count("T")
count_G = dnabig.count("G")
count_C = dnabig.count("C")
length = len(dnabig)
A = count_A / length * 100
T = count_T / length * 100
G = count_G / length * 100
C = count_C / length * 100

print("=== Анализ последовательности ДНК ===")
print(f"Введите последовательность ДНК: {dna}\nПоследовательность ДНК в верхнем регистре:{dnabig}")
print(f"Подсчет нуклеотидов:\nA: {count_A}\nT: {count_T}\nG: {count_G}\nC: {count_C}")
print(f"Процентное содержание А: {A:.2f}%\nПроцентное содержание T: {T:.2f}%")
print(f"Процентное содержание G: {G:.2f}%\nПроцентное содержание C: {C:.2f}%")
print(f"Общая длина последовательности: {length} нуклеотидов")