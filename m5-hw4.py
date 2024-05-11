class Building:
    total_building = 0
    def __init__(self):
        Building.total_building += 1
        print('Построено здание ', Building.total_building)


new_building = Building()
for i in range(1, 40):
    new_building = Building()
print('Всего построено зданий ', new_building.total_building)