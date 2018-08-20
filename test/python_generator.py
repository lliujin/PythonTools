# Yang Hui's triangle
def triangles(n):
    l = [1]
    while len(l) <= n:
        yield l
        l = [1] + [l[i] + l[i + 1] for i in range(len(l)-1)] + [1]


for t in triangles(5):
    print(t)