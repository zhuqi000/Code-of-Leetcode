#
# @lc app=leetcode.cn id=2070 lang=python3
#
# [2070] 每一个查询的最大美丽值
#

from bisect import *
from collections import *


# @lc code=start
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x:x[0])
        #如果一个物品比另一个物品更贵，但美丽值却不如另一个物品
        #那么这个物品永远不可能成为最优答案，可以直接删除
        #这主要改善二分部分
        idx=0
        for i in range(1,len(items)):
            if items[i][1]>items[idx][1]:
                idx+=1
                items[idx]=items[i]
        # for i in range(1,len(items)):
        #     items[i][1]=max(items[i][1],items[i-1][1])
        for i,q in enumerate(queries):
            temp=bisect_right(items,q,0,idx+1,key=lambda x:x[0])
            queries[i]=items[temp-1][1] if temp else 0
        return queries

# @lc code=end

