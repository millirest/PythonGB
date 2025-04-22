def calk1(a,b):
    return a+b

def calk2(a,b):
    return a*b

calk3 = lambda a,b: a+b 

def math (op, x, y):
    print(op(x,y))



# math(calk3,5,45) #50
# math(lambda a,b: a+b, 5, 45) # 50

# SelfWork

# data = [1,2,3,4,5,6,7,8,9]
# res = list()
# for i in data:
#     if i%2==0:
#         res.append((i,i**2))
# print(res)


def select(f,col):  ## ->> map()
    return [f(x) for x in col]

def where(f,col):  ## ----> filter
    return [x for x in col if f(x)]

# data = [1,2,3,4,5,6,7,8,1]
# res = select(int, data)
# print(res)
# res = where(lambda x:x %2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)


# list1 = [x for x in range(1,20)]
# print(list1)
# list1 = list(map(lambda x : x + 10 , list1))
# print(list1)

#////////////////

# data1 = '13 123 1 12 45 123'
# print(data1)

# data1 = data1.split()
# print(data1)

# data = '13 123 1 12 45 123'
# data = list(map(int, data.split())) # map итератор данных
# print(data)

#///////////////////

# data = [15, 65, 45, 78, 47, 12, 68]
# print(data)
# res = list(filter(lambda x: x %10 ==5, data))
# print(res)
# res = list(map(lambda x: x %10 ==5, data))
# print(res)

#////////////////
# Функции zip(a,b) и enumerate (x)


# Работа с файлами

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # указывается режим в котором будем работать
# data.writelines(colors) # Разделителей не будет
# data.close()
 

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# path = 'file.txt'
# data = open('file.txt', 'r')
# for line in data:
#     print(line)
# data.close()

#////////////
# Модуль os

# import os
# os.chdir(path) # Смена текущей директории
# os.getcwd() # Текущая рабочая директория
# os.path.basename(path) # Базовое имя пути
# os.path.abspath(path) # Возвращает нормализованный (длинный) абсолютный путь

#//////////////////
# Модуль shutil
# import shutil
# shutil.copyfile(src,dst) # копирует содержимое файла src в файл dst
