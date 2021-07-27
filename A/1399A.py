Time: 186 ms
Memory: 25184 KB
t = int(input())
for l in range(t):
	n = int(input())
	an = list(map(int, input().split()))
	an.sort()
	ma = []
	for r in range(n-1):
		if abs(an[r] - an[r+1]) <= 1:
			ma.append(min(an[r], an[r+1]))
	for d in ma:
		del an[an.index(d)]
	if len(an) == 1:
		print('YES')
	else:
		print('NO')
