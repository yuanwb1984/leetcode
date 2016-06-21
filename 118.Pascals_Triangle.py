# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 12:48:55 2016

@author: 06210
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rows=[[1]]        
        if numRows == 0:
            return []
        elif numRows == 1:
            return rows
        i = 0
        while i < numRows - 1:

            rowk = [0] + rows[i] + [0]
            row = []
            for j in range(len(rowk) - 1):
                row = row + [rowk[j] + rowk[j + 1]]
            i = i + 1
            rows.append(row)
        return rows
n = Solution()
print(n.generate(5))