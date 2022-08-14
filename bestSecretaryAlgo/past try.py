
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

""" 
def test_1(lis, i, check, target):
    while i < 10:
        if check > target:
            print("one loop")
            return test_1(lis, i + 1, check)
    return lis[check]
"""

"""def add_smartness(lis, num):
    if ran_list != []:
        if not test_1_start(lis, num):
            i = 0
            while i < len(lis):
                if i == len(lis) - 1 and :
                    lis.append(num)
                elif num < lis[i]:
                    lis.insert(i, num)
                    print("added " + str(num) + " to position " + str(i))
                    print(ran_list)
                    i = len(lis) + 1
                i += 1
    else:
        lis.append(num)
        print("added " + str(num))
        print(lis)"""

"""def trestr():
    i = 0
    c = 0
    t = None

    while i < 10:
        if arr_tst[c] == arr_tst[len(arr_tst) - 1]:
            return print("done! The last number is: " + str(arr_tst[len(arr_tst) - 1]))
        else:
            if t == c:
                print(arr_tst[c])
                c = (arr_tst[c] + 1 - arr_tst[c]) // 2 + c + 1
                t = c
                print("went left")
                i += 1
            elif t != c:
                print(arr_tst[c])
                c = (arr_tst[c] + 1 - arr_tst[c]) // 2 + c
                t = c
                print("went right")
                i += 1

trestr()"""