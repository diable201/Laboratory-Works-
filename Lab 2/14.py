def more(my_list, number):
    new_list = []
    for i in range(0, len(my_list)):
        if my_list[i] > number:
            new_list.append(my_list[i])
    print(new_list)
    

mt_list = [11, 2, 44, 23]
mt_number = 10
more(mt_list, mt_number)
