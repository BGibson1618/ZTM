def fac_recur(num):
    if num == 1:
        return 1
    else:
        return num * fac_recur(num - 1)


def fac_iter(num):
    accum = 1
    while num > 1:
        accum *= num
        num -= 1
    return accum
