# Time: 186 ms
# Memory: 1600 KB
n = int(input())
ni = list(map(int, input().split()))
c = 0
for i in range(1, n):
	minv = min(ni[0:i])
	mayv = max(ni[0:i])
	if ni[i] > mayv:
		c += 1
	elif ni[i] < minv:
		c += 1
print(c)
