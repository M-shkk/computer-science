# task_2-7_1
files = ["seq1", "seq2", "seq3", "seq4"]
for name in files:
   new_name = name + ".18.12.2001.fasta"
   print(f"{new_name}")

# task_2-7_2
seq = ["ATATACGCGTA", "CTTCGGNGGA"]

for name in seq:
    print(name)
    for letter in name:
       print(letter)

print("Цикл выполнен")