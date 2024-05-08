def calculate_structure_sum(data_structure):
    global sum_of_data_structure
    data_type = str(type(data_structure))
    if data_type == "<class 'int'>":
        sum_of_data_structure += data_structure
        return sum_of_data_structure
    if data_type == "<class 'str'>":
        sum_of_data_structure += len(data_structure)
        return sum_of_data_structure
    if data_type == "<class 'list'>":
        for i in range(0, len(data_structure)):
            calculate_structure_sum(data_structure[i])
    else:
        if data_type == "<class 'dict'>":
            calculate_structure_sum(list(data_structure.items()))
        else:
            calculate_structure_sum(list(data_structure))
    return sum_of_data_structure


sum_of_data_structure = 0
data_structure_test = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure_test)
print(result)
