# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:00:19 2016

@author: 06210
"""

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4 != 0