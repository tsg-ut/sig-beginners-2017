import math
# listを使えばもっと良い実装ができるけれど，使わないとこんな感じかなぁ
def is_goldbach(n):
    for i in range(2, n):
        if is_prime(i) and is_prime(n-i):
            print(n, '=',i, '+', n-i)
            return True
    return False

# これももっと早い実装がありそう？
def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            break
    else:
        return True;
    return False


for i in range(4, 101, 2):
    if not is_goldbach(i):
        print(i, "is Counterexample")
        break
else:
    print("No Counterexample was Found!")
