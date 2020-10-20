#! /usr/bin/env python3

import os

directory = r'/dev'
file_list = []
for root, dirs, files in os.walk(directory):
    file_list.extend(files)
print("Number of files in the folder", directory, len(file_list))
