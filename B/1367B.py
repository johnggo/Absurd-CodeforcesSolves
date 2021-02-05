t = int(input())
for j in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	sol = 0
	al = 0
	for i in range(n):
		if i%2 != a[i]%2:
			if i%2 == 0:
				sol += 1
			else:
				al += 1
	if sol != al:
		print(-1) 
	else:
		print(sol)
