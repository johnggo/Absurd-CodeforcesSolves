# Code by JohnXdator
# Using Euclid's algorithm: https://en.wikipedia.org/wiki/Euclidean_algorithm
t = int(input())
for i in range(t):
	b = int(input())
	a = b // 2
	if b == 0:
		gcd = 0
	else:
		gcd = a % b
	print(gcd)
