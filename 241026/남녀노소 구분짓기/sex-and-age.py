a = int(input())
b = int(input())

m = "남자"
w = "여자"

if b >= 19:
    p = "성인"
    if a == 0:
        print("MAN")
    else:
        print("WOMAN")
else:
    p = "미성년"
    if a == 0:
        print("BOY")
    else:
        print("GIRL")