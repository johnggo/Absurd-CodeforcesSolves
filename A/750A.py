# Code by JohnXdator
n, k = map(int, input().split())
s = (240-k)
a = 0
while s >= (5*(a + 1)):
    a += 1
    s -= (5*a)
print(min(a, n))
