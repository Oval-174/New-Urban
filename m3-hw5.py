# m3-hw2.py "Рекурсия"
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if first == 0:  # последний 0 заменяем на 1
        first = 1
    if len(str_number) == 1:
        return first
    return first*get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(40203)
print(result)

result = get_multiplied_digits(402030)
print(result)
