# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 09:07:36 2020

@author: Gautam_Pai
"""
from typing import List

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        if len(releaseTimes) != len(keysPressed):
            print("Invalid input combination")
        
        dict1 = dict()
        dict1[keysPressed[0]] = releaseTimes[0]
        for i in range(1, len(keysPressed)):
            if keysPressed[i] in dict1.keys(): 
                keyreleasetime = releaseTimes[i]-releaseTimes[i-1]
                dict1[keysPressed[i]] = max(keyreleasetime, dict1[keysPressed[i]])
            else:
                dict1[keysPressed[i]] = releaseTimes[i]-releaseTimes[i-1]
        
        
        k = [k for k,v in dict1.items() if v == max(dict1.values())]
        
                
        return max(k)
    
sln = Solution()
sln.slowestKey(releaseTimes=[19,22,28,29,66,81,93,97], keysPressed="fnfaaxha")