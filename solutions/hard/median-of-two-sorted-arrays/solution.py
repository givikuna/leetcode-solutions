import math

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        mid = len(nums) / 2
        if len(nums) % 2 == 0:
            return (nums[mid-1] + nums[mid]) / 2.0
        else:
            return nums[mid]

