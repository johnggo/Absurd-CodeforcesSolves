n, h = map(int, input().split())
ai = map(int, input().split())
mp = 0
for i in ai:
	if i > h:
		mp += 2
	else:
		mp += 1
print(mp)
