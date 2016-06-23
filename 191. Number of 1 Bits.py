# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:13:35 2016

@author: 06210
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')