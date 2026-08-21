// 242. Valid Anagram
// https://leetcode.com/problems/valid-anagram/description/
// Time: O(n) Space: O(1)
// Build arrayCounter for all chars, count and substract to get anagrams

class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()) {
            return false;
        }

        int[] arrayCounter = new int[26];

        for (int i = 0; i < s.length(); i++) {
            int a = s.charAt(i) - 'a';
            int b = t.charAt(i) - 'a';
            arrayCounter[a]++;
            arrayCounter[b]--;
        }

        for (int i = 0; i < arrayCounter.length; i++) {
            if (arrayCounter[i] != 0) {
                return false;
            }
        }

        return true;
    }
}