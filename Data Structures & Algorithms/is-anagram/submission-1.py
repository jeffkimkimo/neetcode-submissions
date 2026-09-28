class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dct = {}
        for char in s:
            if char in dct:
                dct[char]+=1
            else:
                dct[char]=1
        for char in t:
            if char in dct:
                dct[char]-=1
            else:
                return False
            if dct[char]<0:
                return False
        return True