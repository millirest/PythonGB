# a = int(input('Введите число:'))
# print(type(a))
# print(f"{a} + {a} = {a+a}")

# int(a)
# float(a)
# str(a)
# b =1
# bool(b)
# print("{} * {} =".format(a,a))  # Вывод 

a1 = 5.3453443
a2 = 4.323415
a3=a2
a3 +=a1
print(round(a1+a2,3)) # Округление

b1 = 2 <3 and 2> 1  # Логические операнды
print(b1)

b2 = 1 < 2 < 3 < 9 # Логические операнды
print(b2)

c1 = "qwerty" # Цикл for
for i in c1:
    print(i)
for i in range(5):
    print(i)

d = "Текст"
print(len(d))  # Выявление длины строки
print("ст" in d)    # Условие нахождения в тексте
print(d.lower()) # Нижний регистр  
print(d.upper())
print(d.replace("екст", "Нетекст"))
print(d[-1])    #Вывод по индексу 0,1, len-1, -1, [:], [:2], [0:len-2], [::6]-от 0 жл конца с шагом 6, 