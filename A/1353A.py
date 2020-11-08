# Code by JohnXdator
t = int(input())
for t in range(t):
  n, m = list(map(int, input().split()))
  sol = m*(min(n-1, 2))
  print(sol)
