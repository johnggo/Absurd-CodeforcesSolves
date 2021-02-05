n = int(input())
a,b = 0, 0
s = map(int, input().split())
for i in s:
	a += i
	if a<0:
		b += 1
		a = 0
print(b)
