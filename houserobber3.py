# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:13:21 2020

@author: Gautam_Pai
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rob(self, root:TreeNode) -> int:
        
        def solve(node):
            if node is None:
                return (0,0)
            
            left = solve(node.left)
            right = solve(node.right)
            
            #return (max(left) + max(right), left[0]+right[0]+node.val)
            return (max(left) + max(right), left[0] + right[0] + node.val)
        
        return max(solve(root))

#[3,4,5,1,3,null,1]
tn = TreeNode(3)
tn.left = TreeNode(4)
tn.right = TreeNode(5)
tn.left.left = TreeNode(6)
tn.left.right = TreeNode(3)
tn.right.right = TreeNode(4)
tn.right.left = TreeNode(2)

  
sln = Solution()
sln.rob(tn)






