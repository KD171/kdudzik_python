#! /usr/bin/env python3

name = None
surname = None
year = None

while True:
    input_string = input("Enter your name, surname, and year of birth ")
    data = input_string.split(' ')
    while '' in data:
        data.remove('')
    if len(data) == 3:
        name, surname, year = data
        try:
            year = int(year)
            break
        except ValueError as e:
            print('Year is not a number')
            print(e)
    elif len(data) > 3:
        print("Try again\nToo many argument")
    elif len(data) < 3:
        print("Try again\nInsufficient number of arguments")
print('Your data:'
      '\nname: \t\t', name,
      '\nsurname: \t', surname,
      '\nyear:  \t\t', year
      )


