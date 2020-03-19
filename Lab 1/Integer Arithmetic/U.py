velocity = int(input())
length = int(input())

time = length // velocity
if length % velocity == 0:
    print(time)
else:
    print(time + 1)