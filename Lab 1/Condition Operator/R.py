N = int(input())
M = int(input())
x = int(input())
y = int(input())
my_max = max(N, M)
my_min = min(N, M)
N = my_max - y
M = my_min - x
print(min(x,y,M,N))