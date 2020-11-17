# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 00:27:28 2020

@author: Gautam_Pai
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        found = False
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                found = True
                break
        return found

sln = Solution()
sln.containsDuplicate([1,2,3,1])