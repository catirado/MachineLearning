import random


def separate_list(inital_list, num):
    list = []
    diff_list = []

    indexs = random.sample(xrange(0, len(inital_list)), num)

    i = 0
    for x in inital_list:
        if i in indexs:
            list.append(x)
        else:
            diff_list.append(x)
        i += 1

    return list, diff_list


def unicode_to_int(list):
    new_list = []
    for x in list:
        if isinstance(x, unicode):
            new_list.append(int(x))
        else:
            new_list.append(x)

    return new_list
