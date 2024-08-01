#  m9-hw7 "Декораторы в Python"

def is_prime(func):
    def wrapper(*args):
        n = sum(args)
        test_n = True
        if n <= 1:
            test_n = False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                test_n = False
        if test_n:
            print("Простое")
        else:
            print("Составное")
        return func(*args)
    return wrapper


@is_prime
def sum_three(*args):
    summ = sum(args)
    return summ


result = sum_three(2, 3, 6)
print(result)
