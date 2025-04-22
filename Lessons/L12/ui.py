from logger import input_data, print_data

def interface():
    print("Добрый день, вы попали на спец. бот \n" \
    "1 - Запись даных\n" \
    "2 - Вывод данных")
    command = int(input('Введите число:\n'))

    while command !=1 and command !=2 :
        print("Неправильный ввод")
        command = int(input('Введите число:\n'))

    if command == 1:
        input_data()
    elif command == 2:
        print_data() 