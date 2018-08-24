# practice: primes with filter()
def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def not_divisible(n):
        return lambda x: x % n > 0


def primes():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n), it)


for n in primes():
    if n < 1000:
        print(n)
    else:
        break


# practice： screen over  palindrome with filter()
def condition(n1):
    s = str(n1)
    for i in range(len(s)):
        return s[i] == s[-(i + 1)]


def is_palindrome():
    return filter(condition, range(1000))


print(list(is_palindrome()))


# another way to screen over palindrome
def is_palindrome(n2):
    s = str(n2)
    return s == s[::-1]


print(list(filter(is_palindrome, range(1000))))



