def most(L):
    if L == []:
        return None
    mx = 0
    val = L[0]
    for x in L:
        c = L.count(x)
        if c > mx:
            mx = c
            val = x
    return val


def not_in_b_case_insnstv(a, b):
    B = []
    for z in b:
        try:
            B.append(z.lower())
        except:
            B.append(str(z).lower())
    out = []
    for ITEM in a:
        try:
            if ITEM.lower() not in B:
                out.append(ITEM)
        except:
            if str(ITEM).lower() not in B:
                out.append(ITEM)
    return out


def fin(start, rate, years):
    # rate is e.g. 0.05 for 5%
    s = start
    y = 0
    while y < years:
        s = s * (1+rate)
        y = y+1
    return s


if __name__ == "__main__":
    print(most([1, 2, 2, 3, 3, 3, 2]))
    print(not_in_b_case_insnstv(
        ['Apple', 'banana', 'Cherry'], ['BANANA', 'pear']))
    print(fin(1000, 0.05, 3))
