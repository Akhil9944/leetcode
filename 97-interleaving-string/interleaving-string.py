class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        
        # If the total lengths don't match, they can't interleave to form s3
        if m + n != len(s3):
            return False
            
        # dp[j] will store whether s1[:i] and s2[:j] can form s3[:i+j]
        dp = [False] * (n + 1)
        
        dp[0] = True
        
        for j in range(1, n + 1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
            
        for i in range(1, m + 1):
           
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            
            for j in range(1, n + 1):
               
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or \
                        (dp[j-1] and s2[j-1] == s3[i+j-1])
                        
        return dp[n]