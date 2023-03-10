calc1 = 0
calc2 = 0


def fibo(n):
    global calc1
    calc1 += 1
    if n < 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


def fibMemo():
    cache = dict()

    def func(n):
        global calc2
        calc2 += 1
        if n < 2:
            return n
        else:
            if n in cache:
                return cache[n]
            else:
                cache[n] = func(n - 1) + func(n - 2)
                return cache[n]

    return func


n = 100

# print("Recursive solution", fibo(n))
# print("Recursive calcs", calc1)

fibTest = fibMemo()
print("Dynamic solution", fibTest(n))
print("Dynamic calcs", calc2)
