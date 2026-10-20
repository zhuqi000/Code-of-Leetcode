#
# @lc app=leetcode.cn id=3488 lang=python3
#
# [3488] 距离最小相等元素查询
#

from bisect import *
from collections import *


# @lc code=start
# class Solution:
#     def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
#         num_pos=defaultdict(list)
#         for i in range(0,len(nums)):
#             num_pos[nums[i]].append(i)
#         for pos in num_pos.values():
#             x=pos[0]
#             pos.insert(0,pos[-1]-len(nums))
#             pos.append(x+len(nums))
#         for i,x in enumerate(queries):
#             pos_num=nums[x]
#             pos_list=num_pos[pos_num]
#             if len(pos_list)==3:
#                 queries[i]=-1
#                 continue
#             index=bisect_left(pos_list,x)
#             queries[i]=min(pos_list[index+1]-x,x-pos_list[index-1])
        # return queries
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n=len(nums)
        left=[0]*n
        right=[0]*n
        pos={}
        for i in range(-n,n):
            if i>=0:
                left[i]=pos[nums[i]]
            pos[nums[(i+n)%n]]=i
        for i in range(2*n-1,-1,-1):
            if i<n:
                right[i]=pos[nums[i]]
            pos[nums[i%n]]=i
        for i,q in enumerate(queries):
            l=left[q]
            queries[i]=-1 if q-l==n else min(q-l,right[q]-q)
        return queries
            
        
# @lc code=end

