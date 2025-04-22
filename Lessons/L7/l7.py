# def sum_numbers1(n, y = 'hello'): # Функция
#     print(y)
#     summa = 0 
#     for i in range(n+1):
#         summa += i
#     print(summa)

# sum_numbers1(5, "qwert")

# def sum_numbers2(n): # Возврящаемое значение
#     summa = 0 
#     for i in range(n+1):
#         summa += i
#     return summa
#     print('stop')

# print(sum_numbers2(5))

# def sum_str(*args): # Неизвестное кол-во аргументов
#     res = ''
#     for i in args:
#         res += str(i)
#     return res

# print(sum_str('q', 'e', 'r'))
# print(sum_str('q', 'e', 'r', 't'))
# print(sum_str(1, 4, 5))


# import modul1 # Импорт модуля
# from modul1 import max1 # Импорт функции из модуля
# from modul1 import * # Импорт из модуля всех функций
# import modul1 as m1 # Импорт модуля и переимнование вызова

# print(modul1.max1(5,9)) # Вызов функции из модуля
# print(max1(6,9))
# print(m1.max1(7,9))

# Рекурсия в Python. Число фибоначи
def fib(n):  
    if n in [1,2]:
        return 1
    return fib(n-1) + fib(n-2)

# list_1 =[]
# for i in range(1,11):
#     list_1.append(fib(i))
# print(list_1)


# Быстрая сортировка # Руекурсией

def quick_sort(array):
    if len(array) <=1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i<= pivot]
    greater = [i for i in array[1:] if i> pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
# print(quick_sort([10, 5, 2]))


# Сортировка слиянием
def merge_sort(nums): 
    if len( nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left [i]
                i += 1
            else :
                nums[k] = right[j]
                j += 1
            k +=1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list1= [1,5,6,7,5,4,4,6,7,4,33,2,4,5]
#merge_sort(list1)
# print(list1)

    
    