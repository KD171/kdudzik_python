import os


def open_and_print(directory, deep=1):
    all_item = os.listdir(directory)
    tab1 = ['----' for url in range(deep-1)]
    print(''.join(tab1) + '>', os.path.basename(directory))
    for item in all_item:
        if os.path.isfile(os.path.join(directory, item)):
            text = ''
            for d in range(deep):
                text += '\t'
            print(text + '>', item)
        else:
            open_and_print(directory + '/' + item, deep + 1)

open_and_print(r'C:\Users\kdudz\Downloads\text_files')