class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        L = []
        for x in nums:
            if x in L:
                return True
            L.append(x)
        return False
