# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 09:08:16 2020

@author: Gautam_Pai
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > k:
            nums[:] = nums[-k:]+nums[:-k]
        elif len(nums) < k:
            nums[:] = nums[-(k-len(nums)):] + nums[:-(k-len(nums))]
            

sln = Solution()
numbers = [1,2]
sln.rotate(numbers,k=3)