class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for char in s:
            if char.isalnum():
                clean+=char
        
        s = clean.lower()

        #print(s)
        

        #print(s)
        if s == " ":
            return True
        
        left = 0
        right = len(s)-1

        while left<right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True
