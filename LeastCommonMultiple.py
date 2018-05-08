def lcm(a, b):
    assert a > 0 and b > 0
    mult = a * b
    while (a % b!=0) and (b % a!=0):
        if a > b:
            a = a % b
        else:
            b = b% a
    return mult/min(a,b)
