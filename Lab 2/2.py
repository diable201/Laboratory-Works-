def even():
    my_list = []
    even_list = []
    print('The number of elements in list:')
    i = int(input())
    print('Append data in list of:')
    for i in range(i):
        data = int(input())
        my_list.append(data)
        if i % 2 == 0:
            even_list.append(data)
    print(f'The list = {even_list}')

    # Better use this:
    # list = [9, 0, 12, 3, 4, 56, 9, 16]
    # res = list[::2] - odd
    # print(res)


even()
