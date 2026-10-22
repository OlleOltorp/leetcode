# Time: O(n)
# Space: O(n)

class Solution: 
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        seen = dict()
    
        for num in nums: 
            val = seen.get(num, 0) +1
            seen[num] = val

        buckets = []
        for _ in range(len(nums) + 1):
            buckets.append([])

        for key, val in seen.items():
            buckets[val].append(key)

        output = []
        for bucket in reversed(buckets):
            if bucket == []:
                continue
            for num in bucket: 
                output.append(num) 
                if len(output) == k:
                    return output
            
        return output
