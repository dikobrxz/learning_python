num = float(input('Введите произвольное число: '))
border = float(input('Введите пограничное число: '))

if num < border:
    print("Произвольное число "+ "%.0f" % num + " меньше, чем пограничное " + "%.0f" % border)
elif num > border:
    print("Произвольное число "+ "%.0f" % num + " больше, чем пограничное " + "%.0f" % border)
elif border * 3 < num:
    print(" более чем в 3 раза")
else:
    print("Произвольное число "+ "%.0f" % num + " равно пограничному " + "%.0f" % border)