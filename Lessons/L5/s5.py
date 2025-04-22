# Задача 1
# list1 = [1, 2, 3, 4, 5, 5]
# print(len(set(list1)))

# Задача 2

# list2 = [1, 2, 3, 4, 5, 6]
# print(list2)
# k = int(input())
# k= k % len(list2)
# list_res = []
# print(k)

# # for i in range(k):
# #     list_res.append(list2[len(list2)-1-i])
# # print(list_res)

# for i in range(k):
#     list_res.append(list2[i-k])
# print(list_res)


# for i in range(len(list2)-k):
#     list_res.append(list2[i])
# print(list_res)

# Задача 3

# list3 = [{"V": "S001"}, {"VI": "S002"}, {"V": "S001"}] #Словарь
# set_1 = set()
# for i in list3:
#     for j  in i:
#         set_1.add(i[j]) # Добавляем в множество
#         print(i,j, i[j])
# print(set_1)

# Задача 4 / 23

# list4 = [0, -1, 5, 2, 3]
# count = 0

# for i in range (1, len(list4)):
#     if list4[i] > list4[i-1]:
#         count+=1
# print(count)

