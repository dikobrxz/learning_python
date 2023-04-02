import math
import random

while True:
    print("Выберите операцию:")
    print("+ для сложения")
    print("- для вычитания")
    print("* для умножения")
    print("/ для деления")
    print("** для возведения в степень")
    print("mod для вычисления модуля")
    print("rd для генерации случайного числа")
    print("! для вычисления факториала")
    print("acos для вычисления арккосинуса")

    choice = input("Введите операцию: ")

    if choice == "+":
        a = float(input("Введите первое слагаемое: "))
        b = float(input("Введите второе слагаемое: "))
        print("Результат:", a + b)
    if choice == "-":
        a = float(input("Введите уменьшаемое: "))
        b = float(input("Введите вычитаемое: "))
        print("Результат:", a - b)
    if choice == "*":
        a = float(input("Введите первый множитель: "))
        b = float(input("Введите второй множитель: "))
        print("Результат:", a * b)
    if choice == "/":
        a = float(input("Введите делимое: "))
        b = float(input("Введите делитель: "))
        if b == 0:
            print("Ошибка: деление на ноль")
        else:
            print("Результат:", a / b)
    if choice == "**":
        a = float(input("Введите число: "))
        b = float(input("Введите степень: "))
        print("Результат:", a ** b)
    if choice == "mod":
        a = float(input("Введите число: "))
        print("Результат:", abs(a))
    if choice == "rd":
        a = float(input("Введите минимальное значение: "))
        b = float(input("Введите максимальное значение: "))
        print("Результат:", random.uniform(a, b))
    if choice == "!":
        n = int(input("Введите число: "))
        print("Результат:", math.factorial(n))
    if choice == "acos":
        x = float(input("Введите число: "))
        print("Результат:", math.acos(x))