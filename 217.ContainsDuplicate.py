# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:06:44 2016

@author: 06210
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == []:
            return False
        d = {}
        for k in nums:
            if k in d:
                d[k] = d[k] +1
            else:
                d[k] = 1
        for key in d:
            if d[key] > 1:
                return True
        return False