# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:20:12 2016

@author: 06210
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        i = 0
        while i < len(nums) :
            if target - nums[i] in dict:
                return [dict[target - nums[i]], i]
            else:
                dict[nums[i]] = i
            i = i + 1
        