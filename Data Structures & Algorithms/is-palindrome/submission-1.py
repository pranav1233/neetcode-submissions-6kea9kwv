class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in range(len(s)-1,-1,-1):
            if s[i].isalnum():
                res += s[i].lower()
        actual =""
        for i in range(len(s)):
            if s[i].isalnum():
                actual += s[i].lower()

        return actual == res