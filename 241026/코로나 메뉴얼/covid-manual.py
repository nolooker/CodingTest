a1, a2 = input().split()
b1, b2 = input().split()
c1, c2 = input().split()

a2 = int(a2)
b2 = int(b2)
c2 = int(c2)

count = 0

if a1 == "Y" and a2 >= 37:
    count += 1

if b1 == "Y" and b2 >= 37:
    count += 1

if c1 == "Y" and c2 >= 37:
    count += 1

if count >= 2:
    print("E")
else:
    print("N")