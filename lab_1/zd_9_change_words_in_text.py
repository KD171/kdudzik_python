#! /usr/bin/env python3

import os
import re

directory_list = ['./zd_9/krakow_policja_klub.txt', './zd_9/szpital_polowy_w_targach_kielce_ruszyl.txt']
change_word_dict = {'i': 'Oraz', 'oraz': 'i', 'nigdy': 'prawie nigdy', 'dlaczego': 'czemu'}
ignore_big_letter = True

def change_word(dir_list, dict_words, big_letter):
    if big_letter:
        temp_dict = {}
        for x in dict_words:
            temp_dict[x.lower()] = dict_words[x]
        dict_words = temp_dict
    for file in dir_list:
        result_text = ''
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                text = re.split(r'(\W+)', line)
                new_text = []
                for word in text:
                    word_temp = word
                    first_letter_big = False
                    if big_letter:
                        if len(word) > 0:
                            if word[0].isupper() and word[1:].islower():
                                first_letter_big = True
                        word_temp = word.lower()
                    if word_temp in dict_words:
                        word_temp = dict_words.get(word_temp)
                        if first_letter_big:
                            word_temp = word_temp[0].upper() + word_temp[1:]
                        new_text.append(word_temp)
                    else:
                        new_text.append(word)
                result_text += ''.join(new_text)
        new_file_name = list(os.path.splitext(file))
        new_file_name.insert(-1, '_filtered')
        new_file_name = ''.join(new_file_name)
        with open(new_file_name, "w+") as f:
            f.write(result_text)


change_word(directory_list, change_word_dict, ignore_big_letter)

#
# def big_small_letter(word):
#     for x in word:
#         if x.isupper():
#             pass



#
# def delete_text_from_file(directory):
#     print(directory)
#     for file in directory:
#         with open(file, 'r') as f:
#             lines = f.readlines()
#             for line in lines:
#                 for delete in delete_list:
#                     listek = line.split(' ')
#                     print(listek)
#                     x = []
#                     for lis in listek:
#                         if delete in lis:
#                             x.append(listek.index(lis))
#                     print(x)
#                     for i in reversed(x):
#                         print(listek[i])
#                         if listek[i] == delete or listek[i] == delete + '\n':
#                             del listek[i]
#                         else:
#                             pass
#                     print(listek)
#
#
# dir = r'/home/krzysztof/Pobrane/pliki'
#
#
# def all_path_to_file(directory, deep=1):
#     all_item = os.listdir(directory)
#     all_item.sort()
#     directory_list = []
#     for item in all_item:
#         if os.path.isdir(os.path.join(directory, item)):
#             directory_list.extend(all_path_to_file(directory + '/' + item, deep + 1))
#         else:
#             directory_list.append(directory + '/' + item)
#     return directory_list
#
#
# directory_list = all_path_to_file(dir)



