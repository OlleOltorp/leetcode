// 1. Two Sum
// https://leetcode.com/problems/two-sum/
// Time: O(n) Space: O(n)

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];

            int complement = target - num;

            Integer complementIndex = seen.get(complement);
            seen.put(num, i);

            if (complementIndex != null) {
                return new int[] { i, complementIndex };
            }

        }
        return null;
    }
}