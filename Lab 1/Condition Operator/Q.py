a = int(input())

if 10 < a % 100 < 15:
    print(a, 'korov')
elif a % 10 == 1:
    print(a, 'korova')
elif 2 <= a % 10 <= 4:
    print(a, 'korovy')
else:
    print(a, 'korov')