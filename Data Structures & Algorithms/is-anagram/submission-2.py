class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        dict_s = {}
        dict_t = {}

        for x in s:
            if x in dict_s:
                dict_s[x] += 1
            else:
                dict_s[x] = 1

        for x in t:
            if x in dict_t:
                dict_t[x] += 1
            else:
                dict_t[x] = 1

        if dict_s != dict_t:
            return False
        
        return True