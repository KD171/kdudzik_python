#! /usr/bin/env python3

import os

def delete_from_text(dir_file, delete_text):
    print(delete_text)
    print(dir_file)


dir = r'/home/krzysztof/Pobrane/pliki'


def all_path_to_file(directory, deep=1):
    all_item = os.listdir(directory)
    all_item.sort()
    directory_list = []
    for item in all_item:
        if os.path.isdir(os.path.join(directory, item)):
            directory_list.extend(all_path_to_file(directory + '/' + item, deep + 1))
        else:
            directory_list.append(directory + '/' + item)
    return directory_list


directory_list = all_path_to_file(dir)
dir = ['./zd_8/krakow_policja_klub.txt']


delete_list = ['się', 'i', 'oraz', 'nigdy', 'dlaczego']


def delete_text_from_file(directory):
    print(directory)
    for file in directory:
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                for delete in delete_list:
                    listek = line.split(' ')
                    print(listek)
                    x = []
                    for lis in listek:
                        if delete in lis:
                            x.append(listek.index(lis))
                    print(x)
                    for i in reversed(x):
                        print(listek[i])
                        if listek[i] == delete or listek[i] == delete + '\n':
                            del listek[i]
                        else:
                            pass
                    print(listek)


def delete_text_from_file3(directory):
    import re
    print(directory)
    for file in directory:
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                for delete in delete_list:
                    text = re.split(r'(\W+)', line)
                    i = []
                    for x in range(len(text)):
                        if delete == text[x]:
                            i.append(x)
                    for t in reversed(i):
                        print(text[t - 1], 't-1')
                        print(text[t], 't')
                        print(text[t+1], 't+1')
                        print(text)
                        if text[t - 1] == ' ' and text[t + 1] == ' ':
                            print('1')
                            del text[t + 1]

                            del text[t]
                        elif text[t - 1] == ' ':
                            print('2')
                            del text[t]
                            del text[t - 1]

                        elif text[t + 1] == ' ':
                            print('3')
                            del text[t + 1]

                            del text[t]
                        else:
                            del text[t]

                        print(text)
                    text = ''.join(text)
                    print(text)
                    #
                    #         print(text[x])
                    # text = re.compile('(\s*)' + delete + '(\s*)')
                    # line = text.sub(' ', line)
                    # print(text)
                    # print(line)






delete_text_from_file3(dir)

colors_dict = {'i': 'oraz', 'oraz': 'i', 'nigdy': 'prawie nigdy',
                       'dlaczego': 'czemu'}