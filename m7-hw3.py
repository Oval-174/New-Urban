# m7-hw3 "Найдёт везде"

class WordsFinder:

    def __init__(self, *arg_file):
        self.file_names = arg_file

    def get_all_words(self):
        all_worlds = {}
        deleted_char = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                file_worlds = []
                for line in file:
                    for c in deleted_char:
                        line = line.replace(c, '')
                    for world in line.lower().split():
                        file_worlds.append(world)
                all_worlds[name] = file_worlds
        return all_worlds

    def find(self, word):
        for name, words in self.get_all_words().items():
            for i in range(0, len(words)):
                if words[i] == word.lower():
                    return {name: i + 1}
            return 'нет такого слова'

    def count(self, word):
        for name, words in self.get_all_words().items():
            count_word = 0
            for i in range(0, len(words)):
                if words[i] == word.lower():
                    count_word += 1
            return {name: count_word}


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
