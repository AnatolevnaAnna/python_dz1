num = input("Введи число: ")

if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print(f"Число {int(num)} является четным")
    else:
        print(f"Число {int(num)} не является четным")
else:
    print(f"Это не число?")
