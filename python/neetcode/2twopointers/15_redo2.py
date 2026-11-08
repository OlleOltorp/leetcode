class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        result = []

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            target = -nums[i]
            while left != right:
                if nums[i] == nums[i - 1] and i > 0:
                    break

                if nums[left] + nums[right] == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while right > left and nums[left] == nums[left - 1]:
                        left += 1
                    continue

                if nums[left] + nums[right] < target:
                    left += 1
                    continue

                if nums[left] + nums[right] > target:
                    right -= 1
                    continue
        return result
