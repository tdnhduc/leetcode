#!/usr/bin/env python3
# link : https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # hmaps dung cho viec luu tru lai index cua phan tu 
        hmaps = {}

        for i, num in enumerate(nums):
            # neu number trong da co trong hmaps va index hien tai  - index cu <= k
            # return true
            # roi cap nhat lai index cua number hien tai
            if num in hmaps and i - hmaps[num] <= k:
                return True
            hmaps[num] = i
        return False
        

a = Solution()
print(a.containsNearbyDuplicate([1,2,3,1,2,3],2))