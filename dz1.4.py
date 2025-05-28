while True:
    num = input("Введи число: ")

    if num == "exit":
        print("Выход из программы...")
        break

    mnum = num.lstrip('-')

    if mnum.isdigit():
        dig = len(mnum)
        print(f"В этом числе {dig} цифры.")

    else:    
        print(f"Ошибка: данные не являются числом.")