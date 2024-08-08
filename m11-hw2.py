# m11-hw-2
import inspect


class Vehicle:
    __COLOR_VARIANTS = ('RED', 'BLUE', 'GREEN', 'BLACK', 'WHITE')

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        if self.__COLOR_VARIANTS.count(__color.upper()):
            self.__color = __color
        else:
            self.__color = 'BLACK'

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец: {self.owner}')

    def set_color(self, new_color):
        if self.__COLOR_VARIANTS.count(new_color.upper()):
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):

    __PASSENGERS_LIMIT = 5

    def p_limit(self):
        return self.__PASSENGERS_LIMIT


def introspection_info(obj):
    methods = [func for func in dir(obj) if callable(getattr(obj, func))]
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    module = inspect.getmodule(obj).__name__
    return f"Type: {type(obj)}\nAttributes: {attributes}\nMethods: {methods}\nModule: {module}"


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Пример использования функции для объекта vehicle1
print(introspection_info(vehicle1))
