def item_in_common(list3, list4):
    for i in list3:
        for j in list4:
            if i == j:
                return True
    return False


def item_in_common2(list3, list4):
    my_dict = {}
    for i in list3:
        my_dict[i] = True
    for j in list4:
        if j in my_dict:
            return True
    return False


list1 = [1, 3, 5]
list2 = [2, 4, 6]

print(item_in_common2(list1, list2))
