# Time: 93 ms
# Memory: 20 KB
no = str(input())
noi = str(input())
sol = ''
for i in range(len(no)):
	if no[i] != noi[i]:
		sol += '1'
	else:
		sol += '0'
print(sol)
