class Solution:

    def encode(self, strs: List[str]) -> str:

        total = []

        # each string given in strs will be 1. counted 2. appended with a x# in front
        for string in strs:
            total.append(str(len(string))+"#"+string) # prob not append and something else
        
        return "".join(total)

    def decode(self, s: str) -> List[str]:

        new = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            start = j + 1
            length = int(s[i:j])
            new.append(s[start:start+length])
            i = start + length

        return new