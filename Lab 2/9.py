def mutable(my_tuple):
	islist = False
	for i in range(len(my_tuple)):
		if isinstance(my_tuple[i], list) in my_tuple:
			islist = True
			return True
	return islist
        	

mt_tuple = ((5, 2.5, 8, 4, 'Hi', -5, True, 6))
print(mutable(mt_tuple))