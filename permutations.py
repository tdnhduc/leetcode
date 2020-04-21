#!/usr/bin/python3.8
class Solution:
    def permute(self, nums):
        def backtrack(curr,nums):
            if len(nums) == 0:
                output.append(curr)
            else:
                for i in range(len(nums)):
                    tmp = curr + [nums[i]]
                    backtrack(tmp, nums[:i] + nums[i+1:])
        output = []
        curr = list()
        backtrack(curr,nums)
        return output

                    
a = Solution()
# import pdb;pdb.set_trace()
print(a.permute(nums = [1,2,3]))