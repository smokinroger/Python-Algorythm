import random

# Задача 1
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь


def les1():

    digit = input("Введите трех значное число")

    if len(digit) != 3 or not digit.isdigit():
        print("Ошибка, число не верное")
        les1()
    else:
        digits = list(map(int, digit))

        dsum = digits[0] + digits[1] + digits[2]
        dmultiply = digits[0]*digits[1]*digits[2]
        print(f'Сумма {dsum}, Произведение {dmultiply}')
#les1

# Задача 2
# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.


print("Побитовое И(5&6) результат:{}. 5 это 101 а 6 это 110 результат 100".format(5 & 6))
print("Побитовое ИЛИ(5|6) результат:{}. 5 это 101 а 6 это 110 результат 111 ".format(5 | 6))
print("Побитовое Исключающее ИЛИ(xor)(5^6) результат:{}. 5 это 101 а 6 это 110 результат 011".format(5 ^ 6))
print("Побитовое НЕ (~5 ~6) результат:{} и {}. 5 это 101 а 6 это 110 результат 010 и 001, "
      "но в питоне опреация эквивалентна -(x+1)".format(~5, ~6))
print("Побитовые свдиги(5>>2 5<<2) результат:{} и {}. 5 это 101  результат 001 и 100 ".format(5 >> 2, 5 << 2))
print("Побитовые сдвиги(6>>2 6<<2) результат:{} и {}. 6 это 110 результат 001 и 000 ".format(6 >> 2, 6 << 2))


# Задача 3
# По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

A = list(map(int, input("Введите координаты точки A в формате x,y").split(',')))
B = list(map(int, input("Введите координаты точки B формате x,y").split(',')))

if len(A) != 2 or len(B) != 2 or A == B:
    print(f"Координаты одной из точек не верны или одинаковы Точки: {A}, {B}")
else:
    k = (B[1]-A[1])/(B[0]-A[0])
    b = A[1] - k*A[0]

    print(f"Для введенных точек: A({A}), B({B}),уравнение прямой "
          f"вида y = kx + b будет иметь коэффициенты k{k:.2f} и b{b:.2f}")

# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.


case = int(input("1.Вывод случайного целого \n"
                 "2.Вывод случайного дробного \n"
                 "3.Вывод случайного символа \n"))
print(f"Выбран пункт: {case}")

if case == 1:
    a, b = map(int, input("Введите границы диапазаноа в формате 1,2").split(','))
    print("Случайное целое: {}".format((random.randint(a, b) if a < b else random.randint(b, a))))
    pass
elif case == 2:
    a, b = map(float, input("Введите границы диапазаноа в формате 1,2").split(','))
    print("Случайное дробное: {}".format((random.uniform(a, b) if a < b else random.randint(b, a))))
elif case == 3:
    a, b = input("Введите границы диапазаноа в формате a,b").split(',')
    print("Случайный символ {}".format(chr(random.randint(ord(a), ord(b)) if a < b else random.randint(ord(b), ord(a)))))


