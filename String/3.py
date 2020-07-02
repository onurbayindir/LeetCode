class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        curChars = set()
        maxLength = 0
        while end < len(s):
            if s[end] not in curChars:
                curChars.add(s[end])
                end += 1
            else:
                curChars.remove(s[start])
                start += 1
            maxLength = max(maxLength, end - start)
        return maxLength