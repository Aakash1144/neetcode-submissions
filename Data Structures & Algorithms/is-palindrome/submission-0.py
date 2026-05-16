class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        clean_s = ''.join(i.lower() for i in s if i.isalnum())
        right = len(clean_s)-1
        
        while left<right:

            if(clean_s[left]!=clean_s[right]):
                return False
            left = left + 1
            right = right -1    
        return True        