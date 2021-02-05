n = int(input())
a = []
b = []
s = 0
for i in range(n):
	h, e = map(int,input().split())
	a.append(h)
	b.append(e)	
for i in a:
	s += b.count(i)
print(s)
