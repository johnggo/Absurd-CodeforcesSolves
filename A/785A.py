# Code by JohnXdator
a = {'T':4, 'C':6, 'O':8, 'D':12, 'I':20}
n = int(input())
s = 0
for i in range(n):
  b = input()
  s += a[b[0]]
print(s)
