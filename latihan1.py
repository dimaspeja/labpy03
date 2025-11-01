import random

n = int(input("Masukkan nilai N: "))
i = 0  
while i < n:
    for _ in range(1):
        bilangan = random.random()
        if bilangan < 0.5:
            i += 1
            print(f"data ke-{i} => {bilangan}")

print("Selesai")