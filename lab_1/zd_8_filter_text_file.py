#! /usr/bin/env python3

import os
import re

directory_list = ['./zd_8/krakow_policja_klub.txt']
word_to_delete = ['się', 'i', 'oraz', 'nigdy', 'dlaczego']


def delete_text_from_file3(directory, delete_list):
    for file in directory:
        result_text = ''
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                text = re.split(r'(\W+)', line)
                for delete in delete_list:
                    i = []
                    for x in range(len(text)):
                        if delete == text[x]:
                            i.append(x)
                    for t in reversed(i):
                        if text[t - 1] == ' ' and text[t + 1] == ' ':
                            del text[t + 1]
                            del text[t]
                        elif text[t - 1] == ' ':
                            del text[t]
                            del text[t - 1]
                        elif text[t + 1] == ' ':
                            del text[t + 1]
                            del text[t]
                        else:
                            del text[t]
                result_text += ''.join(text)
        new_file_name = list(os.path.splitext(file))
        new_file_name.insert(-1, '_filtered')
        new_file_name = ''.join(new_file_name)
        with open(new_file_name, "w+") as f:
            f.write(result_text)


delete_text_from_file3(directory_list, word_to_delete)