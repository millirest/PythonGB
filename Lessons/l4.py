list1 = [] # Пустой список
list2 = list() #Пустой список
list1 = [1, 2, 3, 5]
print(list1)
print(*list1)

for i in list1:
    print(i)

print(len(list1)) #Length
print(list1[-2]) #3

# Добваление элемента списка
list2 = [1, 5]
list2.append(8) #add 8
list2.append(85) #add 85
print(list2)

list3= []
for i in range(5):
    list3.append(i)
    print(list3)



#УДаление элемента списка методом pop
list4 = [12,7,-5,-7, 9]
print(list4)
print(list4.pop()) # 9 
print(list4) # [12,7,-5,-7]
print(list4.pop()) # -7
print(list4) # [12,7,-5]
print(list4.pop(1)) #7
print(list4) # [12,-5]

# Добавление элемента списка на конкретную позицию

list5 = [12,7,-5,-7, 9]
print(list5.insert(2,2)) #2
print(list5) # [12, 7, 2, -5, -7, 9]

#Работа со срезами
list6 = [1,2,3,4,5,6,7,8,9,10]
print(list6[0])  #1
print(list6[-1]) #10
print(list6[:]) #[1,2,3,4,5,6,7,8,9,10]
#[начало:конец]
print(list6[:2]) #[1,2]
print(list6[-2:]) #[9,10]

# List Comprehension

list_Co = []
for i in range(1, 101):
    list_Co.append(i)
print(list_Co)

# Эту же функцию можно записать по другому:
list_Co = [i for i in range(1, 101)]

list_Co = [i for i  in range(1,101) if i %2 ==0]

list_Co2 = [(i,i) for i in range(1,101) if i %2 == 0]

list_Co3 = [i*2 for i in range(1,101) if i %2 == 0]


# Кортежи - неизменяемые списки
tuple1 = ()
print(type(tuple1))
tuple1 = (1)
tuple1 = (1,)

tuple2 = [1,2,3]
print(tuple2)
print(type(tuple2))

tuple3 = tuple(tuple2)
print(tuple3)
print(type(tuple3))

#a=b=1 a,b = 1, 2

a,b,c = tuple3 # Множественное присваивание
print(a,b,c) # 1 2 3


t = (2,3,4,5,)

for i in range(len(t)):
    print(t[i])

#Словари
d = {} # Пустой словарь
d  = dict()
d['q'] = "qwerty"
print(d) 
d['w'] = "werty"
print(d) 
print(d['q'])   

dictionary ={}
dictionary ={'up':'↑', 'left':'←', 'down': '↓', 'right': '→'} 
print(dictionary) # {'up': '←', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary['left']) # ←
print(dictionary['up']) # ↑
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
del dictionary['left']
dictionary[234] = 4356
print("dictionary.items()",dictionary.items())
for item in dictionary:
    print(item)
    print('{}:{}'.format(item, dictionary[item]))

for (k,v) in dictionary.items():
    print(k,v)

# Множества

colors = {'red', 'green', 'blue'}
print (colors) # {'green', 'red', 'blue'}
print (*colors) # green blue red
colors.add('red') # red уже есть, оно уникально, ещё не добавится
print(colors) # {'blue', 'green', 'red'} 
colors.add('gray')
print(colors) # {'blue', 'green', 'gray', 'red'}
colors.remove('red') # Удаление объекта
print(colors) # {'blue', 'green', 'gray'}
#colors.remove('red') # Error
colors.discard('red') #ok
colors.clear() # Удаление всех объектов
print(colors)
q = set('hi')
print(q)

a = {1, 2, 3, 5, 8}
b = {2, 5 ,8 , 13, 19}
c = a.copy() # {1, 2, 3, 5, 8}
print(c) 
u = a.union(b) # {1, 2, 3, 5, 8, 13, 19} # Обьединение
print(u)
print(a.intersection(b)) # {8, 2, 5} # Совпадения
print(a.difference(b)) # {1, 3} a-b
print(b.difference(a)) # {19, 13} b-a
print(a.union(b).difference(a.intersection(b))) # {19, 1, 3, 13}

# Замороженные множества

a = [1,8,6]
b = frozenset(a)
print(b)