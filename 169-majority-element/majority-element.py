class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj=None
        cnt=0

        for num in nums:
            if cnt==0:
                maj=num
            cnt+=1 if num == maj else -1
        return maj

        