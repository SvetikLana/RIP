# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from operator import itemgetter


class Construc:
    """Синтаксическая конструкция"""

    def __init__(self, _id, name, size, lang_id):
        self.id = _id
        self.name = name
        self.size = size
        self.lang_id = lang_id


class Lang:
    """Язык программирования"""
    def __init__(self, _id, name):
        self.id = _id
        self.name = name


class ConstrucLang:
    """Конструкции языка программирования"""

    def __init__(self, _lang_id, _Construc_id):
        self.lang_id = _lang_id
        self.Construc_id = _Construc_id


# Языки программирования
langs = [
    Lang(1, 'Python'),
    Lang(2, 'C++'),
    Lang(3, 'C#'),

    Lang(4, 'Pascal'),
    Lang(5, 'Java'),
    Lang(6, 'Basic'),
]

# Синтаксические конструкции
construcs = [
    Construc(1, 'А1 конструкция', 15, 1),
    Construc(2, 'В1 конструкция', 20, 2),
    Construc(3, 'С1 конструкция', 10, 2),
    Construc(4, 'А2 конструкция', 10, 3),
    Construc(5, 'В2 конструкция', 30, 3),
    Construc(6, 'С2 конструкция', 25, 3),
]

construcs_langs = [
    ConstrucLang(1, 1),
    ConstrucLang(2, 2),
    ConstrucLang(2, 3),
    ConstrucLang(3, 4),
    ConstrucLang(3, 5),
    ConstrucLang(3, 6),

    ConstrucLang(4, 1),
    ConstrucLang(4, 2),
    ConstrucLang(5, 3),
    ConstrucLang(5, 4),
    ConstrucLang(6, 5),
    ConstrucLang(6, 6),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [
        (c.name, c.size, L.name)
        for L in langs
        for c in construcs
        if c.lang_id == L.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [
        (L.name, cl.lang_id, cl.Construc_id)
        for L in langs
        for cl in construcs_langs
        if L.id == cl.lang_id]

    many_to_many = [
        (c.name, c.size, lang_name)
        for lang_name, lang_id, Construc_id in many_to_many_temp
        for c in construcs
        if c.id == Construc_id]

    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)

    print('\nЗадание А2')
    res_12_unsorted = []
    for d in langs:
        d_construcs = list(filter(lambda i: i[2] == d.name, one_to_many))
        #
        if len(d_construcs) > 0:
            d_sizes = [size for _, size, _ in d_construcs]

            d_sizes_sum = sum(d_sizes)
            res_12_unsorted.append((d.name, d_sizes_sum))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание А3')
    res_13 = {}
    for d in langs:
        if 'C' in d.name:
            d_construcs = list(filter(lambda i: i[2] == d.name, many_to_many))
            d_construcs_names = [x for x, _, _ in d_construcs]

            res_13[d.name] = d_construcs_names

    print(res_13)


if __name__ == '__main__':
    main()


# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
