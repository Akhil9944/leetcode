from collections import Counter, defaultdict

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        n = len(s)

        need = Counter(words)
        ans = []

        for i in range(word_len):
            left = i
            seen = defaultdict(int)
            count = 0

            for right in range(i, n - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in need:
                    seen[word] += 1
                    count += 1

                    while seen[word] > need[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len

                    if count == word_count:
                        ans.append(left)

                else:
                    seen.clear()
                    count = 0
                    left = right + word_len

        return ans