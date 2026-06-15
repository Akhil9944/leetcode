class Solution(object):
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in freq:
            if freq[ch] < k:
                ans = 0

                for part in s.split(ch):
                    ans = max(ans,
                              self.longestSubstring(part, k))

                return ans

        return len(s)