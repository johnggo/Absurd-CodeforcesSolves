# Code by JohnXdator
n = int(input())
s=list(map(int,input().split()))
c=0
for i in range(1,n):
    if (s[i]>max(s[0:i])) or (s[i] < min(s[0:i])):
        c=c+1
print(c)
