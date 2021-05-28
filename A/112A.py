# Time: 186 ms
# Memory: 20 KB
n = input().lower()
s = input().lower()
if n == s:
	print(0)
elif n > s:
	print(1)
else:
	print(-1)	
