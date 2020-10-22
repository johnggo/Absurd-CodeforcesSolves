# Code by JohnXdator
n = int(input())
s = list(map(int, input().split()))
sol = n*max(s)-sum(s)
print(sol)
