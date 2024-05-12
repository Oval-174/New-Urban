class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        return "Unknown"

class Nissan(Car):
    def __init__(self):
        super().__init__()
        self.price = 1500000

    def horse_powers(self):
        return 300

class Kia(Car):
    def __init__(self):
        super().__init__()
        self.price = 1200000

    def horse_powers(self):
        return 250

# Пример использования
car1 = Car()
nissan1 = Nissan()
kia1 = Kia()

print(car1.price)  # Выведет: 1000000
print(nissan1.price)  # Выведет: 1500000
print(nissan1.horse_powers())  # Выведет: 300
print(kia1.horse_powers())  # Выведет: 250