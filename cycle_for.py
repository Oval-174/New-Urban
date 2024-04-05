list_of_cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]
cars_count = 0
for i in range(len(list_of_cars)):
    print('Я езжу на автомобиле марки ' + list_of_cars[i] + '.')
    cars_count += 10
    print(cars_count)
