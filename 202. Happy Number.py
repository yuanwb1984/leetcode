# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:16:22 2016

@author: 06210
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        pool = set()        
        while n != 1:
            m = list(str(n))
            n = 0
            for x in m:
                n = n + int(x) ** 2
            if n == 1:
                return True
            elif n in pool:
                return False
            else:
                pool.add(n)
        return True