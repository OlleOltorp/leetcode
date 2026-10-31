class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numdict = dict()

        for i in range(len(nums)):
            num = nums[i]

            needed = target - num

            if needed in numdict:
                pos = numdict[needed]
                return [i, pos]

            numdict[num] = i
