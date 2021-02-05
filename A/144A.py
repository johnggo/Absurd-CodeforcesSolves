a = int(input())
l = list(map(int, input().split()))
c = l.index(max(l))
sol = l[::-1].index(min(l))
if c < len(l) - sol - 1:
  print(c + sol)
else:
  print(c + sol - 1)
