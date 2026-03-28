class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            substr = haystack[i:i+len(needle)]
            if substr == needle:
                index = i
                return i
        return -1