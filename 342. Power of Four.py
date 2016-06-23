# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:19:01 2016

@author: 06210
"""

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        bn = bin(num)
        if bn.count('1') != 1 :
            return False
        if (bn.count('0') - 1) % 2 != 0:
            return False
        
        return True