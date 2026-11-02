class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        resultlist = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            first = nums[i]
            l = i + 1
            r = len(nums) - 1

            target = -first
            while l < r:
                second = nums[l]
                third = nums[r]

                result = second + third

                if result == target:
                    resultlist.append([first, second, third])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                elif result < target:
                    l += 1

                else:
                    r -= 1
        return resultlist
