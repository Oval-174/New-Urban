class Vehicle:
    vehicle_type = "none"


class Car(Vehicle):
    price = 1000000

    def horse_powers(self):
        return 200


class Nissan(Car):
    def __init__(self):
        self.vehicle_type = "car"
        self.price = 2000000

    def horse_powers(self):
        return 300


nissan = Nissan()
print(nissan.vehicle_type, nissan.price)  # Вывод: car 2000000
