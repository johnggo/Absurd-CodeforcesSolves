# Time: 218 ms
# Memory: 4 KB
for i in range(5):
	m = list(map(int, input().split()))
	if 1 in m:
		r, c = (m.index(1)), (i)
sol = abs(r - 2) + abs(2 - c)
print(sol)
