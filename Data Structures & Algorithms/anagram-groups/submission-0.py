class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = {}

        for x in strs:
            if tuple(sorted(x)) in dict:
                dict[tuple(sorted(x))].append(x)
            else:
                dict[tuple(sorted(x))] = [x]
        
        return list(dict.values())