# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:04:21 2016

@author: 06210
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        numr = []
        len1 = len(nums1) -1
        len2 = len(nums2) -1
        nums1.sort()
        nums2.sort()
        if len1 > len2:
            nums1, nums2 = nums2, nums1
            len1, len2 = len2, len1
        p1 = p2 = 0
        while p1 <= len1 and p2 <= len2:
            
            if nums1[p1] == nums2[p2]:
                numr.append(nums1[p1])
                p1 = p1 + 1
                p2 = p2 + 1
            elif nums1[p1] > nums2[p2]:
                p2 = p2 +1
            else: 
                p1 = p1 +1
        
        return list(set(numr))