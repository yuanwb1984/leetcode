# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:18:10 2016

@author: 06210
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = len(nums) - 1
        while l >= 0:
            if nums[l] == val:
                nums.pop(l)
            l = l - 1
        return len(nums)