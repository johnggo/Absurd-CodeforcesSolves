n = int(input())
x = 0
for i in range(n):
	sign = str(input())
	if sign[0] == '+' or sign[-1] == '+':
		x+=1
	else:
		x-=1
print(x)