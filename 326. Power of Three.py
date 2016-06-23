# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:14:17 2016

@author: 06210
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        m = 0
        while 3 ** m < n:
            m = m + 1
        return 3 ** m == n