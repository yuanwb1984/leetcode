# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:18:41 2016

@author: 06210
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l =  len(digits)
        digits[l - 1] = digits[l - 1] + 1        
        x = l - 1
        while x >= 0:
            if digits[x] == 10:
                if x == 0:
                    digits[x] = 0
                    digits.insert(0, 1)
                else:
                    digits[x-1] = digits[x-1] + 1
                    digits[x] = 0
            x = x - 1 

        return digits    