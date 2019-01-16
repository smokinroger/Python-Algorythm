# Задача 1.
# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке
# и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль,
# если он ввел 0 в качестве делителя.


def division(a: float, b: float):
    return a/b


def simple_calculator():
    operation = input("Выберите совершаемую операцию между числами А и B \n"
                      "(Доступные: +, -, *, / , 0 - выход)")

    opers = {'+': float.__add__,
             '-': float.__sub__,
             '*': float.__mul__,
             '/': division}

    if operation != '0':
        num1 = input("Введите число А")
        num2 = input("Введите число B")

        if len(operation) == 1 and opers.__contains__(operation):
            print(opers[operation](float(num1), float(num2)))
        else:
            print("Введена не корректная операция")
        simple_calculator()
    elif operation == '0':
        return


#simple_calculator()

# Задача 2 и 3.
# 2.Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# 3.Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

digit = input("Введите произвольное число")
count = 0

if digit.isdigit():
    for a in digit:
        count += 1 if float(a) % 2.0 != 0 else 0
    print(f"Введено число: {digit}. \n"
          f"Количество нечетных симоволов {count}")
    bstr = list()
#задача 3
    for i in range(len(digit)-1, -1, -1):
          bstr.append(digit[i])
    print(f"Задом на перед:) {str(bstr)} ")
else:
    print(f"Введена символьная строка вместо числа {digit}")

# Задача 4
dim = (1, -0.5, 0.25, -0.125)
dsum = 0.0
print(f"\n Есть ряд елементов {dim}")
n = input("Введите количество елментов для получения их суммы")

if n.isdigit() and len(n) == 1:
    for a in range(0, int(n)):
        dsum += float(dim[a])
    print(f"Сумма {len(n)} елементов {dsum}")

# Task 5
dim = list()
for n in range(32, 128):
    dim.append(chr(n))

cnt = len(dim)
flg = 0
print(len(dim))
while cnt > 0:
    plist = list()
    b = flg
    for i in range(b, b+10):
        if i < len(dim):
            plist.append(f"{ord(dim[i])}:{dim[i]}")
    print(plist)
    flg += 10
    cnt -= 10




