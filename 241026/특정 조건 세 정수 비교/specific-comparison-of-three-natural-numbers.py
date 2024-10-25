a,b,c = map(int, input().split())

x = 1
y = 0

if b % a == 0 and c % a == 0:
    res1 = x
else:
    res1 = y

if a == b and a == c:
    res2 = x
else:
    res2 = y

print(res1,res2)