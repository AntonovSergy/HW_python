def thesaurus_adv(*args):
    my_dict = {}
    for name_surname in args:
        name, surname = name_surname.split()
        my_dict.setdefault(surname[0], {})
        my_dict[surname[0]].setdefault(name[0], [])
        my_dict[surname[0]][name[0]].append(name_surname)

    sorted_dict = {x: my_dict[x] for x in sorted(my_dict)}
    return my_dict

print(thesaurus_adv('Sergey Antonov', 'Svetlana Antonova', 'Evgeny Shkarin', 'Dmitry Suharev'))