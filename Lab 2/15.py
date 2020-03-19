def func():
    a = [0, 3, 11, 2, 44, 23, 4]
    tmp = 0
    for i in range(len(a)):
        if a[i] % 2 != 0 and i % 2 == 0:
            tmp += 1
    print(tmp)


func()
