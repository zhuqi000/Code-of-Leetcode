/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 *
 * https://leetcode.cn/problems/two-sum/description/
 *
 * algorithms
 * Easy (55.06%)
 * Likes:    20665
 * Dislikes: 0
 * Total Accepted:    7.1M
 * Total Submissions: 13M
 * Testcase Example:  '[2,7,11,15]\n9'
 *
 * 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
 * 
 * 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
 * 
 * 你可以按任意顺序返回答案。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [2,7,11,15], target = 9
 * 输出：[0,1]
 * 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [3,2,4], target = 6
 * 输出：[1,2]
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：nums = [3,3], target = 6
 * 输出：[0,1]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 2 <= nums.length <= 10^4
 * -10^9 <= nums[i] <= 10^9
 * -10^9 <= target <= 10^9
 * 只会存在一个有效答案
 * 
 * 
 * 
 * 
 * 进阶：你可以想出一个时间复杂度小于 O(n^2) 的算法吗？
 * 
 */

// @lc code=start

// #include <vector>
// class Solution {
// public:
//     vector<int> twoSum(vector<int>& nums, int target) {
//         for (int i=0;i<nums.size();i++)
//             for (int j=i+1;j<nums.size();j++)
//             {
//                 if(nums[i]+nums[j]==target)
//                 {
//                     return {i,j};
//                 }
//             }
//         return {};
//     }
// };

#include <unordered_map>
#include <vector>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> idx;
        for (int i=0;;i++)
        //for (int i=0; i<nums.size(); i++)时
        //对于编译器来说，“循环结束”是一条明确的、可能的执行路径
        // 在这条路径上，函数没有返回值
        {
            auto it =idx.find(target-nums[i]);
            if (it!=idx.end())
            {
                return {it->second,i};
            }
            idx[nums[i]]=i;
        }
    }
};
// @lc code=end

