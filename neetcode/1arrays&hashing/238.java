// 238. Product of Array Except Self
// https://leetcode.com/problems/product-of-array-except-self
// Time: O(n) Space: O(1) (Per problem instructions not counting outputArray)
// Idea: Forward pass then backward pass with variable

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int numsLength = nums.length;
        int[] finalArray = new int[numsLength];
        finalArray[0] = 1;

        for (int i = 1; i < numsLength; i++) {
            finalArray[i] = nums[i - 1] * finalArray[i - 1];
        }

        int afterVariable = 1;

        for (int i = numsLength - 1; i > 0; i--) {
            finalArray[i] = finalArray[i] * afterVariable;
            afterVariable = afterVariable * nums[i];
        }
        finalArray[0] = afterVariable;

        return finalArray;
    }
}