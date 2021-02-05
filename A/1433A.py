t = int(input())
for i in range(t):
	x = input()
	num = x[0]
	l = len(x)
	sol = (int(num)-1)*10+(l*(l+1))//2
	print(sol)
