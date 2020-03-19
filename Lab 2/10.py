def neighbor(my_set):
	new_set = set()
	for i in my_set:
		new_set.add(i - 1)
		new_set.add(i + 1)
	print(new_set)


numbers = list(map(int, input().split()))
mt_set = set(numbers)
neighbor(mt_set)