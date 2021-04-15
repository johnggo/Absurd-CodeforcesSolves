n, k, i, c, d, p, nl, np = map(int, input().split())
ki = k*i
cd = c*d
pn = p // np
t = ki // nl
print(min(t//n, cd//n, pn//n))
