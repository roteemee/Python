while True:
    number = input("Enter a number: ")
    try:
         int(number)
    except ValueError:
        continue
    else:
        break