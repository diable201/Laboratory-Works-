def delete(my_list, my_index):
    for i in range(my_index, len(my_list)):
        my_list.pop(my_index)


mt_list = [10, 3, 4, 5, 9]
mt_index = 1
delete(mt_list, mt_index)
print(mt_list)
