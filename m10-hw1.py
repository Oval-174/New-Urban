#  m10-hw1 "Потоковая запись в файлы"

# Импорты необходимых модулей и функций

from threading import Thread
from time import sleep
from datetime import datetime


# Объявление функции write_words
def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding='utf-8')
    print(f"Началась запись в файл {file_name}")
    for i in range(word_count):
        file.write(f'Какое-то слово № {i + 1}\n')
        sleep(0.1)
    file.close()
    print(f"Завершилась запись в файл {file_name}")

def write_words_1(word_count, file_name):
    file = open(file_name, 'w', encoding='utf-8')
    print(f"Началась запись в файл {file_name}")
    for i in range(word_count):
        file.write(f'Какое-то слово № {i + 1}\n')
        sleep(0.1)
    file.close()
    print(f"Завершилась запись в файл {file_name}")

# Взятие текущего времени
time_start = datetime.now()

# Запуск функций с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени
time_end = datetime.now()

# Вывод разницы начала и конца работы функций
print(f'Работа функций: {time_end - time_start}')

# Взятие текущего времени
time_start = datetime.now()

# Создание и запуск потоков с аргументами из задачи
thr_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=write_words, args=(100, 'example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()

# Взятие текущего времени
time_end = datetime.now()

# Вывод разницы начала и конца работы функций
print(f'Работа потоков: {time_end - time_start}')
