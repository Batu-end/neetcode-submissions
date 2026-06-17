class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []

        running = 1
        for number in nums:
            prefix.append(running)
            running *= number

        running = 1
        for number in reversed(nums):
            suffix.append(running)
            running *= number
        
        suffix.reverse()
        result = []

        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])

        return result