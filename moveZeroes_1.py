# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 08:50:52 2020

@author: Gautam_Pai
"""
from typing import List

class Solution:
    def moveZeroes(self, nums:List[int]) -> None:
        explorer = 0
        anchor = 0
        
        for explorer in range(len(nums)):
            if nums[explorer] != 0:
                nums[explorer], nums[anchor] = nums[anchor], nums[explorer]
                anchor += 1
            else:
                explorer += 1
        
        return nums

sln = Solution()
sln.moveZeroes([0,1,0,3,12])