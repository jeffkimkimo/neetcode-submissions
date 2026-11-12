class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
        
        for char in t:
            if char in count:
                count[char] -= 1
        
        return  all(val == 0 for val in count.values())
        