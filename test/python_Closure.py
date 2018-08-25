# practice: Closure
def counter():
    L = [0]

    def count():
        L[0] = L[0] + 1
        return L[0]
    return count


counterA = counter()
print(counterA(), counterA(), counterA(), counterA(), counterA())     # 1 2 3 4 5
counterB = counter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


# Closure does mot reference any loop variables
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        a = f
        fs.append(a)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


# compare with the last example
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))    # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

