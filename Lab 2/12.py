def power():
	listOfElems = [1, 2, 2, 3, 4]
	for elem in listOfElems:
		if listOfElems.count(elem) > 1:
			listOfElems[elem] = listOfElems[elem] ** 2
	print(listOfElems)


power()