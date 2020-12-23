# Code by JohnXdator
w = str(input()).lower()
sol = ''.join('.' + r for r in w if r not in 'aoyeui')
print(sol)
