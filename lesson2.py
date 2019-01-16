##Домашние задание. Урок 2
##Easy
import random
import math
import datetime

listEasy = ["яблоко", "банан", "киви", "арбуз"]
listNormal = ['2', '-5', '8', '9', '-25', '25', '4']

print("Уровень Easy")

#Задача 1
print("Задача 1")
print(listEasy)

for value in listEasy:
    index = listEasy.index(value)
    print(str(index)+'.'+str.rjust(value, 10, " "))


#Задача 2
print("\n ---------------------------------------\n")
print("Задача 2")

fst_list = list()
snd_lst = list()
idx = 0

while idx < 10:
    idx += 1
    fst_list.insert(idx, random.randint(0, 100))
    snd_lst.insert(idx, random.randint(0, 100))


print(f'frist list \n {fst_list}')
print(f'second list \n {snd_lst}')
print(f'first list - second list \n {list(set(fst_list)-set(snd_lst))}')

#Задача 3
print("\n ---------------------------------------\n")
print("Задача 3")

fst_list = list()
snd_lst = list()
idx = 0
while idx < 10:
    idx += 1
    fst_list.insert(idx, random.randint(0, 100))
idx = 0
for x in fst_list:

    if (int(x) % 2) == 0:
        snd_lst.insert(idx, int(x) / 4)
    else:
        snd_lst.insert(idx, int(x) * 2)
    idx += 1

print(f'frist list \n {fst_list}')
print(f'second list \n {snd_lst}')



print("\n ----------------Normal Level-----------------------\n")
## Задача 1
print("\n Задача 1")

fst_list = list()
snd_lst = list()
idx = 0
while idx < 10:
    idx += 1
    fst_list.insert(idx, random.randint(0, 100))

print(fst_list)
idx = 0
for x in fst_list:
    if math.modf(math.sqrt(int(x)))[0] == 0:
        print(f'Нет дробной части {math.modf(math.sqrt(int(x)))}. Результат корня: {math.sqrt(int(x))}')
    else:
        print(f'Есть дробная часть {math.modf(math.sqrt(int(x)))}. Результат корня: {math.sqrt(int(x))}')
    idx += 1

## Задача 2
print("\n Задача 2")
date = datetime.date.today().strftime("%d.%m.%Y")

day_list = ['первое', 'второе', 'третье', 'четвёртое',
            'пятое', 'шестое', 'седьмое', 'восьмое',
            'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
            'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
            'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
            'двадцать первое', 'двадцать второе', 'двадцать третье',
            'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
            'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
            'тридцатое', 'тридцать первое']
month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

print(date)
date_list = str(date).split('.')
print(date_list)

result_date_string = (day_list[int(date_list[0]) - 1] + ' ' + month_list[int(date_list[1]) - 1] + ' ' + date_list[2] + ' года')
print(result_date_string)

##Задача 3
print("\n Задача 3")
fst_list = list()
idx = 0
n = input("введите количество эелементов в списке")
if str(n).isdigit():
    while idx < int(n):
        idx += 1
        fst_list.insert(idx, random.randint(-100, 100))
print(fst_list)

## Задача 4
print("\n Задача 4")

fst_list = list()
snd_lst = list()
idx = 0

while idx < 10:
    idx += 1
    fst_list.insert(idx, random.randint(0, 100))
    snd_lst.insert(idx, random.randint(0, 100))

fst_list = [1, 2, 3, 4, 5, 5, 2, 2, 6, 3]
print(fst_list)
print(f'frist list \n {set(fst_list)}')

snd_lst = list()

for x in fst_list:
    if fst_list.count(x) == 1:
        snd_lst.append(x)
print(f'second list \n {snd_lst}')
 