# Code by JohnXdator
n, m = map(int, input().split())
for i in range(n):
	if i % 2 == 0:
		print('#'*m)
	else:
		print(['#'+'.'*(m-1),'.'*(m-1)+'#'][(i-1) % 4 == 0])
