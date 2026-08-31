class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        window = 0

        for r, elem in enumerate(s):
            while elem in seen:
                seen.remove(s[l])
                l += 1
            seen.add(elem)
            window = max(window, r - l + 1)

        return window
            

        