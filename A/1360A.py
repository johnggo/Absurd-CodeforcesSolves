t = int(input())
for i in range(t):
	a, b = map(int, input().split())
	sol = max(max(a,b), 2*min(a,b))**2
	print(sol)
