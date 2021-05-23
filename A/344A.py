# This code exceeds time limit, but is correct.
# I tried different implementations, with same result:
# Time limit exceeded on test 7
n = int(input())
mpl = ""
mpcount = 0
for i in range(n):
	mp = str(input())
	if mp != mpl:
		mpcount += 1
	mpl = mp
print(mpcount)
