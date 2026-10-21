// 49. Group Anagrams
// https://leetcode.com/problems/group-anagrams/
// Time: O(n*k) Space: O(n*k)
// Idea: Build identifier arrays for all words, these are unique check for the same 

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.List;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagramMap = new HashMap<>();

        for (int i = 0; i < strs.length; i++) {
            String s = strs[i];
            int[] charCounter = new int[26];

            for (int j = 0; j < s.length(); j++) {
                int a = s.charAt(j) - 'a';
                charCounter[a]++;
            }

            String identifier = Arrays.toString(charCounter);

            List<String> anagrams = anagramMap.get(identifier);
            if (anagrams == null) {
                List<String> anagramList = new ArrayList<>();
                anagramList.add(s);
                anagramMap.put(identifier, anagramList);
                continue;
            }
            anagrams.add(s);
        }

        return new ArrayList<>(anagramMap.values());
    }
}