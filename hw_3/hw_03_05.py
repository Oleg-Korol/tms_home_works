#Example.5

# Реализовать вычисление факториала с помощью цикла while и for.
# Продумать область допустимых значений.
# Добавить проверки, исключаютщие бесконечный цикл.
# Написать тесты на различные варианты.

#Используем цикл While===================================================================================================


n = int(input("Введите число"))
if n<=0:
    exit()
f = 1
while n > 1:
    assert n>0
    f = f*n
    n -= 1
print("Факториалл равен:", (f))



# Используя цикл For=====================================================================================================


n = int(input("Введите число"))
if n<=0:
    exit()
f = 1
for i in range(2, n + 1):
    f=f* i
print("Факториалл равен:", (f))
