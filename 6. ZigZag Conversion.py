# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:20:04 2016

@author: 06210
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
            
        r = []
        for x in range(numRows):
            r.append([])
        x = 0
        l = len(s)
        m = 0
        i = 0
        j = numRows-2
        rows = []
        if numRows == 2:
            while m < l:
                r[0].append(s[m])
                m = m + 1
                if m == l:
                    break
                r[1].append(s[m])
                m = m + 1
        if numRows > 2:
            while m < l:
                j = numRows-2
                r[i].append(s[m])
                m = m + 1
                i = i + 1            
                if i == numRows:
                    while j > 0 and m < l:
                        r[j].append(s[m])
                        m = m + 1
                        j = j - 1
                        if j == 0:
                            i = 0
        
        for x in range(numRows): 
             rows = rows + r[x]
                
          
          
          
        return ''.join(rows)