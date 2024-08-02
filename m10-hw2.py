#  m10-hw2 "За честь и отвагу!"

# Импорты необходимых модулей и функций
from time import sleep
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        self.NAME = name
        self.POWER = power
        super().__init__()

    def run(self):
        print(f"\n{self.NAME}, на нас напали!")
        days = 0
        enemies = 100
        while enemies > 0:
            sleep(1)
            days += 1
            enemies -= self.POWER
            if enemies < 0:
                enemies = 0
            print(f'\n{self.NAME} сражается {days} дней, осталось {enemies} воинов.')
        print(f'\n{self.NAME} одержал победу спустя {days} дней(дня)!')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print(f'\nВсе битвы закончились!')
