#
# @lc app=leetcode.cn id=3090 lang=python3
#
# [3090] 每个字符最多出现两次的最长子字符串
#

from bisect import *
from collections import *


# @lc code=start
# class Solution:
#     def maximumLengthSubstring(self, s: str) -> int:
        # cnt=defaultdict(int)
        # left=ans=0
        # for right in range(len(s)):
        #     cnt[s[right]]+=1
        #     while cnt[s[right]]>2:
        #         cnt[s[left]]-=1
        #         left+=1
        #     ans=max(ans,right-left+1)
        # return ans
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left=ans=0
        last1 = [-1] * 26
        last2 = [-1] * 26

        for right, c in enumerate(s):
            i = ord(c) - ord('a')

            left = max(left, last2[i] + 1)

            last2[i] = last1[i]
            last1[i] = right

            ans = max(ans, right - left + 1)
        return ans

# @lc code=end

