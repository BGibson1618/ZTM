calc1 = 0
calc2 = 0
calc3 = 0


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


def fibBottomUp(n):
    arr = [0, 1]
    global calc3
    for i in range(2, n):
        arr.append(arr[i - 2] + arr[i - 1])
        calc3 += 1
    return arr.pop()


n = 5

print("Recursive solution", fibo(n))
print("Recursive calcs", calc1)

fibTest = fibMemo()
print("Dynamic solution", fibTest(n))
print("Dynamic calcs", calc2)

print("Bottom Up solution", fibBottomUp(n))
print("Bottom up calculations", calc3)
