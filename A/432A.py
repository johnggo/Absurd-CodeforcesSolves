n, k = map(int, input().split())
y = sorted(map(int, input().split()))
sol = 0
for i in y:
  if k <= (5-i):
    sol += 1
print(sol//3)
