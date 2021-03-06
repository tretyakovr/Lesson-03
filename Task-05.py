# Третьяков Роман Викторович
# Факультет Geek University Python-разработки. Основы языка Python
# Урок 3. Задание 5:
# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter
# должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом
# и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если
# специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
# чисел к полученной ранее сумме и после этого завершить программу

total_sum = 0
is_break = False

while not is_break:
    num_str = input('Введите строку чисел, разделенных пробелами (! - для завершения ввода): ')
    num_list = num_str.split(' ')

    for i, el in enumerate(num_list):
        # Здесь не делаю проверку на ввод именно специального символа. Исключение будет срабатывать при
        # неудачной попытке вызова float()
        try:
            total_sum += float(el)
        except:
            # Взводим is_break в True, чтобы прервать ввод новых строк
            is_break = True

            # Этот break нужен, чтобы выйти из цикла for
            # В случае ввода строки вида: 1 2 3 ! 1, числа после спецсимвола нельзя обрабатывать!
            break

    if not is_break:
        print('Промежуточная сумма введенных чисел равна:', total_sum)

print('Окончательная сумма введенных чисел равна:', total_sum)