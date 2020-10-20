#! /usr/bin/env python3

import os


def open_and_print(directory, deep=1):
    all_item = os.listdir(directory)
    all_item.sort()
    tab1 = ['   ' for url in range(deep - 1)]
    tab1.extend(['└───'])
    print(''.join(tab1) + '>', os.path.basename(directory))
    for item in all_item:
        if os.path.isdir(os.path.join(directory, item)):
            open_and_print(directory + '/' + item, deep + 1)
        else:
            text = ''
            for d in range(deep):
                text += '\t'
            print(text + '└>', item)


open_and_print(r'/home/krzysztof/PycharmProjects/kdudzik_python')
