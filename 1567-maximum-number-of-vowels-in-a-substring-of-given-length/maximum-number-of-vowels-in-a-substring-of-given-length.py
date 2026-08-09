class Solution(object):
    def maxVowels(self, s, k):
        
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = "aeiou"
    
        left = 0
        count = 0
        maximum = 0

        for right in range(len(s)):

            if s[right] in vowels:
                count += 1

            if right - left + 1 == k:

                maximum = max(maximum, count)

                if s[left] in vowels:
                    count -= 1

                left += 1

        return maximum