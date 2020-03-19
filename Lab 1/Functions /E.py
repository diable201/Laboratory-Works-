def IsPointInCircle(x, y, xc, yc, r):
    if abs(x - xc)*abs(x - xc) + abs(y - yc)*abs(y - yc) <= r*r:
    	return True
    else:
    	return False

x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if IsPointInCircle(x, y, xc, yc, r):
	print('YES')
else:
	print('NO')