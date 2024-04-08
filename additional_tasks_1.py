# for if 1.
while True:
    test_year = int(input('Введите номер года по григорианскому календарю: '))
    if test_year < 0:
        print('Game over')
        break
    if test_year < 1582:
        print('Григорианский календарь был введен в действие в 1582 году римским папой Григорием XIII')
        continue
    else:
        if test_year % 400 == 0:
            print(test_year, '- високосный год')
            continue
        else:
            if test_year % 100 == 0:
                print(test_year, '- невисокосный год')
                continue
            else:
                if test_year % 4 == 0:
                    print(test_year, '- високосный год')
                    continue
                else:
                    print(test_year, '- невисокосный год')
                    continue
# for if 2.
while True:
    package_weight = int(input('Введите вес посылки в кг: '))
    if package_weight < 0:
        print('Game over')
        break
    if package_weight > 10:
        print('Стоимость доставки посылки весом ', package_weight, 'кг - 200 рублей')
        continue
    else:
        if package_weight <= 2:
            print('Стоимость доставки посылки весом ', package_weight, 'кг - 50 рублей')
            continue
        else:
            package_cost = 50 + 20 * (package_weight - 2)
            print('Стоимость доставки посылки весом ', package_weight, 'кг -', package_cost, 'рублей')
            continue
# for while 1.
while True:
    high_number = int(input('Введите верхнюю границу для поиска простых чисел ( < 20 ): '))
    if high_number <= 0:
        print('Game over')
        break
    list_prime_numbers = []
    test_number = high_number
    for i in range(1, high_number + 1):

        print(i)
