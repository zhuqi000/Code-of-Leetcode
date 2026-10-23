#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#

from bisect import *
from collections import *
from sortedcontainers import *


# @lc code=start
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left=0
        idx=defaultdict(int)
        ans=0
        for right in range(0,len(fruits)):
            idx[fruits[right]]+=1
            while len(idx)>2:
                idx[fruits[left]]-=1
                if idx[fruits[left]]==0:
                    del idx[fruits[left]]
                left+=1
            ans=max(right-left+1,ans)
        return ans
# @lc code=end

