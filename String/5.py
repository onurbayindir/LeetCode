class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        longestPalindrome = s[0]
        for i in range(len(s)):
            # There are two possible ways to obtain a center
            # First: if current character is equal to the next one
            if i < len(s) - 1 and s[i] == s[i+1]:
                if 2 > len(longestPalindrome):
                    longestPalindrome = s[i:i+2]
                for j in range(len(s)):
                    if i - j < 0 or i + j + 1 >= len(s) or s[i-j] != s[i+j+1]:
                        break
                    if len(s[i-j:i+j+2]) > len(longestPalindrome):
                        longestPalindrome = s[i-j:i+j+2]
            # Second: if previous and next character is similar
            for j in range(len(s)):
                if i - j < 0 or i + j >= len(s) or s[i-j] != s[i+j]:
                    break
                if len(s[i-j:i+j+1]) > len(longestPalindrome):
                    longestPalindrome = s[i-j:i+j+1]
        return longestPalindrome
        