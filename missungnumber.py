#!/usr/bin/env python3
# link : https://leetcode.com/problems/missing-number/solution/


class Solution:
    # Dung de XOR bit
    @staticmethod
    def missingNumber(nums):
        missing = len(nums)
        print(f"nums : {nums}")
        for i, num in enumerate(nums):
            print(f"i: {bin(i)}")
            print(f"i : {bin(num)}")
            missing ^= i ^ num
            print(f"After XOR: {bin(missing)}\n")
        print(f'Final bin(missing) is: {bin(missing)}')
        return missing



class Solution:
    # Cong thuc sum = n(n+1)/2
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        sum_expect = length*(length + 1)/2
        sum_reality = 0
        for num in nums:
            sum_reality += num
        return int(sum_expect - sum_reality)

result = Solution.missingNumber([1,2,5,3,0])