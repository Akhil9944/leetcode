class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n=len(mat)
        total=0

        for i in range(n):
            for j in range(n):
                if i==j:
                    total+=mat[i][j]
                elif i+j==n-1:
                    total+=mat[i][j]
        return total
