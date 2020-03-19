def IsPointInSquare(x, y):
    if abs(x) + abs(y) <= 1:
    	return True
    else:
    	return False

a = float(input())
b = float(input())
if IsPointInSquare(a, b):
    print('YES')
else:
    print('NO')