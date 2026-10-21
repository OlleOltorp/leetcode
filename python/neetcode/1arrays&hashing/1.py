# Time: O(n)
# Space: O(n)

class Solution: 
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = dict()

        for i, num in enumerate(nums): 
            seen[num] = i
        
        soughtnum = None
        for i, num in enumerate(nums):
            soughtnum = target-num
            if soughtnum in seen:
                indice1 = i
                indice2 = seen.pop(soughtnum)
                if indice1 == indice2:
                    continue
                return [indice1, indice2]
