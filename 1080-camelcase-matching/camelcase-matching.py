class Solution(object):
    def camelMatch(self, queries, pattern):
        def check(word):
            j=0
            for ch in word:
                if j < len(pattern) and ch == pattern[j]:
                    j+=1
                elif ch.isupper():
                    return False
            return j==len(pattern)

        ans=[]
        for word in queries:
            ans.append(check(word))
        return ans
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        