# Time: 92 ms
# Memory: 12 KB
n, m = map(int, input().split())
for i in range(1, n + 1):
	np = (-1) ** (i)
	if i % 2 != 0:
		print('#'*m)
	else:
		if i % 4 != 0:
			print('.'*(m-1) + '#')
		else:
			print('#' + '.'*(m-1))
