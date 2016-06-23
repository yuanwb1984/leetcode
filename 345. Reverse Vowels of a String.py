# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:17:02 2016

@author: 06210
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        p1 = 0
        p2 = len(s)-1
        s = list(s)
        while p1 < p2:
            if s[p1] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                if s[p2] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                    tmp1 = s[p1]
                    tmp2 = s[p2]
                    s[p1] = tmp2
                    s[p2] = tmp1
                    p2 = p2 -1
                    p1 = p1 + 1
                else:
                    p2 = p2 -1
            else:                
                p1 = p1 + 1
        return ''.join(s)