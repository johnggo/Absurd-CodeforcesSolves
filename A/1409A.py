#Code by JohnXdator
t = int(input())
for i in range(t):
  a,b = map(int, input().split())
  print((abs(a-b)+9)//10)