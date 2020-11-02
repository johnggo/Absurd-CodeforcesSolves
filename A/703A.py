# Code by JohnXdator
n = int(input())
m = 0
c = 0
for t in range(n):
  mi, ci = list(map(int, input().split()))
  m += mi > ci
  c += ci > mi 
if m > c:
  print("Mishka")
elif c > m:
  print("Chris")
else:
  print("Friendship is magic!^^")
