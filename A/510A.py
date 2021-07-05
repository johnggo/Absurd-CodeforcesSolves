# Time: 124 ms
# Memory: 12 KB
n, m = map(int, input().split())
s = '.'*(m-1) + '#'
for i in range(1, n + 1):
	np = (-1) ** (i)
	if i % 2 != 0:
		print('#'*m)
	else:
		if i % 4 != 0:
			print(s)
		else:
			print(s[::-1])
