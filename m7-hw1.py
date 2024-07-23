# m7-hw1 "Учёт товаров"
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:

    __file_name = 'products.txt'

    def __init__(self):
        file = open('products.txt', 'w')
        file.write('')
        file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        file_ret = file.read()
        file.close()
        return file_ret

    def add(self, *products):
        for i in products:
            file = self.get_products()
            if i.name in file:
                print(f'Продукт {i.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)
print(s1.get_products())

p4 = Product('Potato', 50.5, 'Vegetables')
p5 = Product('Spaghetti', 3.4, 'Groceries')
p6 = Product('Potato', 5.5, 'Vegetables')

print(p5)  # __str__

s1.add(p4, p5, p6)
print(s1.get_products())
