# Time: 265 ms
# Memory: 5100 KB
t = int(input())
for i in range(t):
	a, b = map(int, input().split())
	if a % b == 0:
		print(0)
	else:
		print(((a + b) - (a % b)) - a)
