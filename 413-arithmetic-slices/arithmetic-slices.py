class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        n=len(nums)
        curr=0
        ans=0
        for i in range(2,n):
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                curr+=1
                ans+=curr
            else:
                curr=0
        return ans
        """
        :type nums: List[int]
        :rtype: int
        """
        