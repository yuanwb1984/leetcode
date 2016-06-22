# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:20:40 2016

@author: 06210
查找字典是否有，有pop掉，无添加到字典。
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pool = {}
        l = len(nums) -1
        for i in range(l, -1, -1):
            if nums[i] in pool:
                nums.pop(i)
            else:
                pool[nums[i]] = i
        return len(nums)
#       return len(list(set(nums)))
#上一句在leetcode不通过
n = Solution()
print(n.removeDuplicates([]))