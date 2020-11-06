# Code by JohnXdator
n = int(input())
t = list(map(int, input().split()))
m = min(t.count(1), t.count(2), t.count(3))
print(m)
for i in range(m):
  a = t.index(1)
  t[a] = 0
  b = t.index(2)
  t[b] = 0
  c = t.index(3)
  t[c] = 0
  print(a+1,b+1,c+1)
