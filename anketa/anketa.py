class Questionary:
    name = input("Введите свое имя")
    surname = input("Введите фамилию")
    age = int(input("Введите свой возраст"))
    weight = float(input("Введите свой вес"))
    height = float(input("Введите свой рост"))
    gender = input("Какой ваш пол? (М/Ж)")

    bmi = weight / (height ** 2)

    print("\nСпасибо за заполнение анкеты.")
    print("Ваши данные:")
    print("Имя:", name)
    print("Возраст:", age)
    print("Вес:", weight, "кг")
    print("Рост:", height, "м")
    print("Пол:", gender)
    print("Индекс массы тела (ИМТ):", bmi)



