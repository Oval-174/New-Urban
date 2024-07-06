# m3-hw3.py "Распаковка"
def print_params(a=1, b='строка', c=True):
    print(f'a = {a} {type(a)}, b = {b} {type(b)}, c = {c} {type(c)}')


# 1
print('# 1')
print_params()
print_params(2)
print_params(3, '4')
print_params(3, '2', 3)
print_params(b=25)
print_params(c=[1, 2, 3])

# 2
print('# 2')
values_list = [0, 'text', False]
values_dict = {'a': False, 'b': 2, 'c': 'err'}
print_params(*values_list)
print_params(**values_dict)

# 3
print('# 3')
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
