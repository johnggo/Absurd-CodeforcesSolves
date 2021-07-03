# Time: 216 ms
# Memory: 16 KB
n = int(input())
chi, cai = [], []
ccount = 0
for i in range(n):
	hi, ai = map(int, input().split())
	chi.append(hi)
	cai.append(ai)
for e in chi:
	ccount += cai.count(e)
print(ccount)
