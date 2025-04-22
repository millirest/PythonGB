from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = address_data()
    var = int(input(f"В каком формате записать данные \n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{adress}\n\n"
    f"2 вариант \n\n"
    f"{name}; {surname}; {phone}; {adress}\n\n"
    f"Выберете варинт:"))
    while var !=1 and var !=2 :
        print("Неправильный ввод")
        var = int(input('Введите число:\n'))

    if var == 1:
        with open('data_first_variants.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{adress}\n\n")

    if var == 2:
        with open('data_second_variants.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}; {surname}; {phone}; {adress}\n\n")

def print_data():
    print("Вывожу данные из 1 файла: \n")
    with open('data_first_variants.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or  i == len(data_first)-1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))
        
    print("Вывожу данные из 2 файла: \n")
    with open('data_second_variants.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)
