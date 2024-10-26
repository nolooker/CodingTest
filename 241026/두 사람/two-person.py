a1,b1 = input().split()
a2,b2 = input().split()

a1 = int(a1)
a2 = int(a2)

result = 0

if a1 >= 19 and b1 == "M" and a2 >= 19 and b2 =="M":
    result = 1
elif a1 >= 19 and b1 == "M":
    result = 1
elif a2 >= 19 and b2 == "M":
    result = 1
else:
    result = 0

print(result)