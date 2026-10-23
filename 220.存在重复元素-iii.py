#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#

from bisect import *
from collections import *
from sortedcontainers import *

# @lc code=start
# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
#         ans=SortedList([nums[0]])
#         for right in range(1,len(nums)):
#             temp=ans.bisect_left(nums[right]-valueDiff)
#             if temp<len(ans) and ans[temp]-nums[right]<=valueDiff:
#                 return True
#             ans.add(nums[right])
#             if right >= indexDiff:
#                 ans.remove(nums[right - indexDiff])
#         return False
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        bucket={}
        bucket_size=valueDiff+1
        for right in range(len(nums)):
            idx=nums[right]//bucket_size
            if idx in bucket:
                return True
            if idx - 1 in bucket and nums[right]-bucket[idx-1]<=valueDiff:
                return True
            if idx + 1 in bucket and bucket[idx+1]-nums[right]<=valueDiff:
                return True
            bucket[idx]=nums[right]
            if right>=indexDiff:
                bucket.pop((nums[right-indexDiff])//bucket_size)
        return False
# @lc code=end

