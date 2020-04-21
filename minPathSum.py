#!/usr/bin/env python3.8
class Solution:
    def print(self, grid):
        for i in grid:
            print(i)
        print("\n \n")
    def minPathSum(self, grid):

        def is_valid (x,y, rows, cols):
            if x < 0 or x >= rows:
                return False
            if y < 0 or y >= cols:
                return False
            return True
        
        
        rows = len(grid)
        cols = len(grid[0])
        for row in range(1, rows):
            for col in range(1 , cols):

                xLeft = row ; yLeft = col - 1; vLeft = -1
                xAbove = row - 1 ; yAbove = col; vAbove = -1
                # Get min of left and above of current position
                if is_valid(xLeft, yLeft, rows, cols):
                    vLeft = grid[xLeft][yLeft]
                if is_valid(xAbove, yAbove, rows, cols):
                    vAbove = grid[xAbove][yAbove]
                if vAbove != -1 and vLeft != -1:
                    grid[row][col] += min(vAbove, vLeft)
                elif vAbove != -1:
                    grid[row][col] += vAbove
                elif vLeft != -1:
                    grid[row][col] += vLeft
                else:
                    continue
                self.print(grid)
        return grid[rows - 1][cols - 1]

a = Solution()
print(a.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
            
        
        
        

                    
                    
                    
                
            
        