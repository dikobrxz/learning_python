string = input('Введите строку: ')
symbol_c=""
for i, c in enumerate(string):
    if i == 2:
        continue
    if c == 'c':
        symbol_c ="Найден символ 'c'"
    print(c, end="")
print("\nДлина строки:", len(string))
print("Строка без последнего символа:", string[:-1])
print (symbol_c)