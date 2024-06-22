# 1 m1-hw5.py Неизменяемые и изменяемые объекты. Кортежи
# 2
immutable_var = 1, True, "Hi baby", [0, 1]
print(type(immutable_var), immutable_var)
# 3
# immutable_var[1] = False
immutable_var[3].append(2)
print(immutable_var)
# 4
mutable_list = [1, True, "Hi baby", [0, 1]]
print(type(mutable_list), mutable_list)
mutable_list[1] = False
print(mutable_list)
