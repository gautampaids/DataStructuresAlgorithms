# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 23:13:22 2020

@author: Gautam_Pai
"""
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        i=0
        while i<len(nums)-count:
            if nums[i]==0:               
                count+=1 
                x = i
                y = x+1
                while y <= len(nums) - count:
                    nums[x] = nums[y]
                    x = y
                    y = y+1
                
                nums[len(nums) - count] = 0
            else:
                i = i+1           
        
        print(nums)
                

sln = Solution()
sln.moveZeroes([0,1,0,3,12])