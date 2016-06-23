# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:03:48 2016

@author: 06210
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a = len(nums) - 1        
        b = len(nums)
        c = 0
        while c <= a:
            if nums[c] == 0:
               nums.pop(c)
               a = a - 1
               c = c - 1
            c = c + 1
        d = len(nums)
        e = b - d 
        for f in range(e):
            nums.append(0)       
#        return nums    