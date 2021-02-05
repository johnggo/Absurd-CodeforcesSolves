n = int(input())
s = sum(map(int, input().split()))
sol = s/n
f = float(sol)
print(format(f, '.10f'))
