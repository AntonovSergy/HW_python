my_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(enter_word):
    if enter_word[0].isupper():
        enter_word = enter_word.lower()
        return my_dict[enter_word].capitalize()
    else:
        return my_dict[enter_word]


print(input('Enter word: '))