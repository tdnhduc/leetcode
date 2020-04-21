#!/usr/bin/env python3.8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        prev = [TreeNode]
        result = []
        curr = root
        while(True):
            if curr is None:
                if len(prev) > 0:
                    if prev[-1].right is not None:
                        prev.appen(prev[-1].right)
                        curr
            else:
                prev.append(curr)
                result.append(curr.val)
                curr = curr.left
        return result

a = TreeNode(1)
b = None
c = TreeNode(2)
d = TreeNode(3)
a.left = b
a.right = c
a.right.right = d

result = Solution()
import pdb;pdb.set_trace()
print(result.preorderTraversal(a))