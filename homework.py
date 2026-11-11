name = input("Ваше прізвище: ")
points = int(input("Введіть кількість балів: "))

if points >= 80:
    print(f" Студент {name} здав іспит")
else:
    print(f"{name}, Студент {name} не здав іспит")