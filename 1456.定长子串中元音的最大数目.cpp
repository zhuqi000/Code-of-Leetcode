/*
 * @lc app=leetcode.cn id=1456 lang=cpp
 *
 * [1456] 定长子串中元音的最大数目
 *
 * https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
 *
 * algorithms
 * Medium (61.78%)
 * Likes:    233
 * Dislikes: 0
 * Total Accepted:    155.3K
 * Total Submissions: 251.3K
 * Testcase Example:  '"abciiidef"\n3'
 *
 * 给你字符串 s 和整数 k 。
 * 
 * 请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。
 * 
 * 英文中的 元音字母 为（a, e, i, o, u）。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：s = "abciiidef", k = 3
 * 输出：3
 * 解释：子字符串 "iii" 包含 3 个元音字母。
 * 
 * 
 * 示例 2：
 * 
 * 输入：s = "aeiou", k = 2
 * 输出：2
 * 解释：任意长度为 2 的子字符串都包含 2 个元音字母。
 * 
 * 
 * 示例 3：
 * 
 * 输入：s = "leetcode", k = 3
 * 输出：2
 * 解释："lee"、"eet" 和 "ode" 都包含 2 个元音字母。
 * 
 * 
 * 示例 4：
 * 
 * 输入：s = "rhythms", k = 4
 * 输出：0
 * 解释：字符串 s 中不含任何元音字母。
 * 
 * 
 * 示例 5：
 * 
 * 输入：s = "tryhard", k = 4
 * 输出：1
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= s.length <= 10^5
 * s 由小写英文字母组成
 * 1 <= k <= s.length
 * 
 * 
 */

// @lc code=start
class Solution {
public:
    bool CheckVowels(char a)
    {
        if(a=='a'||a=='e'||a=='i'||a=='o'||a=='u'){
            return true;
        }
        return false;
    }
    int maxVowels(string s, int k) {
        //基本逻辑：进入循环时进行更新
        // 更新前进行必要检查
        // 更新后为下次更新做准备
        int num_vowels=0;
        int ans=0;
        for(int right=0;right<s.size()&&num_vowels!=k;right++){
            if(CheckVowels(s[right])){
                num_vowels++;
            }
            int left=right-k+1;
            if(left<0){continue;}
            ans=max(ans,num_vowels);
            if(CheckVowels(s[left])){num_vowels--;}
        }
        return ans;
    }
};

// @lc code=end

