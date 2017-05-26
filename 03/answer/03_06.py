def my_sum(*args):
    s = 0
    for i in args:
        s += i
    return s

print(my_sum(1,2,3,4,5,6,7,8,9))
