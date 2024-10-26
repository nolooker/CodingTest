a1,b1 = map(int, input().split())
a2,b2 = map(int, input().split())

if a1 > a2:
    print("A")
elif a1 < a2:
    print("B")
else:
    if b1 > b2:
        print("A")
    else:
        print("B")