# Coded by JohnXdator
n = int(input())
i = False
while not i:
  n += 1
  s = str(n)
  e = set(s)
  if len(s) == len(e):
    i = True
print(n)
