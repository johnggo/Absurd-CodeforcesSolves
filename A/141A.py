# Time: 310 ms
# Memory: 12 KB
inv = str(input())
anf = str(input())
sor = str(input())
if sorted(inv + anf) == sorted(sor):
	print('YES')
else:
	print('NO')
