import collections
from memory_profiler import profile



# Задача 1
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
#  для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.


@profile
def fill_enterprise_info():
    ent_count = int(input("Количество предприятий: "))

    enterprise = collections.defaultdict(list)

    for i in range(ent_count):
        name = input("Наименование предприятия")
        income = [float(input(f"Доход предприятия за {x} квартал")) for x in range(1, 5)]
        enterprise[name] = income

    average = 0

    print(enterprise.values())

    for i in enterprise.values():
        average += sum(i)

    print(average/enterprise.__len__())
    average = average/enterprise.__len__()

    print("Companies with income greater than average: ")
    for e in enterprise.keys():
        if sum(enterprise[e]) > average:
            print(f"Company: {e} Income: {sum(enterprise[e])}")

    print("Companies with income lesser than average: ")
    for e in enterprise.keys():
        if sum(enterprise[e]) < average:
            print(f"Company: {e} Income: {sum(enterprise[e])}")

    avg = filter((lambda n: sum(n) > average),enterprise)

    print(avg)

fill_enterprise_info()


# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
@profile
def hex_sum():
    num1 = list(input("Первое hex число"))
    num2 = list(input("Второе hex число"))

    print(num1)
    print(num2)

    sumr = int((''.join(num1)), 16) + int((''.join(num2)), 16)
    multr = int((''.join(num1)), 16) * int((''.join(num2)), 16)
    print(f"Сумма hex чисел {list(hex(sumr))[2:]}")
    print(f"Произведение hex чисел {list(hex(multr))[2:]}")

hex_sum()

@profile
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

find_eratosfen(100000)

@profile
def find_simple(n):
    lst = []
    for i in range(2, n+1):
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    print(lst)

find_simple(100000)
# Версия Python 3.7.0 , Windows10 64bit
# В среднем все три выбранные алгоритма используются почти одинаковое количество памяти, ,Базового выделилось
# 11.4 мб памяти, в результате работы первых двух алгоритмов количества памяти было достаточно и увеличения
# в использовании не наблюдается, алгоритм "решето ератосфена" привел к увеличению памяти для большого количества данных
# в ходе работы было использовано на 2.2 мб больше памяти, видимо расширение произошло при расширении списка для хранения простых чисел


#алгоритм поиска простых чисел без решета, для большого количества значений потребил