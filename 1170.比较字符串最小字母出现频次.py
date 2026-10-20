#
# @lc app=leetcode.cn id=1170 lang=python3
#
# [1170] 比较字符串最小字母出现频次
#
# https://leetcode.cn/problems/compare-strings-by-frequency-of-the-smallest-character/description/
#
# algorithms
# Medium (67.14%)
# Likes:    170
# Dislikes: 0
# Total Accepted:    54.2K
# Total Submissions: 80.8K
# Testcase Example:  '["cbd"]\n["zaaaz"]'
#
# 定义一个函数 f(s)，统计 s  中（按字典序比较）最小字母的出现频次 ，其中 s 是一个非空字符串。
# 
# 例如，若 s = "dcce"，那么 f(s) = 2，因为字典序最小字母是 "c"，它出现了 2 次。
# 
# 现在，给你两个字符串数组待查表 queries 和词汇表 words 。对于每次查询 queries[i] ，需统计 words 中满足
# f(queries[i]) < f(W) 的 词的数目 ，W 表示词汇表 words 中的每个词。
# 
# 请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是第 i 次查询的结果。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：queries = ["cbd"], words = ["zaaaz"]
# 输出：[1]
# 解释：查询 f("cbd") = 1，而 f("zaaaz") = 3 所以 f("cbd") < f("zaaaz")。
# 
# 
# 示例 2：
# 
# 
# 输入：queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
# 输出：[1,2]
# 解释：第一个查询 f("bbb") < f("aaaa")，第二个查询 f("aaa") 和 f("aaaa") 都 > f("cc")。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 1 
# queries[i][j]、words[i][j] 都由小写英文字母组成
# 
# 
#

# @lc code=start
from bisect import *
# class Solution:
#     def fun_s(self,input_str):
#         temp=input_str[0]
#         ans=1
#         for i in range(1,len(input_str)):
#             if input_str[i]<temp:
#                 temp=input_str[i]
#                 ans=1
#             elif input_str[i]==temp:
#                 ans+=1
#         return ans
#     def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
#         cnt=[0]*12
#         for y in words:
#             cnt[self.fun_s(y)]+=1
#         for i in range(9,0,-1):
#             cnt[i]+=cnt[i+1]
#         ans=[]
#         for x in queries:
#             ans.append(cnt[self.fun_s(x)+1])
#         return ans
            
class Solution:
    def numSmallerByFrequency(self, queries: list[str], words: list[str]) -> list[int]:
        cnt=[0]*12
        for y in words:
            cnt[y.count(min(y))]+=1
        for i in range(9,0,-1):
            cnt[i]+=cnt[i+1]
        ans=[]
        for x in queries:
            ans.append(cnt[x.count(min(x))+1])
        return ans
        
# @lc code=end

