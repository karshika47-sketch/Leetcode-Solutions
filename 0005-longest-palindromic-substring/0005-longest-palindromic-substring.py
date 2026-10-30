class Solution:
    def longestPalindrome(self, s: str) -> str:
    
        if len(s) <= 1:
            return s

        max_len = 1
        max_str = s[0]

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]

                if len(sub) > max_len and sub == sub[::-1]:
                    max_len = len(sub)
                    max_str = sub

        return max_str
        

        