# задача 1 / 31
# Последовательность фибоначи

# def fib(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     return fib(n-1) + fib(n-2)
# list1 = []

# def Numfib(m):
#     list1.append(0)
#     for i in range(m):
#         list1.append(fib(i))
#         #print(i)
#     print(list1)
#     return list1[m]
# #print(list1)
# print(Numfib(6))

# 0 1 1 2 3 5 8 13 21
def f(n):
    if n == 0 or n == 1:
        return 1
    return f(n-1) + f(n-2)

# n = int(input())
# print (f(n-2))

# Задача 2 / 33

# n = int(input())
# list1 = list()

# for i in range(n):
#     x = int(input())
#     list1.append(x)

# max_n = max(list1)
# min_n = min(list1)

# for i in range(len(list1)):
#     if list1[i] == max_n:
#         list1[i] = min_n

# print(list1)

# Задача 3 / 35
# Функция определения простого числа

# def prime(n):
#     flag = True
#     i = 2
#     while i < n  and flag:
#         if n % i == 0:
#             flag = False
#         i +=1
#     if flag == True:
#         return "yes"
#     else: return "no"
 
# n = int(input())
# print(prime(n))

#Задача 4 / 37
# Последовательность N элементов

def Pos(n):
    if n == 1:
        print(n, end=' ')
    else:
        print(n, end=" ")
        Pos(n-1)
# Pos(2)

# Решение преподователя
def f(n):
    if n == 0:
        return ''
    k = int(input())
    return (f(n-1)+ f'{k}')

n = int(input())
print (f(n))    
    