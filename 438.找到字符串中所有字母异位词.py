#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

from bisect import *
from collections import *


# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt=Counter(p)
        ans=[]
        if len(p)>len(s):
            return ans
        left=0
        for right,letter in enumerate(s):
            cnt[letter]-=1
            while cnt[letter]<0:
                cnt[s[left]]+=1
                left+=1
            if right-left+1==len(p):
                ans.append(left)
        return ans
            
# @lc code=end
