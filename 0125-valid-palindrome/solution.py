class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ""
        for ch in s:
            if ch.isalnum():
                x += ch.lower()
        r = x[::-1]
        if r == x:
            return True
        else:
            return False
