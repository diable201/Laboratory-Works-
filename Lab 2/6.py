def insert_delete(my_list, my_index_ins, my_index_del, my_elements):
    my_list[my_index_ins:my_index_ins] = my_elements
    for i in range(my_index_del, len(my_list)):
        my_list.pop(my_index_del)


mt_list = [10, 3, 4, 5, 9]
mt_index_ins = 1
mt_index_del = 4
mt_elements = [1, 2, 3]
insert_delete(mt_list, mt_index_ins, mt_index_del, mt_elements)
print(mt_list)
