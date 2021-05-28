# Time: 216 ms
# Memory: 20 KB
n = str(input())
sol = 0
for i in range(len(n)):
	if n[i] == '4' or n[i] == '7':
		sol += 1
if sol == 4 or sol == 7:
	print('YES')
else:
	print('NO')
