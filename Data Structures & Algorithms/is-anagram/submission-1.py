class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        first = {}
        second = {}

        for x in s:
            if x in first:
                first[x] += 1
            else:
                first[x] = 1

        for x in t:
            if x in second:
                second[x] += 1
            else:
                second[x] = 1

        if first == second:
            return True
        elif first != second:
            return False