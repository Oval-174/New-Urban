def test_func(*arg, **names):
    print(arg, names)
    print(names)

def factorial_n(n = 0):
    if n == 0:
        return 1
    else:
        return n * factorial_n(n-1)


list_ = [1, 2]
test_func(1, 2, list_, name='sss', course='ddd')



while True:
    n = int(input('Введите целое число: '))
    if n < 0:
        break
    print(n, '! = ', factorial_n(n))
