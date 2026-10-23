class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub=[]
        for x in nums:
            import bisect
            idx=bisect.bisect_left(sub,x)
            if idx==len(sub):
                sub.append(x)
            else:
                sub[idx]=x
        return len(sub)