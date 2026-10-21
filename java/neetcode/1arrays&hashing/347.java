// 347. Top K Frequent Elements
// https://leetcode.com/problems/top-k-frequent-elements/
// Time: O(n) Space: O(n)

// Idea: 
// Three passes
// First pass counts
// Second pass creates sorted index array
// Third pass takes out largest values (starting at the end)

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> seenMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            seenMap.merge(nums[i], 1, (a, b) -> a + b);
        }

        List<Integer>[] indexArray = new ArrayList[nums.length + 1];

        for (Map.Entry<Integer, Integer> numEntry : seenMap.entrySet()) {
            int key = numEntry.getKey();
            int val = numEntry.getValue();

            List<Integer> list = indexArray[val];
            if (list == null) {
                list = new ArrayList<>();
                indexArray[val] = list;
            }
            list.add(key);
        }

        int[] returnList = new int[k];
        int currentFree = k - 1;
        for (int i = indexArray.length - 1; i >= 0; i--) {
            if (currentFree == -1) {
                return returnList;
            }
            List<Integer> list = indexArray[i];

            if (list == null) {
                continue;
            }

            for (Integer integer : list) {
                returnList[currentFree] = integer;
                currentFree--;
            }
        }
        return null;
    }
}