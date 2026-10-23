# Time: O(n)
# Space: O(n)

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        forward = [0] * (len(nums))
        forward[0] = 1
        for i in range(1, len(nums)):
            forward[i] = nums[i - 1] * forward[i - 1]

        backward = [0] * (len(nums))
        backward[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            backward[i] = nums[i + 1] * backward[i + 1]

        result = [0] * len(nums)
        
        for i in range(0, len(nums), 1):
            result[i] = forward[i] * backward[i]
    
        return result
