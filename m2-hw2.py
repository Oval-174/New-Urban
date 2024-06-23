# m2-hw2.py "Условная конструкция. Операторы if, elif, else."
first = int(input("Введите число:"))
second = int(input("Введите еще число:"))
third = int(input("Введите последнее число:"))
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)
