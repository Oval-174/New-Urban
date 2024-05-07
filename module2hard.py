while True:
    num = int(input('Введите число "замок": '))
    if num < 3:
        break
    key = ''
    for i in range(1, num + 1):
        for j in range(i + 1, num):
            if num % (i + j) == 0:
                key = key + str(i) + str(j)
    print('         Число "ключ": ', key)
