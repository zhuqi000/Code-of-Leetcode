#
# @lc app=leetcode.cn id=2653 lang=python3
#
# [2653] 滑动子数组的美丽值
#

from bisect import *
from collections import *


# @lc code=start
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        cnt=[0]*101
        for n in nums[:k-1]:
            cnt[n]+=1
        ans=[0]*(len(nums)-k+1)
        for j,(input,output) in enumerate(zip(nums[k-1:],nums[:])):
            cnt[input]+=1
            temp=x
            for i in range(-50,0):
                temp-=cnt[i]
                if temp<=0:
                    ans[j]=i
                    break
            cnt[output]-=1
        return ans
                
        
        
# @lc code=end

