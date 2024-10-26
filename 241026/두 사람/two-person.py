a1,b1 = map(str, input().split())
a2,b2 = map(str, input().split())

a1 = int(a1)
a2 = int(a2)

if a1 >= 19 or a2 >= 19:
    if b1 == "M" or b2 == "M":
        print(1)
    else:
        print(0)
else:
    print(0)