#Example 5.
# Сделать функцию которая на вход принимает строку.
# Анализирует исключительно методом isdigit() без доп библиотек и переводит строку в число.
# Функция умеет распозновать отрицательные числа и дроби.
# Примеры:
# -6.7 Вы ввели дробное отрицательное число -6.7
# 5.4r Вы ввели не корректное число 5.4r
# 5    Вы ввели положительное целое число 5
#  -.777  Вы ввели отрицательное дробное число -0.777

def filter_number(a):
    for i in range(len(a)):
        if a[i] in "".join(map(chr, range(97, 123))):
            print("Вы ввели не корректное число", a)
            exit()
    if not a.isdigit():
            if abs(float(a)).isalnum()!=True:
                if "." in a:
                   if float(a) > 0:
                        print("Вы ввели положительное дробное число", float(a))
                   else:
                        print("Вы ввели отрицательное дробное число", float(a))
                else:
                    print("Вы ввели не корректное число", a)
            else:
                ("Вы ввели отрицательное целое число", int(a))
    else:
            print("Вы ввели положительное целое число", int(a))
filter_number("-5")
# filter_number(input().lower())
