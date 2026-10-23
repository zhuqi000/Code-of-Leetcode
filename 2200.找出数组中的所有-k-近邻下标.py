#
# @lc app=leetcode.cn id=2200 lang=python3
#
# [2200] 找出数组中的所有 K 近邻下标
#

from bisect import *
from collections import *


# @lc code=start
class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        ans=[]
        right=0
        for i,num in enumerate(nums):
            if num==key:
                ans.extend(range(max(right,i-k),min(i+k+1,len(nums))))
                right=i+k+1#open
        return ans
# @lc code=end

