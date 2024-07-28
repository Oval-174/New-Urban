# m8-hw1 "Программистам всё можно"

def add_everything_up(a, b):
    if type(a) == type(b):
        return a + b
    try:
        summ_a_b = a + b
    except TypeError:
        return str(a) + str(b)
    return round(summ_a_b, 10)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up('яблоко', 'строка'))
