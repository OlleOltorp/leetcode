// 217. Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/
// Time: O(n) Space: O(n)
// Idea: Use Map

import java.util.Set;
import java.util.HashSet;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();

        for (int num : nums) {
            if (!seen.add(num)) {
                return true;
            }
        }
        return false;
    }
}