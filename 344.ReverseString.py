# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:00:22 2016

@author: 06210
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        for i in range(0, int(len(s)/2)):
            
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]  

        return ''.join(s)
        