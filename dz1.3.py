age = input("Введи возраст: ")

if not age.isdigit() and age.isalpha():
    print(f"Ошибка: введено не число!")

else:    
    age = int(age)
    if age >= 18:
        print(f"Ты уже взрослый мальчик")
    elif 0 < age < 18:
        print(f"Ты еще малой")
    elif age < 0:
        print(f"Ошибка: возраст не может быть отрицательным!")