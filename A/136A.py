n = int(input())
lst = list(map(int, input().split()))
sol = [0] * n
for i in range(n):
	sol[lst[i] - 1] = i + 1
print(" ".join(map(str, sol)))
