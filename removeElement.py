# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 23:47:14 2020

@author: Gautam_Pai
"""
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #count = 0
        i=0
        
        while i < len(nums):
            if nums[i] == val:                
                x = i
                y = x+1
                while y < len(nums):
                    nums[x] = nums[y]
                    x = y
                    y = y+1
                del nums[-1]
            else:
                i = i+1
        
        return len(nums)
        

sln = Solution()
sln.removeElement(nums=[0,1,2,2,3,0,4,2], val=2)
sln.removeElement(nums=[3,2,2,3],val=3)