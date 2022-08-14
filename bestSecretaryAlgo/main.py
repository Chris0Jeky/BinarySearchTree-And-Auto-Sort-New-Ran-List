import time
import random

print(time.perf_counter())

name = []
name1 = []

ran_list = []


def add_to_list():
    time1 = time.perf_counter()
    i = 0
    while i < 200000:
        name.append(i)
        i += random.randint(1, 10)
    time2 = time.perf_counter()
    print("total time spent: " + str(time2 - time1))


def add_to_list1():
    time1 = time.perf_counter()
    i = 0
    while i < 10:
        name1.append(i)
        i += 1
    time2 = time.perf_counter()
    print("total time spent: " + str(time2 - time1))


def add_smartness(lis, num):
    i = 0
    if len(lis) == 0:
        lis.append(num)
        return
    if not test_1_start(lis, num):
        while i < len(lis):
            if num < lis[i]:
                lis.insert(i, num)
                return
            elif num > lis[i]:
                if i == len(lis) - 1:
                    lis.append(num)
                    return
                else:
                    i += 1


def start_smartness_with_random(lis, bigness, m_len):
    if m_len > bigness:
        print("List Name, Max value of number number, max length of the list")
        print("Please enter a Bigness higher than m_len (first value higher than the second")
    else:
        while len(lis) < m_len:
            ran_num = random.randint(0, bigness)
            add_smartness(lis, ran_num)


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


def test_1_start(lis, to_find):
    max_len = len(lis)
    min_len = 0
    check = (max_len - min_len) // 2
    return test_1(lis, 0, check, min_len, max_len, to_find)


def test_1(lis, i, check, min_len, max_len, to_find):
    while i < 23:
        chk = check + min_len
        if to_find == lis[chk]:
            return True
        elif to_find > lis[chk]:
            if (max_len - min_len) // 2 == 0:
                return False
            else:
                min_len = min_len + check
                check = (max_len - min_len) // 2
                return test_1(lis, i + 1, check, min_len, max_len, to_find)
        elif to_find < lis[chk]:
            max_len = max_len - check
            check = (max_len - min_len) // 2
            return test_1(lis, i + 1, check, min_len, max_len, to_find)
    return False


def find_rand_in_array(lis):
    to_find_array_pos = random.randint(0, len(lis))
    print(str(to_find_array_pos))
    to_find = lis[to_find_array_pos]
    print(str(to_find))
    test_1_start(lis, to_find)


"""print(name1)
add_to_list1()
print(name1)
test_1_start(name1, 9)
print(name1)"""

# find_rand_in_array(name)
start_smartness_with_random(ran_list, 500, 15)
find_rand_in_array(ran_list)
print(ran_list)

# arr_tst = [1, 2, 3, 4]
