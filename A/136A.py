n = int(input())
f = list(map(int, input().split()))
s = [0] * n
for i in range(n):
  s[f[i] - 1] = i + 1
print(" ".join(map(str, s)))
