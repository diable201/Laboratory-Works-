import math

number = int(input())
div = 1
i = 2
while i <= math.sqrt(number):
	if number % i == 0:
		div = i
		break
	i += 1
if div == 1:
	print(number)
else:
	print(div)