class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mp = {}
        ans = -1

        for num in nums:

            total = 0
            temp = num

            while temp > 0:
                total += temp % 10
                temp //= 10

            if total in mp:
                ans = max(ans, num + mp[total])

            if total not in mp or num > mp[total]:
                mp[total] = num

        return ans