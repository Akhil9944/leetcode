class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        sorted_nums2=sorted(enumerate(nums2),key=lambda x:x[1],reverse=True)

        res=[0]*len(nums1)
        left=0
        right=len(nums1)-1

        for original_idx,val2 in sorted_nums2:
            if nums1[right]>val2:
                res[original_idx]=nums1[right]
                right-=1
            else:
                res[original_idx]=nums1[left]
                left+=1
        return res
        