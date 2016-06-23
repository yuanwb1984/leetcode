# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:16:46 2016

@author: 06210
"""

# -*- coding: utf-8 -*-
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 0, 1
        c = 0
        while c < n:
            c = c + 1
            a, b = b, a + b
        return b
