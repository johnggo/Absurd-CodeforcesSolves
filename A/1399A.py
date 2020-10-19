# Code by JohnXdator
t = int(input())
for w in range(t):
  n = int(input())
  s = list(map(int, input().split()))
  s.sort()
  sol = 'YES'
  for i in range(n-1):
    if s[i+1]-s[i] > 1:
      sol = 'NO'
  print(sol)
