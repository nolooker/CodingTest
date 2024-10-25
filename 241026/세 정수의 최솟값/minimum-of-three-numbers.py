a,b,c = map(int, input().split())

x = a if a < b else b

y = b if b < c else c

if x < y:
    print(x)
else:
    print(y)