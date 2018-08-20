from functools import reduce


# practice capitalize with map()
def normalize(l1):
    return l1[0].upper() + l1[1:].lower()


l1 = ['dff', 'HkEEf', 'dfjOFF']
print(list(map(normalize, l1)))


# practice product with reduce