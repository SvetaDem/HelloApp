print("Hello Python from Visual Studio!")
s = "*"*30
print(s)
print("New project")
print(s)

# Дана строка. Вывести первые три символа и последний три символа, если длина строки больше 5.
# Иначе вывести первый символ столько раз, какова длина строки.

s = str(input("Введите строку: "))
if len(s) > 5:  # Проверка длины строки
    print('Первые три символа: ', s[:3])
    print('Последние три символа: ', s[-3:])
else:
    for i in s:
       print(s[0])

