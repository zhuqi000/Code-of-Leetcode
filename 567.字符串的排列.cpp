/*
 * @lc app=leetcode.cn id=567 lang=cpp
 *
 * [567] 字符串的排列
 *
 * https://leetcode.cn/problems/permutation-in-string/description/
 *
 * algorithms
 * Medium (46.37%)
 * Likes:    1089
 * Dislikes: 0
 * Total Accepted:    342.9K
 * Total Submissions: 738.9K
 * Testcase Example:  '"ab"\n"eidbaooo"'
 *
 * 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的 排列。如果是，返回 true ；否则，返回 false 。
 * 
 * 换句话说，s1 的排列之一是 s2 的 子串 。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：s1 = "ab" s2 = "eidbaooo"
 * 输出：true
 * 解释：s2 包含 s1 的排列之一 ("ba").
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：s1= "ab" s2 = "eidboaoo"
 * 输出：false
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= s1.length, s2.length <= 10^4
 * s1 和 s2 仅包含小写字母
 * 
 * 
 */

// @lc code=start
#include <unordered_map>
#include <vector>
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int k=s1.size();
        int cnt[26]={};
        int count=0;
        for(int i=0;i<k;i++){
            if(cnt[s1[i]-'a']++==0)
            {count++;}
            
        }
        if(k>s2.size()){
            return false;
        }
        for(int right=0;right<s2.size();right++){
            if(--cnt[s2[right]-'a']==0){
                count--;
            }
            cout<<right<<","<<
            int left=right-k+1;
            if(left<0){continue;}
            if(count==0){return true;}
            if(cnt[s2[right]-'a']++==0){
                count++;
            }
        }
        return false;
    }
};
// @lc code=end

