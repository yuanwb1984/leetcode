# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:21:52 2016

@author: 06210
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        l = len(str)
        if l == 0:
            return 0
        i = 0 #计数
        z = 0 #正负号
        b = 0 #0计数
        s = 0 #计数开始
        e = 1 #负号标记
        nums = []
        pool = ['0','1','2','3','4','5','6','7','8','9',' ','+','-']
        numspool = ['1','2','3','4','5','6','7','8','9'] 
        while i < l:
            if str[i] not in pool and s == 0 :
                return 0
            elif str[i] not in pool and s != 0:
                return int(''.join(nums)) * e

            
            elif str[i] in ['+','-'] and z != 0:
                return 0
            elif str[i] in ['+','-'] and b != 0:
                return 0
            elif str[i] in ['+','-'] and s != 0:
                return int(''.join(nums)) * e

            elif str[i] in ['+','-']:
                if str[i] == '-':
                    e = -1                
                i += 1
                z += 1
                
            elif str[i] == '0' and s == 0:
                i += 1
                b += 1
            elif str[i] == '0' and s != 0:
                nums += str[i]
                i += 1
                

            elif str[i] == ' ' and b != 0 and s == 0:
                return 0
            elif str[i] == ' ' and b == 0 and s == 0:
                i += 1
            elif str[i] == ' ' and s != 0:
                return int(''.join(nums)) * e

                
            elif str[i] in numspool:
                nums += str[i]                
                i += 1
                s += 1
            else:
                return int(''.join(nums)) * e

        if nums == []:
            return 0
        return int(''.join(nums)) * e

n = Solution()
print(n.myAtoi('- 564654651'))