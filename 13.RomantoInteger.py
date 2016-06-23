# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:11:12 2016

@author: 06210
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        lr = 0
        R = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        romans = list(s[::-1])
        for roman in romans:
            if lr > R[roman]:
                i = i - R[roman]
            else:
                i = i + R[roman]
                lr = R[roman]
        return i