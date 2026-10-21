#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

from bisect import *
from collections import *


# @lc code=start
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         cnt=Counter()
#         left=0
#         ans=0
#         for right in range(len(s)):
#             cnt[s[right]]+=1
#             while cnt[s[right]]>1:
#                 cnt[s[left]]-=1
#                 left+=1
#             ans=max(right-left+1,ans)
#         return ans
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos={}
        left=ans=0
        for right in range(len(s)):
            left=max(left,pos.get(s[right],-1)+1)
            pos[s[right]]=right
            ans=max(ans,right-left+1)
        return ans
# @lc code=end

