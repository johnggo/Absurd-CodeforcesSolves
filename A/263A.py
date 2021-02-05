for i in range(5):
	mat = list(map(int,input().split()))
	if 1 in mat:
		r,l = (i, mat.index(1))
		
print(abs(2-r) + abs(2-l))
