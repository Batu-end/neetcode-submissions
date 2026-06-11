class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, num in enumerate(nums):

            need = target - num  # so just look for a complementary number

            if need in seen:
                return [seen[need], i] # return index of num

            seen[num] = i


        return False