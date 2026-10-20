#
# @lc app=leetcode.cn id=2080 lang=python3
#
# [2080] 区间内查询数字的频率
#

from bisect import *
from collections import *

# @lc code=start
class RangeFreqQuery:

    def __init__(self, arr: list[int]):
        self.pos=defaultdict(list)
        for i in range(0,len(arr)):
            self.pos[arr[i]].append(i)
    def query(self, left: int, right: int, value: int) -> int:
        pos_list=self.pos[value]
        start=bisect_left(pos_list,left)
        return bisect_right(pos_list,right,start)-start



# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
# @lc code=end

