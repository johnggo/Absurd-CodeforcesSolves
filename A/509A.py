# Code by JohnXdator
n = int(input())
a = [1] * n
for i in range(n - 1):
  for j in range(n - 1):
    a[j + 1] += a[j]
print(a[-1])
