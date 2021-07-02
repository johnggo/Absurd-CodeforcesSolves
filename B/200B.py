# Time: 218 ms
# Memory: 20 KB
n = int(input())
nith = list(map(int, input().split()))
sol = (sum(nith)/n)
# See what '{:.12f}' means at
# https://docs.python.org/3/library/string.html#format-examples
print('{:.12f}'.format(sol)) 
