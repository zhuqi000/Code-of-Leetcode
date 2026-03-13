/*
 * @lc app=leetcode.cn id=3694 lang=cpp
 *
 * [3694] 删除子字符串后不同的终点
 *
 * https://leetcode.cn/problems/distinct-points-reachable-after-substring-removal/description/
 *
 * algorithms
 * Medium (56.13%)
 * Likes:    17
 * Dislikes: 0
 * Total Accepted:    5.4K
 * Total Submissions: 9.6K
 * Testcase Example:  '"LUL"\n1'
 *
 * 给你一个由字符 'U'、'D'、'L' 和 'R' 组成的字符串 s，表示在无限的二维笛卡尔网格上的移动。
 * 
 * 
 * 'U': 从 (x, y) 移动到 (x, y + 1)。
 * 'D': 从 (x, y) 移动到 (x, y - 1)。
 * 'L': 从 (x, y) 移动到 (x - 1, y)。
 * 'R': 从 (x, y) 移动到 (x + 1, y)。
 * 
 * 
 * 你还得到了一个正整数 k。
 * 
 * 你 必须 选择并移除 恰好一个 长度为 k 的连续子字符串 s。然后，从坐标 (0, 0) 开始，按顺序执行剩余的移动。
 * 
 * 返回可到达的 不同 最终坐标的数量。
 * 
 * 
 * 
 * 示例 1:
 * 
 * 
 * 输入：s = "LUL", k = 1
 * 
 * 输出：2
 * 
 * 解释：
 * 
 * 移除长度为 1 的子字符串后，s 可以是 "UL"、"LL" 或 "LU"。执行这些移动后，最终坐标将分别是 (-1, 1)、(-2, 0) 和
 * (-1, 1)。有两个不同的点 (-1, 1) 和 (-2, 0)，因此答案是 2。
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入：s = "UDLR", k = 4
 * 
 * 输出：1
 * 
 * 解释：
 * 
 * 移除长度为 4 的子字符串后，s 只能是空字符串。最终坐标将是 (0, 0)。只有一个不同的点 (0, 0)，因此答案是 1。
 * 
 * 
 * 示例 3:
 * 
 * 
 * 输入：s = "UU", k = 1
 * 
 * 输出：1
 * 
 * 解释：
 * 
 * 移除长度为 1 的子字符串后，s 变为 "U"，它总是以 (0, 1) 结束，因此只有一个不同的最终坐标。
 * 
 * 
 * 
 * 
 * 提示:
 * 
 * 
 * 1 <= s.length <= 10^5
 * s 只包含 'U'、'D'、'L' 和 'R'。
 * 1 <= k <= s.length
 * 
 * 
 */

// @lc code=start
// class Solution {
// public:
//     int distinctPoints(string s, int k) {
//         long x=0,y=0;
//         std::pmr::unordered_map<string, long> idx;
//         for(int right=0;right<s.size();right++){
//             if(s[right]=='U'){y++;}
//             if(s[right]=='D'){y--;}
//             if(s[right]=='L'){x--;}
//             if(s[right]=='R'){x++;}
//             if(right<k-1){continue;}
//             idx[std::to_string(x)+"x"+std::to_string(y)]++;
//             int left=right-k+1;
//             if(s[left]=='U'){y--;}
//             if(s[left]=='D'){y++;}
//             if(s[left]=='L'){x++;}
//             if(s[left]=='R'){x--;}
//         }
//         return idx.size();
//     }
// };

class Solution {
public:
    int distinctPoints(string s, int k) {
        int32_t n = s.size();
        unordered_set<long long> st;
        int32_t x = 0, y = 0;
        for (int i = 0; i < n; i++) {
            //简单分支多状态使用switch
            switch (s[i]) {
                case 'L': x--; break;
                case 'R': x++; break;
                case 'D': y--; break;
                case 'U': y++; break;
            }

            int left = i + 1 - k;
            if (left < 0) {
                continue;
            }

            // 把两个 int32_t 压缩到一个int64_t中，+n 避免负数
            st.insert(int64_t(1) * (x+n) << 32 | (y+n));
            //为负，左移可能触发未定义行为
            switch (s[left]) {
                case 'L': x++; break;
                case 'R': x--; break;
                case 'D': y++; break;
                case 'U': y--; break;
            }
        }
        return st.size();
    }
};

// @lc code=end

