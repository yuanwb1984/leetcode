# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 13:52:17 2016
@author: 06210
"""
import math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        elif x < 0:
            return False
        l = int(math.log10(x))
        if l == 0:
            return True
        sum = 0
        i = 1
        y = x
        while i <= (l+1):
            tmp = x % 10
            sum = sum + tmp * (10**((l+1)-i))
            x = x // 10
            i = i + 1
        if sum == y:
            return True
        return False


            
n = Solution()
print(n.isPalindrome(12321))