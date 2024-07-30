# m8-hw2 "Вызов разом"

def apply_all_func(int_list, *functions):
    results = {}
    for fanc in functions:
        results[fanc.__name__] = fanc(int_list)
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
