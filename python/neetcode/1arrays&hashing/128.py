# Time: O(n)
# Space: O(n)

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numset = set(nums)

        sequencestarters = []

        for num in numset:
            if num - 1 not in numset:
                sequencestarters.append(num)

        longestsequence = 0
        for starter in sequencestarters:
            length = 1
            nextnum = starter
            while True:
                nextnum = nextnum + 1
                if nextnum in numset:
                    length += 1
                else:
                    if length > longestsequence:
                        longestsequence = length
                    break

        return longestsequence
