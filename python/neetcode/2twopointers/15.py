# Time: O(n^2)
# Space: O(n)

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        print(nums)

        seenfirsts = set()

        triplets = list()
        for i in range(0, len(nums) - 2):
            num0 = nums[i]
            if num0 in seenfirsts:
                continue

            seenfirsts.add(num0)

            pointer1 = i + 1
            pointer2 = len(nums) - 1
            print(pointer1, pointer2)

            needed = -num0

            while True:
                if pointer1 == pointer2:
                    break

                if nums[pointer1] + nums[pointer2] == needed:
                    if triplets == []:
                        triplets.append([num0, nums[pointer1], nums[pointer2]])
                    elif triplets[-1] != [num0, nums[pointer1], nums[pointer2]]:
                        triplets.append([num0, nums[pointer1], nums[pointer2]])

                    pointer1 += 1
                    continue

                if nums[pointer2] > needed - nums[pointer1]:
                    pointer2 -= 1
                    continue

                if nums[pointer2] < needed - nums[pointer1]:
                    pointer1 += 1

        return triplets
