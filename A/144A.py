# Time: 280 ms
# Memory: 16 KB
n = int(input())
num = list(map(int, input().split()))
maxi = max(num)
mini = min(num)
sol = num.index(maxi) + num[::-1].index(mini)
print(sol - (sol >= n)) # In case that sol >= n, sol gotta be decreased by True i. e. 1
