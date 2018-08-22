# Select string and output lowercase
L1 = ('Hello', 'World', 18, 'Apple', None)
L2 = []
for s in L1:
    if isinstance(s, str):
        L2.append(s.lower())
print(L2)


# Pick the maximum and minimum in the list
def min_max(l):
    if len(l) == 0:
        return None, None
    min = l[0]
    max = l[0]
    for i in l:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max


print(min_max([1, 3, 9, 6]))


# the num of the product
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1, 2, 3]))