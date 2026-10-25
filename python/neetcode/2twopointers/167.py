# Time: O(n)
# Space: O(1)

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        pointer1 = 0
        pointer2 = len(numbers) - 1
        while True:
            num1 = numbers[pointer1]
            num2 = numbers[pointer2]

            needed1 = target -num2
            needed2 = target-num1

            if num1 + num2 == target:
                return [pointer1 + 1, pointer2 + 1]

            if num2 > needed2:
                pointer2 -=1
                continue

            if num2 < needed2:
                pointer1 +=1
