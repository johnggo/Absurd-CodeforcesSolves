# Code by JohnXdator
k, l, m, n, d = (int(input()) for i in range(5))
y = 0
for i in range(d+1):
  if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
    y+=1
print((y)-1)
