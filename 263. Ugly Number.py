# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:15:19 2016

@author: 06210
"""

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l = [2, 3, 5]
        for n in l:
            while num > 1:
                if num % n == 0:
                    num = num / n
                else:
                    break
        return num == 1