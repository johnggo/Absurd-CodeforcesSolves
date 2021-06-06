# Time: 171 ms
# Memory: 20 KB
n = int(input())
s = str(input())
if len(set(s.lower())) == 26:
	print('YES')
else:
	print('NO')
