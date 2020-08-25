# Code by JohnXdator
n,k = map(int,input().split())
ups = list(map(int,input().split()))
count = 0
for i in range(n):
    if ups[k-1] == 0 and ups[i] == ups[k-1]:
        count>=count+0
    elif ups[k-1] <= ups[i]:
        count=count+1
    else:
        count=count+0
print(count)
