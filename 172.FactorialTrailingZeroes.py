# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 12:44:47 2016
累加5**n的个数
@author: 06210
"""
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 5:
            return 0
        sum = 0
        i = 1
        m = 1
        while m != 0:
           m = (n // (5 ** i))
           sum = sum + m
           i = i + 1
        return(sum)
n = Solution()
print(n.trailingZeroes(25))