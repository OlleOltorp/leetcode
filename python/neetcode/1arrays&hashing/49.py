# Time: O(nk)
# Space: O(nk)

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen = dict()
        for anagram in strs: 
            lookup = [0] * 26 
            for char in anagram:
                lookup[ord(char) - ord('a')] += 1

            key = tuple(lookup)
            if key not in seen:
                seen[key] = []
            seen[key].append(anagram)

        return list(seen.values())
