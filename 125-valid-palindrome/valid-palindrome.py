class Solution(object):
    def isPalindrome(self, s):  # ← ADD 'self' here
        
        left = 0
        right = len(s) - 1
    
        while left < right:
            # Skip non-alphanumeric on LEFT
            while left < right and not s[left].isalnum():
                left += 1
        
            # Skip non-alphanumeric on RIGHT
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
            
            # Move pointers inward
            left += 1
            right -= 1
        
        return True