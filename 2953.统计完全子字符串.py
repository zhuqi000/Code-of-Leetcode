#
# @lc app=leetcode.cn id=2953 lang=python3
#
# [2953] 统计完全子字符串
#

from bisect import *
from collections import *


# @lc code=start
class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        ans=0
        cnt=Counter()
        odd=0
        
        for start in range(k):
            left=right=start
            for right in range(start,len(word)):
                cnt[word[right]]+=1
                if cnt[word[right]]==k:
                    odd+=1
                    
            
            
        return ans
# @lc code=end

