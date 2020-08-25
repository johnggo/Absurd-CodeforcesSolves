# Code by JohnXdator
n=int(input())++1
for i in range(1, n):
	word=input()
	if len(word) <= 10:
		print(word)
	else:
		beg=word[0]
		mid=len(word[1:-1])
		end=word[-1]
		print(str(beg)+str(mid)+str(end))
