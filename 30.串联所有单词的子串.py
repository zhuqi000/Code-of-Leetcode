#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

from bisect import *
from collections import *


# @lc code=start
    
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len=len(words[0])
        win_len=word_len*len(words)
        target_cnt=Counter(words)
        ans=[]
        for start in range(word_len):
            cnt=defaultdict(int)
            over=0
            for right in range(start + word_len,len(s)+1,word_len):
                in_word=s[right-word_len:right]
                if cnt[in_word]==target_cnt[in_word]:
                    over+=1
                cnt[in_word]+=1
                left=right-win_len
                if left<0:
                    continue
                if over == 0:
                    ans.append(left)
                out_word=s[left:left+word_len]
                cnt[out_word]-=1
                if cnt[out_word]==target_cnt[out_word]:
                    over-=1
        return ans

                
# @lc code=end

