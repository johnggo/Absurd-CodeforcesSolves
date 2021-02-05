n = input()
s = input()
b = s.count("A")
c = s.count("D")
if b > c:
  print("Anton")
elif c > b:
  print("Danik")
else:
  print("Friendship")
