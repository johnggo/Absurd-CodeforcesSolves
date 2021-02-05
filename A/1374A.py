t = int(input())
for i in range(t):
	x, y, n = map(int, input().split())
	sol = n-(n-y)%x
	print(sol)
