# Time: 93 ms
# Memory: 12 KB
n = int(input())
sol = n//100 + n%100 // 20 + n%20 // 10 + n%10 // 5 + n%5
print(sol)
