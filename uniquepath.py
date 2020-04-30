#!/usr/bin/env python3
# link : https://leetcode.com/problems/unique-paths/submissions/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create grid with size mxn
        dp = [[0 for rows in range(n)] for cols in range(m)]
        # initial col 0 = 1
        for row in range(m):
            dp[row][0] = 1
        # initial row 0 = 1
        for col in range(n):
            dp[0][col] = 1
        # dynamic programing
        # current value(row,col) = value(row-1,col) + value(row,col-1)
        for row in range(1 , m):
            for col in range(1 , n):
                dp[row][col] = dp[row - 1][col]  + dp[row][col - 1]
        return dp[-1][-1]


a = Solution()
print(a.uniquePaths(7,3))