#! /usr/bin/env python3

import random

random_list = []
sort_list = []
for x in range(1, 50):
    random_list.append(random.randint(0, x*10))

for x in range(len(random_list)):
    if len(sort_list) == 0:
        sort_list.append(random_list[0])
    else:
        for y in range(x):
            if sort_list[y] < random_list[x]:
                sort_list.insert(y, random_list[x])
                break
        if len(sort_list) != x + 1:
            sort_list.append(random_list[x])

random_list.sort(reverse=True)
if sort_list == random_list:
    print('Random list\t', random_list)
    print('Sort list\t', sort_list)
    print('Same')

