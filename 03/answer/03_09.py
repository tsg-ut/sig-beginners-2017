def is_complete(n):
    s = 0
    for i in range(1,n):
        if n % i == 0:
            s += i
    return s == n

def my_filter(r, f):
    for i in r:
        if f(i):
            print(i)

my_filter(range(1,10000), is_complete)
