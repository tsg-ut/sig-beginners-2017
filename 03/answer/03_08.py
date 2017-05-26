def is_complete(n):
    s = 0
    for i in range(1,n):
        if n % i == 0:
            s += i
    return s == n


for i in range(1, 1000):
    print(i, ":\t", is_complete(i))
