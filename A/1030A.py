# Time: 109 ms
# Memory: 8 KB
n = int(input())
np = [int(np) for np in input().split()]
sol = 0
for i in np:
	sol += i
if sol > 0:
	print('HARD')
elif sol == 0:
	print('EASY')
