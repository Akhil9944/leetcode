class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n=len(matrix)
        low,high=matrix[0][0],matrix[n-1][n-1]
        def countLessEqual(x):
            count=0
            row,col=n-1,0
            while row>=0 and col<n:
                if matrix[row][col]<=x:
                    count+=row+1
                    col+=1
                else:
                    row-=1
            return count
        while low<high:
            mid=(low+high)//2
            if countLessEqual(mid)<k:
                low=mid+1
            else:
                high=mid
        return low