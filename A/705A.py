# Time: 93 ms
# Memory: 12 KB
n = int(input())
flst = ["I hate", "I love"] * n
clst = [" that"] * n
for i in range(n):
	if i == n - 1:
		clst[i] = " it"
	sol = flst[i] + clst[i]
	print(sol, end = " ")
