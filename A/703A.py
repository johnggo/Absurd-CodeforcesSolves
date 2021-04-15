n = int(input())
mi = 0
ci = 0
for i in range(n):
	m, c = map(int, input().split())
	if m > c:
		mi += 1
	elif c > m:
		ci += 1
if mi > ci:
	print('Mishka')
elif ci > mi:
	print('Chris')
else:
	print('Friendship is magic!^^')
