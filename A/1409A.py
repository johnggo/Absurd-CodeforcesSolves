# Time: 390 ms
# Memory: 26852 KB
t = int(input())
for i in range(t):
	a, b = map(int, input().split())
	sol = abs(a-b)
	ope = sol - 10*(sol//10)
	# ope >= 1 evaluates to True or False
	# where True is 1 and False 0
	print(sol//10 + (ope >= 1))
