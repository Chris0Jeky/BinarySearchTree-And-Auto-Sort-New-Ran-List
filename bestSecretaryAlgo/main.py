import time
import random

print(time.perf_counter())

arr1 = []
arr2 = []

ran_list = []

# Add 10 random numbers to arr1

def add_to_arr1():
    time1 = time.perf_counter()
    i = 0
    while i < 200000:
        arr1.append(i)
        i += random.randint(1, 10)
    time2 = time.perf_counter()
    print("total time spent: " + str(time2 - time1))


# add numbers: 0 to 9 to arr2

def add_to_arr2():
    time1 = time.perf_counter()
    i = 0
    while i < 10:
        arr2.append(i)
        i += 1
    time2 = time.perf_counter()
    print("total time spent: " + str(time2 - time1))

# add_origin_number_to_arr takes in 2 parameters: an array and a number
# it checks whether the array contains the number using the binary search function binary_search_start
# if the number is not contained in the array, it'll be added
# the first if checks whether the array is empty, and if it is, it won't use the binary search function
# before the number is added, it'll find the index to be added to so that the result will be a sorted array

def add_origin_number_to_arr(lis, num):
    i = 0
    if len(lis) == 0:
        lis.append(num)
        return
    if not binary_search_start(lis, num):
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

# it calls add_origin_number_to_arr passing as arguments an array and the maximum value of the random number that will
# be generated; it takes as parameter the size of the array that will be generated
# it'll check whether the size of the array is large enough to contain every random integer that will be generated
# then it will generate random numbers, given the specifications, as long as there is space in the array
# then it will call add_origin_number_to_arr, which will add or discard the randomly generated number

def start_add_origin_with_random(lis, bigness, m_len):
    if m_len > bigness:
        print("List arr1, Max value of number number, max length of the list")
        print("Please enter a Bigness higher than m_len (first value higher than the second")
    else:
        while len(lis) < m_len:
            ran_num = random.randint(0, bigness)
            add_origin_number_to_arr(lis, ran_num)

# search_for_loop is a simple linear search given a number and an array

def search_for_loop(element, lis):
    for i in range(len(lis)):
        if element == lis[i]:
            return i

# find_index_of_element simply returns the index of a number in an array given a number and an array

def find_index_of_element(element, lis):
    time1 = time.perf_counter()
    result = search_for_loop(element, lis)
    time2 = time.perf_counter()
    print("total time spent: " + str(time2 - time1))
    return result


def print_results(element, lis, pref_method):
    if pref_method == 0:
        print("the number " + str(element) + " is present at index No. :" + str(find_index_of_element(element, lis)))

# binary_search_start will set the max_len

def binary_search_start(lis, to_find):
    max_len = len(lis)
    min_len = 0
    check = (max_len - min_len) // 2
    return binary_search(lis, 0, check, min_len, max_len, to_find)


def binary_search(lis, i, check, min_len, max_len, to_find):
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
                return binary_search(lis, i + 1, check, min_len, max_len, to_find)
        elif to_find < lis[chk]:
            max_len = max_len - check
            check = (max_len - min_len) // 2
            return binary_search(lis, i + 1, check, min_len, max_len, to_find)
    return False


def find_rand_in_array(lis):
    to_find_array_pos = random.randint(0, len(lis) - 1)
    print(str(to_find_array_pos))
    to_find = lis[to_find_array_pos]
    print(str(to_find))
    binary_search_start(lis, to_find)


print(arr2)
add_to_arr2()
print(arr2)
binary_search_start(arr2, 9)
print(arr2)

# find_rand_in_array(arr1)
start_add_origin_with_random(ran_list, 500, 15)
find_rand_in_array(ran_list)
print(ran_list)


# arr_tst = [1, 2, 3, 4]
