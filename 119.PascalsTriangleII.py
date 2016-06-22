# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 12:48:55 2016

@author: 06210
[1],
[1,1],
[1,2,1],
[1,3,3,1],

  [0]+[1,3,3,  1],
+ [1,  3,3,1]+[0],
------------------
= [1,  4,6,4,  1]

"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowlast=[1]        
        if rowIndex == 0:
            return rowlast
        i = 0
        while i < rowIndex:
            rowk = [0] + rowlast + [0]
            rowlast = []
            for j in range(len(rowk) - 1):
                rowlast = rowlast + [rowk[j] + rowk[j + 1]]
            i = i + 1
        return rowlast
        
n = Solution()
print(n.getRow(3))