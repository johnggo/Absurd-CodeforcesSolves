t = int(input())
for i in range(t):
	a, b = map(int, input().split())
	sol = 0
	if a == b:
		sol = 0
	elif a > b and (a - b)%2 == 0 or a < b and (b - a)%2 != 0:
		sol = 1
	else:
		sol = 2
	print(sol)
