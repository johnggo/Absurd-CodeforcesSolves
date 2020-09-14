# Code by JohnXdator
t = int(input())
for x in range(t):
	n = input()
	sol = []
	for i in range(len(n)):
		if n[i] != '0':
			sol.append(n[i] + '0' * (len(n)-i-1))
	print(len(sol))
	print(*sol)
