# m10-hw5 ''
import random
import threading
import time

class WarehouseManager:
    def __init__(self):
        self.data = {}

    def process_request(self, request):
        time.sleep(10 * random.random())
        print(request, self.data)
        product, action, quantity = request
        if action == "receipt":
            if product in self.data:
                self.data[product] += quantity
            else:
                self.data[product] = quantity
        elif action == "shipment":
            if product in self.data:
                if self.data[product] >= quantity:
                    self.data[product] -= quantity
                else:
                    print(f"Error: Insufficient quantity of {product} for shipment")
            else:
                print(f"Error: Product {product} not found for shipment")
        print(request, self.data)
        time.sleep(10 * random.random())

    def process_request_thread(self, request):
        thread = threading.Thread(target=self.process_request, args=(request,))
        thread.start()

    def run(self, requests):
        for request in requests:
            self.process_request_thread(request)

# Создаем менеджера склада
manager = WarehouseManager()

# Множество запросов на изменение данных о складских запасах
requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)
]

# Запускаем обработку запросов
manager.run(requests)

# Выводим обновленные данные о складских запасах
while True:
    print(f'Final: {manager.data}')
    time.sleep(60)
