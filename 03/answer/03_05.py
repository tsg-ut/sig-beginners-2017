def fib(n):
    return fib2(n, 1, 0)

def fib2(n, a, b):
    if n == 0:
        return b;
    else:
        return fib2(n-1, a + b, a)

print(fib(10))
