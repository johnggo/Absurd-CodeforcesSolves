n = int(input())
print(n//2)
sol = ""
while n > 3:
	sol += "2 " 
	n -= 2
print(sol+str(n))
