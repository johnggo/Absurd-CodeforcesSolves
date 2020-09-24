# Code By JohnXdator
for i in range(int(input())):
    n = int(input())
    if n % 4 == 0:
        print('YES')
        print(*range(2, n + 1, 2), end=' ')
        print(*range(1, n - 1, 2), n + (n // 2 - 1))
    else:
        print('NO')
