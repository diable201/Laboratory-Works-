def square(my_list, my_index):
    for i in range(my_index, len(my_list)):
        my_list[i] = my_list[i] * my_list[i]


mt_list = [10, 3, 4, 5, 9]
mt_index = 2
square(mt_list, mt_index)
print(mt_list)
