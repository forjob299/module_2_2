try:
    data = input('Введите поочередно три числа через пробел: ')
    data = data.strip().replace(' ', '/').replace('//', '/')
    data = data.split('/')
    int_data = [int(a) for a in data]
    if len(data) < 3:
        print('Вы ввели менее трех чисел')
    elif len(data) == 3:
        first = int_data[0]
        second = int_data[1]
        third = int_data[2]
        if first == second and first == third:
            print('Все числа равны: 3')
        elif first == second or first == third or second == third:
            print('Хотя бы два числа равны: 2')
        else:
            print('Числа не равны: 0')
    else:
        print('Вы ввели более трех чисел')
except ValueError:
    print('Ошибка: Данные введены некорректно')