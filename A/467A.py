# Coded by JohnXdator
s = int(input())
print(sum(eval(input().replace(' ','-')) < -1 for i in range(s)))
