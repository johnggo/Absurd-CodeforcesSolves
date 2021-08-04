# Time: 280 ms
# Memory: 23864 KB
t = int(input())
for tst in range(t):
	n = str(input())
	mi = 0
	smnd = []
	for ni in range(len(n)):
		if n[ni] != '0':
			smnd.append(n[ni] + (len(n[ni:-1])*'0'))
			mi += 1
	print(mi)
	print(' '.join(smnd))
