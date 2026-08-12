class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left=0
        count={}
        max_freq=0
        maxi=0

        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0)+1
            max_freq=max(max_freq,count[s[right]])

            while(right-left+1)-max_freq>k:
                count[s[left]]-=1
                left+=1
            maxi=max(maxi,right-left+1)

        return maxi
