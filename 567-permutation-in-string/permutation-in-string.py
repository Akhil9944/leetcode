class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        need = [0] * 26
        window = [0] * 26

        for c in s1:
            need[ord(c) - ord('a')] += 1

        k = len(s1)

        for i in range(k):
            window[ord(s2[i]) - ord('a')] += 1

        if need == window:
            return True

        for i in range(k, len(s2)):
            # add new character
            window[ord(s2[i]) - ord('a')] += 1

            # remove old character
            window[ord(s2[i - k]) - ord('a')] -= 1

            if need == window:
                return True

        return False