from functools import reduce


# practice： capitalize with map()
def normalize(l1):
    return l1[0].upper() + l1[1:].lower()


l1 = ['dff', 'HkEEf', 'dfjOFF']
print(list(map(normalize, l1)))


# practice: product with reduce（）
def fn(x, y):
    return x * y


def prod(l2):
    return reduce(fn, l2)


print(prod([3, 5, 7, 9]))


# practice: str to float with map() and reduce()
def str_to_num(s):
    def f(x1, y1):
        return x1 * 10 + y1
    s = s.split('.')
    if len(s) == 1:
        return reduce(f, map(int, s[0]))
    else:
        return reduce(f, map(int, s[0] + s[1])) / pow(10, len(s[1]))


print(str_to_num('123.456'))
print(str_to_num('0.123'))
print(str_to_num('123.'))
print(str_to_num('123'))
