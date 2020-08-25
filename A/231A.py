# Code by JohnXdator
n=int(input())
count = 0
while(n>0):
	n-=1
	de = input()
	if de.count('1') >= 2:
		count+=1
print(count)
