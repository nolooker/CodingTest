c, n = input().split()

c = str(c)
n = int(n)

if c == 'A':
    for i in range(n):
        print(i+1, end=' ')
elif c == 'D':
    for i in range(n):
        print(n, end=' ')
        n -= 1