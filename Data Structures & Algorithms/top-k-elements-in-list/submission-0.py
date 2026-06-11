class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict = {}

        # 1. we store each number along with its frequency
        # 2. then we sort the frequencies
        # 3. then we return the key of top k frequencies (frequencies are values)

        for x in nums:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        
        final = sorted(dict, key=lambda x:dict[x], reverse=True)
        
        return final[0:k]