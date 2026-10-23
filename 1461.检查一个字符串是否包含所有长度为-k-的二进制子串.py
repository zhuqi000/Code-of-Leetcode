#
# @lc app=leetcode.cn id=1461 lang=python3
#
# [1461] 检查一个字符串是否包含所有长度为 K 的二进制子串
#

from bisect import *
from collections import *


# @lc code=start
# class Solution:
#     def hasAllCodes(self, s: str, k: int) -> bool:
#         pos=set(s[left:left+k] for left in range(len(s)-k+1))
#         return len(pos)==(1 << k)
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        MASK = (1 << k) - 1
        has = [False] * (1 << k)
        cnt = x = 0
        for i, ch in enumerate(s):
            # 把 ch 加到 x 的末尾：x 整体左移一位，然后或上 ch
            # &MASK 目的是去掉超出 k 的比特位
            x = (x << 1 & MASK) | int(ch)
            if i < k - 1 or has[x]:
                continue
            has[x] = True
            cnt += 1
            if cnt == 1 << k:
                return True
        return False

# @lc code=end

