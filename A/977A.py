n, k = input().split()
n = int(n)
k = int(k)
for i in range(k):
  u = n % 10
  if u == 0:
    n = n/10
  else:
    n = n - 1
print(int(n))
