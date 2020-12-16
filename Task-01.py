# Третьяков Роман Викторович
# Факультет Geek University Python-разработки. Основы языка Python
# Урок 3. Задание 1:
#  Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#  Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль

def divide_num(*args):

    return args[0]/args[1]


def get_num(order_num):

    while True:
        input_num = input(f'Введите {order_num} число, либо пустое значение для прерывания ввода: ')
        if input_num == '':
            break

        try:
            input_num = float(input_num)
        except ValueError:
            print('Ошибка при преобразовании введенного значения в число! Повторите ввод')
        else:
            break

    return input_num


while True:
    first_num = get_num(1)
    if first_num == '':
        break

    second_num = get_num(2)
    if second_num == '':
        break

    try:
        divide_res = divide_num(first_num, second_num)
    except ZeroDivisionError:
        print('Ошибка деления на ноль!')
        continue
    else:
        print(f'Результат операции {first_num} : {second_num} = {divide_res}')

print('Операция отменена!')