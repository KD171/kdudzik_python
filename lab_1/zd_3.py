name = None
surname = None
year = None

while True:
    input_string = input("Enter your name, surname, and year of bird ")
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
    else:
        print("Try again")
print('Your data:'
      '\nname: \t\t', name,
      '\nsurname: \t', surname,
      '\nyear:  \t\t', year
      )


