# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:14:54 2016

@author: 06210
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n >= 1 and bin(n).count('1') == 1