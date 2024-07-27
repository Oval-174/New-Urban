# m7-hw2 "Записать и запомнить"

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    list_strings = strings
    __result = {}
    for i in range(0, len(list_strings)):
        __result[i + 1, file.tell()] = list_strings[i]
        file.write(list_strings[i] + '\n')
    file.close()
    return __result


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
