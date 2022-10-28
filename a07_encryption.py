from math import sqrt, floor, ceil

sinput = 'have a nice day'
expect = 'hae and via ecy'

def encryption(s):
    s = ''.join(s.strip().split())
    L = len(s)
    sq = sqrt(L)
    sq0, sq1 = floor(sq), ceil(sq)
    m, n = (sq0, sq0) if sq0 == sq1 else (sq0, sq1) if sq0 * sq1 >= L else (sq1, sq1)
    grid = []
    for p in range(0, L, n):
        line = s[p:p+n]
        line += ' ' * (n - len(line))
        grid.append(line)
    tgrid = zip(*grid)
    result = ' '.join([''.join(t).strip() for t in tgrid])
    return result

actual = encryption(sinput)
print(expect == actual)
