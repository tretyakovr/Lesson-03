# Третьяков Роман Викторович
# Факультет Geek University Python-разработки. Основы языка Python
# Урок 3. Задание 2:
# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя,
# фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Реализовать вывод данных о пользователе одной строкой

def define_user(first_name='', last_name='', birth_year='', city='', email='', phone_num=''):

    if first_name:
        print('Имя:', first_name, end = '; ')

    if last_name:
        print('Фамилия:', last_name, end = '; ')

    if birth_year:
        print('Год рождения:', birth_year, end = '; ')

    if city:
        print('Город проживания:', city, end = '; ')

    if email:
        print('e-mail:', email, end = '; ')

    if phone_num:
        print('№ телефона:', phone_num, end = '; ')

    print('\n')

define_user(first_name = 'Roman', last_name = 'Tretyakov', birth_year = 1975)
define_user(first_name = 'Roman', city = 'Ussuriisk', email = 'rtretyakov@outlook.com')
define_user(first_name = 'Roman', last_name = 'Tretyakov')