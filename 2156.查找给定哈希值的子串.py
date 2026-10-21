#
# @lc app=leetcode.cn id=2156 lang=python3
#
# [2156] 查找给定哈希值的子串
#

from bisect import *
from collections import *


# @lc code=start
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        #乘法比除法更加方便，模运算不可逆在非互质条件下
        p=pow(power,k-1,modulo)
        ans_left=0
        hash_temp=0
        for left in range(len(s)-1,-1,-1):
            hash_temp=(hash_temp*power+(ord(s[left])&31))%modulo
            right=left+k-1
            if right>=len(s):
                continue
            if hash_temp==hashValue:
                ans_left=left
            hash_temp=(hash_temp-(ord(s[right])&31)*p)%modulo
        return s[ans_left:ans_left+k]
# @lc code=end

