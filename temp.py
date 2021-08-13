
import array
import random

num = array.array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


def fill_array(num):
    for i in range(len(num)):
        num[i] = random.randint(1, 10)


def print_array(num):
    for i in range(len(num)):
        print(num[i])


def find_sum(num):
    for i in range(len(num)):
        sum =  sum + num[i]
        return sum


def find_min(num):
    min = num[0]
    for i in range(len(num)):
        if num[i] < min:
            min = num[i]
    return min

def find_min_index(num):
    min = num[0]
    index = 0
    for i in range(0, len(num)):
        if num[i] < min:
            min = num[i]
            index = i
    return index


def swap(num, i, j):
    place_holder = num[i]
    num[i] = num[j]
    num[j] = place_holder

def find_min_index_from(num ,start):

    min = num[start]
    index = start
    for i in range(start, len(num)):
        if num[i] < min:
            min = num[i]
            index = i
    return index


# def sort(num):
#     for i in range(0, len(num) - 1):
#         j = find_min_index_from(num, i)
#         swap(num, i, j)


def sort(num):
    for i in range(0, len(num) - 1):
        swap(num, i, find_min_index_from(num, i))


def find_number(n):
    count_num = 0
    for i in range(0, len(num)):
        if num[i] == n:
            count_num += 1
    return count_num






fill_array(num)
print_array(num)
print('---------')
# total = sum(num)
# print(total)
# print("Min")
# print(find_min(num))
# print('Min Index')
# print(find_min_index(num))
# # print("Swap Function:")
# i= input("Enter I:")
# j= input("Enter J: ")
# swap(num, i, j)
# print_array(num)
#
# print(find_index_from(num, 7))
# print('sort')
# sort(num)
# print_array(num)
n = input("Please input a number: ")
print(find_number(n))