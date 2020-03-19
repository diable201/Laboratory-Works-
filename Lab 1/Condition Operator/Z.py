kotlets = int(input())
minutes = int(input())
number = int(input())

if number <= kotlets:
    t = minutes * 2
elif number * 2 % kotlets == 0:
    t = (minutes * (number * 2 // kotlets))
elif number * 2 % kotlets != 0:
    t = minutes * ((number * 2 // kotlets) + 1)
print(t)