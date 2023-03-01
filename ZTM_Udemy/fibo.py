def fibo_recur(n):
    if n < 2:
        return n
    else:
        return fibo_recur(n - 1) + fibo_recur(n - 2)


def fibo_iter(n):
    if n < 2:
        return n
    else:
        x, y = 0, 1
        for i in range(2, n + 1):
            val = x + y
            x, y = y, val
        return val
