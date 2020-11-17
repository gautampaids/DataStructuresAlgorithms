# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 11:38:50 2020

@author: Gautam_Pai
"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # if len(nums) == 1:
        #     return nums[0]
        # if len(nums) == 0:
        #     return 0
        
        # dict = {i:k for i,k in enumerate(nums)} #first convert into keyvalue pairs
        # max_pair = [(k,v) for k,v in dict.items() if v == max(dict.values())]
        # min_value = min(dict.values())
        
        # sums = []
        # for i,k in max_pair:
        #     sum = k
        #     j = i
            
            
        #     if j == 0:                
        #         j=j+1
        #     elif j == len(nums)-1:                
        #         j=j-1
        #     else:
        #         neighbour = max(dict[j-1],dict[j+1])
        #         if neighbour == dict[j-1]:
        #             j = j-1
        #         else:
        #             j=j+1 
            
        #     if j < i:
        #         while (dict[j] != min_value) & (j != 0):
        #             sum += dict[j]
        #             j = j-1
        #     else:
        #         while (dict[j] != min_value) & (j != len(nums)-1):
        #             sum += dict[j]
        #             j = j+1
            
        #     sums.append(sum)
        # return max(sums)
        max_sum = 0
        sub_max_sum = 0
        
        for i,k in enumerate(nums):
            if sub_max_sum + k >0:
                sub_max_sum +=k
            else:
                sub_max_sum = 0
            if sub_max_sum > max_sum:
                max_sum = sub_max_sum
        if max_sum == 0:
            return max(nums)
        return max_sum
        
sln = Solution()
sln.maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,5])

    