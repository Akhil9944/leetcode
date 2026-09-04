class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        result=[]
        for target_val in range(len(arr),1,-1):
            idx=arr.index(target_val)
            if idx==target_val-1:
                continue
            if idx!=0:
                result.append(idx+1)
                arr[:idx+1]=reversed(arr[:idx+1])
            result.append(target_val)
            arr[:target_val]=reversed(arr[:target_val])
        return result