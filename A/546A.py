k,n,w = map(int, input().split())
c = 0
for i in range(1, w+1):
	c = c + i * k
b = c - n 
if b <= 0:
	b = 0
print(b)
