/*
 * @lc app=leetcode.cn id=1297 lang=cpp
 *
 * [1297] 子串的最大出现次数
 *
 * https://leetcode.cn/problems/maximum-number-of-occurrences-of-a-substring/description/
 *
 * algorithms
 * Medium (55.72%)
 * Likes:    155
 * Dislikes: 0
 * Total Accepted:    30.8K
 * Total Submissions: 55.2K
 * Testcase Example:  '"aababcaab"\n2\n3\n4'
 *
 * 给你一个字符串 s ，请你返回满足以下条件且出现次数最大的 任意 子串的出现次数：
 * 
 * 
 * 子串中不同字母的数目必须小于等于 maxLetters 。
 * 子串的长度必须大于等于 minSize 且小于等于 maxSize 。
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
 * 输出：2
 * 解释：子串 "aab" 在原字符串中出现了 2 次。
 * 它满足所有的要求：2 个不同的字母，长度为 3 （在 minSize 和 maxSize 范围内）。
 * 
 * 
 * 示例 2：
 * 
 * 输入：s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
 * 输出：2
 * 解释：子串 "aaa" 在原字符串中出现了 2 次，且它们有重叠部分。
 * 
 * 
 * 示例 3：
 * 
 * 输入：s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
 * 输出：3
 * 
 * 
 * 示例 4：
 * 
 * 输入：s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
 * 输出：0
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= s.length <= 10^5
 * 1 <= maxLetters <= 26
 * 1 <= minSize <= maxSize <= min(26, s.length)
 * s 只包含小写英文字母。
 * 
 * 
 */

// @lc code=start
#include <string>
#include <unordered_map>
class Solution {
public:
    int maxFreq(string s, int maxLetters, int minSize, int maxSize) {
        // maxSize大小的字串包含minSize大小的字串
        // 如果maxSize的子串出现了s次
        // 那么其子串的子串必定出现至少s次
        // 且更加满足maxLetters的要求
        std::pmr::unordered_map<char, int>idx;
        std::pmr::unordered_map<string, int>num_string;
        int ans=0;
        for(int right=0;right<s.size();right++)
        {
            idx[s[right]]++;
            int left=right-minSize+1;
            if (left<0){continue;}
            int cnt=++num_string[s.substr(left,minSize)];
            if(idx.size()<=maxLetters){
                ans=max(ans,cnt);
            }
            if(--idx[s[left]]==0){
                idx.erase(s[left]);
            }
        }
        return  ans;
    }
};
// @lc code=end

