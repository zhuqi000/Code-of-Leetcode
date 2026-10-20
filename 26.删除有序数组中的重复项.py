#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

from bisect import *
from collections import *


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        new_idx=1
        for old_idx in range(1,len(nums)):
            if nums[old_idx]!=nums[old_idx-1]:
                nums[new_idx]=nums[old_idx]
                new_idx+=1
        return new_idx
# @lc code=end

