# Time: 93 ms
# Memory: 12 KB
n = int(input())
apy = list(map(int, input().split()))
apx = list(map(int, input().split()))
apset = set(apy[1:] + apx[1:])
# n*(n+1)//2 is 1 + 2 + 3... n
# https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
if sum(apset) == n*(n+1)//2:
	print('I become the guy.')
else:
	print('Oh, my keyboard!')
