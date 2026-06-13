class Solution(object):
    def mapWordWeights(self, words, weights):
        ans = ""

        for word in words:
            total = 0

            for ch in word:
                total += weights[ord(ch) - ord('a')]

            mod = total % 26
            ans += chr(ord('z') - mod)

        return ans