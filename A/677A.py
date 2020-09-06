# Coded by JohnXdator
n,t = map(int, input().split())
print(n + sum(i > t for i in map(int,input().split())))
