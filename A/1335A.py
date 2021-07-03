# Time: 233 ms
# Memory: 4732 KB	
t = int(input())
for i in range(t):
	n = int(input())
	wp = 0
	a = n - 1
	if a > 0:
		wp = a // 2
	print(wp)
