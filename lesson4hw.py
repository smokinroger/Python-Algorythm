
import timeit
import cProfile

#Задача 1
# Проанализировать скорость и сложность одного любого алгоритма,
#  разработанных в рамках домашнего задания первых трех уроков.
def division(a: float, b: float):
    return a/b


def simple_calculator(a: float, b: float, c):

    operation = c

    opers = {'+': float.__add__,
             '-': float.__sub__,
             '*': float.__mul__,
             '/': division}

    if operation != '0':
        num1 = a  # input("Введите число А")
        num2 = b  # input("Введите число B")

        if opers.__contains__(operation):

                 d = opers[operation](float(num1), float(num2))

            # print("Введена не корректная операция")


def wrapper():
        for j in ('+', '-', '*', '/', '0'):
            simple_calculator(2, 5, j)


print("time {}".format(timeit.timeit(wrapper, number=1000)))

cProfile.run('wrapper()')

# сложно оценить насколько алгоритм эффективный, но мне кажется вполне сносно
# для примитивного калькулятора в которм для двух чисел  выполняется 4 операции
# 1000 повторений выполняется за 6 милисекунд. - что как по мне очень быстро


# Попробую определить асимптотическую сложность алгоритма.
# Добавив входной параметр N который определяет количество раз которые должен выполнится калькулятор и
# сами значения собственно для которых они выполняются


def wrapper2(n):
    for i in range(n):
        for j in ('+', '-', '*', '/', '0'):
            simple_calculator(i, i+2, j)

#Profile.run('wrapper2(10)')

#cProfile.run('wrapper2(100)')

#cProfile.run('wrapper2(1000)')

#Profile.run('wrapper2(10000)')

#cProfile.run('wrapper2(100000)')

# Как я понимаю алгоритм имеет линейную сложность O(5n). Такому выводу я прихожу по тому что
# у нас есть N операций для каждой из которых будет 5 раз вызван калькулятор, который в свою очередь
# выполняет одну из операций, так же вызываются функция contains которая выполнится 4 раза (по количеству операций в словаре(
# В результате получается функция N(5+4+1) - N раз для 5 операций калькулятора должно выполнится по 4операции contains
# и выполнение собственно одной из операций что в итоге дает 5N+4N+1 сложность определяем по наиболее влиятельной операции


# Задача 2
# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»


# Без решета
def find_simple(n):
    lst = []
    for i in range(2, n+1):
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    print(lst)

# Как мне кажется алгоритм имеет сложность O(n*log(n)), так как  осуществляя поиск делителей только среди простых чисел
# не превышающих делимое и в случае нахождения такого часть отбрасывается и дальше поиск не осуществляется

cProfile.run('find_simple(100000)')

def find_eratosfen(n):
    a = [i for i in range(n + 1)]
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1
    print(lst)

cProfile.run('find_eratosfen(100000)')
# Получается что у нас есть N операций для которых должно выполнится N/K операций N*(N/K) что будет N^2/K, где К это шаг
# Но я не знаю как описать шаг, видимо по этому не могу далее правильно оценить.
# я бы предположил что сложность такая же как у первого алгоритма O(n*log(n))
# Но он выполняется в 1000 раз быстрее для одинакового количества элементов, судя по википедии
# сложность алгоритма O(n*log(log(n))) но я не могу к ней придти,  подскажите пожалуйста что делаю не так.
