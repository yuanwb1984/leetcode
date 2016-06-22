# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 12:44:47 2016
一行代码看不懂
@author: 06210
"""
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        if n < 5:
            return 0
        else:
            sum = n//5
            sum = sum + self.trailingZeroes(n//5)
        return(sum)


n = Solution()
print(n.trailingZeroes(126))