from collections import defaultdict

class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1 
        
        curr_sum = 0
        total_subarrays = 0
        
        for num in nums:
            curr_sum += num
            
            if (curr_sum - goal) in prefix_sums:
                total_subarrays += prefix_sums[curr_sum - goal]
                
            prefix_sums[curr_sum] += 1
            
        return total_subarrays