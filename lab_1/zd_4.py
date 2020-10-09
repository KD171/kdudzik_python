pin = None
while True:
    try:
        pin = input("Enter new PIN: ")
        pin = int(pin)
        break
    except ValueError as e:
        print("Enter PIN as numbers")
        print(e)
while True:
    try:
        new_pin = input("Enter PIN: ")
        new_pin = int(new_pin)
        if new_pin == pin:
            print("PIN correct")
            break
        else:
            print("PIN incorrect")
    except ValueError as e:
        print("Enter PIN as a numbers")
        print(e)
