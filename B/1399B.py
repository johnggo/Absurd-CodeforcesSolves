# Code by JohnXdator
t = int(input())
for i in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	x = min(a)
	y = min(b)
	sol = 0
	for s in range(n):
		sol += max(a[s]-x, b[s]-y)
	print(sol)
