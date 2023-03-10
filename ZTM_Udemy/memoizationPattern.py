def memoAddTo80():
    cache = dict()

    def func(n):
        if n in cache:
            return cache[n]
        else:
            print("long time")
            cache[n] = 80 + n
            return cache[n]

    return func


mem = memoAddTo80()
print(mem(5))
print(mem(5))