class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        for ch in range(len(s)):
            if freq[s[ch]] == 1:
                return ch
        return -1