phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for x in phone_numbers.values():
    y = x.replace("+", "00")
    print(y)
    print(x)