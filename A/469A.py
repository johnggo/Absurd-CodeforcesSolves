n = int(input())
x = input().split()[1:]
y = input().split()[1:]
if len(set(x+y)) == n:
  print("I become the guy.")
else:
  print("Oh, my keyboard!")
