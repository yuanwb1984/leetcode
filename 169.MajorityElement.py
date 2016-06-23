# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:05:57 2016

@author: 06210
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for k in nums:
            if k in d:
                d[k] = d[k] + 1
            else:
                d[k] = 1
        l = len(nums)
        for k in d:
            if d[k] * 2 > l:
                return k