class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        length = 0 
        window = set()
        for i in range(len(s)):

            while s[i] in window:
                window.remove(s[l])
                l += 1

            window.add(s[i])
            length = max(length, len(window))
        return length