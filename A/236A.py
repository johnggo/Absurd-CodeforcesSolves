n = str(input())
d = ''.join(set(n))
l = len(d)
if l % 2 == 0:
	print("CHAT WITH HER!")
else:
	print("IGNORE HIM!")
