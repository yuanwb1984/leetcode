# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:17:52 2016

@author: 06210
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
        nj1 = 0
        nj2 = 0
        for i in nums:
            nj2 = nj1
            nj1 = n        
            n = max(nj2 + i, nj1)
        return n