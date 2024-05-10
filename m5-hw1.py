class House:
    def __init__(self):
        pass

    @staticmethod
    def print_number_of_floors(num):
        for i in range(num):
            print('Текущий этаж:', i + 1)


my_house = House()
my_house.number_of_floors = 10
my_house.print_number_of_floors(my_house.number_of_floors)
