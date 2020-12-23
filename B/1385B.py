# Source https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
# Adecuated to the problem by JohnXdator
t = int(input())
for e in range(t):
  n = int(input())
  a = map(int, input().split())
  sol = [] 
  for i in a: 
    if i not in sol: 
        sol.append(i)
  print(*sol, sep=' ')
