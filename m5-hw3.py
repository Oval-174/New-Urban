class Buiding:

    def __init__(self, number_of_floors, building_type):
        self.number_of_floors = number_of_floors
        self.building_type = building_type

    def __eq__(self, other):
        return (self.number_of_floors == other.number_of_floors) and (self.building_type == other.building_type)


building_1 = Buiding(1, 'bank')
building_2 = Buiding(1, 'bank')
building_3 = Buiding(1, 'hostel')
print(building_1 == building_2)
print(building_1 == building_3)
