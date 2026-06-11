class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        result = sorted(counts, key=lambda x:counts[x], reverse=True)

        return result[0:k]