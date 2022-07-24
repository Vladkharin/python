
# number = 3
# number = 4
# number2 = 5
# result = number + number2
# # print(result)

# num1 = num2 = num3 = 5

# # print(num1, num2, num3)

# num_1, num_2 = 6, 9

# # print(num_1, num_2)

# swap1 = 8
# swap2 = 15

# # print(swap1, swap2)

# swap1, swap2 = swap2, swap1 + swap2 #Обмен между переменными 

# # print(swap1, swap2)

# swap2 -= number

# # print(swap2)

# #Распаковка списков по периметру

# *z, x, y, a = [1, 2, 3, 4, 5]

# # print(z)
# # print(x)
# # print(y)
# # print(a)

# # Типы данных

# a = None # отсутсвие данных
# # print(type(a))
# a = 1 # целые числа
# # print(type(a))
# a = 1.0 # числа с плавующие точкой
# # print(type(a))
# a = 1 + 1j # комбинированные числа
# # print(type(a))
# a = '1' # строка
# # print(type(a))
# a = [1, 1, 'a'] # список
# # print(type(a))
# a = (1, 1, 'a') # кортеж
# # print(type(a))
# a = {1, 2, 'a'} # множество
# # print(type(a))
# a = {'a' : 1, 'b': 2} # словарь
# # print(type(a))
# a = True # логические bollean значения
# # print(type(a))


# x = float(input('Введите число '))
# y = float(input('Введите число '))
# r = x + y
# print('Результат ' + str(r))

# x = -1

# if x == 0:
#     print('if')
# elif x > 0:
#     print('elif')
# else:
#     print('else')

# x = 'a'

# if not x == 0:
#     x = 1
#     # print('x был равен нулю')
# elif type(x) == type(1) and type(x) == type(5.5):
#     # print('x допустимое значения')
# else:
#     # print('В x недопустимый тип данных')
#     x = 1

# import os
# import time

# while True:
#     sayt = input('Введите свой сайт\n ')

#     if sayt == 'завершить':
#         break

#     if 'https://' in sayt:
#         os.system('start ' + sayt)
#         print('if')

#     elif 'www.' in sayt:
#         sayt = 'https://' + sayt
#         os.system('start ' + sayt)
#         print('elif')

#     else:
#         sayt = 'https://www.' + sayt
#         os.system('start ' + sayt)
#         print('else')

#     time.sleep(5)

#     os.startfile('steam://rungameid/730')

# while True:
#     x = int(input('Введите число '))
#     count = 0
#     y = 1

#     while count < x:
#         count += 1
#         y  *= count

#     else: 
#         print(y)

# x = ''

# while len(x) < 5:
#     y = input('Ввод данных: ')
#     if y == 'o' or y == '':
#         continue
#     if y == 'l':
#         break

#     x += y 
# else:
#     print(x)

# print('Программа работает дальше')

# m = 'stroka texta'
# count = 0

# for i in m:
#     if i == 't':
#         continue
#         print('надпись в строке есть буква t')
#         count += 1
#     print(i)
# else:
#     print('Цикл завершен, букв t ', count)

# print('Программа работает дальше')

# x = 'абвгдеёжзийклмнопрстуфхцшщьыъэюя'
# y = input('Введите строку ')


# for i in x:
#     count = 0
#     for r in y:
#         if i == r:
#             count += 1 
#     if count > 0:
#         print('Букв', i, 'было', count)



# for x in range(10, -10, -3):
#     print(x)

# from re import T, U
# from tkinter import N, Y


# m = [[5, 6], [1, 5], [1, 2]]
# x = [1, 2, 3]
# n = list(range(10))

# m[0] = 9

# print(n)

# print(m)

# m[0] = m[0] + 2

# print(m)

# m[1], m[2] = m[2], m[1]

# print(m)

# m = m + x

# print(m)

# x = [9, 8, 7, 6, 5]

# x.append(1)

# print(x)

# x.insert(1, 7)

# print(x)

# print(x.count(7))

# x.sort()

# print(x)

# x.reverse()

# print(x)

# y = x.pop(0)

# print(y)
# print(x)

# x.remove(7)

# print(x)

# x.clear()

# print(x)

# x.extend(['a, s'])

# print(x)

# h = x.copy()

# print(h)

# x = (9, 8, 7, 6, 5, 4, 3, 2, 1)

# print(x.index(2))

# h = (1, 2, 3)
# h += (4, 5, 6)

# print(h)

# y = []

# for i in range(len(x)):
#     y.append(x[i] + 3)
# print(y)

# t = list(x)
# t[0] =10
# x = tuple(t)

# print(x)
# print(x [1:5])

# print(x[0])

# z, c, *b = x

# r = 5
# u = 7

# r, u = u, r

# x = tuple('stroka')


# print(z)
# print(c)
# print(b)
# print(r)
# print(u)


# import os
# import time 

# spisok = []
# for adress, dirs, files in os.walk('C:\\Users\koooo\Desktop\Portfolio'):
#     for file in files:
#         full = os.path.join(adress, file)
#         if time.time() - os.path.getctime(full) < 86400:
#             spisok.append(full)
# print(spisok)

# print('До функций')

# from re import X


# def show():
#     print('функция')

# show()



# def show2():
#     x = 7 + z
#     return x
# z = 7
# y = show2()
# # z = show2() + 9

# print(y)
# z = 9

# print(show2())
# print(z)
# # print(x)
# print(show())
# print('после функций')





# from itertools import count


# def count_list(list,par2= False, count = 0):
#     if par2 == True:
#         typ = type(list[0])
#         for i in list:
#             count += 1
#         return count, typ
#     else:
#         for i in list:
#             count += 1
#         return count

# j = [9, 8, 7, 6]

# h = ['a', 'b', 'c']

# k = [1, 2, 3, 4, 5, 6]


# print(count_list(j))
# print(count_list(h))
# print(count_list(k, True))
# print(count_list('любая строка '))

# def name(h, *args, key):
#     print(args, h, key)
# name(7, 2, 3, 5, 5, key = 7)

# def exclusive_item(*args, key = False):
#     new_list = []
#     for i in args:
#         for arg in i:
#             if arg not in new_list:
#                 new_list.append(arg)

#     if key == True:
#         new_list.sort()
#     return new_list


# z = [9,8,7]
# x = [8,8,9,7,6,5]
# c = [1,2,3,4,5,6,7,7]

# t = exclusive_item(z,x,c, key = True)

# print(t)


# x = 5

# def name():
#     y = 1
#     print(x)
#     return y

# h = name()

# print(h)

# import math

# PI = math.pi

# def radius():
#     n = float(input('Диаметр цилиндра в см: '))
#     n /= 2
#     return n

# def height():
#     m = float(input('Высота цилиндра в см: '))
#     return m



# def volume():
#     r = radius()
#     h = height()

#     s = PI*r**2
#     v = s*h

#     return v

# print('Обьем цилиндра',volume(), 'см3')

# def massa(v):
#     n = float(input('удельный вес г/см3: '))
#     return v*n/1000
# print('Вес цилиндра в кг: ', massa(volume()))

# d1 = {'a': 7, 'b': 9}
# d2 = dict()
# d3 = dict.fromkeys('1')


# d5 = d1.copy()

# d1['c'] = 3



# print(d5)
# print(d1.items())
# print(d1.keys())
# print(d1.values())
# d1.update(price)
# print(d1)


# if 'c' in d1:
#     d1['c']

# y = d1.get('c')
# t = d1.pop('a')

# print(y)
# print(t, d1)

# def buy():
#     pay = 0
#     while True:
#         enter = input('Что покупаем??? ')
#         if enter == 'end':
#             break
#         pay += price[enter]
#     return pay

# i = buy()

# print(i)


# users = {
#     'Alex7': {'password': 123456, 'id': 1111},
#     'Jimmy99': {'password': 123456, 'id': 1223}
# }

# price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}

# new_price = {}

# for i in price:
#     new_price[i] = round(price[i] * 0.85, 2)


# x = price.keys()
# print(x)


# for key in price.keys():
#     print(key)

# new = {}
# for key, value in price.items():
#     new[value] = key
# print(new)
# print(list(x))
# print(price)
# print(new_price)



# r = open('text.txt')

# for i in r:
#     if 'read.py' in i:
#         print(i)

# r.close()

# r = open('e.exe', 'wb')

# r = open('e.exe', 'rb')

# y = open('Копия e.exe', 'wb')

# while True:
#     var = r.read(1024*1024)

#     print(var.__sizeof__())

#     if var.__sizeof__() == 33:
#         break
    
#     y.write(var)
# print('Control')

# r.close()
# y.close()

# r = open('text2.txt', 'w', encoding='utf-8')
# r.write('stroka')
# print(r)

# r.close()

# h = open('text2.txt', encoding='utf-8')

# print(h.read())

# h.close()

# t = {1, 2, 3, 25}
# y = set()


# import time
# def f(*args) :
#     list_new = []
#     for i in args:
#         for y in i:
#             if y not in list_new:
#                 list_new.append(y)

#     return list_new

# z = list(range(10000))
# x = list(range(5000, 15000))
# c = list(range(10000, 20000))

# start = time.time()
# f(z, x, c)
# stop = time.time() - start

# print(stop)

# start2 = time.time()
# r = set(z)
# t = r.union(set(x), set(c))

# stop2 = time.time() - start2

# print(stop2)


# zz = {1, 2, 3, 4, 5}
# xx = {3, 4, 5, 6, 7}

# zz.add(6)
# zz.remove(6)
# zz.discard(1)
# # zz.update(xx)


# # yy = zz.intersection(xx)

# yy = zz.difference(xx)




# # yy = zz.union(xx)

# print(zz, yy)

# import os 



# z = open('text2.txt', encoding='utf-8')
# r = open('text.txt', encoding='utf-8')

# r1 = set(z.read().split())
# z1 = set(r.read().split())
# r.close()
# z.close()


# new = r1.difference(z1)
# print(new)

# import os

# s = 'Let\'s \n write \n string as "s"'
# url = r'https:\www.youtube.com\new'

# # os.walk('D:\\')


# # x = 'C:\\Users\\PyHS\\Desltop'

# print(s)
# print(url)
# # print(s)

# s = 'stroka texta'

# # print('str' in s)

# # s.upper()

# print(s.upper())
# print(s.lower())
# print(s.capitalize()) # Первая буква в верхним регистре
# print(s)

# path = 'C:/Users/PyHS/Desktop/s.py'

# path1 = path.replace('/', '\\')

# print(path1)

# r = path1.split('\\')

# print(r[-1])

# q = open('text.txt', encoding='utf-8' )
# r = q.read()

# list_znk = ['(', ')', '"', "'", '\n']

# for i in list_znk:
#     r = r.replace(i, '')

# print(r)

# r1 = r.split()

# print(r1)

# new_text = ' '.join(r1)

# print(new_text)

# enter = input('Your name: ')
# name = 'Pytyhon'


# s = 'Hello %s' %enter

# s1 = 'Hello {1}, i AM {0}'.format(enter, 'Python')
# var = 'storka'
# s2 = f'Hello {enter}, i AM {len(var)}'
# print(s)
# print(s1)
# print(s2)
# while True:
#     try:
#         enter = float(input('Введите число '))
#         print(100/enter)

#     except ValueError:
#         print('Вы ввели не число')
#     else:
#         print('Пользователь молодец, с первого раза')
#     finally:
#         print('Вывод finally')


# print('Все нормально')

# import sys

# url_list = ['text.txt', 'text2.txt', 'text25.txt', 'text3.txt']

# list_defect = []
# list_info = []

# try:
#     for url in url_list:
#         try:
#             r = open(url, encoding='utf-8')
#             list_info.append(r.read())
#             print('здесь')
#             # print(list_info)
#         except Exception:
#             list_defect.append(url)
#             print('тут')
#             # print(list_defect)

#             sys.exit()
#             continue    
# finally:
#     r = open('save.txt', 'a', encoding='utf-8')
#     for i in list_info:
#         r.write(i)
#     r.write(str(list_defect))
#     r.close()
#     print('Я все записал')



