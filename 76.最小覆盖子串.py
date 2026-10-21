#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

from bisect import *
from collections import *


# @lc code=start
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         left=0
#         cnt_t=Counter(t)
#         cnt_s=Counter()
#         ans_left=-1
#         ans_right=len(s)
#         for right,letter in enumerate(s):
#             cnt_s[letter]+=1
#             if cnt_s>=cnt_t:
#                 while cnt_s[s[left]]>cnt_t[s[left]]:
#                     cnt_s[s[left]]-=1
#                     left+=1
#                 if right-left+1<ans_right-ans_left:
#                     ans_left=left
#                     ans_right=right+1
#         return "" if ans_left < 0 else s[ans_left: ans_right]

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        diff = defaultdict(int)
        for item in t:
            diff[item]-=1
        kind=len(diff)
        ans_left=-1
        ans_right=len(s)
        left=0
        get_kind=0
        for right,item in enumerate(s):
            diff[item]+=1
            if diff[item]==0:
                get_kind+=1
            while get_kind==kind:
                if right-left<ans_right-ans_left:
                    ans_right,ans_left=right,left
                x=s[left]
                if diff[x]==0:
                    get_kind-=1
                diff[x]-=1
                left+=1
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]
# @lc code=end

