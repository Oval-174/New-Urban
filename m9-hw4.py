# m9-hw4 "Функциональное разнообразие"

import random

#  Lambda-функция

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))


#  Замыкание

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, 'a', encoding='utf-8')
        for line in data_set:
            file.write(f'{line}\n')
        file.close()
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#  Метод __call__:


class MysticBall:

    def __init__(self, *words):
        self.__words = tuple(words)

    def __call__(self):
        return random.choice(self.__words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
