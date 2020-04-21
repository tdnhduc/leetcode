#!/usr/bin/env python3.8

def compare(list1, list2):
    print("List1 compare: ", list1)
    print("List2 compare: ", list2)
    for i in list1:
        if i not in list2:
            return False
    return True

def check_repeating(nums):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if compare(nums[i], nums[j]):
                del nums[i]
                print("Nums after delete: ", nums)
    return nums


def threesum(nums):
    result = []
    len_nums = len(nums)
    for i in range(len_nums - 1):
        for j in range(i + 1, len_nums):
            if -(nums[i] + nums[j]) in nums[j + 1 : ]:
                result.append([nums[i], nums[j], -(nums[i] + nums[j])])
                continue
    print(result)
    return check_repeating(result)

a = threesum([0,0,0,0])
print(a)