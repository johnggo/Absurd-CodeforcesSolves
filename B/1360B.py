t = int(input())
for w in range(t):
  n = int(input())
  s = list(map(int, input().split()))
  s.sort()
  sol = [s[i+1]-s[i] for i in range(n-1)]
  print(min(sol))
