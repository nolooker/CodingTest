a, b = map(int, input().split())

if a >= 90:
    x = 1
else:
    x = 0

if x == 1:
    if b >= 95:
        print(100000)
    elif 95 > b >= 90:
        print(50000)
    else:
        print(0)
else:
    print(0)