a = int(input())
b = int(input())

if a != 0:
    if b % a == 0:
        x = -b//a
        print(x)
    else:
        print("NO")
elif b == 0:
    print("INF")
else:
    print("NO")