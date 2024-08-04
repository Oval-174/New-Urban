import threading
import time
import queue


class Table:
    def __init__(self, number, is_busy=False):
        self.number = number
        self.is_busy = is_busy


class Customer(threading.Thread):
    def __init__(self, cafe, number):
        super().__init__()
        self.cafe = cafe
        self.number = number

    def run(self):
        try:
            table_number = self.cafe.get_free_table()
            if table_number is not None:
                self.cafe.tables[table_number].is_busy = True
                print(f"Посетитель номер {self.number} сел за стол {self.cafe.tables[table_number].number}.")
                time.sleep(5)  # время обслуживания
                self.cafe.tables[table_number].is_busy = False
                print(f"Посетитель номер {self.number} покушал и ушел.")
                self.cafe.serve_customer()
            else:
                self.cafe.queue.put(self.number)
                print(f"Посетитель номер {self.number} ожидает свободный стол.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


class Cafe:
    def __init__(self, tables):
        self.tables = tables
        self.queue = queue.Queue()

    def get_free_table(self):
        for i, table in enumerate(self.tables):
            if not table.is_busy:
                return i
        return None

    def customer_arrival(self):
        for i in range(1, 21):
            customer = Customer(self, i)
            customer.start()
            time.sleep(1)
        not_end = True
        while not_end:
            time.sleep(3)
            not_end = False
            for table in cafe.tables:
                if table.is_busy:
                    not_end = True

    def serve_customer(self):
        if not self.queue.empty():
            next_customer = self.queue.get()
            customer = Customer(self, next_customer)
            customer.start()


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_serve_thread = threading.Thread(target=cafe.serve_customer)
customer_arrival_thread.start()
customer_serve_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
customer_serve_thread.join()
