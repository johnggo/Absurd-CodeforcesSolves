n = int(input())
e = 0
s = 0
for i in range(n):
    s =s- eval(input().replace(' ', '-'))
    e = max(e, s)
print(e)
