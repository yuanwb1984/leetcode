# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:21:16 2016

@author: 06210
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = 1
        if x < 0:
            a = -1
            x = abs(x)
        l = list(str(x))
        l = l[::-1]
        x = ''.join(l)
        z = int(x) * a
        if z >= 2147483651 or z <= -2147483651:
            z = 0
        return z