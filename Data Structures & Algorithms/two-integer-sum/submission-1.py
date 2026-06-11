class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for x, n in enumerate(nums):
            res = target - n # 4, 7, 3
            if res in seen:
                return [seen[res], x]

            seen[n] = x

        return []