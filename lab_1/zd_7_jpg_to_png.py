#! /usr/bin/env python3

import os

from PIL import Image


def jpg_to_png(files):
    for jpg in files:
        try:
            image = Image.open(jpg)
            jpg = jpg.replace('.jpg', '.png')
            image.save(jpg)
        except Exception as e:
            print(e)


dir_path = os.path.dirname(os.path.realpath(__file__))
all_files = os.listdir(dir_path)
directory = [dir_path + '/' + file for file in all_files if '.jpg' in file]
jpg_to_png(directory)
