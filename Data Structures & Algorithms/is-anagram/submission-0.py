class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d = {}
        c = {}

        for x in s:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        
        for k in t:
            if k in c:
                c[k] += 1
            else:
                c[k] = 1

        if d == c:
            return True
        elif d != c:
            return False
