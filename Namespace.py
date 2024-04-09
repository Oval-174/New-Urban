def test():
    a = 5
    b = 10
    print(a, b)


def test2(a, b, c):
    print(a, b, c)


def print_params(a = 1, b = 'str', c = True):
    print(a, b, c)


print_params(1, b = 2, c = 3)
print_params(1, 2)
print_params(c = 1)
print_params()
print_params(b = 25)
print_params(c = [1,  2, 3])

value_list = [2, 'STR', False]
value_list_2 = [2, 'STR']
value_dict = {'a' : 'str', 'b' : True, 'c' : 255}

print_params(*value_list)
print_params(**value_dict)
print_params(*value_list_2,42)

# test()
# test2('a', 'b', 'c')
