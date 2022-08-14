import time

print(time.perf_counter())

name = []


def add_to_list():
    time1 = time.perf_counter()
    i = 0
    while i < 50000:
        name.append(i)
        i += 1
    time2 = time.perf_counter()
    print("total time spent: " + str(time2 - time1))


add_to_list()


def search_for_loop(element, lis):
    for i in range(len(lis)):
        if element == lis[i]:
            return i


def find_index_of_element(element, lis):
    time1 = time.perf_counter()
    result = search_for_loop(element, lis)
    time2 = time.perf_counter()
    print("total time spent: " + str(time2 - time1))
    return result


def print_results(element, lis, pref_method):
    if pref_method == 0:
        print("the number " + str(element) + " is present at index No. :" + str(find_index_of_element(element, lis)))


"""    elif pref_method == 1:
        print("the number " + str(element) + " is present at index No. :" + str(initialize_binary(element, lis)))


def initialize_binary(element, lis):
    min_len = 0
    max_len = len(lis)
    return binary_search(element, lis, min_len, max_len)


def binary_search(element, lis, min_len, max_len):
    check = (max_len - min_len) // 2
    if element == lis[check]:
        return check
    elif element > lis[check]:
        return binary_search(element=element, lis=lis, min_len=check, max_len=max_len)
    elif element < lis[check]:
        return binary_search(element=element, lis=lis, min_len=min_len, max_len=check)


print_results(1000, name, 1)
"""


def test_1_start():
    max_len = len(name)
    min_len = 0
    check = (max_len - min_len) // 2
    return test_1(name, 0, check, min_len, max_len, 49000)


def test_1(lis, i, check, min_len, max_len, to_find):
    while i < 25:
        print(str(max_len) + " " + str(min_len))
        chk = check + min_len
        print(str(chk))
        if to_find == name[chk]:
            print("Found! " + str(name[chk]) + ", it took: " + str(i) + " attempts")
            i = 25
        elif to_find > name[chk]:
            min_len = min_len + check
            check = (max_len - min_len) // 2
            return test_1(lis, i + 1, check, min_len, max_len, to_find)
        elif to_find < name[chk]:
            max_len = max_len - check
            check = (max_len - min_len) // 2
            return test_1(lis, i + 1, check, min_len, max_len, to_find)

print(test_1_start())

"""def test_1(lis, i, check, target):
    while i < 10:
        if check > target:
            print("one loop")
            return test_1(lis, i + 1, check)
    return lis[check]
"""
