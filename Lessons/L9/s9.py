# Задача 1 / 39

# list1 = (1,2,3,4,5)
# list2 = (1,2,5,7,8)

# for i in list1:
#     if i in list2:
#         print('')
#     else:
#         print(i, end=' ')

# Решение препода

# n = int(input())
# list1 = list()
# for i in range(n):
#     x = int(input())
#     list1.append(x)

# m = int(input())
# list2 = list()
# for i in range(m):
#     x = int(input())
#     list2.append(x)

# count = 0
# for i in range(n):
#     for j in range(m):
#         if list1[i] == list2[j]:
#             count +=1
#     if count == 0:
#         print (list1[i])
#     count = 0

# Задача 2 / 41

# n = int(input())
# list1 = list()
# for i in range(n):
#     x = int(input())
#     list1.append(x)

# count = 0
# for i in range(1, n-1):
#     if list1[i-1] < list1[i] > list1[i+1]:
#         count +=1

# print(count)

# задача 3 / 43

# list1 = [1,2,3,4,1,2,1]
# count = 0

# for i in range(len(list1)):
#     for j in range(i+1, len(list1)):
#         if i  != j and list1[i] == list1[j]:
#             count += 1

# print(count)

# Задача 4 / 45

k  = int(input())
list1 = list()

for i in range(k):
    summa = 0
    for j in range(1, i//2 + 1):
        if i % j ==0:
            summa += j
    list1.append(tuple([i,summa]))
        

for i in range(len(list1)):
    for j in range(i, len(list1)):
        if i != j and list1[i][0] == list1[j][1] and list1[i][1] == list1[j][0]:
            print(*list1[i])