# Удвоение или смена знака у A, B, C
while True:
    try:
        a = float(input("Введите A: "))
        b = float(input("Введите B: "))
        c = float(input("Введите C: "))
        break
    except ValueError:
        print("Введите правильные числа")
if a < b < c:
        a = a * 2
        b = b * 2
        c = c * 2
else:
        a = -a
        b = -b
        c = -c

print(f"A = {a}, B = {b}, C = {c}")