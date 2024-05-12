class Building:
    total_building = 0
    def __init__(self):
        Building.total_building += 1
        self.addr = ''
    #    print('Построено здание ', self)


new_building = ['']
for i in range(1, 41):
    new_building.append(Building())
for i in range(1, 41):
    new_building[i] = Building()
    print('Построено здание ', i, ' ', new_building[i])
setattr(new_building[5], 'addr', 'Как войдешь в Африку - направо')
print(new_building[5].addr)
