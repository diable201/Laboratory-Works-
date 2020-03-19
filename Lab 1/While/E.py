def log(n):
    k = 0
    while n > 1:
        k += 1
        n = (n + 1) // 2
    return k

n = int(input())
print(log(n))
		   # n k
# for n = 7: 4 1
		   # 2 2
		   # 1 3