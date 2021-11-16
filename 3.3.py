def thesaurus(*args):
    my_dict = dict()
    for name in args:
        my_dict.setdefault(name[0], [])
        my_dict[name[0]].append(name)
    return my_dict

print(thesaurus('Sergey', 'Svetlana', 'Evgeny', 'Mihail', 'Dmitry', 'Ekaterina'))