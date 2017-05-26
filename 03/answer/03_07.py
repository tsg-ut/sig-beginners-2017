def add_n(n):
    def add(x):
        return x + n
    f = add
    return f

f = add_n(10)
print(f(5))
print(f(3))

print(add_n(3)(4))
