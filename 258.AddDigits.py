# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:02:17 2016

@author: 06210
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        global numb
        numb = num
        txt = str(numb)
        if len(txt) > 1:
            numb = 0
            for s in txt:
                numb = numb + int(s)
            self.addDigits(numb)
        return numb