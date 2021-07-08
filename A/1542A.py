# Time: 108 ms
# Memory: 1480 KB
t = int(input())
for i in range(t):
	n = int(input())
	ai = list(map(int, input().split()))
	s = 0
 	for x in ai:
		s += x % 2
	if s == n:
		print('Yes')
	else:
		print('No')
