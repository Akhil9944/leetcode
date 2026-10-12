class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
            
        rightmost_bit = xor_sum & -xor_sum
        num1, num2 = 0, 0
        for num in nums:
            if num & rightmost_bit:
                num1 ^= num
            else:
                num2 ^= num
                
        return [num1, num2]