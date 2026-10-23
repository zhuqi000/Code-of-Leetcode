#
# @lc app=leetcode.cn id=2269 lang=python3
#
# [2269] 找到一个数字的 K 美丽值
#

from bisect import *
from collections import *


# @lc code=start
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_s=str(num)
        ans=0
        for right in range(k,len(num_s)+1):
            temp=int(num_s[right-k:right])
            if temp and num%temp==0:
                ans+=1
        return ans
# @lc code=end

