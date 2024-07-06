# m3-hw4.py "Однокоренные"
def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        i_lower = i.lower()
        if root_word.lower().find(i_lower) != -1 or i_lower.find(root_word.lower()) != -1:
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
