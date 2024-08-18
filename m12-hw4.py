# m12_hw4
import unittest
import logging

logging.basicConfig(level='INFO', filemode='w', filename="test_runner.log", encoding='utf-8',
                    format='%(levelname)s | %(message)s')
logging.info(f'm12-hw4')


# class Runner from GitHub
class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, '')
    def test_walk(self):
        logging.info(f'"test_walk"')
        try:
            t1 = Runner('t1', -5)
            for i in range(10):
                t1.walk()
            self.assertEqual(t1.distance, 50)
            logging.info(f'"test_walk" выполнен успешно')
        except ValueError:
            logging.warning(f'Неверная скорость для Runner')

    @unittest.skipIf(is_frozen, '')
    def test_run(self):
        logging.info(f'"test_run"')
        try:
            t2 = Runner(5, 5)
            for i in range(10):
                t2.run()
            self.assertEqual(t2.distance, 100)
        except TypeError:
            logging.warning(f'Неверный тип данных для объекта Runner')


if __name__ == '__main__':
    unittest.main()
