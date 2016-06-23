# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:05:11 2016

@author: 06210
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if set(s) != set(t):
            return False
            
        if len(s) != len(t):
            return False
            
        s = list(s)
        t = list(t)            
        s.sort()
        t.sort()
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True