# Time: O(n)
# Space: O(1)
# Better solution: Use ordered list instead of dict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        seen = dict()
        for char in s:
            val = seen.get(char, 0)
            seen[char] = val + 1

        for char in t: 
            val = seen.get(char, 0)
            seen[char] = val -1 
            if seen.get(char, 0) == 0:
                seen.pop(char)

        return len(seen) == 0
        return False
