#
# @lc app=leetcode.cn id=2563 lang=python3
#
# [2563] 统计公平数对的数目
#

from bisect import *
from collections import *


# @lc code=start
# class Solution:
#     def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
#         n=len(nums)
#         ans=0
#         nums.sort()
#         for i in range(0,n-1):
#             lo=lower-nums[i]
#             up=upper-nums[i]
#             left=bisect_left(nums,lo,i+1)
#             right=bisect_right(nums,up,left)
#             ans+=right-left
#         return ans
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans=0
        l=r=len(nums)
        for i,num in enumerate(nums):
            while r and nums[r-1]>upper-num:
                r-=1
            while l and nums[l-1]>=lower-num:
                l-=1
            ans+=min(r,i)-min(l,i)
        return ans
# @lc code=end

