def easy(a, b):
    '''
    2.1.2 На easy
        На вход программе подаются два целых числа a и b. Напишите программу, которая выводит:

        сумму чисел a и b;
        разность чисел a и b;
        произведение чисел a и b;
        частное чисел a и b;
        целая часть от деления числа a на b;
        остаток от деления числа a на b;
        корень квадратный из суммы их 10-х степеней:
        
        Формат входных данных
        На вход программе подаются два целых числа a и b \, (b \neq 0)b(b
        
        =0), каждое на отдельной строке.

        Формат выходных данных
        Программа должна вывести результаты математических операций в соответствии с условием задачи.

        Тестовые данные
            Sample Input 1:
            3
            8
            Sample Output 1:
            11
            -5
            24
            0.375
            0
            3
            32768.90100384814
    '''

    total = a + b
    diff = a - b
    product = a * b
    quotient = a / b
    whole_quotient = a // b
    reminder = a % b
    square_root = (a ** 10 + b ** 10) ** 0.5

    return total, diff, product, quotient, whole_quotient, reminder, square_root

# a, b = int(input()), int(input())
# print(*easy(a, b), sep="\n")

def imt(weight, height):
    '''
    2.1.3 Индекс массы тела
        Напишите программу для вычисления и оценки индекса массы тела (ИМТ) человека. ИМТ показывает весит человек больше или меньше нормы для своего роста. ИМТ человека рассчитывают по формуле: 
        imt = weight / (height ** 2)
        где масса измеряется в килограммах, а рост — в метрах.
        Масса человека считается оптимальной, если его ИМТ находится между 18.518.5 и 2525. Если ИМТ меньше 18.518.5, то считается, что человек весит ниже нормы. Если значение ИМТ больше 2525, то считается, что человек весит больше нормы.

        Программа должна вывести "Оптимальная масса", если ИМТ находится между 18.518.5 и 2525 (включительно). "Недостаточная масса", если ИМТ меньше 18.518.5 и "Избыточная масса", если значение ИМТ больше 2525.

        Формат входных данных
        На вход программе подается два числа: масса и рост человека, каждое на отдельной строке. Все входные числа являются вещественными, используйте для них тип данных float.

        Формат выходных данных
        Программа должна вывести текст в соответствии с условием задачи.

        Sample Input 1:
        65
        1.75
        Sample Output 1:
        Оптимальная масса
    '''

    imt = weight / (height ** 2)
    if imt < 18.5:
        return 'Недостаточная масса'
    elif 18.5 <= imt <= 25:
        return 'Оптимальная масса'
    else:
        return 'Избыточная масса'

# a, b = float(input()), float(input())
# print(imt(a, b))

def string_price(string):
    '''
    2.1.4 Стоимость строки
        ана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ (в том числе пробел) стоит 6060 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.
        Формат входных данных
        На вход программе подается строка текста.
        Формат выходных данных
        Программа должна вывести стоимость строки.
        Тестовые данные
        Sample Input 1:
        Привет, как дела?!
        Sample Output 1:
        10 р. 80 коп.
    '''
    
    symbol_price = 60
    total_price = len(string) * symbol_price
    rub = str(total_price // 100) + ' р. '
    kop = str(total_price % 100) + ' коп.'
    result = rub + kop
    return result

# print(string_price(input()))

def count_words(string):
    '''
    2.1.5 Количество слов
        Дана строка, состоящая из слов, разделенных пробелами. Напишите программу, которая подсчитывает количество слов в этой строке.
        Формат входных данных
        На вход программе подается строка.
        Формат выходных данных
        Программа должна вывести количество слов в строке.
        Примечание 1. Кроме слов в тексте могут присутствовать только пробелы (один или несколько).
        Примечание 2. Решите задачу в одну строчку кода.
        
        Тестовые данные
        Sample Input 1:
        Hello world
        Sample Output 1:
        2
        
        Sample Input 2:
        Timur forever young
        Sample Output 2:
        3
        
        Sample Input 3:
        The future belongs to those who believe in beauty of their dreams
        Sample Output 3:
        12
    '''
    
    return len(string.split())

# print(count_words(input()))

def zodiac(year):
    '''
    2.1.6 Зодиак
        Китайский гороскоп назначает животным годы в 1212-летнем цикле. Один 1212-летний цикл показан в таблице ниже. Таким образом, 20122012 год будет очередным годом дракона.

        Год	    Животное    
        2004	Обезьяна    0
        2005	Петух       1
        2006	Собака      2
        2007	Свинья      3
        2008	Крыса       4
        2009	Бык         5
        2010	Тигр        6
        2011	Заяц        7
        2012	Дракон      8
        2013	Змея        9
        2014	Лошадь      10
        2015	Овца        11

        Напишите программу, которая считывает год и отображает название связанного с ним животного. Ваша программа должна корректно работать с любым годом, не только теми, что перечислены в таблице.

        Формат входных данных
        На вход программе подается одно целое число – год.

        Формат выходных данных
        Программа должна вывести текст – название животного.

        Тестовые данные
        Sample Input 1:
        2020
        Sample Output 1:
        Крыса
        Sample Input 2:
        1945
        Sample Output 2:
        Петух
        Sample Input 3:
        2000
        Sample Output 3:
        Дракон
    '''
    signs = ['Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц', 'Дракон', 'Змея', 'Лошадь', 'Овца']
    return signs[int(year) % 12]

# print(zodiac('1988'))

def invert_last_five_numbers(number_str):
    '''
    2.1.7 Переворот числа
        Дано пятизначное или шестизначное натуральное число. Напишите программу, которая изменит порядок его последних пяти цифр на обратный.

        Формат входных данных
        На вход программе подается одно натуральное пятизначное или шестизначное число.

        Формат выходных данных
        Программа должна вывести число, которое получится в результате разворота, указанного в условии задачи. Число нужно выводить без незначащих нулей.

        Тестовые данные
        Sample Input 1:
        12345
        Sample Output 1:
        54321
        Sample Input 2:
        987654
        Sample Output 2:
        945678
        Sample Input 3:
        25000
        Sample Output 3:
        52
        Sample Input 4:
        560000
        Sample Output 4:
        500006
    '''
    return int(number_str[-1:-6:-1]) if len(number_str) == 5 else int(number_str[0] + number_str[-1:-6:-1])

# print(invert_last_five_numbers('987654'))

def add_sac_commas(number_str):
    '''
    2.1.8 Standard American Convention
        На вход программе подаётся натуральное число. Напишите программу, которая вставляет в заданное число запятые в соответствии со стандартным американским соглашением о запятых в больших числах.

        Формат входных данных
        На вход программе подаётся натуральное число n, \, (0 < n < 10^{100})n,(0<n<10 
        100
        ).

        Формат выходных данных
        Программа должна вывести число с запятыми в соответствии с условием задачи.

        Тестовые данные 🟢
        Sample Input 1:

        1000000
        Sample Output 1:

        1,000,000
        Sample Input 2:

        100
        Sample Output 2:

        100
        Sample Input 3:

        12345
        Sample Output 3:

        12,345

    '''
    number_with_commas = ''
    for letter_index in range(-1, (len(number_str) * -1) - 1, -1):
        if letter_index in range(-4, len(number_str) * -1 - 1, -3):
            number_with_commas += ',' + number_str[letter_index]
        else:
            number_with_commas += number_str[letter_index]

    return number_with_commas[::-1]

# number = '100000000000000000000000'
# print(add_sac_commas(number))

def flavius_josephus(n, k):
    '''
    НЕ РЕШЕНА 2.1.10 Задача Иосифа Флавия
        n человек, пронумерованных числами от 1 до n, стоят в кругу. Они начинают считаться, каждый k-й по счету человек выбывает из круга, после чего счет продолжается со следующего за ним человека. Напишите программу, определяющую номер человека, который останется в кругу последним.

        Формат входных данных
        На вход программе подаются два числа n и k, записанные на отдельных строках.

        Формат выходных данных
        Программа должна вывести одно число – номер человека, который останется в кругу последним.

        Примечание 1. Подробнее ознакомиться с классической задачей Иосифа Флавия можно https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0_%D0%98%D0%BE%D1%81%D0%B8%D1%84%D0%B0_%D0%A4%D0%BB%D0%B0%D0%B2%D0%B8%D1%8F.

        Примечание 2. Визуализацию работы алгоритма можно посмотреть https://www.geogebra.org/m/ExvvrBbR.

        Тестовые данные 🟢
        Sample Input 1:
        2
        1
        Sample Output 1:
        2
        Sample Input 2:
        5
        2
        Sample Output 2:
        3
        Sample Input 3:
        7
        5
        Sample Output 3:
        6
    '''
    list_of_people = [i for i in range(1, n + 1)]
    print(list_of_people)

    while len(list_of_people) > 1:
        for i in range(len(list_of_people)):
            del list_of_people[(i + (k) - 1) % (len(list_of_people))]
            print(list_of_people)

    # for i in range(1, n + 1):
    #     if list_of_people[i - 1] != 0:
    #         print(i % n)
    #         list_of_people[i % n] = 0


    for i in range(1, n):
        print((i) % n)
        if list_of_people[(k * i) % n] != 0:
            list_of_people[(k * i) % n] = 0
            print(list_of_people)

# print(flavius_josephus(41, 2))

def coord_quadrants(n):
    '''
    2.2.1 Координатные четверти
        Дан набор точек на координатной плоскости. Необходимо подсчитать и вывести количество точек, лежащих в каждой координатной четверти.

        Формат входных данных
        В первой строке записано количество точек. Каждая следующая строка состоит из двух целых чисел — координат точки (сначала абсцисса – xx, затем ордината – yy), разделенных символом пробела.

        Формат выходных данных
        Программа должна вывести количество точек, лежащих в каждой координатной четверти, как в примерах.

        Примечание. Учтите, что точки, лежащие на осях координат, не принято относить к какой либо координатной четверти.

        Sample Input 1:
        4
        0 -1
        1 2
        0 9
        -9 -5
        Sample Output 1:
        Первая четверть: 1
        Вторая четверть: 0
        Третья четверть: 1
        Четвертая четверть: 0
        Sample Input 2:

        10
        4 8
        -3 -1
        -4 9
        4 0
        -4 0
        5 -2
        0 0
        1 1
        13 -3
        -43 3
        Sample Output 2:

        Первая четверть: 2
        Вторая четверть: 2
        Третья четверть: 1
        Четвертая четверть: 2
    '''
    one = 0
    two = 0
    three = 0
    four = 0
    for i in range(n):
        a = input().split()
        x = int(a[0])
        y = int(a[1])
        if x > 0 and y > 0:
            one += 1
        if x < 0 and y > 0:
            two += 1
        if x < 0 and y < 0:
            three += 1
        if x > 0 and y < 0:
            four += 1
    
    print('Первая четверть: ', one)
    print('Вторая четверть: ', two)
    print('Третья четверть: ', three)
    print('Четвертая четверть: ', four)

