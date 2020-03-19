def palindrome(l: list) -> str:

    dict_to_check = dict()

    for i in l:
        if i in dict_to_check:
            dict_to_check[i] += 1
        else:
            dict_to_check[i] = 1
    odds = 0
    for i in dict_to_check.values():
        if i % 2 != 0:
            odds += 1
        if odds > 1:
            return "No"
    return "Yes"


print(palindrome([1, 2, 3, 4, 1]))
print(palindrome([1, 2, 3, 1, 2]))