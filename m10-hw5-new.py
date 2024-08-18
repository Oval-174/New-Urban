#m10-hw5-new
import multiprocessing
import time
def read_info(name):
    all_data = []  # Создаем пустой локальный список
    with open(name, 'r', encoding='utf-8') as file:  # Открываем файл для чтения
        line = file.readline()  # Считываем первую строку
        while line:  # Пока строка не пустая
            all_data.append(line)  # Добавляем строку в список
            line = file.readline()  # Считываем следующую строку

if __name__ == "__main__":
    file_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

    # Линейный вызов
    start_time = time.time()
    for file in file_names:
        read_info(file)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f'Однопроцессный вариант выполнен за {execution_time} секунд')

    # Многопроцессный
    start_time = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_names)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f'Многопроцессный вариант выполнен за {execution_time} секунд')
