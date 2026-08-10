class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str=""
        for c in s:
            if c.isalnum():
                if c.isalpha():
                    new_str+=c.lower()
                else:
                    new_str+=c   
        return new_str==new_str[::-1]   