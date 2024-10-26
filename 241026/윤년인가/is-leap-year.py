y = int(input())

x = "true"
z = "false"
res = ""

if y % 4 == 0:
    if y % 100 == 0 and y % 400 == 0:
        res = z
    else:
        res = x
else:
    res = z

print(res)