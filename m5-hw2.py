class House:
    def __init__(self, num):
        self.number_of_floors = num

    def set_new_number_off_floors(self, floors):
        self.number_of_floors = floors
        print('Этажей в доме: ', self.number_of_floors)

my_house = House(0)
print('Этажей в доме: ', getattr(my_house, 'number_of_floors'))
my_house.set_new_number_off_floors(5)
